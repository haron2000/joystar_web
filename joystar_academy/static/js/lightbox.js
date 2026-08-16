document.addEventListener("DOMContentLoaded", function () {
  const items = Array.from(document.querySelectorAll("[data-lightbox-item]"));
  if (items.length === 0) return;

  const overlay = document.getElementById("lightbox-overlay");
  const imgEl = document.getElementById("lightbox-image");
  const captionEl = document.getElementById("lightbox-caption");
  const closeBtn = document.getElementById("lightbox-close");
  const prevBtn = document.getElementById("lightbox-prev");
  const nextBtn = document.getElementById("lightbox-next");

  let index = 0;

  function open(i) {
    index = i;
    updateImage();
    overlay.classList.add("is-open");
    overlay.setAttribute("aria-hidden", "false");
    closeBtn.focus();
    document.body.style.overflow = "hidden";
  }

  function close() {
    overlay.classList.remove("is-open");
    overlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  function updateImage() {
    const item = items[index];
    imgEl.src = item.getAttribute("data-full");
    imgEl.alt = item.getAttribute("data-caption") || "";
    captionEl.textContent = item.getAttribute("data-caption") || "";
  }

  function go(delta) {
    index = (index + delta + items.length) % items.length;
    updateImage();
  }

  items.forEach((item, i) => {
    item.addEventListener("click", () => open(i));
  });

  closeBtn.addEventListener("click", close);
  nextBtn.addEventListener("click", () => go(1));
  prevBtn.addEventListener("click", () => go(-1));

  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) close();
  });

  document.addEventListener("keydown", (e) => {
    if (!overlay.classList.contains("is-open")) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowRight") go(1);
    if (e.key === "ArrowLeft") go(-1);
  });
});