// Sticky navbar: solid background after scrolling past the top bar.
// Mobile menu toggle with basic aria-expanded handling.
document.addEventListener("DOMContentLoaded", function () {
  const header = document.querySelector(".site-header");
  const navbar = document.querySelector(".navbar");
  const toggle = document.querySelector(".nav-toggle");

  function onScroll() {
    if (window.scrollY > 24) {
      navbar.classList.add("is-scrolled");
    } else {
      navbar.classList.remove("is-scrolled");
    }
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  if (toggle && header) {
    toggle.addEventListener("click", function () {
      const isOpen = header.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  }
});