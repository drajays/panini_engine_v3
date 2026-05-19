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

import importlib
import inspect as _inspect
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

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
# Presentation-layer transliteration helpers
# (pure view code — never touches State internals)
# ─────────────────────────────────────────────────────────────────

# Structural step IDs → clean Devanāgarī labels shown in the UI.
_STRUCTURAL_DEV: dict[str, str] = {
    "__MERGE__"             : "पद-मेलनम्",
    "__FIXED_POINT__"       : "स्थिर-बिन्दुः",
    "__TRIPADI_ENTER__"     : "त्रिपाद्याः-प्रवेशः",
    "__ANGA_SWEEP__"        : "अङ्ग-परीक्षा",
    "__IT_LOPA_PASS__"      : "इत्-लोपः",
    "__SANDHI_PASS__"       : "सन्धिः",
    "__COMPOUND_MERGE__"    : "समास-मेलनम्",
}


def _slp1_str_to_dev(slp1_str: str) -> str:
    """
    Convert a flat SLP1 form string (as stored in trace form_before/form_after)
    to Devanāgarī for display.

    Strategy: parse the SLP1 string through the engine's phoneme parser so that
    conjunct consonants, mātrās, and halanta virāmas are rendered correctly by
    the joiner — identical to how State.flat_dev() works on the live State tape.

    Structural IDs (e.g. '__MERGE__') are mapped to Devanāgarī labels.
    Empty strings stay empty.  Unparseable strings fall back to the original.
    """
    if not slp1_str:
        return ""
    # Structural marker
    if slp1_str in _STRUCTURAL_DEV:
        return _STRUCTURAL_DEV[slp1_str]
    try:
        from phonology.varna import parse_slp1_upadesha_sequence
        from phonology.joiner import slp1_to_devanagari
        varnas = parse_slp1_upadesha_sequence(slp1_str)
        return slp1_to_devanagari(varnas)
    except Exception:
        return slp1_str  # safe fallback — never break the UI


def _enrich_trace(raw_trace: list[dict]) -> list[dict]:
    """
    Add presentation-layer fields to every trace step dict:

      form_before_dev   : Devanāgarī rendering of form_before (SLP1 → Dev)
      form_after_dev    : Devanāgarī rendering of form_after  (SLP1 → Dev)
      _sutra_text_dev   : sūtra text from SUTRA_REGISTRY (was already set inline)
      _padaccheda_dev   : padaccheda from SUTRA_REGISTRY
      _anuvritti_from   : list of IDs from SUTRA_REGISTRY
      _is_structural    : True for __MERGE__ etc.
      _structural_dev   : Devanāgarī label for structural steps

    The original SLP1 strings in form_before / form_after are left intact;
    only the _dev variants are added.  State objects are never imported here.
    """
    out = []
    for step in raw_trace:
        sid = step.get("sutra_id", "")
        rec = SUTRA_REGISTRY.get(sid) if sid and not sid.startswith("__") else None
        is_struct = bool(sid.startswith("__")) if sid else False

        fb = step.get("form_before", "") or ""
        fa = step.get("form_after",  "") or ""

        out.append({
            **step,
            # Devanāgarī transliterations (presentation only)
            "form_before_dev" : _slp1_str_to_dev(fb),
            "form_after_dev"  : _slp1_str_to_dev(fa),
            # Sūtra metadata from registry
            "_is_structural"  : is_struct,
            "_structural_dev" : _STRUCTURAL_DEV.get(sid, "") if is_struct else "",
            "_sutra_text_dev" : getattr(rec, "text_dev",       None),
            "_padaccheda_dev" : getattr(rec, "padaccheda_dev", None),
            "_anuvritti_from" : list(getattr(rec, "anuvritti_from", ()) or ()),
        })
    return out


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

    enriched = _enrich_trace(state.trace)

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

# Paradigm presets — shown as quick-load buttons in matrix + showcase pages.
_PARADIGM_PRESETS: list[dict] = [
    {
        "stem_slp1"  : "rADA",
        "stem_dev"   : "राधा",
        "linga"      : "strīliṅga",
        "class_short": "अकारान्त · स्त्री",
        "class_dev"  : "आकारान्त स्त्रीलिङ्गम् (ā-anta)",
        "samjna_dev" : [],
        "featured"   : False,
    },
    {
        "stem_slp1"  : "rAma",
        "stem_dev"   : "रामः",
        "linga"      : "pulliṅga",
        "class_short": "अकारान्त",
        "class_dev"  : "अकारान्त पुंलिङ्गम्",
        "samjna_dev" : [],
        "featured"   : False,
    },
    {
        "stem_slp1"  : "hari",
        "stem_dev"   : "हरिः",
        "linga"      : "pulliṅga",
        "class_short": "इकारान्त · घि",
        "class_dev"  : "इकारान्त पुंलिङ्गम् (घिसंज्ञक)",
        "samjna_dev" : ["घिसंज्ञक (१.४.७)"],
        "featured"   : False,
    },
    {
        "stem_slp1"  : "SamBu",
        "stem_dev"   : "शम्भुः",
        "linga"      : "pulliṅga",
        "class_short": "उकारान्त · घि",
        "class_dev"  : "उकारान्त पुंलिङ्गम् (घिसंज्ञक)",
        "samjna_dev" : ["घिसंज्ञक (१.४.७)"],
        "featured"   : True,
    },
    {
        "stem_slp1"  : "sarva",
        "stem_dev"   : "सर्वः",
        "linga"      : "pulliṅga",
        "class_short": "सर्वनाम",
        "class_dev"  : "अकारान्त सर्वनाम पुंलिङ्गम्",
        "samjna_dev" : ["सर्वनाम (१.१.२७)"],
        "featured"   : False,
    },
    {
        "stem_slp1"  : "anya",
        "stem_dev"   : "अन्यः",
        "linga"      : "pulliṅga",
        "class_short": "सर्वनाम",
        "class_dev"  : "अकारान्त सर्वनाम पुंलिङ्गम् (अन्य)",
        "samjna_dev" : ["सर्वनाम (१.१.२७)"],
        "featured"   : False,
    },
    {
        "stem_slp1"  : "guru",
        "stem_dev"   : "गुरुः",
        "linga"      : "pulliṅga",
        "class_short": "उकारान्त · घि",
        "class_dev"  : "उकारान्त पुंलिङ्गम् (घिसंज्ञक)",
        "samjna_dev" : ["घिसंज्ञक (१.४.७)"],
        "featured"   : True,
    },
]


