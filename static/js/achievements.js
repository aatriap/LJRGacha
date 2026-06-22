// Santuario Arcano — lógica de la página de Logros

const achievementList = document.getElementById("achievement-list");
const achProgressNumber = document.getElementById("ach-progress-number");

async function loadAchievements() {
  const res = await fetch("/api/logros");
  const data = await res.json();
  renderAchievements(data.achievements);
}

function renderAchievements(list) {
  const claimedCount = list.filter((a) => a.claimed).length;
  achProgressNumber.textContent = `${claimedCount} / ${list.length}`;

  achievementList.innerHTML = "";
  list.forEach((a) => {
    const pct = Math.min(100, Math.round((a.current / a.target) * 100));
    const el = document.createElement("div");
    el.className =
      "achievement" + (a.claimed ? " is-claimed" : a.unlocked ? " is-ready" : "");

    let actionHtml;
    if (a.claimed) {
      actionHtml = `<span class="ach-claimed-tag">✓ Reclamado</span>`;
    } else if (a.unlocked) {
      actionHtml = `<button class="ach-claim-btn" data-id="${a.id}">Reclamar</button>`;
    } else {
      actionHtml = `<button class="ach-claim-btn" disabled>Bloqueado</button>`;
    }

    el.innerHTML = `
      <div class="ach-medal">${a.claimed ? "★" : a.unlocked ? "✦" : "✦"}</div>
      <div class="ach-body">
        <div class="ach-name">${a.name}</div>
        <div class="ach-desc">${a.description}</div>
        <div class="ach-bar-track"><div class="ach-bar-fill" style="width:${pct}%"></div></div>
        <div class="ach-progress-text">${a.current} / ${a.target}</div>
      </div>
      <div class="ach-action">
        <span class="ach-reward">+${a.reward} sobre${a.reward > 1 ? "s" : ""}</span>
        ${actionHtml}
      </div>
    `;
    achievementList.appendChild(el);
  });

  achievementList.querySelectorAll(".ach-claim-btn[data-id]").forEach((btn) => {
    btn.addEventListener("click", () => claimAchievement(btn.dataset.id, btn));
  });
}

async function claimAchievement(id, btn) {
  btn.disabled = true;
  btn.textContent = "Reclamando…";
  try {
    const res = await fetch(`/api/logros/${id}/reclamar`, { method: "POST" });
    const data = await res.json();
    if (!res.ok) {
      Gacha.toast(data.error || "No se pudo reclamar el logro.");
      btn.disabled = false;
      btn.textContent = "Reclamar";
      return;
    }
    Gacha.applyServerState(data);
    Gacha.toast(`Logro reclamado: +${data.reward} sobre${data.reward > 1 ? "s" : ""}`);
    loadAchievements();
  } catch (e) {
    Gacha.toast("No se pudo contactar al Santuario.");
    btn.disabled = false;
    btn.textContent = "Reclamar";
  }
}

loadAchievements();
