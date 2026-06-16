(() => {
  const VERSION = "v108.0";
  const STORAGE_KEY = "webappsReviewSettings";
  const defaults = {
    language: "en",
    theme: "day",
    transparency: 74,
    translucency: 18
  };

  const root = document.documentElement;
  const overlay = document.querySelector("[data-settings-overlay]");
  const openButton = document.querySelector("[data-settings-open]");
  const closeButton = document.querySelector("[data-settings-close]");
  const stickyCta = document.querySelector("[data-sticky-cta]");
  const hero = document.querySelector(".hero");

  const readSettings = () => {
    try {
      return { ...defaults, ...JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}") };
    } catch {
      return { ...defaults };
    }
  };

  const writeSettings = (settings) => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(settings));
    } catch {
      /* localStorage is optional for file previews and strict browser modes. */
    }
  };

  let settings = readSettings();

  const setPressed = (selector, value) => {
    document.querySelectorAll(selector).forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.value === value));
    });
  };

  const applySettings = () => {
    const alpha = Math.min(0.88, Math.max(0.58, Number(settings.transparency) / 100));
    const blur = Math.min(26, Math.max(8, Number(settings.translucency)));

    root.dataset.theme = settings.theme === "night" ? "night" : "day";
    root.lang = ["en", "fr", "es"].includes(settings.language) ? settings.language : "en";
    root.style.setProperty("--glass-alpha", alpha.toFixed(2));
    root.style.setProperty("--glass-blur", `${blur}px`);

    setPressed("[data-setting='language']", root.lang);
    setPressed("[data-setting='theme']", root.dataset.theme);

    document.querySelectorAll("[data-version-label]").forEach((node) => {
      node.textContent = VERSION;
    });

    const transparency = document.querySelector("[data-setting-range='transparency']");
    const translucency = document.querySelector("[data-setting-range='translucency']");
    const transparencyValue = document.querySelector("[data-setting-output='transparency']");
    const translucencyValue = document.querySelector("[data-setting-output='translucency']");

    if (transparency) transparency.value = String(settings.transparency);
    if (translucency) translucency.value = String(settings.translucency);
    if (transparencyValue) transparencyValue.textContent = `${settings.transparency}%`;
    if (translucencyValue) translucencyValue.textContent = `${settings.translucency}px`;
  };

  const openSettings = () => {
    if (!overlay) return;
    overlay.hidden = false;
    document.body.dataset.settingsOpen = "true";
    window.requestAnimationFrame(() => closeButton?.focus());
  };

  const closeSettings = () => {
    if (!overlay) return;
    overlay.hidden = true;
    delete document.body.dataset.settingsOpen;
    openButton?.focus();
  };

  const updateStickyCta = () => {
    if (!stickyCta || !hero) return;
    const pastHero = window.scrollY > hero.offsetHeight * 0.72;
    stickyCta.classList.toggle("is-visible", pastHero);
  };

  document.querySelectorAll("[data-setting]").forEach((button) => {
    button.addEventListener("click", () => {
      settings = { ...settings, [button.dataset.setting]: button.dataset.value };
      writeSettings(settings);
      applySettings();
    });
  });

  document.querySelectorAll("[data-setting-range]").forEach((range) => {
    range.addEventListener("input", () => {
      settings = { ...settings, [range.dataset.settingRange]: Number(range.value) };
      writeSettings(settings);
      applySettings();
    });
  });

  document.querySelectorAll(".site-card, .glass-button, .card-link, .mobile-sticky-cta").forEach((node) => {
    node.addEventListener("pointerdown", () => node.classList.add("is-pressed"));
    node.addEventListener("pointerup", () => node.classList.remove("is-pressed"));
    node.addEventListener("pointerleave", () => node.classList.remove("is-pressed"));
    node.addEventListener("pointercancel", () => node.classList.remove("is-pressed"));
  });

  openButton?.addEventListener("click", openSettings);
  closeButton?.addEventListener("click", closeSettings);
  overlay?.addEventListener("click", (event) => {
    if (event.target === overlay) closeSettings();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && overlay && !overlay.hidden) closeSettings();
  });
  window.addEventListener("scroll", updateStickyCta, { passive: true });
  window.addEventListener("resize", updateStickyCta);

  applySettings();
  updateStickyCta();
})();