def _load_gold_for_stem(stem: str, linga: str) -> dict[str, str]:
    """Auto-load gold reference for (stem, linga) from subanta_gold directory."""
    gold_dir = _ROOT / "data" / "reference" / "subanta_gold"
    if not gold_dir.exists():
        return {}
    suffix = {"pulliṅga": "pullinga", "strīliṅga": "strilinga",
               "napuṃsaka": "napumsaka"}.get(linga, "pullinga")
    for fname in (f"{stem}_{suffix}.json", f"{stem.lower()}_{suffix}.json"):
        p = gold_dir / fname
        if p.exists():
            gdata = json.loads(p.read_text(encoding="utf-8"))
            return {c: d["form_dev"] for c, d in gdata.get("cells", {}).items()}
    for jf in sorted(gold_dir.glob("*.json")):
        try:
            gdata = json.loads(jf.read_text(encoding="utf-8"))
            if gdata.get("stem_slp1") == stem and gdata.get("linga") == linga:
                return {c: d["form_dev"] for c, d in gdata.get("cells", {}).items()}
        except Exception:
            pass
    return {}


@app.route("/matrix")
def matrix():
    stem = request.args.get("stem", "rAma")
    return render_template(
        "matrix.html",
        nav_active="matrix",
        stem=stem,
        vibhakti_dev=_VIBHAKTI_DEV,
        vacana_dev=_VACANA_DEV,
        presets=_PARADIGM_PRESETS,
        cov=coverage_report(SUTRA_REGISTRY),
    )


@app.route("/api/matrix")
def api_matrix():
    """Derive all 24 cells and return {cell: {surface_dev, path}}."""
    stem  = request.args.get("stem", "rAma")
    linga = request.args.get("linga", "pulliṅga")

    gold = _load_gold_for_stem(stem, linga)

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

    match_count = sum(1 for c in cells.values() if c.get("match") is True)
    return jsonify({
        "stem"        : stem,
        "linga"       : linga,
        "cells"       : cells,
        "has_gold"    : bool(gold),
        "match_count" : match_count,
        "total_cells" : 24,
    })


# ─────────────────────────────────────────────────────────────────
# पाठ-विश्लेषण — text / śloka analysis
# ─────────────────────────────────────────────────────────────────

@app.route("/patha")
def patha_page():
    from pipelines.patha_pipeline import get_form_index, lexicon_info
    index = get_form_index()          # build + cache on first request
    lex   = lexicon_info()
    return render_template(
        "patha.html",
        nav_active="patha",
        cov=coverage_report(SUTRA_REGISTRY),
        lexicon=lex,
        lexicon_count=len(lex),
        index_forms=len(index),
    )


@app.route("/api/patha/analyze", methods=["POST"])
def api_patha_analyze():
    data = request.get_json(force=True)
    text = (data.get("text") or "").strip()
    if not text:
        return jsonify({"error": "empty text"}), 400
    from pipelines.patha_pipeline import analyze_patha
    return jsonify(analyze_patha(text))


@app.route("/api/patha/trace", methods=["POST"])
def api_patha_trace():
    """Full prakriyā trace for one (stem, vibhakti, vacana, linga) tuple."""
    data  = request.get_json(force=True)
    stem  = (data.get("stem_slp1") or "").strip()
    vibh  = int(data.get("vibhakti", 1))
    vac   = int(data.get("vacana",   1))
    linga = data.get("linga", "pulliṅga")
    if not stem:
        return jsonify({"error": "stem_slp1 required"}), 400
    try:
        state = derive(stem, vibh, vac, linga=linga)
    except Exception as ex:
        return jsonify({"error": f"{type(ex).__name__}: {ex}"}), 500
    from phonology.joiner import slp1_to_devanagari
    surface_dev = slp1_to_devanagari(state.terms[0].varnas) if state.terms else ""
    enriched = _enrich_trace(state.trace)
    tr = state.trace
    return jsonify({
        "stem_slp1"   : stem,
        "vibhakti"    : vibh,
        "vacana"      : vac,
        "linga"       : linga,
        "surface_dev" : surface_dev,
        "surface_slp1": state.render(),
        "trace"       : enriched,
        "stats": {
            "total_steps"   : len(tr),
            "applied_count" : sum(1 for s in tr if s.get("status") == "APPLIED"),
            "blocked_count" : sum(1 for s in tr if s.get("status") == "BLOCKED"),
            "skipped_count" : sum(1 for s in tr if s.get("status") == "SKIPPED"),
        },
    })


