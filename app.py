# -*- coding: utf-8 -*-
import os
import random
import secrets
from datetime import datetime, timedelta

from flask import Flask, g, jsonify, render_template, request
from werkzeug.middleware.proxy_fix import ProxyFix

from models import db, PackState, UserCard, ClaimedAchievement
from cards_data import (
    CARDS, CARDS_BY_ID, CARDS_BY_RARITY, RARITY_ORDER, RARITY_WEIGHTS,
    RARITY_LABELS, TOTAL_CARDS, ALL_CATEGORIES,
)
from achievements_data import ACHIEVEMENTS, ACHIEVEMENTS_BY_ID

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
COOKIE_NAME = "santuario_uid"
COOKIE_MAX_AGE = 60 * 60 * 24 * 365 * 5  # ~5 años

app = Flask(__name__)
# Render (y la mayoría de los hosts) terminan el HTTPS en un proxy y le
# reenvían la request a la app por HTTP plano. Esto le dice a Flask que
# confíe en el header X-Forwarded-Proto para saber que en realidad es HTTPS
# (importante para que la cookie de identidad se marque "secure" bien).
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1, x_for=1)

DB_PATH = os.environ.get("DATABASE_PATH", os.path.join(BASE_DIR, "gacha.db"))
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAX_PACKS"] = 5
app.config["PACK_INTERVAL_SECONDS"] = int(os.environ.get("PACK_INTERVAL_SECONDS", 300))
app.config["STARTER_PACKS"] = 2

db.init_app(app)


# ---------------------------------------------------------------------------
# Identidad anónima por visitante (cookie con un token aleatorio, sin login)
# ---------------------------------------------------------------------------

@app.before_request
def _load_uid():
    uid = request.cookies.get(COOKIE_NAME)
    if not uid:
        uid = secrets.token_urlsafe(24)
        g.new_uid = uid
    g.uid = uid


@app.after_request
def _persist_uid(response):
    new_uid = getattr(g, "new_uid", None)
    if new_uid:
        response.set_cookie(
            COOKIE_NAME,
            new_uid,
            max_age=COOKIE_MAX_AGE,
            httponly=True,
            samesite="Lax",
            secure=request.is_secure,
        )
    return response


# ---------------------------------------------------------------------------
# Helpers de estado / lógica de juego (todo recibe el uid del visitante)
# ---------------------------------------------------------------------------

def get_or_create_state(uid):
    state = db.session.get(PackState, uid)
    if state is None:
        state = PackState(
            user_id=uid,
            pending_packs=app.config["STARTER_PACKS"],
            last_tick=datetime.utcnow(),
            total_packs_opened=0,
        )
        db.session.add(state)
        db.session.commit()
    return state


