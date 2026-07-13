/* CME — Centre for Multidisciplinary Education, IIT Bombay
   Vanilla JS: no external dependencies (privacy-friendly, works offline) */
(function () {
  "use strict";
  var root = document.documentElement;

  /* ---------- Theme ---------- */
  var stored = null;
  try { stored = localStorage.getItem("cme-theme"); } catch (e) {}
  var prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  root.setAttribute("data-theme", stored || (prefersDark ? "dark" : "light"));

  function toggleTheme() {
    var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("cme-theme", next); } catch (e) {}
  }

  /* ---------- On DOM ready ---------- */
  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    /* theme toggles */
    document.querySelectorAll("[data-theme-toggle]").forEach(function (b) {
      b.addEventListener("click", toggleTheme);
    });

    /* mobile menu */
    var menu = document.getElementById("mobileMenu");
    var mBtn = document.getElementById("menuBtn");
    if (mBtn && menu) {
      mBtn.addEventListener("click", function () {
        var open = menu.classList.toggle("open");
        document.body.style.overflow = open ? "hidden" : "";
        mBtn.setAttribute("aria-expanded", open ? "true" : "false");
      });
      menu.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", function () {
          menu.classList.remove("open");
          document.body.style.overflow = "";
        });
      });
    }

    /* header scroll state */
    var header = document.querySelector(".site-header");
    function onScroll() {
      var y = window.scrollY || window.pageYOffset;
      if (header) header.classList.toggle("scrolled", y > 12);
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    /* scroll reveal */
    var reveals = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window && reveals.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
      reveals.forEach(function (el) { io.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add("in"); });
    }

    /* animated counters */
    function animateCount(el) {
      var target = parseFloat(el.getAttribute("data-count"));
      var dec = (el.getAttribute("data-dec") | 0);
      var dur = 1400, start = null;
      function step(ts) {
        if (!start) start = ts;
        var p = Math.min((ts - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        var val = target * eased;
        el.textContent = dec ? val.toFixed(dec) : Math.round(val).toString();
        if (p < 1) requestAnimationFrame(step);
        else el.textContent = dec ? target.toFixed(dec) : target.toString();
      }
      requestAnimationFrame(step);
    }
    var counters = document.querySelectorAll("[data-count]");
    if ("IntersectionObserver" in window && counters.length) {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { animateCount(en.target); cio.unobserve(en.target); }
        });
      }, { threshold: 0.6 });
      counters.forEach(function (el) { cio.observe(el); });
    }

    /* FAQ accordion */
    document.querySelectorAll(".faq-q").forEach(function (q) {
      q.addEventListener("click", function () {
        var item = q.closest(".faq-item");
        var ans = item.querySelector(".faq-a");
        var open = item.classList.toggle("open");
        ans.style.maxHeight = open ? ans.scrollHeight + "px" : 0;
      });
    });

    /* Students: search + filter */
    var searchInput = document.getElementById("stuSearch");
    var filterBtns = document.querySelectorAll("[data-filter]");
    var cards = document.querySelectorAll("[data-student]");
    var activeFilter = "all";
    function applyStudents() {
      var term = (searchInput && searchInput.value || "").toLowerCase().trim();
      var shown = 0;
      cards.forEach(function (c) {
        var batch = c.getAttribute("data-batch");
        var hay = c.getAttribute("data-search") || "";
        var matchF = activeFilter === "all" || batch === activeFilter;
        var matchS = !term || hay.indexOf(term) !== -1;
        var show = matchF && matchS;
        c.style.display = show ? "" : "none";
        if (show) shown++;
      });
      var empty = document.getElementById("stuEmpty");
      if (empty) empty.style.display = shown ? "none" : "block";
    }
    if (searchInput) searchInput.addEventListener("input", applyStudents);
    filterBtns.forEach(function (b) {
      b.addEventListener("click", function () {
        filterBtns.forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active");
        activeFilter = b.getAttribute("data-filter");
        applyStudents();
      });
    });

  });
})();