# ─────────────────────────────────────────────────────────────────
# Paradigm showcase — शम्भु development page
# ─────────────────────────────────────────────────────────────────

@app.route("/showcase")
def showcase_page():
    return render_template(
        "showcase.html",
        nav_active="showcase",
        cov=coverage_report(SUTRA_REGISTRY),
        vibhakti_dev=_VIBHAKTI_DEV,
        vacana_dev=_VACANA_DEV,
        presets=_PARADIGM_PRESETS,
    )


@app.route("/api/paradigm-presets")
def api_paradigm_presets():
    return jsonify({"presets": _PARADIGM_PRESETS})


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
# Pipeline showcase — auto-discovery
# ─────────────────────────────────────────────────────────────────

_EXCLUDED_PIPELINE_STEMS = frozenset({
    "subanta", "subanta_trc", "krdanta", "tinanta",
    "dhatupatha", "preflight_lopa_samjna", "dik_caturthi_glassbox_text",
})

_CATEGORY_ORDER = [
    "Corrected", "Kṛdanta", "Tiṅanta", "Taddhita", "Samāsa", "Paribhāṣā", "Demo",
]

_PIPELINE_CATALOG: list[dict[str, Any]] | None = None


def _categorize_pipeline(stem: str) -> str:
    s = stem.lower()
    if "corrected" in s:
        return "Corrected"
    if any(x in s for x in [
        "_kta_", "_ktri_", "ktavatu", "nistha", "_kvip", "_kvi_",
        "_ghurac_", "_lyuw_", "_lyap_", "krdanta",
    ]):
        return "Kṛdanta"
    if any(x in s for x in [
        "_lat_", "_lag_", "_lun_", "_lut_", "_lig_", "_lit_", "_lrt_",
        "tinanta", "atmanepada", "parasmaipada", "_nic_", "_kyaz_", "_san_",
        "split_prakriyas",
    ]):
        return "Tiṅanta"
    if any(x in s for x in ["taddhita", "saliya", "maliya", "matup"]):
        return "Taddhita"
    if any(x in s for x in ["samasa", "bahuvrihi", "dvandva", "tatpurusha"]):
        return "Samāsa"
    if "_note_" in s or "paribhasha" in s or s.endswith("_note"):
        return "Paribhāṣā"
    return "Demo"


def _build_pipeline_catalog() -> list[dict[str, Any]]:
    global _PIPELINE_CATALOG
    if _PIPELINE_CATALOG is not None:
        return _PIPELINE_CATALOG

    pipelines_dir = _ROOT / "pipelines"
    catalog: list[dict[str, Any]] = []

    for py_file in sorted(pipelines_dir.glob("*.py")):
        stem = py_file.stem
        if stem.startswith("_") or stem in _EXCLUDED_PIPELINE_STEMS:
            continue
        mod_name = f"pipelines.{stem}"
        try:
            mod = importlib.import_module(mod_name)
        except Exception as ex:
            catalog.append({
                "key": f"{stem}__error",
                "stem": stem,
                "fn_name": "— import error —",
                "category": _categorize_pipeline(stem),
                "description": f"Import failed: {type(ex).__name__}: {ex}",
                "needs_args": False,
                "error": True,
            })
            continue

        fns_added = 0
        for fn_name, fn in _inspect.getmembers(mod, _inspect.isfunction):
            if fn.__module__ != mod_name:
                continue
            if not (fn_name.startswith("derive_") or fn_name == "derive"):
                continue
            sig = _inspect.signature(fn)
            needs_args = any(
                p.default is _inspect.Parameter.empty
                for p in sig.parameters.values()
            )
            doc = _inspect.getdoc(fn) or _inspect.getdoc(mod) or ""
            first_line = next(
                (ln.strip() for ln in doc.splitlines() if ln.strip()), stem
            )
            catalog.append({
                "key": f"{stem}__{fn_name}",
                "stem": stem,
                "fn_name": fn_name,
                "category": _categorize_pipeline(stem),
                "description": first_line,
                "needs_args": needs_args,
                "error": False,
            })
            fns_added += 1

    order = {c: i for i, c in enumerate(_CATEGORY_ORDER)}
    catalog.sort(key=lambda p: (order.get(p["category"], 99), p["stem"], p["fn_name"]))
    _PIPELINE_CATALOG = catalog
    return catalog


@app.route("/pipelines")
def pipelines_page():
    cat = _build_pipeline_catalog()
    count = sum(1 for p in cat if not p.get("error"))
    return render_template(
        "pipelines.html",
        nav_active="pipelines",
        cov=coverage_report(SUTRA_REGISTRY),
        pipeline_count=count,
    )


