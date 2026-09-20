/* Aperture Media: small, dependency-free enhancements. The site works without JS. */
(function () {
  "use strict";
  var doc = document;

  /* ---- mobile navigation ---- */
  var header = doc.querySelector(".site-header");
  var toggle = doc.querySelector(".menu-toggle");
  if (header && toggle) {
    var setOpen = function (open) {
      header.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
      toggle.textContent = open ? "Close" : "Menu";
      doc.body.style.overflow = open ? "hidden" : "";
    };
    toggle.addEventListener("click", function () { setOpen(!header.classList.contains("is-open")); });
    doc.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && header.classList.contains("is-open")) { setOpen(false); toggle.focus(); }
    });
    header.querySelectorAll(".nav a").forEach(function (a) {
      a.addEventListener("click", function () { setOpen(false); });
    });
    window.addEventListener("resize", function () { if (window.innerWidth > 999) setOpen(false); });
  }

  /* ---- work filters ---- */
  var filterBar = doc.querySelector("[data-filters]");
  if (filterBar) {
    var cards = doc.querySelectorAll("[data-cats]");
    var status = doc.querySelector("[data-filter-status]");
    filterBar.addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-filter]");
      if (!btn) return;
      var f = btn.getAttribute("data-filter");
      filterBar.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", String(b === btn)); });
      var shown = 0;
      cards.forEach(function (c) {
        var match = f === "all" || c.getAttribute("data-cats").split(" ").indexOf(f) > -1;
        c.hidden = !match;
        if (match) shown++;
      });
      if (status) status.textContent = shown + (shown === 1 ? " project shown" : " projects shown");
    });
  }

  /* ---- before / after slider ---- */
  doc.querySelectorAll(".ba").forEach(function (ba) {
    var input = ba.querySelector("input[type=range]");
    if (!input) return;
    var update = function () { ba.style.setProperty("--pos", input.value + "%"); };
    input.addEventListener("input", update);
    update();
  });

  /* ---- contact form ---- */
  var form = doc.querySelector("[data-contact-form]");
  if (form) {
    var statusEl = form.querySelector(".form-status");
    var email = form.getAttribute("data-email") || "";
    var show = function (kind, msg) {
      statusEl.hidden = false;
      statusEl.className = "form-status form-status--" + kind;
      statusEl.textContent = msg;
      statusEl.focus();
    };
    var clearErrors = function () {
      form.querySelectorAll("[aria-invalid]").forEach(function (el) { el.removeAttribute("aria-invalid"); });
      form.querySelectorAll(".field-error").forEach(function (el) { el.remove(); });
    };
    var flag = function (el, msg) {
      el.setAttribute("aria-invalid", "true");
      var p = doc.createElement("p");
      p.className = "field-error"; p.id = el.id + "-err"; p.textContent = msg;
      el.setAttribute("aria-describedby", p.id);
      el.parentNode.appendChild(p);
    };

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      clearErrors();
      var name = form.elements["name"], mail = form.elements["email"], details = form.elements["details"];
      var bad = null;
      if (!name.value.trim()) { flag(name, "Enter your name."); bad = bad || name; }
      if (!/^\S+@\S+\.\S+$/.test(mail.value.trim())) { flag(mail, "Enter a valid email address."); bad = bad || mail; }
      if (!details.value.trim()) { flag(details, "Tell us a little about the project."); bad = bad || details; }
      if (bad) { bad.focus(); return; }

      var endpoint = form.getAttribute("data-endpoint");
      var data = new FormData(form);
      var btn = form.querySelector("button[type=submit]");
      btn.disabled = true; btn.textContent = "Sending…";

      var opts = endpoint
        ? { method: "POST", body: data, headers: { Accept: "application/json" } }
        : { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: new URLSearchParams(data).toString() };

      fetch(endpoint || "/", opts).then(function (r) {
        if (!r.ok) throw new Error("bad status");
        form.reset();
        show("ok", "Thanks, we have your details. We will reply within one business day.");
      }).catch(function () {
        show("error", "That did not send. Please email us at " + email + " instead.");
      }).finally(function () {
        btn.disabled = false; btn.textContent = "Send project details";
      });
    });
  }
})();