def tick(state):
    """Acumula sobres según el tiempo transcurrido, sin pasarse del tope."""
    max_packs = app.config["MAX_PACKS"]
    interval = app.config["PACK_INTERVAL_SECONDS"]
    now = datetime.utcnow()

    if state.pending_packs < max_packs:
        elapsed = (now - state.last_tick).total_seconds()
        ticks_elapsed = int(elapsed // interval)
        if ticks_elapsed > 0:
            room = max_packs - state.pending_packs
            add = min(ticks_elapsed, room)
            state.pending_packs += add
            state.last_tick = state.last_tick + timedelta(seconds=add * interval)
            if state.pending_packs >= max_packs:
                state.last_tick = now
    else:
        state.last_tick = now

    db.session.commit()
    return state


def seconds_to_next(state):
    max_packs = app.config["MAX_PACKS"]
    if state.pending_packs >= max_packs:
        return None
    interval = app.config["PACK_INTERVAL_SECONDS"]
    elapsed = (datetime.utcnow() - state.last_tick).total_seconds()
    remaining = max(0, int(interval - elapsed))
    return remaining


def roll_rarity():
    roll = random.random()
    cumulative = 0.0
    for rarity in RARITY_ORDER:
        cumulative += RARITY_WEIGHTS[rarity]
        if roll <= cumulative:
            return rarity
    return RARITY_ORDER[-1]


def open_one_pack():
    drawn = []
    for _ in range(5):
        rarity = roll_rarity()
        pool = CARDS_BY_RARITY[rarity]
        drawn.append(random.choice(pool))
    return drawn


def get_stats(uid):
    user_cards = UserCard.query.filter_by(user_id=uid).all()
    unique_total = len(user_cards)
    dupes_total = sum(uc.count for uc in user_cards)
    unique_by_rarity = {r: 0 for r in RARITY_ORDER}
    for uc in user_cards:
        card = CARDS_BY_ID.get(uc.card_id)
        if card:
            unique_by_rarity[card["rarity"]] += 1
    state = get_or_create_state(uid)
    return {
        "unique_total": unique_total,
        "dupes_total": dupes_total,
        "unique_by_rarity": unique_by_rarity,
        "total_packs_opened": state.total_packs_opened,
    }


def achievement_progress(ach, stats):
    cond = ach["condition"]
    if cond == "open_packs":
        current = stats["total_packs_opened"]
    elif cond == "unique_total":
        current = stats["unique_total"]
    elif cond == "unique_rarity":
        current = stats["unique_by_rarity"].get(ach.get("rarity"), 0)
    elif cond == "dupes_total":
        current = stats["dupes_total"]
    else:
        current = 0
    return current, ach["value"]


def serialize_achievement(ach, claimed_ids, stats):
    current, target = achievement_progress(ach, stats)
    unlocked = current >= target
    return {
        "id": ach["id"],
        "name": ach["name"],
        "description": ach["description"],
        "reward": ach["reward"],
        "current": min(current, target),
        "target": target,
        "unlocked": unlocked,
        "claimed": ach["id"] in claimed_ids,
    }


def state_payload(state):
    return {
        "pending_packs": state.pending_packs,
        "max_packs": app.config["MAX_PACKS"],
        "seconds_to_next": seconds_to_next(state),
        "pack_interval": app.config["PACK_INTERVAL_SECONDS"],
        "total_packs_opened": state.total_packs_opened,
    }


# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html", active="sanctum")


@app.route("/coleccion")
def coleccion_page():
    return render_template("collection.html", active="coleccion")


@app.route("/logros")
def logros_page():
    return render_template("achievements.html", active="logros")


# ---------------------------------------------------------------------------
# API
# ---------------------------------------------------------------------------

@app.route("/api/estado")
def api_estado():
    state = tick(get_or_create_state(g.uid))
    return jsonify(state_payload(state))


@app.route("/api/abrir", methods=["POST"])
def api_abrir():
    uid = g.uid
    state = tick(get_or_create_state(uid))
    if state.pending_packs <= 0:
        return jsonify({"error": "No tienes sobres disponibles todavía."}), 400

    state.pending_packs -= 1
    state.total_packs_opened += 1

    drawn = open_one_pack()
    results = []
    for card in drawn:
        uc = db.session.get(UserCard, (uid, card["id"]))
        is_new = uc is None
        if uc is None:
            uc = UserCard(user_id=uid, card_id=card["id"], count=1, first_obtained_at=datetime.utcnow())
            db.session.add(uc)
        else:
            uc.count += 1
        results.append({**card, "is_new": is_new, "owned_count": uc.count})

    db.session.commit()

    payload = state_payload(state)
    payload["cards"] = results
    return jsonify(payload)


@app.route("/api/coleccion")
def api_coleccion():
    uid = g.uid
    owned = {uc.card_id: uc for uc in UserCard.query.filter_by(user_id=uid).all()}
    out = []
    for card in CARDS:
        uc = owned.get(card["id"])
        out.append({
            **card,
            "rarity_label": RARITY_LABELS[card["rarity"]],
            "owned": uc is not None,
            "count": uc.count if uc else 0,
        })
    stats = get_stats(uid)
    rarity_totals = {r: len(CARDS_BY_RARITY[r]) for r in RARITY_ORDER}
    return jsonify({
        "cards": out,
        "total_cards": TOTAL_CARDS,
        "unique_total": stats["unique_total"],
        "unique_by_rarity": stats["unique_by_rarity"],
        "rarity_totals": rarity_totals,
        "rarity_order": RARITY_ORDER,
        "rarity_labels": RARITY_LABELS,
        "all_categories": ALL_CATEGORIES,
    })


@app.route("/api/logros")
def api_logros():
    uid = g.uid
    stats = get_stats(uid)
    claimed_ids = {c.achievement_id for c in ClaimedAchievement.query.filter_by(user_id=uid).all()}
    out = [serialize_achievement(a, claimed_ids, stats) for a in ACHIEVEMENTS]
    return jsonify({"achievements": out})


@app.route("/api/logros/<ach_id>/reclamar", methods=["POST"])
def api_reclamar(ach_id):
    uid = g.uid
    ach = ACHIEVEMENTS_BY_ID.get(ach_id)
    if ach is None:
        return jsonify({"error": "Logro inexistente."}), 404

    if db.session.get(ClaimedAchievement, (uid, ach_id)) is not None:
        return jsonify({"error": "Ese logro ya fue reclamado."}), 400

    stats = get_stats(uid)
    current, target = achievement_progress(ach, stats)
    if current < target:
        return jsonify({"error": "Todavía no cumples ese logro."}), 400

    state = tick(get_or_create_state(uid))
    state.pending_packs += ach["reward"]
    db.session.add(ClaimedAchievement(user_id=uid, achievement_id=ach_id, claimed_at=datetime.utcnow()))
    db.session.commit()

    payload = state_payload(state)
    payload["reward"] = ach["reward"]
    payload["achievement_id"] = ach_id
    return jsonify(payload)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(debug=debug_mode, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