@app.route("/api/pipelines")
def api_pipelines():
    cat = _build_pipeline_catalog()
    seen: set[str] = set()
    categories: list[str] = []
    for p in cat:
        c = p["category"]
        if c not in seen:
            seen.add(c)
            categories.append(c)
    return jsonify({"pipelines": cat, "categories": categories})


@app.route("/api/pipeline/<path:key>", methods=["POST"])
def api_pipeline_run(key: str):
    """Run a single demo pipeline by catalog key (stem__fn_name)."""
    cat = _build_pipeline_catalog()
    entry = next((p for p in cat if p["key"] == key), None)
    if entry is None:
        return jsonify({"error": f"pipeline '{key}' not found"}), 404
    if entry.get("error"):
        return jsonify({"error": entry["description"]}), 500
    if entry["needs_args"]:
        return jsonify({"error": "Pipeline requires arguments — not auto-runnable."}), 400

    stem, fn_name = entry["stem"], entry["fn_name"]
    try:
        mod = importlib.import_module(f"pipelines.{stem}")
    except Exception as ex:
        return jsonify({"error": f"Import failed: {ex}"}), 500

    fn = getattr(mod, fn_name, None)
    if fn is None:
        return jsonify({"error": f"Function {fn_name} not found."}), 404

    try:
        state = fn()
    except Exception as ex:
        import traceback as _tb
        return jsonify({
            "error": f"{type(ex).__name__}: {ex}",
            "traceback": _tb.format_exc()[-2000:],
        }), 500

    from phonology.joiner import slp1_to_devanagari
    try:
        all_varnas = [v for t in state.terms for v in t.varnas]
        surface_dev = slp1_to_devanagari(all_varnas) if all_varnas else ""
    except Exception:
        surface_dev = ""

    surface_slp1 = ""
    try:
        surface_slp1 = state.flat_slp1()
    except Exception:
        pass
    if not surface_slp1:
        try:
            surface_slp1 = state.render()
        except Exception:
            pass

    enriched = _enrich_trace(state.trace)

    tr = state.trace
    return jsonify({
        "key": key,
        "fn_name": fn_name,
        "category": entry["category"],
        "description": entry["description"],
        "surface_dev": surface_dev,
        "surface_slp1": surface_slp1,
        "trace": enriched,
        "stats": {
            "total_steps": len(tr),
            "applied_count": sum(
                1 for s in tr if s.get("status") in {"APPLIED", "APPLIED_VACUOUS"}
            ),
            "audit_count":   sum(1 for s in tr if s.get("status") == "AUDIT"),
            "blocked_count": sum(1 for s in tr if s.get("status") == "BLOCKED"),
            "skipped_count": sum(1 for s in tr if s.get("status") == "SKIPPED"),
        },
    })


# ─────────────────────────────────────────────────────────────────
# Tiṅanta derivation
# ─────────────────────────────────────────────────────────────────

@app.route("/tinanta")
def tinanta_page():
    lak_meta_path = _ROOT / "data" / "inputs" / "lakara_metadata.json"
    lak_meta = {}
    if lak_meta_path.exists():
        lak_meta = json.loads(lak_meta_path.read_text(encoding="utf-8"))
    lakara_choices = {k: v for k, v in lak_meta.items() if not k.startswith("_")}
    return render_template(
        "tinanta.html",
        nav_active="tinanta",
        cov=coverage_report(SUTRA_REGISTRY),
        lakara_choices=lakara_choices,
    )


@app.route("/api/tinanta", methods=["POST"])
def api_tinanta():
    from pipelines.tinanta import derive as tin_derive, _dhatu_row_by_upadesha
    data    = request.get_json(force=True)
    dhatu   = (data.get("dhatu") or "BU").strip()
    lakara  = (data.get("lakara") or "laT").strip()
    prayoga = (data.get("prayoga") or "kartari").strip()
    purusha = int(data.get("purusha", 3))
    vacana  = int(data.get("vacana", 1))

    if not dhatu:
        return jsonify({"error": "dhatu required"}), 400
    if prayoga not in ("kartari", "karmani", "bhave"):
        return jsonify({"error": "prayoga must be kartari/karmani/bhave"}), 400

    # Normalize Devanāgarī input
    if any(0x0900 <= ord(c) <= 0x097F for c in dhatu):
        from pipelines.dhatupatha import _payload, _envelope
        env = _envelope(_payload())
        match = next(
            (e for e in env["entries"]
             if e.get("mula_dhatu_dev","").strip() == dhatu.strip()),
            None
        )
        if not match:
            return jsonify({"error": f"Devanāgarī dhātu '{dhatu}' not found"}), 404
        dhatu = match["upadesha_slp1"]

    try:
        row = _dhatu_row_by_upadesha(dhatu)
    except KeyError as e:
        return jsonify({"error": str(e)}), 404

    supported_gana = row.get("gana", 1)
    # lṛṭ/laṅ: vikaraṇa selection is gaṇa-independent for these lakāras.
    if lakara not in ("lRT", "laG", "liG", "AsIrliG", "luG", "lRG") and supported_gana not in (1, 4, 6):
        return jsonify({
            "warning": f"Gaṇa {supported_gana} vikaraṇa not yet implemented; using bhvādi logic.",
            "gana_override": 1,
        }), 202

    try:
        state = tin_derive(dhatu, lakara, prayoga, purusha, vacana)
    except NotImplementedError as e:
        return jsonify({"error": f"Not implemented: {e}"}), 501
    except Exception as ex:
        return jsonify({"error": f"{type(ex).__name__}: {ex}"}), 500

    surface_dev  = state.flat_dev()
    surface_slp1 = state.flat_slp1()

    enriched = _enrich_trace(state.trace)

    tr = state.trace
    return jsonify({
        "dhatu_slp1"  : dhatu,
        "dhatu_dev"   : row.get("mula_dhatu_dev", dhatu),
        "artha_dev"   : row.get("artha_dev", ""),
        "artha_en"    : row.get("artha_en", ""),
        "gana"        : row.get("gana", 1),
        "gana_dev"    : row.get("gana_label_dev", ""),
        "pada_dev"    : row.get("pada_label_dev", ""),
        "lakara"      : lakara,
        "prayoga"     : prayoga,
        "purusha"     : purusha,
        "vacana"      : vacana,
        "surface_dev" : surface_dev,
        "surface_slp1": surface_slp1,
        "trace"       : enriched,
        "stats": {
            "total_steps"   : len(tr),
            "applied_count" : sum(1 for s in tr if s.get("status") in {"APPLIED","APPLIED_VACUOUS"}),
            "audit_count"   : sum(1 for s in tr if s.get("status") == "AUDIT"),
            "skipped_count" : sum(1 for s in tr if s.get("status") == "SKIPPED"),
        },
    })


