# -*- coding: utf-8 -*-
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Todas las tablas están scopeadas por user_id: un identificador anónimo
# guardado en una cookie de navegador (ver app.py, _load_uid / _persist_uid).
# No hay login ni datos personales: es solo un token aleatorio por visitante.


class PackState(db.Model):
    """Estado de sobres acumulados, una fila por usuario (user_id)."""
    __tablename__ = "pack_state"

    user_id = db.Column(db.String(64), primary_key=True)
    pending_packs = db.Column(db.Integer, default=0, nullable=False)
    last_tick = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    total_packs_opened = db.Column(db.Integer, default=0, nullable=False)


class UserCard(db.Model):
    """Cuántas copias de cada carta posee cada usuario."""
    __tablename__ = "user_card"

    user_id = db.Column(db.String(64), primary_key=True)
    card_id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0, nullable=False)
    first_obtained_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


class ClaimedAchievement(db.Model):
    """Logros ya reclamados (recompensa ya entregada) por usuario."""
    __tablename__ = "claimed_achievement"

    user_id = db.Column(db.String(64), primary_key=True)
    achievement_id = db.Column(db.String(64), primary_key=True)
    claimed_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
