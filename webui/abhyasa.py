"""
webui/abhyasa.py — JSON for the अभ्यास tab (/practice): sanskritabhyas.in's drills, answered by the engine.

All question logic lives in core/abhyasa.py (plan: docs/ABHYASA_PLAN.md). This blueprint only adapts it to HTTP and
renders an explanation as the site's shared derivation view expects (webui/app._pack).
"""
from __future__ import annotations

from typing import Any

from flask import Blueprint, jsonify, request

from core import abhyasa as A

bp = Blueprint("abhyasa", __name__)


def _err(ex: Exception, code: int = 400):
    return jsonify({"error": f"{type(ex).__name__}: {ex}"[:400]}), code


@bp.get("/api/abhyasa/catalog")
def catalog():
    return jsonify(A.catalog())


@bp.post("/api/abhyasa/question")
def question():
    q = request.get_json(force=True) or {}
    try:
        return jsonify(A.question(q.get("family", "noun"), q.get("drill", "mcq"), int(q.get("level") or 1),
                                  q.get("filters") or {}, q.get("seed")))
    except (LookupError, ValueError) as ex:
        return _err(ex, 404)


@bp.post("/api/abhyasa/paradigm")
def paradigm():
    """पूर्ण रूप / तुलना: one whole table (noun, pronoun, number, verb, nāmadhātu)."""
    q = request.get_json(force=True) or {}
    strict = not q.get("vidyut_fallback")
    try:
        if q.get("family") == "verb":
            p = A.verb_paradigm(q["ref"], q.get("lakara") or "laT", q.get("prayoga") or "kartari", q.get("pada") or "",
                                q.get("sanadi") or "", q.get("prefix") or "", strict, 40.0)
        elif q.get("family") == "namadhatu":
            p = A.namadhatu_paradigm(q["stem"], q["pratyaya"], q.get("lakara") or "laT")
        else:
            p = A.noun_paradigm(q["stem"], q.get("linga") or "pulliṅga", strict)
    except (KeyError, LookupError, ValueError) as ex:
        return _err(ex, 404)
    return jsonify({**p, "cells": [{**c, "dev": A.dev(c["primary"]), "accepted_dev": [A.dev(a) for a in c["accepted"]]}
                                   for c in p["cells"]]})


@bp.get("/api/abhyasa/list")
def lists():
    a = request.args
    return jsonify(A.lists(a.get("family", "noun"), a.get("q", ""), a.get("anta", ""), a.get("linga", ""),
                           int(a.get("limit", 200))))


@bp.post("/api/abhyasa/grade")
def grade():
    q = request.get_json(force=True) or {}
    try:
        return jsonify(A.grade_compose(q["sentence_id"], q.get("answer") or []))
    except (KeyError, LookupError) as ex:
        return _err(ex, 404)


@bp.post("/api/abhyasa/explain")
def explain():
    """The engine's derivation of one answer (+ Vidyut's steps), for the shared prakriyā view."""
    from webui.app import _pack
    q = request.get_json(force=True) or {}
    kind = q.get("kind")
    try:
        if kind == "subanta":
            st = A._sub_state(q["stem"], q.get("linga") or "pulliṅga", int(q["vibhakti"]), int(q["vacana"]))
            vid = A.vidyut({"op": "steps", "stem": q["stem"], "linga": q.get("linga") or "pulliṅga",
                            "vibhakti": int(q["vibhakti"]), "vacana": int(q["vacana"])})
        elif kind == "tinanta":
            from pipelines.tinanta import derive as tin_derive
            d = next(x for x in A.dhatu_pool() if x["ref"] == q["ref"])
            kw: dict[str, Any] = {"pada": q["pada"]} if q.get("pada") and q.get("prayoga", "kartari") == "kartari" else {}
            if q.get("prefix"):
                kw["upasargas"] = q["prefix"].split("+")
            if q.get("sanadi") in ("Ric", "san"):
                kw[{"Ric": "nic_recipe", "san": "san_recipe"}[q["sanadi"]]] = True
            st = tin_derive(d["id"], q["lakara"], q.get("prayoga") or "kartari", int(q["purusha"]), int(q["vacana"]), **kw)
            vid = A.vidyut({"op": "steps", "upadesha": d["upadesha"], "path_id": d["ref"], "lakara": q["lakara"],
                            "purusha": int(q["purusha"]), "vacana": int(q["vacana"]), "prayoga": q.get("prayoga") or "kartari",
                            "pada": q.get("pada") or None, "prefixes": [p for p in (q.get("prefix") or "").split("+") if p],
                            "sanadi": [s for s in (q.get("sanadi") or "").split("+") if s]})
        else:
            return _err(ValueError(f"no live derivation view for {kind!r}; the question carries its sūtra steps"), 404)
    except Exception as ex:  # noqa: BLE001 — the engine's own gap is the answer
        return _err(ex, 422)
    return jsonify({**_pack(st), "vidyut": vid or []})


@bp.post("/api/abhyasa/search")
def search():
    q = request.get_json(force=True) or {}
    if not (q.get("q") or "").strip():
        return _err(ValueError("empty query"))
    return jsonify(A.search(q["q"], q.get("linga") or ""))


@bp.post("/api/abhyasa/vyutpatti")
def vyutpatti():
    """व्युत्पत्तिः: kośa proposals, Kāśikā / uṇādi citations, Vidyut verification, recursion to the base (core/vyutpatti)."""
    from core.vyutpatti import explain
    q = request.get_json(force=True) or {}
    try:
        return jsonify(explain(q["word"], q.get("linga") or "", int(q.get("depth") or 2)))
    except KeyError as ex:
        return _err(ex)


@bp.post("/api/abhyasa/vyutpatti/engine")
def vyutpatti_engine():
    """Our engine's own attempt at one proposal (slow: a full derivation with every vikalpa)."""
    from core.vyutpatti import engine_check
    from webui.app import _pack
    q = request.get_json(force=True) or {}
    try:
        r = engine_check(q["kind"], q.get("base") or "", q["pratyaya"], q.get("linga") or "pulliṅga", q["word"],
                         q.get("dhatu_ref") or "", tuple(q.get("sutras") or ()))
    except Exception as ex:  # noqa: BLE001 — the engine's own gap is the answer
        return _err(ex, 422)
    st = r.pop("state", None)
    return jsonify({**r, **({"derivation": _pack(st)} if st is not None else {})})


@bp.get("/api/abhyasa/gaps")
def gaps():
    """Engine ≠ Vidyut cells met while drilling (this server's run) — for the engine agents."""
    return jsonify({"runtime": A.GAPS[-500:], "doc": "docs/ABHYASA_PLAN.md §6"})


@bp.post("/api/abhyasa/lipi")
def lipi():
    q = request.get_json(force=True) or {}
    return jsonify(A.vidyut({"op": "lipi", "text": q.get("text", ""), "to": q.get("to") or list(A.LIPIS)}) or {})