@app.route("/api/tinanta/paradigm", methods=["POST"])
def api_tinanta_paradigm():
    """Derive all 9 parasmaipada cells for a dhātu + lakāra."""
    from pipelines.tinanta import derive as tin_derive, _dhatu_row_by_upadesha
    data    = request.get_json(force=True)
    dhatu   = (data.get("dhatu") or "BU").strip()
    lakara  = (data.get("lakara") or "laT").strip()
    prayoga = (data.get("prayoga") or "kartari").strip()
    pada    = (data.get("pada") or "parasmai").strip()

    try:
        row = _dhatu_row_by_upadesha(dhatu)
    except KeyError as e:
        return jsonify({"error": str(e)}), 404

    from phonology.joiner import slp1_to_devanagari
    PURUSHA_ORDER = [3, 2, 1]
    VACANA_ORDER  = [1, 2, 3]

    cells = {}
    for p in PURUSHA_ORDER:
        for v in VACANA_ORDER:
            key = f"{p}-{v}"
            try:
                state = tin_derive(dhatu, lakara, prayoga, p, v)
                cells[key] = {
                    "surface_dev" : state.flat_dev(),
                    "surface_slp1": state.flat_slp1(),
                }
            except Exception as ex:
                cells[key] = {"error": f"{type(ex).__name__}: {ex}"}

    return jsonify({
        "dhatu_slp1": dhatu,
        "dhatu_dev" : row.get("mula_dhatu_dev", dhatu),
        "lakara"    : lakara,
        "pada"      : pada,
        "cells"     : cells,
    })


# ─────────────────────────────────────────────────────────────────
# All-10-lakāra paradigm page
# ─────────────────────────────────────────────────────────────────

_ALL_LAKARAS = [
    ("laT",      "लट्",   "Present"),
    ("liT",      "लिट्",  "Perfect"),
    ("luT",      "लुट्",  "Periphrastic Future"),
    ("lRT",      "लृट्",  "Simple Future"),
    ("loT",      "लोट्",  "Imperative"),
    ("laG",      "लङ्",   "Imperfect"),
    ("liG",      "विधिलिङ्", "Optative"),
    ("AsIrliG",  "आशीर्लिङ्", "Benedictive"),
    ("luG",      "लुङ्",  "Aorist"),
    ("lRG",      "लृङ्",  "Conditional"),
]


@app.route("/tinanta/all")
def tinanta_all_page():
    lak_meta_path = _ROOT / "data" / "inputs" / "lakara_metadata.json"
    lak_meta = {}
    if lak_meta_path.exists():
        lak_meta = json.loads(lak_meta_path.read_text(encoding="utf-8"))
    return render_template(
        "tinanta_all.html",
        nav_active="tinanta",
        cov=coverage_report(SUTRA_REGISTRY),
        all_lakaras=_ALL_LAKARAS,
        lak_meta=lak_meta,
    )


