// Santuario Arcano — estado global compartido entre páginas
// Maneja el polling del estado de sobres y el indicador de la barra superior.

function fmtTime(totalSeconds) {
  const m = Math.floor(totalSeconds / 60);
  const s = totalSeconds % 60;
  return String(m).padStart(2, "0") + ":" + String(s).padStart(2, "0");
}

function renderSigils(container, pending, max) {
  container.innerHTML = "";
  const filled = Math.min(pending, max);
  for (let i = 0; i < max; i++) {
    const s = document.createElement("span");
    s.className = "sigil" + (i < filled ? " filled" : "");
    container.appendChild(s);
  }
  if (pending > max) {
    const extra = document.createElement("span");
    extra.textContent = "+" + (pending - max);
    extra.style.fontSize = "0.7rem";
    extra.style.color = "var(--gold-bright)";
    extra.style.marginLeft = "3px";
    container.appendChild(extra);
  }
}

const Gacha = {
  state: {
    pending_packs: 0,
    max_packs: 5,
    seconds_to_next: null,
    pack_interval: 300,
    total_packs_opened: 0,
  },
  listeners: [],

  onUpdate(fn) {
    this.listeners.push(fn);
    fn(this.state);
  },

  _notify() {
    this.listeners.forEach((fn) => fn(this.state));
    this._renderNav();
  },

  async refresh() {
    try {
      const res = await fetch("/api/estado");
      if (!res.ok) return;
      const data = await res.json();
      this.state = { ...this.state, ...data };
      this._notify();
    } catch (e) {
      /* sin conexión momentánea: se reintenta en el próximo ciclo */
    }
  },

  applyServerState(data) {
    this.state = {
      ...this.state,
      pending_packs: data.pending_packs,
      max_packs: data.max_packs,
      seconds_to_next: data.seconds_to_next,
      total_packs_opened: data.total_packs_opened,
    };
    this._notify();
  },

  _tickLocal() {
    if (this.state.seconds_to_next != null && this.state.pending_packs < this.state.max_packs) {
      this.state.seconds_to_next = Math.max(0, this.state.seconds_to_next - 1);
      if (this.state.seconds_to_next === 0) {
        this.refresh();
      }
      this._notify();
    }
  },

  _renderNav() {
    const sigilsEl = document.getElementById("nav-sigils");
    const timerEl = document.getElementById("nav-timer");
    if (sigilsEl) renderSigils(sigilsEl, this.state.pending_packs, this.state.max_packs);
    if (timerEl) {
      timerEl.textContent =
        this.state.seconds_to_next == null ? "Sello lleno" : fmtTime(this.state.seconds_to_next);
    }
  },

  toast(msg) {
    const stack = document.getElementById("toast-stack");
    if (!stack) return;
    const el = document.createElement("div");
    el.className = "toast";
    el.textContent = msg;
    stack.appendChild(el);
    setTimeout(() => el.remove(), 3000);
  },
};

// Construye el contenido interno de una carta: imagen, nombre, categorías +
// rareza, y una breve descripción. Se usa tanto para cartas descubiertas
// como para las todavía no obtenidas (estas se ven traslúcidas vía CSS,
// pero muestran la misma información).
function cardInnerHTML(card, opts) {
  opts = opts || {};
  const categorias = card.categorias && card.categorias.length ? card.categorias.join(", ") : "";
  let html = "";
  if (card.rarity === "legendaria") html += '<div class="card-shimmer"></div>';
  if (opts.isNew) html += '<span class="new-flag">Nueva</span>';
  html += cardArtHTML(card);
  html += `<div class="card-name">${card.name}</div>`;
  html += `<div class="card-rarity-tag">${card.rarity_label || rarityLabelOf(card.rarity)}${categorias ? " · " + categorias : ""}</div>`;
  if (card.flavor) html += `<div class="card-desc">${card.flavor}</div>`;
  if (opts.count) html += `<div class="card-count">x${opts.count}</div>`;
  if (opts.locked) html += `<div class="card-locked-tag">No obtenida</div>`;
  return html;
}

// Imagen de la carta. Si no hay imagen (o falla al cargar), se muestra un
// respaldo tipográfico con las iniciales del nombre — sin emojis.
function cardArtHTML(card) {
  const initials = initialsOf(card.name);
  if (!card.image) {
    return `<div class="card-art card-art--fallback"><span class="card-initials">${initials}</span></div>`;
  }
  const src = `/static/images/cards/${card.image}`;
  return `<div class="card-art"><img src="${src}" alt="${card.name}" loading="lazy" onerror="window.cardImgFallback(this,'${initials}')"></div>`;
}

window.cardImgFallback = function (img, initials) {
  const wrap = img.closest(".card-art");
  if (wrap) {
    wrap.classList.add("card-art--fallback");
    wrap.innerHTML = `<span class="card-initials">${initials}</span>`;
  }
};

function initialsOf(name) {
  if (!name) return "?";
  const words = name.trim().split(/\s+/).filter(Boolean);
  const letters = words.slice(0, 2).map((w) => w[0].toUpperCase());
  return letters.join("") || "?";
}

function rarityLabelOf(rarity) {
  const map = { comun: "Común", rara: "Rara", epica: "Épica", legendaria: "Legendaria" };
  return map[rarity] || rarity;
}

window.Gacha = Gacha;
window.renderSigils = renderSigils;
window.fmtTime = fmtTime;
window.cardInnerHTML = cardInnerHTML;
window.cardArtHTML = cardArtHTML;
window.rarityLabelOf = rarityLabelOf;

setInterval(() => Gacha._tickLocal(), 1000);
setInterval(() => Gacha.refresh(), 8000);
document.addEventListener("DOMContentLoaded", () => Gacha.refresh());
