// Santuario Arcano — lógica de la página principal (apertura de sobres)

const heroSigils = document.getElementById("hero-sigils");
const heroTimerText = document.getElementById("hero-timer-text");
const openBtn = document.getElementById("open-btn");
const openError = document.getElementById("open-error");
const revealArea = document.getElementById("reveal-area");
const revealCards = document.getElementById("reveal-cards");
const emptyHint = document.getElementById("empty-hint");

let isFetching = false; // true solo durante la llamada de red a /api/abrir

Gacha.onUpdate((state) => {
  if (!heroSigils) return;
  renderSigils(heroSigils, state.pending_packs, state.max_packs);
  heroSigils.classList.toggle("is-full", state.pending_packs >= state.max_packs);

  if (state.pending_packs >= state.max_packs) {
    heroTimerText.textContent = "El sello está al límite. Abre un sobre antes de que se desborde.";
  } else if (state.seconds_to_next != null) {
    heroTimerText.textContent = `Próximo sobre en ${fmtTime(state.seconds_to_next)} · ${state.pending_packs}/${state.max_packs} guardados`;
  }

  if (!isFetching) {
    openBtn.disabled = state.pending_packs <= 0;
  }
});

// --- Sonidos por rareza: intenta un .mp3 propio primero, y si no existe usa
// un sonido sintetizado de respaldo (no depende de archivos externos). ---

const RARITY_GLOW = {
  comun: "rgba(154, 163, 181, 0.45)",
  rara: "rgba(91, 155, 217, 0.55)",
  epica: "rgba(176, 107, 224, 0.6)",
  legendaria: "rgba(240, 169, 61, 0.75)",
};

let audioCtx = null;
function getAudioCtx() {
  if (!audioCtx) {
    const Ctx = window.AudioContext || window.webkitAudioContext;
    audioCtx = new Ctx();
  }
  if (audioCtx.state === "suspended") audioCtx.resume();
  return audioCtx;
}

const RARITY_NOTES = {
  comun: [523.25],
  rara: [523.25, 659.25],
  epica: [392.0, 523.25, 659.25, 783.99],
  legendaria: [392.0, 523.25, 659.25, 783.99, 1046.5],
};

function playSynthSound(rarity) {
  try {
    const ctx = getAudioCtx();
    const notes = RARITY_NOTES[rarity] || RARITY_NOTES.comun;
    const now = ctx.currentTime;
    const isLegendary = rarity === "legendaria";
    notes.forEach((freq, i) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = isLegendary ? "sine" : rarity === "epica" ? "triangle" : "sine";
      osc.frequency.value = freq;
      const start = now + i * (isLegendary ? 0.1 : 0.08);
      const peak = isLegendary ? 0.22 : 0.15;
      const dur = isLegendary ? 0.9 : 0.45;
      gain.gain.setValueAtTime(0, start);
      gain.gain.linearRampToValueAtTime(peak, start + 0.02);
      gain.gain.exponentialRampToValueAtTime(0.001, start + dur);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(start);
      osc.stop(start + dur + 0.05);
    });
  } catch (e) {
    /* el navegador puede bloquear audio sin interacción previa; se ignora */
  }
}

// Para cambiar los sonidos: poné tus archivos en static/audio/ con estos
// nombres exactos (comun.mp3, rara.mp3, epica.mp3, legendaria.mp3). Si un
// archivo no existe o falla, se usa automáticamente el sonido sintetizado.
function playRaritySound(rarity) {
  let fallbackFired = false;
  const fallback = () => {
    if (fallbackFired) return;
    fallbackFired = true;
    playSynthSound(rarity);
  };
  try {
    const audio = new Audio(`/static/audio/${rarity}.mp3`);
    audio.volume = 0.8;
    audio.addEventListener("error", fallback);
    const playPromise = audio.play();
    if (playPromise && typeof playPromise.catch === "function") {
      playPromise.catch(fallback);
    }
  } catch (e) {
    fallback();
  }
}

function makeFlipSlot() {
  const slot = document.createElement("div");
  slot.className = "reveal-slot";
  slot.innerHTML = `
    <div class="flip-inner">
      <div class="flip-face back">
        <span>✦</span>
        <span class="back-hint">Toca para revelar</span>
      </div>
      <div class="flip-face front"><div class="burst"></div><div class="card"></div></div>
    </div>
  `;
  return slot;
}

function flashLegendary() {
  const flash = document.createElement("div");
  flash.className = "legend-flash";
  document.body.appendChild(flash);
  requestAnimationFrame(() => flash.classList.add("flash-on"));
  setTimeout(() => flash.remove(), 1200);
}

function revealSlot(slot, card) {
  if (slot.classList.contains("is-flipped")) return;

  const cardEl = slot.querySelector(".card");
  const burstEl = slot.querySelector(".burst");
  cardEl.classList.add("rarity-" + card.rarity);
  cardEl.innerHTML = cardInnerHTML(card, { isNew: card.is_new, count: card.owned_count });
  burstEl.style.setProperty("--burst-color", RARITY_GLOW[card.rarity] || RARITY_GLOW.comun);

  slot.classList.add("is-flipped");
  playRaritySound(card.rarity);
  if (card.rarity === "legendaria") flashLegendary();
}

async function openPack() {
  if (isFetching) return;
  if (Gacha.state.pending_packs <= 0) return;

  isFetching = true;
  openBtn.disabled = true;
  openError.hidden = true;
  emptyHint.hidden = true;

  let data;
  try {
    const res = await fetch("/api/abrir", { method: "POST" });
    data = await res.json();
    if (!res.ok) {
      openError.textContent = data.error || "No se pudo abrir el sobre.";
      openError.hidden = false;
      isFetching = false;
      Gacha.refresh();
      return;
    }
  } catch (e) {
    openError.textContent = "No se pudo contactar al Santuario. Intenta de nuevo.";
    openError.hidden = false;
    isFetching = false;
    return;
  }

  isFetching = false;
  Gacha.applyServerState(data);

  // Reemplaza las cartas anteriores por las del nuevo sobre. Las cartas ya
  // quedaron guardadas en tu colección en el momento en que se abrió el
  // sobre (no hace falta ningún paso extra para "guardarlas").
  revealArea.hidden = false;
  revealCards.innerHTML = "";
  data.cards.forEach((card) => {
    const slot = makeFlipSlot();
    revealCards.appendChild(slot);
    slot.addEventListener("click", () => revealSlot(slot, card));
  });
}

openBtn.addEventListener("click", openPack);