@app.route("/api/tinanta/all_lakara", methods=["POST"])
def api_tinanta_all_lakara():
    """Derive all 9 cells × 10 lakāras for a dhātu."""
    from pipelines.tinanta import derive as tin_derive, _dhatu_row_by_upadesha
    data    = request.get_json(force=True)
    dhatu   = (data.get("dhatu") or "paW").strip()
    prayoga = (data.get("prayoga") or "kartari").strip()

    try:
        row = _dhatu_row_by_upadesha(dhatu)
    except KeyError as e:
        return jsonify({"error": str(e)}), 404

    result: dict[str, Any] = {}
    for (lak_id, lak_dev, lak_en) in _ALL_LAKARAS:
        cells: dict[str, Any] = {}
        for p in (3, 2, 1):
            for v in (1, 2, 3):
                key = f"{p}-{v}"
                try:
                    state = tin_derive(dhatu, lak_id, prayoga, p, v)
                    cells[key] = {
                        "surface_dev" : state.flat_dev(),
                        "surface_slp1": state.flat_slp1(),
                    }
                except NotImplementedError as e:
                    cells[key] = {"error": f"Not implemented: {e}"}
                except Exception as ex:
                    cells[key] = {"error": f"{type(ex).__name__}: {ex}"}
        result[lak_id] = {
            "lak_dev" : lak_dev,
            "lak_en"  : lak_en,
            "cells"   : cells,
        }

    return jsonify({
        "dhatu_slp1" : dhatu,
        "dhatu_dev"  : row.get("mula_dhatu_dev", dhatu),
        "artha_dev"  : row.get("artha_dev", ""),
        "artha_en"   : row.get("artha_en", ""),
        "gana"       : row.get("gana", 1),
        "gana_dev"   : row.get("gana_label_dev", ""),
        "pada_dev"   : row.get("pada_label_dev", ""),
        "prayoga"    : prayoga,
        "lakaras"    : result,
    })


# ─────────────────────────────────────────────────────────────────
# Dhātupātha browser
# ─────────────────────────────────────────────────────────────────

@app.route("/dhatufilters")
def dhatufilters_page():
    return render_template(
        "dhatufilters.html",
        nav_active="dhatufilters",
        cov=coverage_report(SUTRA_REGISTRY),
        all_lakaras=_ALL_LAKARAS,
    )


@app.route("/dhatupatha")
def dhatupatha_page():
    return render_template(
        "dhatupatha.html",
        nav_active="dhatupatha",
        cov=coverage_report(SUTRA_REGISTRY),
    )


@app.route("/api/dhatupatha")
def api_dhatupatha_list():
    """List/search dhātus from data/inputs/dhatupatha_upadesha.json."""
    from pipelines.dhatupatha import _payload, _envelope
    env     = _envelope(_payload())
    entries = env["entries"]

    q       = (request.args.get("q") or "").strip().lower()
    gana    = request.args.get("gana", "")
    pada    = request.args.get("pada", "")
    it_cls  = request.args.get("it", "")     # set | anit | vet
    karma   = request.args.get("karma", "")  # sakarmaka | akarmaka
    limit   = min(int(request.args.get("limit", 50)), 200)
    offset  = int(request.args.get("offset", 0))

    filtered = []
    for e in entries:
        if gana and str(e.get("gana","")) != gana:
            continue
        if pada:
            pl = e.get("pada_label_dev","")
            if pada == "parasmai" and "परस्मैपदी" not in pl:
                continue
            if pada == "atmane" and "आत्मनेपदी" not in pl:
                continue
            if pada == "ubhaya" and "उभयपदी" not in pl:
                continue
        if it_cls:
            fl = e.get("flags", {}) or {}
            if it_cls == "set"  and not (fl.get("set") and not fl.get("anit")):
                continue
            if it_cls == "anit" and not fl.get("anit"):
                continue
            if it_cls == "vet"  and not fl.get("vet"):
                continue
        if karma:
            km = e.get("karmatva_label_dev", "") or ""
            if karma == "sakarmaka"  and "सकर्मक" not in km:
                continue
            if karma == "akarmaka"   and "अकर्मक" not in km:
                continue
        if q:
            haystack = (
                e.get("upadesha_slp1","") + " " +
                e.get("mula_dhatu_dev","") + " " +
                e.get("artha_dev","") + " " +
                e.get("artha_en","")
            ).lower()
            if q not in haystack:
                continue
        filtered.append({
            "id"          : e.get("id",""),
            "slp1"        : e.get("upadesha_slp1",""),
            "dev"         : e.get("mula_dhatu_dev",""),
            "artha_dev"   : e.get("artha_dev",""),
            "artha_en"    : e.get("artha_en",""),
            "gana"        : e.get("gana",1),
            "gana_dev"    : e.get("gana_label_dev",""),
            "pada_dev"    : e.get("pada_label_dev",""),
            "it_class"    : e.get("it_class_label_dev",""),
            "karmatva"    : e.get("karmatva_label_dev",""),
        })

    total = len(filtered)
    page  = filtered[offset:offset+limit]
    return jsonify({
        "total"   : total,
        "offset"  : offset,
        "limit"   : limit,
        "entries" : page,
    })


@app.route("/api/dhatupatha/<dhatu_id>")
def api_dhatupatha_detail(dhatu_id: str):
    from pipelines.tinanta import _dhatu_row_by_upadesha
    try:
        row = _dhatu_row_by_upadesha(dhatu_id)
    except KeyError as e:
        abort(404)
    return jsonify(row)


# ─────────────────────────────────────────────────────────────────
# Sūtra quick reference (from sutra_ref_out JSON)
# ─────────────────────────────────────────────────────────────────

_SUTRA_REF_CACHE: dict | None = None


