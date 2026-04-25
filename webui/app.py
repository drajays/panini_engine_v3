#!/usr/bin/env python3
"""
webui/app.py — Flask web UI for Pāṇini Engine v3.
──────────────────────────────────────────────────

Run:
    pip install flask
    cd panini_engine_v3
    python -m webui.app
    # open http://localhost:5000

Zero build step.  Serves Devanāgarī-ready HTML.  Reads the live
SUTRA_REGISTRY and renders traces, matrix, and SIG graph on demand.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

from flask import Flask, render_template, request, jsonify, abort

# Ensure repo root importable when launched as a module.
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sutras  # noqa: F401 — fills SUTRA_REGISTRY
from engine            import SUTRA_REGISTRY, coverage_report, SutraType
from engine.sig        import extract_applied_path
from pipelines.subanta import derive


app = Flask(__name__, template_folder="templates", static_folder="static")


# ─────────────────────────────────────────────────────────────────
# Home / nav
# ─────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("derive.html",
                           nav_active="derive",
                           cov=coverage_report(SUTRA_REGISTRY))


# ─────────────────────────────────────────────────────────────────
# Derivation
# ─────────────────────────────────────────────────────────────────

@app.route("/api/derive", methods=["POST"])
def api_derive():
    data   = request.get_json(force=True)
    stem   = data.get("stem", "rAma").strip()
    vib    = int(data.get("vibhakti", 1))
    vac    = int(data.get("vacana", 1))
    linga  = data.get("linga", "pulliṅga")

    if not stem:
        return jsonify({"error": "empty stem"}), 400
    if not (1 <= vib <= 8) or not (1 <= vac <= 3):
        return jsonify({"error": "vibhakti must be 1-8 and vacana 1-3"}), 400

    try:
        state = derive(stem, vib, vac, linga=linga)
    except Exception as ex:
        return jsonify({"error": f"{type(ex).__name__}: {ex}"}), 500

    # Render surface.
    from phonology.joiner import slp1_to_devanagari
    surface_dev = (
        slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    )
    applied_path = extract_applied_path(state.trace)

    # Annotate trace rows with sūtra metadata for the UI.
    enriched = []
    for step in state.trace:
        sid = step.get("sutra_id", "")
        rec = SUTRA_REGISTRY.get(sid) if sid and not sid.startswith("__") else None
        enriched.append({
            **step,
            "_is_structural" : sid.startswith("__") if sid else False,
            "_sutra_text_dev": getattr(rec, "text_dev",   None),
            "_padaccheda_dev": getattr(rec, "padaccheda_dev", None),
            "_anuvritti_from": list(getattr(rec, "anuvritti_from", ()) or ()),
        })

    return jsonify({
        "stem"         : stem,
        "vibhakti"     : vib,
        "vacana"       : vac,
        "linga"        : linga,
        "surface_dev"  : surface_dev,
        "surface_slp1" : state.render(),
        "phase"        : state.phase,
        "applied_path" : applied_path,
        "trace"        : enriched,
        "stats": {
            "total_steps"   : len(state.trace),
            "applied_count" : sum(1 for s in state.trace if s.get("status") == "APPLIED"),
            "audit_count"   : sum(1 for s in state.trace if s.get("status") == "AUDIT"),
            "blocked_count" : sum(1 for s in state.trace if s.get("status") == "BLOCKED"),
            "skipped_count" : sum(1 for s in state.trace if s.get("status") == "SKIPPED"),
        },
    })


# ─────────────────────────────────────────────────────────────────
# 24-cell matrix
# ─────────────────────────────────────────────────────────────────

_VIBHAKTI_DEV = {
    1: "प्रथमा", 2: "द्वितीया", 3: "तृतीया", 4: "चतुर्थी",
    5: "पञ्चमी", 6: "षष्ठी",     7: "सप्तमी", 8: "सम्बोधन",
}
_VACANA_DEV = {1: "एकवचन", 2: "द्विवचन", 3: "बहुवचन"}


@app.route("/matrix")
def matrix():
    stem = request.args.get("stem", "rAma")
    return render_template(
        "matrix.html",
        nav_active="matrix",
        stem=stem,
        vibhakti_dev=_VIBHAKTI_DEV,
        vacana_dev=_VACANA_DEV,
        cov=coverage_report(SUTRA_REGISTRY),
    )


@app.route("/api/matrix")
def api_matrix():
    """Derive all 24 cells and return {cell: {surface_dev, path}}."""
    stem  = request.args.get("stem", "rAma")
    linga = request.args.get("linga", "pulliṅga")

    # Load gold if present for comparison.
    gold_path = _ROOT / "data" / "reference" / "subanta_gold" / "rama_pullinga.json"
    gold = {}
    if stem == "rAma" and gold_path.exists():
        gdata = json.loads(gold_path.read_text(encoding="utf-8"))
        gold = {c: d["form_dev"] for c, d in gdata.get("cells", {}).items()}

    from phonology.joiner import slp1_to_devanagari

    cells = {}
    for v in range(1, 9):
        for vv in range(1, 4):
            key = f"{v}-{vv}"
            try:
                state = derive(stem, v, vv, linga=linga)
                produced = (slp1_to_devanagari(state.terms[0].varnas)
                            if state.terms else "")
                cells[key] = {
                    "surface_dev"  : produced,
                    "surface_slp1" : state.render(),
                    "gold_dev"     : gold.get(key),
                    "match"        : (produced == gold.get(key))
                                     if gold.get(key) else None,
                    "applied_path" : extract_applied_path(state.trace),
                    "step_count"   : len(state.trace),
                }
            except Exception as ex:
                cells[key] = {"error": f"{type(ex).__name__}: {ex}"}

    return jsonify({"stem": stem, "linga": linga, "cells": cells})


# ─────────────────────────────────────────────────────────────────
# Sūtra detail
# ─────────────────────────────────────────────────────────────────

@app.route("/sutra/<sid>")
def sutra_detail(sid):
    rec = SUTRA_REGISTRY.get(sid)
    if rec is None:
        abort(404)
    return render_template(
        "sutra.html",
        nav_active=None,
        sid=sid,
        rec={
            "sutra_id"       : rec.sutra_id,
            "sutra_type"     : rec.sutra_type.name,
            "text_slp1"      : rec.text_slp1,
            "text_dev"       : rec.text_dev,
            "padaccheda_dev" : rec.padaccheda_dev,
            "why_dev"        : rec.why_dev,
            "anuvritti_from" : list(rec.anuvritti_from or ()),
            "adhikara_scope" : list(rec.adhikara_scope or ()),
            "blocks_sutra_ids": list(rec.blocks_sutra_ids or ()),
        },
    )


@app.route("/api/sutras")
def api_sutras():
    """All sūtras grouped by type — for registry listing."""
    by_type = {}
    for sid, rec in sorted(
        SUTRA_REGISTRY.items(),
        key=lambda p: tuple(int(x) for x in p[0].split(".")),
    ):
        by_type.setdefault(rec.sutra_type.name, []).append({
            "sutra_id"  : sid,
            "text_dev"  : rec.text_dev,
            "why_dev"   : rec.why_dev,
        })
    return jsonify({
        "by_type"  : by_type,
        "coverage" : coverage_report(SUTRA_REGISTRY),
    })


# ─────────────────────────────────────────────────────────────────
# Registry listing page
# ─────────────────────────────────────────────────────────────────

@app.route("/sutras")
def sutras_listing():
    return render_template("sutras.html",
                           nav_active="sutras",
                           cov=coverage_report(SUTRA_REGISTRY))


# ─────────────────────────────────────────────────────────────────
# SIG graph
# ─────────────────────────────────────────────────────────────────

@app.route("/sig")
def sig_page():
    return render_template("sig_graph.html",
                           nav_active="sig",
                           cov=coverage_report(SUTRA_REGISTRY))


@app.route("/api/sig/<name>")
def api_sig(name):
    """Serve any SIG JSON artifact by filename (e.g. 'sutra_interaction_graph')."""
    allowed = {
        "sutra_fire_stats", "sutra_edge_stats", "sutra_interaction_graph",
        "sig_critical_path", "sig_transitions", "sig_linguistic",
        "sig_baseline", "sig_anomalies", "sutra_next_candidates",
        "global_sutra_frequencies", "global_sutra_edges", "global_markov_transitions",
        "coverage",
    }
    if name not in allowed:
        abort(404)
    path = _ROOT / "sig" / f"{name}.json"
    if not path.exists():
        return jsonify({
            "error": f"{name}.json not found. Run: python -m tools.sig_benchmark --freeze"
        }), 404
    return jsonify(json.loads(path.read_text(encoding="utf-8")))


# ─────────────────────────────────────────────────────────────────
# Test suite runner
# ─────────────────────────────────────────────────────────────────

@app.route("/tests")
def tests_page():
    return render_template("tests.html",
                           nav_active="tests",
                           cov=coverage_report(SUTRA_REGISTRY))


@app.route("/api/run-tests", methods=["POST"])
def api_run_tests():
    """Run pytest, return summary."""
    t0 = time.perf_counter()
    try:
        r = subprocess.run(
            [sys.executable, "-m", "pytest", "tests/", "-q", "--no-header",
             "--tb=short"],
            cwd=str(_ROOT),
            capture_output=True,
            text=True,
            timeout=60,
        )
    except subprocess.TimeoutExpired:
        return jsonify({"error": "pytest timed out (60s)"}), 504
    elapsed = time.perf_counter() - t0

    return jsonify({
        "returncode" : r.returncode,
        "stdout"     : r.stdout[-8000:],
        "stderr"     : r.stderr[-2000:],
        "elapsed_s"  : round(elapsed, 2),
    })


@app.route("/api/run-sig", methods=["POST"])
def api_run_sig():
    """Regenerate SIG JSON files."""
    freeze = request.json.get("freeze", False) if request.is_json else False
    args = [sys.executable, "-m", "tools.sig_benchmark"]
    if freeze:
        args.append("--freeze")
    try:
        r = subprocess.run(args, cwd=str(_ROOT), capture_output=True,
                           text=True, timeout=30)
    except subprocess.TimeoutExpired:
        return jsonify({"error": "sig_benchmark timed out (30s)"}), 504
    return jsonify({
        "returncode": r.returncode,
        "stdout"    : r.stdout,
        "stderr"    : r.stderr[-1000:],
    })


# ─────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("═" * 60)
    print(f"  Pāṇini Engine v3 — Web UI")
    print(f"  Registry: {len(SUTRA_REGISTRY)} sūtras loaded")
    print(f"  Open: http://localhost:5000")
    print("═" * 60)
    app.run(host="127.0.0.1", port=5000, debug=False)
