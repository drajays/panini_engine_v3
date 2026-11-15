/* ashtadhyayi.com-style patha filter panel: chip rows + per-category negate. */
(function (global) {
  "use strict";

  function esc(s) {
    return String(s ?? "").replace(/[&<>"']/g, c => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));
  }

  function intersect(a, b) {
    const S = new Set(b);
    return a.filter(x => S.has(x));
  }

  /** One filter category: multi-select chips, optional negate. */
  function PathaFilters(host, spec, { title, kind, onChange } = {}) {
    this.host = typeof host === "string" ? document.getElementById(host) : host;
    this.spec = (spec || []).map(f => ({
      id: f.id,
      label: f.label,
      negate: false,
      options: f.options.map(o => ({ label: o.label, value: o.value, selected: false })),
    }));
    this.title = title || "Select filters";
    this.kind = kind || "item";
    this.onChange = onChange || (() => {});
    this.render();
  }

  PathaFilters.prototype.active = function () {
    return this.spec.some(f => f.options.some(o => o.selected));
  };

  PathaFilters.prototype.selected = function (fid) {
    const f = this.spec.find(x => x.id === fid);
    return f ? f.options.filter(o => o.selected).map(o => o.value) : [];
  };

  PathaFilters.prototype.isNegated = function (fid) {
    const f = this.spec.find(x => x.id === fid);
    return !!(f && f.negate);
  };

  /** Match one item's tag list (and optional field map) against all active filters. */
  PathaFilters.prototype.matches = function (tags, fields) {
    const T = tags || [];
    const F = fields || {};
    for (const f of this.spec) {
      const sel = f.options.filter(o => o.selected).map(o => o.value);
      if (!sel.length) continue;
      let hit;
      if (f.id === "gana" || f.id === "pada" || f.id === "idaagam" || f.id === "karma" || f.id === "linga") {
        const v = F[f.id];
        hit = sel.includes(String(v));
      } else {
        hit = intersect(sel, T).length > 0;
      }
      if (f.negate ? hit : !hit) return false;
    }
    return true;
  };

  PathaFilters.prototype.summary = function (count) {
    if (!this.active()) {
      return `<span class="pf-muted">No filters are active. Select a filter to get started.</span>`;
    }
    if (!count) return `<span>No ${esc(this.kind)}s match the given filter.</span>`;
    return `<span><b>${count.toLocaleString()}</b> ${esc(this.kind)}${count === 1 ? "" : "s"} match.</span>`;
  };

  PathaFilters.prototype.toQuery = function () {
    const parts = [];
    for (const f of this.spec) {
      const sel = f.options.filter(o => o.selected).map(o => o.value);
      if (!sel.length) continue;
      let p = f.id + "~" + sel.join(",");
      if (f.negate) p += "~N";
      parts.push(p);
    }
    return parts.join(";");
  };

  PathaFilters.prototype.fromQuery = function (q) {
    if (!q) return;
    for (const part of String(q).split(";")) {
      const bits = part.split("~");
      if (bits.length < 2) continue;
      const f = this.spec.find(x => x.id === bits[0]);
      if (!f) continue;
      const vals = bits[1].split(",");
      f.negate = bits[2] === "N";
      f.options.forEach(o => { o.selected = vals.includes(o.value); });
    }
    this.render();
  };

  PathaFilters.prototype.clear = function () {
    this.spec.forEach(f => {
      f.negate = false;
      f.options.forEach(o => { o.selected = false; });
    });
    this.render();
    this.onChange();
  };

  PathaFilters.prototype.render = function () {
    const rows = this.spec.map((f, fi) => {
      const chips = f.options.map((o, oi) =>
        `<button type="button" class="pf-chip${o.selected ? " on" : ""}${f.negate && o.selected ? " neg" : ""}" data-f="${fi}" data-o="${oi}">${esc(o.label)}</button>`
      ).join("");
      return `<div class="pf-row${f.negate ? " pf-negated" : ""}" data-f="${fi}">
        <div class="pf-cat"><span class="pf-lab">${esc(f.label)}</span><span class="pf-chev" aria-hidden="true">»</span></div>
        <div class="pf-chips">${chips}</div>
        <div class="pf-adv"><span class="pf-adv-lab">Advanced Option:</span>
          <button type="button" class="pf-negate${f.negate ? " on" : ""}" data-neg="${fi}" title="Exclude matching values">Negate this filter</button>
        </div>
      </div>`;
    }).join("");

    this.host.innerHTML = `<div class="pf-panel">
      <div class="pf-head">
        <div class="pf-title">${esc(this.title)}</div>
        <div class="pf-status" id="pf-status-${this.host.id || "x"}"></div>
        <button type="button" class="pf-clear" data-clear hidden>Clear filters</button>
      </div>
      <div class="pf-body">${rows}</div>
    </div>`;

    this.host.querySelectorAll(".pf-chip").forEach(btn => {
      btn.onclick = () => {
        const f = this.spec[+btn.dataset.f], o = f.options[+btn.dataset.o];
        o.selected = !o.selected;
        this.render();
        this.onChange();
      };
    });
    this.host.querySelectorAll(".pf-negate").forEach(btn => {
      btn.onclick = () => {
        const f = this.spec[+btn.dataset.neg];
        f.negate = !f.negate;
        this.render();
        this.onChange();
      };
    });
    const clr = this.host.querySelector("[data-clear]");
    if (clr) {
      clr.hidden = !this.active();
      clr.onclick = () => this.clear();
    }
  };

  PathaFilters.prototype.setStatus = function (count) {
    const el = this.host.querySelector(".pf-status");
    if (el) el.innerHTML = this.summary(count);
    const clr = this.host.querySelector("[data-clear]");
    if (clr) clr.hidden = !this.active();
  };

  global.PathaFilters = PathaFilters;
})(typeof window !== "undefined" ? window : globalThis);
