/* ==========================================================================
   FAQ Accordion — toggles +/× icons on <details> elements
   ========================================================================== */
document.addEventListener("DOMContentLoaded", function () {
  var items = document.querySelectorAll(".home-redesign .accordion-item details");
  if (items.length === 0) return;

  items.forEach(function (item) {
    var summary = item.querySelector(".accordion-header");
    var icon = item.querySelector(".acc-icon");

    function updateIcon() {
      if (item.open) {
        icon.textContent = "−";
      } else {
        icon.textContent = "+";
      }
    }

    summary.addEventListener("click", function () {
      setTimeout(updateIcon, 0);
    });

    updateIcon();
  });
});
