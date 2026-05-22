"use strict";
(function () {
  var MIN = 0.1, MAX = 8;
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }

  function naturalSize(svg) {
    var w = 0, h = 0;
    try {
      if (svg.viewBox && svg.viewBox.baseVal && svg.viewBox.baseVal.width) {
        w = svg.viewBox.baseVal.width; h = svg.viewBox.baseVal.height;
      }
    } catch (e) {}
    if (!w) { w = parseFloat(svg.getAttribute("width")) || 600; }
    if (!h) { h = parseFloat(svg.getAttribute("height")) || 400; }
    return { w: w, h: h };
  }

  function serialize(svg) {
    var clone = svg.cloneNode(true);
    if (!clone.getAttribute("xmlns")) clone.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    if (!clone.getAttribute("xmlns:xlink")) clone.setAttribute("xmlns:xlink", "http://www.w3.org/1999/xlink");
    return new XMLSerializer().serializeToString(clone);
  }

  function flash(box, msg) {
    var t = box._toast; if (!t) return;
    t.textContent = msg; t.classList.add("show");
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("show"); }, 1600);
  }

  function copySVG(box, svg) {
    var markup = serialize(svg);
    var fail = function () { flash(box, "Copy failed"); };
    if (navigator.clipboard && window.ClipboardItem) {
      try {
        navigator.clipboard.write([new ClipboardItem({
          "image/svg+xml": new Blob([markup], { type: "image/svg+xml" }),
          "text/plain": new Blob([markup], { type: "text/plain" })
        })]).then(function () { flash(box, "SVG copied to clipboard"); }, function () {
          navigator.clipboard.writeText(markup).then(
            function () { flash(box, "SVG copied (as text)"); }, fail);
        });
        return;
      } catch (e) {}
    }
    if (navigator.clipboard) {
      navigator.clipboard.writeText(markup).then(
        function () { flash(box, "SVG copied (as text)"); }, fail);
    } else { fail(); }
  }

  function copyPNG(box, svg, nat) {
    var fail = function (m) { flash(box, m || "Copy failed"); };
    if (!(navigator.clipboard && window.ClipboardItem)) {
      fail("Clipboard images not supported here"); return;
    }
    var markup = serialize(svg);
    var ratio = clamp((window.devicePixelRatio || 1) * 2, 2, 4);
    var img = new Image();
    var url = URL.createObjectURL(new Blob([markup], { type: "image/svg+xml;charset=utf-8" }));
    img.onload = function () {
      var c = document.createElement("canvas");
      c.width = Math.round(nat.w * ratio); c.height = Math.round(nat.h * ratio);
      var cx = c.getContext("2d");
      cx.fillStyle = "#ffffff"; cx.fillRect(0, 0, c.width, c.height);
      cx.drawImage(img, 0, 0, c.width, c.height);
      URL.revokeObjectURL(url);
      if (!c.toBlob) { fail(); return; }
      c.toBlob(function (png) {
        if (!png) { fail(); return; }
        navigator.clipboard.write([new ClipboardItem({ "image/png": png })]).then(
          function () { flash(box, "PNG copied to clipboard"); },
          function () { fail("Browser blocked image clipboard"); });
      }, "image/png");
    };
    img.onerror = function () { URL.revokeObjectURL(url); fail(); };
    img.src = url;
  }

  function enhance(box, viewport, stage, svg, nat) {
    box.classList.add("is-interactive");
    var scale = 1, tx = 0, ty = 0;
    function apply() {
      stage.style.transform = "translate(" + tx + "px," + ty + "px) scale(" + scale + ")";
    }
    function fit() {
      var vw = viewport.clientWidth, vh = viewport.clientHeight;
      if (!vw || !vh) { requestAnimationFrame(fit); return; }
      scale = clamp(Math.min(vw / nat.w, vh / nat.h), MIN, MAX);
      tx = (vw - nat.w * scale) / 2;
      ty = (vh - nat.h * scale) / 2;
      apply();
    }
    function zoomAt(cx, cy, factor) {
      var ns = clamp(scale * factor, MIN, MAX), k = ns / scale;
      tx = cx - k * (cx - tx); ty = cy - k * (cy - ty); scale = ns; apply();
    }
    function center() { return { x: viewport.clientWidth / 2, y: viewport.clientHeight / 2 }; }

    viewport.addEventListener("wheel", function (e) {
      e.preventDefault();
      var r = viewport.getBoundingClientRect();
      zoomAt(e.clientX - r.left, e.clientY - r.top, e.deltaY < 0 ? 1.12 : 1 / 1.12);
    }, { passive: false });

    var dragging = false, lx = 0, ly = 0;
    viewport.addEventListener("pointerdown", function (e) {
      dragging = true; lx = e.clientX; ly = e.clientY;
      viewport.classList.add("grabbing");
      try { viewport.setPointerCapture(e.pointerId); } catch (x) {}
    });
    viewport.addEventListener("pointermove", function (e) {
      if (!dragging) return;
      tx += e.clientX - lx; ty += e.clientY - ly; lx = e.clientX; ly = e.clientY; apply();
    });
    function endDrag() { dragging = false; viewport.classList.remove("grabbing"); }
    viewport.addEventListener("pointerup", endDrag);
    viewport.addEventListener("pointerleave", endDrag);
    viewport.addEventListener("pointercancel", endDrag);
    viewport.addEventListener("dblclick", function () { fit(); });

    var bar = document.createElement("div");
    bar.className = "diagram-toolbar";
    function btn(label, title, fn) {
      var b = document.createElement("button");
      b.type = "button"; b.textContent = label; b.title = title;
      b.addEventListener("click", function (e) { e.preventDefault(); fn(); });
      bar.appendChild(b);
    }
    btn("−", "Zoom out", function () { var c = center(); zoomAt(c.x, c.y, 1 / 1.25); });
    btn("+", "Zoom in", function () { var c = center(); zoomAt(c.x, c.y, 1.25); });
    btn("Fit", "Reset / fit to view (or double-click)", fit);
    btn("PNG", "Copy diagram to clipboard as PNG", function () { copyPNG(box, svg, nat); });
    btn("SVG", "Copy diagram to clipboard as SVG", function () { copySVG(box, svg); });
    box.appendChild(bar);

    var toast = document.createElement("div");
    toast.className = "diagram-toast";
    box.appendChild(toast);
    box._toast = toast;

    fit();
  }

  function setup(box) {
    var viewport = box.querySelector(".diagram-viewport");
    var stage = box.querySelector(".diagram-stage");
    var src = box.getAttribute("data-svg");
    if (!viewport || !stage || !src) return;
    var url;
    try { url = new URL(src, window.location.href).href; } catch (e) { return; }
    fetch(url).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.text();
    }).then(function (text) {
      var doc = new DOMParser().parseFromString(text, "image/svg+xml");
      var svg = doc.documentElement;
      if (!svg || svg.nodeName.toLowerCase() !== "svg") throw new Error("not svg");
      svg = document.importNode(svg, true);
      var nat = naturalSize(svg);
      svg.setAttribute("width", nat.w);
      svg.setAttribute("height", nat.h);
      stage.innerHTML = "";
      stage.appendChild(svg);
      enhance(box, viewport, stage, svg, nat);
    }).catch(function () { /* keep the static <object> fallback */ });
  }

  function init() {
    var boxes = document.querySelectorAll(".diagram[data-diagram]");
    for (var i = 0; i < boxes.length; i++) setup(boxes[i]);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
