document.addEventListener("DOMContentLoaded", function () {
  const root = document.querySelector("[data-hero-slider]");
  if (!root) return;

  const slides = Array.from(root.querySelectorAll(".hero-slide"));
  const dotsWrap = root.querySelector(".hero-dots");
  const prevBtn = root.querySelector(".hero-arrow.prev");
  const nextBtn = root.querySelector(".hero-arrow.next");
  if (slides.length === 0) return;

  let index = 0;
  let timer = null;
  const AUTOPLAY_MS = 5000;

  slides.forEach((_, i) => {
    const dot = document.createElement("button");
    dot.className = "hero-dot" + (i === 0 ? " is-active" : "");
    dot.setAttribute("aria-label", "Go to slide " + (i + 1));
    dot.addEventListener("click", () => { goTo(i); restart(); });
    dotsWrap.appendChild(dot);
  });
  const dots = Array.from(dotsWrap.querySelectorAll(".hero-dot"));

  function goTo(next) {
    slides[index].classList.remove("is-active");
    dots[index].classList.remove("is-active");
    index = (next + slides.length) % slides.length;
    slides[index].classList.add("is-active");
    dots[index].classList.add("is-active");
  }

  function restart() {
    clearInterval(timer);
    timer = setInterval(() => goTo(index + 1), AUTOPLAY_MS);
  }

  nextBtn.addEventListener("click", () => { goTo(index + 1); restart(); });
  prevBtn.addEventListener("click", () => { goTo(index - 1); restart(); });

  // Swipe support
  let touchStartX = 0;
  root.addEventListener("touchstart", (e) => { touchStartX = e.touches[0].clientX; }, { passive: true });
  root.addEventListener("touchend", (e) => {
    const delta = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(delta) > 40) {
      goTo(delta < 0 ? index + 1 : index - 1);
      restart();
    }
  }, { passive: true });

  // Pause on hover (desktop courtesy)
  root.addEventListener("mouseenter", () => clearInterval(timer));
  root.addEventListener("mouseleave", restart);

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!prefersReducedMotion) restart();
});