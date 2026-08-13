/* CME — Centre for Multidisciplinary Education, IIT Bombay
   Minimal vanilla JS: theme toggle + mobile menu only. No dependencies. */
(function () {
  "use strict";
  var root = document.documentElement;

  var stored = null;
  try { stored = localStorage.getItem("cme-theme"); } catch (e) {}
  var prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  root.setAttribute("data-theme", stored || (prefersDark ? "dark" : "light"));

  function toggleTheme() {
    var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("cme-theme", next); } catch (e) {}
  }

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  /* Plays the loading curtain, then calls done(). The logo travels by measuring both
     rects and transforming the difference (a FLIP move), so it lands exactly on the
     header brand whatever the viewport size. Plays once per session. */
  function runCurtain(curtain, done) {
    var HOLD = 1000;    /* lockup stays whole this long */
    var FLIGHT = 800;   /* matches the .pl-logo transition */
    var LEAD = 180;     /* reveals start this early, so their first (expensive) frame
                           lands before the flight rather than on top of it */
    var logo = curtain.querySelector(".pl-logo");
    var mark = document.querySelector(".site-header .brand .mark");
    var finished = false, released = false;

    /* hand the page back just before the backdrop starts fading, so the hero rises in
       through it rather than popping in once the curtain is fully gone */
    function release() {
      if (released) return;
      released = true;
      done();
    }

    function finish() {
      if (finished) return;
      finished = true;
      root.classList.remove("is-loading");
      if (curtain.parentNode) curtain.parentNode.removeChild(curtain);
      release();
    }

    function fly() {
      if (finished) return;
      if (logo && mark) {
        var a = logo.getBoundingClientRect();
        var b = mark.getBoundingClientRect();
        if (a.width && b.width) {
          var to =
            "translate(" + ((b.left + b.width / 2) - (a.left + a.width / 2)).toFixed(2) + "px," +
                           ((b.top + b.height / 2) - (a.top + a.height / 2)).toFixed(2) + "px) " +
            "scale(" + (b.width / a.width).toFixed(4) + ")";
          var played = false;
          /* drive it with the Web Animations API where possible: it starts on the
             compositor on its next frame, instead of depending on a style change
             being noticed as a transition (which can snap instead of glide) */
          if (logo.animate) {
            try {
              logo.animate([{ transform: "none" }, { transform: to }],
                { duration: FLIGHT, easing: "cubic-bezier(.55,.06,.2,1)", fill: "forwards" });
              played = true;
            } catch (e) {}
          }
          if (!played) logo.style.transform = to;   /* CSS transition fallback */
        }
      }
      curtain.classList.add("exit");
      setTimeout(finish, FLIGHT);
    }

    setTimeout(release, HOLD - LEAD);
    setTimeout(fly, HOLD);
    /* safety net: a stuck transition must never leave the site behind a curtain */
    setTimeout(finish, HOLD + FLIGHT + 1200);
  }

  ready(function () {
    var motion = root.classList.contains("js-anim");

    /* scroll reveal — fade + rise as sections enter the viewport.
       Reuses the existing .reveal / data-d markup. Only runs when js-anim is set
       (i.e. motion is allowed); otherwise content stays fully visible. */
    function initReveals() {
      var revealEls = document.querySelectorAll(".reveal");
      if ("IntersectionObserver" in window && revealEls.length) {
        var io = new IntersectionObserver(function (entries) {
          entries.forEach(function (en) {
            if (en.isIntersecting) {
              en.target.classList.add("is-visible");
              io.unobserve(en.target);
            }
          });
        }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
        revealEls.forEach(function (el) { io.observe(el); });
        /* failsafe: if anything is still hidden after 1.8s (e.g. observer never
           fired), reveal it so content can never get stuck invisible. */
        setTimeout(function () {
          document.querySelectorAll(".reveal:not(.is-visible)").forEach(function (el) {
            var r = el.getBoundingClientRect();
            if (r.top < (window.innerHeight || 800)) el.classList.add("is-visible");
          });
        }, 1800);
      } else {
        revealEls.forEach(function (el) { el.classList.add("is-visible"); });
      }
    }

    /* loading curtain — the CME lockup holds centre stage, then the logo flies into
       the header brand while the backdrop fades. <html>.is-loading was set by the
       inline script in the page head, so the curtain is already up by the time we
       get here; all this does is play it out and take it down.
       Reveals are held back until it lifts, so the hero animates in for the visitor
       rather than behind the curtain.
       Runs on every load/refresh by design - to show it once per session instead,
       gate the head script on a sessionStorage flag. */
    var curtain = document.getElementById("preloader");
    if (motion && curtain && root.classList.contains("is-loading")) runCurtain(curtain, initReveals);
    else if (motion) initReveals();

    /* header: solidify (border + shadow) once the page is scrolled */
    var header = document.querySelector(".site-header");
    if (header) {
      var onScroll = function () {
        header.classList.toggle("scrolled", window.scrollY > 8);
      };
      onScroll();
      window.addEventListener("scroll", onScroll, { passive: true });
    }

    /* animated counters for the headline stat strip */
    if (motion && "IntersectionObserver" in window) {
      var countEls = document.querySelectorAll(".stats .num");
      var countUp = function (el) {
        var suf = el.querySelector(".suf");
        var textNode = el.firstChild && el.firstChild.nodeType === 3 ? el.firstChild : null;
        var raw = textNode ? textNode.nodeValue : el.textContent;
        var target = parseInt(String(raw).replace(/[^0-9]/g, ""), 10);
        if (isNaN(target)) return;
        var setVal = function (v) {
          if (textNode) textNode.nodeValue = v;
          else el.insertBefore(document.createTextNode(v), suf || null);
        };
        setVal(0);
        var dur = 1200, startTs = null, done = false;
        var step = function (ts) {
          if (done) return;
          if (startTs === null) startTs = ts;
          var p = Math.min((ts - startTs) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          setVal(Math.round(eased * target));
          if (p < 1) requestAnimationFrame(step);
          else done = true;
        };
        requestAnimationFrame(step);
        /* safety net: if rAF is throttled/never completes, guarantee the final
           value so a counter can never get stuck on a partial number. */
        setTimeout(function () { if (!done) { done = true; setVal(target); } }, dur + 400);
      };
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { countUp(en.target); cio.unobserve(en.target); }
        });
      }, { threshold: 0.4 });
      countEls.forEach(function (el) { cio.observe(el); });
    }

    /* theme toggle */
    document.querySelectorAll("[data-theme-toggle]").forEach(function (b) {
      b.addEventListener("click", toggleTheme);
    });

    /* mobile menu */
    var menu = document.getElementById("mobileMenu");
    var mBtn = document.getElementById("menuBtn");
    if (mBtn && menu) {
      function setMenuOpen(open) {
        menu.classList.toggle("open", open);
        document.body.style.overflow = open ? "hidden" : "";
        mBtn.setAttribute("aria-expanded", open ? "true" : "false");
        mBtn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      }
      mBtn.addEventListener("click", function () {
        setMenuOpen(!menu.classList.contains("open"));
      });
      menu.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", function () { setMenuOpen(false); });
      });
      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape" && menu.classList.contains("open")) {
          setMenuOpen(false);
          mBtn.focus();
        }
      });
    }

    /* student seminar modal (students page) */
    var modal = document.getElementById("stuModal");
    var dataEl = document.getElementById("stu-data");
    var stuData = null;
    if (dataEl) { try { stuData = JSON.parse(dataEl.textContent); } catch (e) {} }
    if (modal && stuData) {
      var mBody = document.getElementById("stuModalBody");
      var mName = document.getElementById("stuModalName");
      var mMeta = document.getElementById("stuModalMeta");
      var mAv = document.getElementById("stuModalAv");
      var lastFocus = null;

      function initials(n) {
        var p = String(n || "").trim().split(/\s+/);
        return (p.length === 1 ? p[0].slice(0, 2) : p[0][0] + p[p.length - 1][0]).toUpperCase();
      }
      function esc(s) {
        var d = document.createElement("div");
        d.textContent = s == null ? "" : s;
        return d.innerHTML;
      }
      function openStu(i) {
        var s = stuData[i];
        if (!s) return;
        lastFocus = document.activeElement;
        mAv.textContent = initials(s.name);
        mName.textContent = s.name;
        var meta = "Batch of " + esc(s.batch);
        if (s.email) meta += ' · <a href="mailto:' + esc(s.email) + '">' + esc(s.email) + "</a>";
        mMeta.innerHTML = meta;
        var rows = "";
        (s.seminars || []).forEach(function (sm) {
          var topic = sm.topic && sm.topic.trim();
          var t = topic
            ? '<div class="sem-topic">' + esc(topic) + "</div>"
            : '<div class="sem-topic empty">Seminar in progress</div>';
          var sub = [];
          if (sm.term) sub.push(esc(sm.term));
          if (sm.guide && sm.guide.trim()) sub.push("Guide · " + esc(sm.guide));
          var m2 = sub.length ? '<div class="sem-meta">' + sub.join(" &nbsp;·&nbsp; ") + "</div>" : "";
          rows += '<div class="sem-item"><span class="sem-tag">' + esc(sm.sem || "—") +
                  '</span><div class="sem-body">' + t + m2 + "</div></div>";
        });
        mBody.innerHTML = rows || '<p style="color:var(--ink-3)">No seminars recorded yet.</p>';
        modal.hidden = false;
        document.body.style.overflow = "hidden";
        var c = modal.querySelector(".stu-modal-close");
        if (c) c.focus();
      }
      function closeStu() {
        modal.hidden = true;
        document.body.style.overflow = "";
        if (lastFocus && lastFocus.focus) lastFocus.focus();
      }
      document.querySelectorAll(".stu[data-stu]").forEach(function (card) {
        var idx = +card.getAttribute("data-stu");
        card.addEventListener("click", function () { openStu(idx); });
        card.addEventListener("keydown", function (e) {
          if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openStu(idx); }
        });
      });
      modal.querySelectorAll("[data-stu-close]").forEach(function (el) {
        el.addEventListener("click", closeStu);
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && !modal.hidden) closeStu();
      });
    }
  });
})();
