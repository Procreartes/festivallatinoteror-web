(function () {
  "use strict";
  try { document.documentElement.classList.remove("sin-js"); } catch (e) {}

  // Menú móvil
  try {
    var boton = document.querySelector(".boton-menu");
    var menu = document.getElementById("menu");
    if (boton && menu) {
      boton.addEventListener("click", function () {
        var abierto = menu.classList.toggle("abierto");
        boton.setAttribute("aria-expanded", abierto ? "true" : "false");
      });
      menu.addEventListener("click", function (e) {
        if (e.target && e.target.tagName === "A") {
          menu.classList.remove("abierto");
          boton.setAttribute("aria-expanded", "false");
        }
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && menu.classList.contains("abierto")) {
          menu.classList.remove("abierto");
          boton.setAttribute("aria-expanded", "false");
          boton.focus();
        }
      });
    }
  } catch (e) {}

  // Aparición al hacer scroll (si falla, el CSS muestra todo igualmente)
  try {
    var elementos = document.querySelectorAll(".aparece");
    if ("IntersectionObserver" in window && elementos.length) {
      var obs = new IntersectionObserver(function (entradas) {
        entradas.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("visible"); obs.unobserve(en.target); }
        });
      }, { rootMargin: "0px 0px -8% 0px" });
      elementos.forEach(function (el) { obs.observe(el); });
    } else {
      elementos.forEach(function (el) { el.classList.add("visible"); });
    }
  } catch (e) {}

  // Año del pie
  try {
    var anio = document.getElementById("anio");
    if (anio) anio.textContent = String(new Date().getFullYear());
  } catch (e) {}
})();
