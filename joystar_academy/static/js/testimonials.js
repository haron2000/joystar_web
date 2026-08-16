document.addEventListener("DOMContentLoaded", function () {
  const root = document.querySelector("[data-testimonials]");
  if (!root) return;

  const slides = Array.from(root.querySelectorAll(".testimonial-slide"));
  const dotsWrap = root.querySelector(".testimonial-dots");
  if (slides.length <= 1) return;

  let index = 0;
  slides.forEach((_, i) => {
    const dot = document.createElement("button");
    dot.className = "hero-dot" + (i === 0 ? " is-active" : "");
    dot.setAttribute("aria-label", "Show testimonial " + (i + 1));
    dot.addEventListener("click", () => goTo(i));
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

  setInterval(() => goTo(index + 1), 6000);
});