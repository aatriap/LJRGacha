// Santuario Arcano — lógica de la página de Colección

const progressNumber = document.getElementById("progress-number");
const rarityBreakdown = document.getElementById("rarity-breakdown");
const viewToggle = document.getElementById("view-toggle");
const rarityFilter = document.getElementById("rarity-filter");
const categoryFilter = document.getElementById("category-filter");
const cardGrid = document.getElementById("card-grid");
const collectionEmptyHint = document.getElementById("collection-empty-hint");

const modal = document.getElementById("card-modal");
const modalPanel = document.getElementById("card-modal-panel");
const modalBackdrop = document.getElementById("card-modal-backdrop");

let collectionData = null;
let currentView = "todas";
let currentRarity = "todas";
let currentCategory = "todas";

async function loadCollection() {
  const res = await fetch("/api/coleccion");
  collectionData = await res.json();
  renderHead();
  renderCategoryFilter();
  renderGrid();
}

function renderHead() {
  progressNumber.textContent = `${collectionData.unique_total} / ${collectionData.total_cards}`;

  rarityBreakdown.innerHTML = "";
  collectionData.rarity_order.forEach((r) => {
    const chip = document.createElement("div");
    chip.className = "rarity-chip";
    chip.innerHTML = `
      <span class="rarity-dot" style="--dot-color: var(--${r})"></span>
      <span>${collectionData.rarity_labels[r]}: ${collectionData.unique_by_rarity[r]} / ${collectionData.rarity_totals[r]}</span>
    `;
    rarityBreakdown.appendChild(chip);
  });
}

// Las categorías son libres (las definís vos en cards_data.py), así que el
// filtro se arma dinámicamente con lo que venga de la API.
function renderCategoryFilter() {
  if (!categoryFilter) return;
  const categories = collectionData.all_categories || [];
  categoryFilter.innerHTML = "";

  const allBtn = document.createElement("button");
  allBtn.dataset.category = "todas";
  allBtn.textContent = "Todas las categorías";
  allBtn.className = currentCategory === "todas" ? "is-active" : "";
  categoryFilter.appendChild(allBtn);

  categories.forEach((cat) => {
    const btn = document.createElement("button");
    btn.dataset.category = cat;
    btn.textContent = cat;
    btn.className = currentCategory === cat ? "is-active" : "";
    categoryFilter.appendChild(btn);
  });
}

function renderGrid() {
  let cards = collectionData.cards;

  if (currentView === "mia") cards = cards.filter((c) => c.owned);
  if (currentRarity !== "todas") cards = cards.filter((c) => c.rarity === currentRarity);
  if (currentCategory !== "todas") {
    cards = cards.filter((c) => c.categorias && c.categorias.includes(currentCategory));
  }

  cardGrid.innerHTML = "";

  if (cards.length === 0) {
    collectionEmptyHint.hidden = false;
    return;
  }
  collectionEmptyHint.hidden = true;

  cards.forEach((card) => {
    const el = document.createElement("div");
    const locked = !card.owned;
    el.className = `card rarity-${card.rarity}` + (locked ? " card--locked" : "");
    el.innerHTML = cardInnerHTML(card, { count: card.count, locked });
    el.addEventListener("click", () => openModal(card));
    cardGrid.appendChild(el);
  });
}

function openModal(card) {
  const categorias = card.categorias && card.categorias.length ? card.categorias.join(", ") : "";
  modalPanel.style.setProperty("--card-color", `var(--${card.rarity})`);
  const countLine = card.owned
    ? `<p class="modal-count">Copias obtenidas: ${card.count}</p>`
    : `<p class="modal-count modal-count--locked">Todavía no la has obtenido</p>`;
  modalPanel.innerHTML = `
    ${card.rarity === "legendaria" ? '<div class="card-shimmer"></div>' : ""}
    <div class="modal-art">${cardArtHTML(card)}</div>
    <div class="modal-name">${card.name}</div>
    <div class="modal-rarity">${card.rarity_label}${categorias ? " · " + categorias : ""}</div>
    <p class="modal-flavor">${card.flavor}</p>
    ${countLine}
    <button class="modal-close" id="modal-close-btn">Cerrar</button>
  `;
  modal.classList.add("is-open");
  document.getElementById("modal-close-btn").addEventListener("click", closeModal);
}

function closeModal() {
  modal.classList.remove("is-open");
}

modalBackdrop.addEventListener("click", closeModal);
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeModal();
});

viewToggle.addEventListener("click", (e) => {
  const btn = e.target.closest("button[data-view]");
  if (!btn) return;
  currentView = btn.dataset.view;
  [...viewToggle.children].forEach((b) => b.classList.toggle("is-active", b === btn));
  renderGrid();
});

rarityFilter.addEventListener("click", (e) => {
  const btn = e.target.closest("button[data-rarity]");
  if (!btn) return;
  currentRarity = btn.dataset.rarity;
  [...rarityFilter.children].forEach((b) => b.classList.toggle("is-active", b === btn));
  renderGrid();
});

if (categoryFilter) {
  categoryFilter.addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-category]");
    if (!btn) return;
    currentCategory = btn.dataset.category;
    [...categoryFilter.children].forEach((b) => b.classList.toggle("is-active", b === btn));
    renderGrid();
  });
}

loadCollection();