def _load_sutra_ref() -> dict:
    global _SUTRA_REF_CACHE
    if _SUTRA_REF_CACHE is not None:
        return _SUTRA_REF_CACHE
    p = _ROOT / "data" / "reference" / "sutra_quick_ref.json"
    if p.exists():
        _SUTRA_REF_CACHE = json.loads(p.read_text(encoding="utf-8"))
    else:
        _SUTRA_REF_CACHE = {}
    return _SUTRA_REF_CACHE


@app.route("/api/sutra-ref/<sid>")
def api_sutra_ref(sid: str):
    ref = _load_sutra_ref()
    data = ref.get(sid)
    if not data:
        return jsonify({"error": f"sūtra {sid} not in quick-ref"}), 404
    rec = SUTRA_REGISTRY.get(sid)
    return jsonify({
        **data,
        "sutra_id"    : sid,
        "implemented" : rec is not None,
        "sutra_type"  : rec.sutra_type.name if rec else None,
        "why_dev"     : getattr(rec, "why_dev", None),
        "anuvritti"   : list(getattr(rec, "anuvritti_from", ()) or ()),
    })


@app.route("/api/sutra-ref/search")
def api_sutra_ref_search():
    q     = (request.args.get("q") or "").strip().lower()
    limit = min(int(request.args.get("limit", 30)), 100)
    ref   = _load_sutra_ref()
    if not q:
        return jsonify({"results": []})
    results = []
    for sid, data in ref.items():
        hay = (data.get("dev","") + " " + data.get("slp1","") + " " +
               data.get("gloss_en","") + " " + sid).lower()
        if q in hay:
            results.append({"sid": sid, **data})
        if len(results) >= limit:
            break
    return jsonify({"results": results, "total": len(results)})


# ─────────────────────────────────────────────────────────────────
# सर्वनाम — pronoun paradigm (अस्मद्)
# ─────────────────────────────────────────────────────────────────

@app.route("/sarvanama")
def sarvanama_page():
    return render_template("sarvanama.html", nav_active="sarvanama",
                           cov=coverage_report(SUTRA_REGISTRY))


@app.route("/api/sarvanama", methods=["POST"])
def api_sarvanama():
    """Return all 21 cells for asmad paradigm."""
    data = request.get_json(force=True)
    pronoun = data.get("pronoun", "asmad")  # future: yuzmad too

    from pipelines.asmad_subanta import derive_asmad
    from phonology.joiner import slp1_to_devanagari

    cells = {}
    VIBHAKTI_DEV = {1: "प्रथमा", 2: "द्वितीया", 3: "तृतीया", 4: "चतुर्थी",
                    5: "पञ्चमी", 6: "षष्ठी", 7: "सप्तमी"}
    VACANA_DEV = {1: "एकवचन", 2: "द्विवचन", 3: "बहुवचन"}

    for v in range(1, 8):  # 7 vibhaktis for pronouns
        for vac in range(1, 4):
            key = f"{v}-{vac}"
            try:
                state = derive_asmad(v, vac)
                surface = state.flat_dev() if hasattr(state, "flat_dev") else ""
                cells[key] = {
                    "surface_dev": surface,
                    "vibhakti_dev": VIBHAKTI_DEV[v],
                    "vacana_dev": VACANA_DEV[vac],
                }
            except Exception as ex:
                cells[key] = {
                    "surface_dev": f"त्रुटिः: {ex}",
                    "vibhakti_dev": VIBHAKTI_DEV[v],
                    "vacana_dev": VACANA_DEV[vac],
                }

    return jsonify({"pronoun": pronoun, "cells": cells})


@app.route("/api/sarvanama/trace", methods=["POST"])
def api_sarvanama_trace():
    """Return trace for a single asmad cell."""
    data = request.get_json(force=True)
    v    = int(data.get("vibhakti", 1))
    vac  = int(data.get("vacana", 1))
    from pipelines.asmad_subanta import derive_asmad
    try:
        state = derive_asmad(v, vac)
        surface = state.flat_dev() if hasattr(state, "flat_dev") else ""
        enriched = _enrich_trace(state.trace)
        return jsonify({"surface_dev": surface, "trace": enriched})
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


# ─────────────────────────────────────────────────────────────────
# कृदन्तम् — kṛdanta derivation (tṛc / ṇvul)
# ─────────────────────────────────────────────────────────────────

@app.route("/krdanta")
def krdanta_page():
    try:
        from pipelines.dhatupatha import list_tfc_demo_ids
        demo_ids = list_tfc_demo_ids()[:20]
    except Exception:
        demo_ids = ["BU", "BvAdi_ciY", "qupa~c~z", "RIY", "kf", "gama~", "dfSi~"]
    return render_template("krdanta.html", nav_active="krdanta",
                           cov=coverage_report(SUTRA_REGISTRY),
                           demo_ids=demo_ids)


@app.route("/api/krdanta", methods=["POST"])
def api_krdanta():
    data     = request.get_json(force=True)
    dhatu_id = (data.get("dhatu_id") or "BU").strip()
    krt_type = data.get("krt_type", "tfc")  # tfc or nvul
    try:
        from pipelines.dhatupatha import get_dhatu_row
        row = get_dhatu_row(dhatu_id)
        if not row:
            return jsonify({"error": f"Unknown dhatu: {dhatu_id}"}), 400
        upadesha = row.get("upadesha_slp1") or row.get("id") or dhatu_id
        udatta   = bool(row.get("flags", {}).get("udatta", False))

        if krt_type == "tfc":
            from pipelines.krdanta import derive_tfc_pratipadika
            from pipelines.subanta_trc import derive_trc_nom_sg_from_state
            tfc_state = derive_tfc_pratipadika(upadesha, udatta_dhatu=udatta)
            nom_state = derive_trc_nom_sg_from_state(tfc_state, vibhakti=1, vacana=1, linga="pulliṅga")
            surface   = nom_state.flat_dev() if hasattr(nom_state, "flat_dev") else ""
            enriched  = _enrich_trace(nom_state.trace)
            return jsonify({
                "surface_dev": surface,
                "trace": enriched,
                "dhatu_id": dhatu_id,
                "krt_type": krt_type,
            })
        elif krt_type == "nvul":
            from pipelines.krdanta import derive_krt
            # Use generic derive_krt with Nvul; stem label derived from upadesha
            label = upadesha.replace("~", "").rstrip("\\") + "aka"
            nvul_state = derive_krt(
                upadesha,
                krt_upadesha_slp1="Nvul",
                merge_pratipadika_label=label,
            )
            surface  = nvul_state.flat_dev() if hasattr(nvul_state, "flat_dev") else ""
            enriched = _enrich_trace(nvul_state.trace)
            return jsonify({
                "surface_dev": surface,
                "trace": enriched,
                "dhatu_id": dhatu_id,
                "krt_type": krt_type,
            })
        else:
            return jsonify({"error": f"Unsupported krt_type: {krt_type}"}), 400
    except Exception as ex:
        import traceback as _tb
        return jsonify({
            "error": f"{type(ex).__name__}: {ex}",
            "traceback": _tb.format_exc()[-2000:],
        }), 500


# ─────────────────────────────────────────────────────────────────
# देवेन्द्र / सूर्योदय — samāsa demo
# ─────────────────────────────────────────────────────────────────

@app.route("/devendra")
def devendra_page():
    return render_template("devendra.html", nav_active="devendra",
                           cov=coverage_report(SUTRA_REGISTRY))


@app.route("/api/devendra", methods=["POST"])
def api_devendra():
    """Derive one of the samāsa examples: devendraH or sUryodayaH."""
    data    = request.get_json(force=True)
    example = (data.get("example") or "devendra").strip().lower()
    from pipelines.devendra import derive_devendraH, derive_sUryodayaH
    try:
        if example == "suryodaya":
            state = derive_sUryodayaH()
            title = "सूर्योदयः"
        else:
            state = derive_devendraH()
            title = "देवेन्द्रः"
        surface  = state.flat_dev() if hasattr(state, "flat_dev") else ""
        enriched = _enrich_trace(state.trace)
        tr = state.trace
        return jsonify({
            "example"      : example,
            "title_dev"    : title,
            "surface_dev"  : surface,
            "surface_slp1" : state.flat_slp1() if hasattr(state, "flat_slp1") else "",
            "trace"        : enriched,
            "stats": {
                "total_steps"   : len(tr),
                "applied_count" : sum(1 for s in tr if s.get("status") in {"APPLIED","APPLIED_VACUOUS"}),
                "audit_count"   : sum(1 for s in tr if s.get("status") == "AUDIT"),
                "blocked_count" : sum(1 for s in tr if s.get("status") == "BLOCKED"),
                "skipped_count" : sum(1 for s in tr if s.get("status") == "SKIPPED"),
            },
        })
    except Exception as ex:
        import traceback as _tb
        return jsonify({
            "error"    : f"{type(ex).__name__}: {ex}",
            "traceback": _tb.format_exc()[-2000:],
        }), 500


# ─────────────────────────────────────────────────────────────────
# दिक्-समासः — dik compound demo
# ─────────────────────────────────────────────────────────────────

@app.route("/dik")
def dik_page():
    return render_template("dik.html", nav_active="dik",
                           cov=coverage_report(SUTRA_REGISTRY))


@app.route("/api/dik/glass", methods=["POST"])
def api_dik_glass():
    """Return glassbox explanation rows for a dik-samāsa preset."""
    data = request.get_json(force=True)
    pid  = (data.get("preset") or "uttarA_pUrvA").strip()
    try:
        from pipelines.dik_caturthi_glassbox_text import glass_rows
        from pipelines.dik_uttarapurva_demo import caturthi_preset
        p    = caturthi_preset(pid)
        rows = glass_rows(p)
        return jsonify({
            "preset"  : pid,
            "title"   : p.title_short_deva,
            "rows"    : [{"label": r[0], "sa": r[1], "slp1": r[2], "hindi": r[3]}
                         for r in rows],
        })
    except Exception as ex:
        return jsonify({"error": f"{type(ex).__name__}: {ex}"}), 500


# ─────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import os as _os
    _port = int(_os.environ.get("PANINI_PORT", 5000))
    print("═" * 60)
    print(f"  Pāṇini Engine v3 — Web UI")
    print(f"  Registry: {len(SUTRA_REGISTRY)} sūtras loaded")
    print(f"  Open: http://localhost:{_port}")
    print("═" * 60)
    app.run(host="127.0.0.1", port=_port, debug=False)
