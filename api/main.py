"""
api/main.py — Pāṇini Engine v3 HTTP API.
────────────────────────────────────────

Every response is a *derivation*, never a lookup: the surface form always
arrives with the ordered chain of sūtras the engine actually applied to reach
it (id · type · form-before → form-after · status · why).  That chain is the
product; the form is a by-product.

Run:
    pip install fastapi uvicorn
    uvicorn api.main:app --reload --port 8000
    # docs: http://127.0.0.1:8000/docs
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sutras  # noqa: F401 — fills SUTRA_REGISTRY
from core.trace_view import attested_for_sutra, enrich_trace, lsk_pages, slp1_str_to_dev
from engine import SUTRA_REGISTRY, coverage_report
from engine.sig import extract_applied_path

app = FastAPI(
    title="Pāṇini Engine v3 API",
    version="3.3",
    description=(
        "Rule-based Sanskrit derivation. Every form is produced by applying "
        "Aṣṭādhyāyī sūtras in order — the full applied chain ships with each "
        "response, so any output can be audited rule by rule."
    ),
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # read-only public API
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# ─────────────────────────────────────────────────────────────────
# Common envelope
# ─────────────────────────────────────────────────────────────────

def _derivation(state: Any, **inputs: Any) -> dict[str, Any]:
    """State → the one response shape every derivation endpoint returns."""
    trace = list(state.trace)
    steps = [
        {
            "n": i + 1,
            "sutra_id": s.get("sutra_id", ""),
            "sutra_type": s.get("sutra_type", ""),
            "type_dev": s.get("type_label", ""),
            "text_dev": s.get("_sutra_text_dev"),
            "status": s.get("status", ""),
            "before": {"slp1": s.get("form_before", ""), "dev": s.get("form_before_dev", "")},
            "after": {"slp1": s.get("form_after", ""), "dev": s.get("form_after_dev", "")},
            "changed": s.get("form_before") != s.get("form_after"),
            "why_dev": s.get("why_dev", ""),
            # Hindi learner aid; UNREVIEWED (core/i18n_hi) — label it as such.
            "hint_hi": s.get("_hint_hi", ""),
            "anuvritti_from": s.get("_anuvritti_from", []),
            "lsk": s.get("_lsk", []),
        }
        for i, s in enumerate(enrich_trace(trace))
    ]
    statuses = [s.get("status") for s in trace]
    return {
        "input": inputs,
        "surface": {"slp1": state.flat_slp1(), "dev": state.flat_dev()},
        "phase": getattr(state, "phase", None),
        "applied_path": extract_applied_path(trace),
        "steps": steps,
        "stats": {
            "total": len(trace),
            "applied": sum(1 for st in statuses if st in {"APPLIED", "APPLIED_VACUOUS"}),
            "audit": statuses.count("AUDIT"),
            "blocked": statuses.count("BLOCKED"),
            "skipped": statuses.count("SKIPPED"),
        },
    }


def _run(fn, *args, **kwargs) -> Any:
    """Call an engine pipeline, mapping its failures onto HTTP status codes."""
    try:
        return fn(*args, **kwargs)
    except KeyError as ex:
        raise HTTPException(404, str(ex)) from ex
    except (ValueError, LookupError) as ex:
        raise HTTPException(422, f"{type(ex).__name__}: {ex}") from ex
    except NotImplementedError as ex:
        raise HTTPException(501, f"Not implemented: {ex}") from ex
    except Exception as ex:                                  # engine bug — say so
        raise HTTPException(500, f"{type(ex).__name__}: {ex}") from ex


# ─────────────────────────────────────────────────────────────────
# Meta
# ─────────────────────────────────────────────────────────────────

@app.get("/v1/health", tags=["meta"])
def health() -> dict[str, Any]:
    return {"ok": True, "sutras": len(SUTRA_REGISTRY), "coverage": coverage_report(SUTRA_REGISTRY)}


@app.get("/v1/sutras", tags=["sūtra"])
def list_sutras(
    type: str | None = Query(None, description="SutraType name, e.g. VIDHI"),
    q: str | None = Query(None, description="substring of id or Devanāgarī text"),
    limit: int = Query(100, le=1000),
    offset: int = 0,
) -> dict[str, Any]:
    def key(sid: str) -> tuple:
        try:
            return tuple(int(x) for x in sid.split("."))
        except ValueError:
            return (99, 99, 99)

    hits = [
        {"sutra_id": sid, "sutra_type": rec.sutra_type.name,
         "text_dev": rec.text_dev, "why_dev": rec.why_dev}
        for sid, rec in sorted(SUTRA_REGISTRY.items(), key=lambda p: key(p[0]))
        if (not type or rec.sutra_type.name == type.upper())
        and (not q or q in sid or q in (rec.text_dev or ""))
    ]
    return {"total": len(hits), "sutras": hits[offset:offset + limit]}


@app.get("/v1/sutras/{sutra_id}", tags=["sūtra"])
def get_sutra(sutra_id: str) -> dict[str, Any]:
    rec = SUTRA_REGISTRY.get(sutra_id)
    if rec is None:
        raise HTTPException(404, f"unknown sūtra: {sutra_id}")
    return {
        "sutra_id": rec.sutra_id,
        "sutra_type": rec.sutra_type.name,
        "text_slp1": rec.text_slp1,
        "text_dev": rec.text_dev,
        "padaccheda_dev": rec.padaccheda_dev,
        "why_dev": rec.why_dev,
        "anuvritti_from": list(rec.anuvritti_from or ()),
        "adhikara_scope": list(rec.adhikara_scope or ()),
        "blocks_sutra_ids": list(rec.blocks_sutra_ids or ()),
        "lsk": lsk_pages(rec.sutra_id),
        "examples": _sutra_examples(rec.sutra_id),
        "attested": attested_for_sutra(rec.sutra_id),
    }


def _sutra_examples(sutra_id: str) -> dict[str, Any]:
    """Verified forms this sūtra shapes; empty (not an error) when the index is unbuilt."""
    from core.practice import sutra_examples
    try:
        return sutra_examples(sutra_id)
    except FileNotFoundError:
        return {"total": 0, "forms": []}


# ─────────────────────────────────────────────────────────────────
# सुबन्त — nominal derivation
# ─────────────────────────────────────────────────────────────────

Linga = Literal["pulliṅga", "strīliṅga", "napuṃsaka"]


class SubantaReq(BaseModel):
    stem: str = Field("rAma", description="prātipadika in SLP1")
    vibhakti: int = Field(1, ge=1, le=8)
    vacana: int = Field(1, ge=1, le=3)
    linga: Linga = "pulliṅga"


@app.post("/v1/subanta", tags=["subanta"])
def subanta(req: SubantaReq, reading: bool = False) -> dict[str, Any]:
    """Derive one nominal cell.

    ``?reading=true`` adds the traditional shape — the form after each change
    with the sūtras that made it (राम + टा → राम + आ → … → रामेण). It is built
    from *this* derivation, never from a stored copy: a page that replays a
    cached prakriyā is showing yesterday's grammar (Art. 17).
    """
    from core.prakriya_view import TermRecorder, reading as build_reading
    from pipelines.subanta import derive

    if not reading:
        state = _run(derive, req.stem, req.vibhakti, req.vacana, linga=req.linga)
        return _derivation(state, **req.model_dump())

    # The recorder rebinds apply_rule while the derivation runs, so this path
    # is deliberately serial — it is a reading aid for one request at a time.
    with TermRecorder() as recorder:
        state = _run(derive, req.stem, req.vibhakti, req.vacana, linga=req.linga)
    out = _derivation(state, **req.model_dump())
    out["reading"] = build_reading(state, recorder)
    return out


@app.get("/v1/shabda", tags=["subanta"])
def shabda_index() -> dict[str, Any]:
    """The attested paradigms vendored under data/reference/shabda_gold/."""
    from tools.shabda_table import paradigms

    return {
        "words": [
            {"stem_slp1": stem, "word": data["word"], "linga": data["linga"],
             "artha": data.get("artha", "")}
            for stem, data in paradigms().items()
        ]
    }


@app.get("/v1/shabda/{stem}", tags=["subanta"])
def shabda_paradigm(stem: str) -> dict[str, Any]:
    """One attested paradigm: 24 cells, each a list of accepted forms."""
    from tools.shabda_table import paradigms

    known = paradigms()
    if stem not in known:
        raise HTTPException(404, f"no vendored paradigm for {stem!r}")
    data = known[stem]
    return {"stem_slp1": stem, "word": data["word"], "linga": data["linga"],
            "artha": data.get("artha", ""), "cells": data["cells"]}


@app.get("/shabda", response_class=HTMLResponse, include_in_schema=False)
def shabda_page() -> str:
    """The paradigm table, deriving every cell live."""
    return (Path(__file__).parent / "shabda.html").read_text(encoding="utf-8")


@app.get("/v1/practice", tags=["abhyāsa"])
def practice(
    kind: Literal["subanta", "tinanta"] = "subanta",
    type: Literal["mcq", "recall", "tf", "sutra"] = "mcq",
    lemma: str | None = None,
    linga: Linga | None = None,
    level: Literal["easy", "hard"] = "easy",
    seed: int | None = None,
) -> dict[str, Any]:
    """One practice question drawn from forms the engine derives (core/practice)."""
    from core.practice import question
    try:
        return question(kind, type, lemma=lemma, linga=linga, level=level, seed=seed)
    except LookupError as ex:
        raise HTTPException(404, str(ex))


@app.get("/v1/practice/lemmas", tags=["abhyāsa"])
def practice_lemmas(kind: Literal["subanta", "tinanta"] = "subanta") -> dict[str, Any]:
    """Lemmas a practice question can be drawn from (verified cells only)."""
    from core.practice import lemmas
    return {"lemmas": lemmas(kind)}


@app.get("/v1/practice/sentences", tags=["abhyāsa"])
def practice_sentence_sets() -> dict[str, Any]:
    """Sentence sets for practice (Saṃsādhanī "1000 Sentences"), with counts."""
    from tools.practice_sentences import ROLES, sets
    return {"sets": sets(), "roles": ROLES}


@app.get("/v1/practice/sentences/{set_id}", tags=["abhyāsa"])
def practice_sentence_list(set_id: str) -> dict[str, Any]:
    from tools.practice_sentences import sentences
    return {"set": set_id, "sentences": _run(sentences, set_id)}


@app.get("/v1/practice/sentences/{set_id}/{sid}", tags=["abhyāsa"])
def practice_sentence(set_id: str, sid: str) -> dict[str, Any]:
    """One sentence with every word's form, written-out tag, gloss, kāraka role (+ sūtras) and engine verdict."""
    from tools.practice_sentences import sentence
    return _run(sentence, set_id, sid)


@app.get("/practice", response_class=HTMLResponse, include_in_schema=False)
def practice_page() -> str:
    """अभ्यास — practice with a sūtra-by-sūtra explanation of every answer."""
    return (Path(__file__).parent / "practice.html").read_text(encoding="utf-8")


@app.get("/v1/lab/grid", tags=["lab"])
def lab_grid(
    kind: Literal["subanta", "tinanta"] = "tinanta",
    lemma: str = "BU",
    lakara: str = "laT",
    prayoga: Literal["kartari", "karmani", "bhave"] = "kartari",
    pada: Literal["parasmai", "atmane"] | None = None,
    linga: Linga = "pulliṅga",
) -> dict[str, Any]:
    """Whole paradigm, engine vs Vidyut per cell (core/lab)."""
    from core.lab import grid
    if kind == "tinanta":
        lemma = _resolve_dhatu(lemma)
    try:
        return grid(kind, lemma, lakara=lakara, prayoga=prayoga, pada=pada, linga=linga)
    except KeyError as ex:
        raise HTTPException(404, str(ex))


@app.get("/v1/lab/lemmas", tags=["lab"])
def lab_lemmas(kind: Literal["subanta", "tinanta"] = "tinanta") -> dict[str, Any]:
    """Every lemma the engine can be asked about: all dhātupāṭha roots, or indexed stems."""
    if kind == "tinanta":
        from pipelines.dhatupatha import _envelope, _payload
        rows = [{"lemma": e["upadesha_slp1"], "dev": e.get("mula_dhatu_dev") or e.get("upadesha_dev", ""),
                 "id": e.get("dhatupatha_id") or "", "pada": e.get("pada_label_dev") or ""}
                for e in _envelope(_payload())["entries"]]
        return {"lemmas": sorted(rows, key=lambda r: (r["id"] or "99", r["lemma"]))}
    from contextlib import closing
    from engine.form_index import connect
    with closing(connect()) as conn:
        rows = conn.execute("SELECT DISTINCT lemma, json_extract(features, '$.linga') FROM forms "
                            "WHERE kind = 'subanta' ORDER BY 1").fetchall()
    return {"lemmas": [{"lemma": l, "dev": slp1_str_to_dev(l), "linga": g} for l, g in rows]}


@app.get("/lab", response_class=HTMLResponse, include_in_schema=False)
def lab_page() -> str:
    """Local test panel: pick a paradigm, compare with Vidyut, open any derivation."""
    return (Path(__file__).parent / "lab.html").read_text(encoding="utf-8")


@app.get("/v1/subanta/paradigm", tags=["subanta"])
def subanta_paradigm(stem: str = "rAma", linga: Linga = "pulliṅga") -> dict[str, Any]:
    """All 24 cells. Per-cell failures are reported, never fatal."""
    from pipelines.subanta import derive
    cells = []
    for vibhakti in range(1, 9):
        for vacana in range(1, 4):
            cell: dict[str, Any] = {"vibhakti": vibhakti, "vacana": vacana}
            try:
                s = derive(stem, vibhakti, vacana, linga=linga)
                cell |= {"slp1": s.flat_slp1(), "dev": s.flat_dev(), "steps": len(s.trace)}
            except Exception as ex:
                cell["error"] = f"{type(ex).__name__}: {ex}"
            cells.append(cell)
    return {"input": {"stem": stem, "linga": linga}, "cells": cells}


# ─────────────────────────────────────────────────────────────────
# तिङन्त — verbal derivation
# ─────────────────────────────────────────────────────────────────

class TinantaReq(BaseModel):
    dhatu: str = Field("BU", description="upadeśa in SLP1, or mūla-dhātu in Devanāgarī")
    lakara: str = "laT"
    prayoga: Literal["kartari", "karmani", "bhave"] = "kartari"
    purusha: int = Field(3, ge=1, le=3)
    vacana: int = Field(1, ge=1, le=3)
    pada: Literal["parasmai", "atmane"] | None = Field(None, description="override the dhātu's pada")


def _resolve_dhatu(dhatu: str) -> str:
    """Devanāgarī mūla-dhātu → SLP1 upadeśa; SLP1 passes through untouched."""
    if not any("\u0900" <= c <= "\u097f" for c in dhatu):
        return dhatu                                   # already SLP1
    from pipelines.dhatupatha import _envelope, _payload
    for e in _envelope(_payload())["entries"]:
        if e.get("mula_dhatu_dev", "").strip() == dhatu.strip():
            return e["upadesha_slp1"]
    raise HTTPException(404, f"Devanāgarī dhātu not found: {dhatu}")


def _homograph_rows(dhatu: str, used_id: str) -> list[dict[str, Any]]:
    """Other dhātupāṭha rows behind the same bare upadeśa. Our upadeśas carry no svara, so शासुँ इच्छायाम्
    (02.0012, ātmanepadī) and शासुँ अनुशिष्टौ (02.0070, parasmaipadī) are both ``SAsu~``; a pāṭha id names one."""
    if not dhatu or dhatu[:1].isdigit():
        return []
    from pipelines.dhatupatha import _envelope, _payload
    return [e for e in _envelope(_payload())["entries"]
            if e["upadesha_slp1"] == dhatu and e.get("dhatupatha_id") != used_id]


@app.post("/v1/tinanta", tags=["tinanta"])
def tinanta(req: TinantaReq) -> dict[str, Any]:
    """One tiṅanta cell. When a bare upadeśa names several dhātus, the first in pāṭha order is derived
    and ``homographs`` lists the others, each with its own form — pass a pāṭha id (``02.0070``) to choose."""
    from pipelines.tinanta import _dhatu_row_by_upadesha, derive
    upadesha = _resolve_dhatu(req.dhatu)
    row = _run(_dhatu_row_by_upadesha, upadesha)
    kw = {"pada": req.pada} if req.pada else {}
    state = _run(derive, upadesha, req.lakara, req.prayoga, req.purusha, req.vacana, **kw)
    out = _derivation(state, **{**req.model_dump(), "dhatu": upadesha})
    out["dhatu"] = {
        "upadesha_slp1": row.get("upadesha_slp1", upadesha),
        "mula_dev": row.get("mula_dhatu_dev", ""),
        "dhatupatha_id": row.get("dhatupatha_id", ""),
        "gana": row.get("gana"),
        "artha_dev": row.get("artha_dev", ""),
        "artha_en": row.get("artha_en", ""),
        "pada_dev": row.get("pada_label_dev", ""),
    }
    homographs = []
    for e in _homograph_rows(upadesha, row.get("dhatupatha_id", "")):
        alt = {"dhatupatha_id": e["dhatupatha_id"], "gana": e.get("gana"), "artha_dev": e.get("artha_dev", ""),
               "pada_dev": e.get("pada_label_dev", "")}
        try:
            s = derive(e["dhatupatha_id"], req.lakara, req.prayoga, req.purusha, req.vacana, **kw)
            alt["surface"] = {"slp1": s.flat_slp1(), "dev": s.flat_dev()}
        except Exception as ex:  # noqa: BLE001 — that row's own gap, reported beside it
            alt["error"] = f"{type(ex).__name__}: {ex}"[:200]
        homographs.append(alt)
    if homographs:
        out["homographs"] = homographs
        out["note"] = (f"upadeśa {upadesha} names {len(homographs) + 1} dhātus; this derivation is "
                       f"{row.get('dhatupatha_id')} ({row.get('artha_dev', '')}). Pass a pāṭha id to choose another.")
    return out


@app.get("/v1/tinanta/paradigm", tags=["tinanta"])
def tinanta_paradigm(
    dhatu: str = "BU",
    lakara: str = "laT",
    prayoga: Literal["kartari", "karmani", "bhave"] = "kartari",
) -> dict[str, Any]:
    """All 9 puruṣa × vacana cells for one lakāra."""
    from pipelines.tinanta import derive
    upadesha = _resolve_dhatu(dhatu)
    cells = []
    for purusha in range(1, 4):
        for vacana in range(1, 4):
            cell: dict[str, Any] = {"purusha": purusha, "vacana": vacana}
            try:
                s = derive(upadesha, lakara, prayoga, purusha, vacana)
                cell |= {"slp1": s.flat_slp1(), "dev": s.flat_dev(), "steps": len(s.trace)}
            except Exception as ex:
                cell["error"] = f"{type(ex).__name__}: {ex}"
            cells.append(cell)
    out: dict[str, Any] = {"input": {"dhatu": upadesha, "lakara": lakara, "prayoga": prayoga}, "cells": cells}
    try:
        from pipelines.tinanta import _dhatu_row_by_upadesha
        used = _dhatu_row_by_upadesha(upadesha).get("dhatupatha_id", "")
    except KeyError:
        return out
    alts = _homograph_rows(upadesha, used)
    if alts:
        out["dhatupatha_id"] = used
        out["homographs"] = [{"dhatupatha_id": e["dhatupatha_id"], "gana": e.get("gana"), "artha_dev": e.get("artha_dev", ""),
                              "pada_dev": e.get("pada_label_dev", "")} for e in alts]
    return out


# ─────────────────────────────────────────────────────────────────
# धातुपाठ
# ─────────────────────────────────────────────────────────────────

@app.get("/v1/dhatu", tags=["dhātu"])
def list_dhatu(
    q: str | None = Query(None, description="match upadeśa, mūla-dhātu, or artha"),
    gana: int | None = Query(None, ge=1, le=10),
    limit: int = Query(50, le=500),
    offset: int = 0,
) -> dict[str, Any]:
    from pipelines.dhatupatha import _envelope, _payload
    entries = _envelope(_payload())["entries"]
    ql = (q or "").strip().lower()
    hits = [
        e for e in entries
        if (gana is None or int(e.get("gana", 0)) == gana)
        and (not ql or any(
            ql in str(e.get(f, "")).lower()
            for f in ("upadesha_slp1", "mula_dhatu_dev", "artha_dev", "artha_en", "dhatupatha_id")
        ))
    ]
    keep = ("dhatupatha_id", "upadesha_slp1", "mula_dhatu_dev", "gana",
            "artha_dev", "artha_en", "pada_label_dev")
    return {
        "total": len(hits),
        "dhatus": [{k: e.get(k) for k in keep} for e in hits[offset:offset + limit]],
    }


@app.get("/v1/dhatu/{dhatu_id}", tags=["dhātu"])
def get_dhatu(dhatu_id: str) -> dict[str, Any]:
    """Accepts upadeśa SLP1 (``BU``), pāṭha id (``01.0001``) or row id."""
    from pipelines.dhatupatha import resolve_dhatu_identifier
    return _run(resolve_dhatu_identifier, dhatu_id)


# ─────────────────────────────────────────────────────────────────
# कृदन्त
# ─────────────────────────────────────────────────────────────────

class KrdantaReq(BaseModel):
    dhatu_id: str = Field("BU", description="upadeśa SLP1, pāṭha id (01.0001), or row id")
    krt: Literal["tfc", "Rvul", "Nvul"] = Field("tfc", description="तृच् or ण्वुल् (Rvul; Nvul kept as an alias)")


@app.post("/v1/krdanta", tags=["krdanta"])
def krdanta(req: KrdantaReq) -> dict[str, Any]:
    from pipelines.dhatupatha import resolve_dhatu_identifier
    row = _run(resolve_dhatu_identifier, req.dhatu_id)
    upadesha = row.get("upadesha_slp1") or row.get("id") or req.dhatu_id

    if req.krt == "tfc":
        from pipelines.krdanta import derive_tfc_pratipadika
        from pipelines.subanta_trc import derive_trc_nom_sg_from_state
        stem_state = _run(derive_tfc_pratipadika, upadesha,
                          udatta_dhatu=bool(row.get("flags", {}).get("udatta", False)))
        state = _run(derive_trc_nom_sg_from_state, stem_state,
                     vibhakti=1, vacana=1, linga="pulliṅga")
    else:
        from pipelines.krdanta import derive_krt
        label = row.get("citation_dhatu_slp1") or row.get("raw_dhatu_after_it_lopa_slp1") or upadesha.rstrip("~").rstrip("\\")
        state = _run(derive_krt, upadesha, krt_upadesha_slp1="Rvul",
                     merge_pratipadika_label=label)
    return _derivation(state, **req.model_dump())


# ─────────────────────────────────────────────────────────────────
# विश्लेषणम् — analysis proposes, generation verifies (Art. 17)
# ─────────────────────────────────────────────────────────────────

class AnalyzeReq(BaseModel):
    text: str = Field(..., max_length=4000, description="Devanāgarī: a word, a line or a verse")
    steps: bool = Field(False, description="attach the forward derivation of the first verified readings of each word")


@app.post("/v1/analyze", tags=["analysis"])
def analyze(req: AnalyzeReq) -> dict[str, Any]:
    """Each word → readings proposed by the form index and Vidyut's kosha, each re-derived by
    the engine. ``verified`` only when a derivation reproduces the word exactly (core/analyze)."""
    from core.analyze import analyze_text, rederive

    out = analyze_text(req.text)
    if req.steps:
        for line in out["lines"]:
            for word in line:
                for r in [r for r in word["readings"] if r["status"] == "derived"][:8]:
                    r["derivation"] = _derivation(_run(rederive, r["request"]), **r["request"])
    return out


# ─────────────────────────────────────────────────────────────────
# Transliteration (SLP1 ↔ Devanāgarī) — handy for clients
# ─────────────────────────────────────────────────────────────────

@app.get("/v1/translit", tags=["meta"])
def translit(slp1: str) -> dict[str, str]:
    return {"slp1": slp1, "dev": slp1_str_to_dev(slp1)}


# ─────────────────────────────────────────────────────────────────
# प्रक्रिया-संशोधनम् — human review of derivations
#
# Corrections are appended to a JSONL file in the repo (not a database):
# they are meant to be read, diffed and committed, and to become test cases.
# Set PANINI_REVIEW_DIR to write elsewhere (a mounted volume, say).
# ─────────────────────────────────────────────────────────────────

REVIEW_FILE = Path(
    os.environ.get("PANINI_REVIEW_DIR", _ROOT / "data" / "reviews")
) / "corrections.jsonl"


class ReviewIn(BaseModel):
    target: str = Field(..., description="derivation key, e.g. 'tinanta:{\"dhatu\":\"gam\",...}'")
    step_n: int | None = Field(None, description="1-based step index; null = the final form")
    sutra_id: str | None = None
    observed_form: str = ""
    expected_form: str = ""
    expected_sutra: str = ""
    note: str = ""


def _read_reviews() -> list[dict[str, Any]]:
    if not REVIEW_FILE.exists():
        return []
    return [json.loads(line) for line in REVIEW_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]


@app.get("/v1/reviews", tags=["review"])
def list_reviews(target: str | None = None) -> dict[str, Any]:
    rows = [r for r in _read_reviews() if target is None or r.get("target") == target]
    return {"total": len(rows), "reviews": rows}


@app.post("/v1/reviews", tags=["review"])
def add_review(req: ReviewIn) -> dict[str, Any]:
    if not (req.expected_form or req.expected_sutra or req.note):
        raise HTTPException(422, "a correction needs an expected form, an expected sūtra, or a note")
    rec = {
        "id": uuid4().hex[:12],
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        **req.model_dump(),
    }
    REVIEW_FILE.parent.mkdir(parents=True, exist_ok=True)
    with REVIEW_FILE.open("a", encoding="utf-8") as fp:
        fp.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


@app.delete("/v1/reviews/{review_id}", tags=["review"])
def delete_review(review_id: str) -> dict[str, Any]:
    rows = _read_reviews()
    keep = [r for r in rows if r.get("id") != review_id]
    if len(keep) == len(rows):
        raise HTTPException(404, f"no such correction: {review_id}")
    REVIEW_FILE.write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in keep), encoding="utf-8"
    )
    return {"deleted": review_id, "remaining": len(keep)}


@app.get("/review", response_class=HTMLResponse, include_in_schema=False)
def review_page() -> str:
    """Derive a form and correct it in the same view."""
    return (Path(__file__).parent / "review.html").read_text(encoding="utf-8")


@app.get("/v1/coverage", tags=["coverage"])
def coverage_status() -> dict[str, Any]:
    """Which sūtras the engine does confidently (docs/CONFIDENT_SUTRAS.md), by pāda,
    plus how far the recipe-free loop gets. Regenerate with ``make confident``."""
    path = _ROOT / "sig" / "sutra_class.json"
    if not path.exists():
        raise HTTPException(503, "run 'make confident' first")
    data = json.loads(path.read_text(encoding="utf-8"))
    padas: dict[str, dict[str, Any]] = {}
    totals: dict[str, int] = {}
    for r in data["rows"]:
        totals[r["status"]] = totals.get(r["status"], 0) + 1
        p = padas.setdefault(r["pada"], {"pada": r["pada"], "total": 0, "confident": []})
        p["total"] += 1
        if r["status"].startswith("confident"):
            p["confident"].append({"id": r["id"], "structural": r["status"] == "confident_structural"})
    auto = _ROOT / "sig" / "autonomy.json"
    return {
        "generated_at": data["generated_at"],
        "totals": totals,
        "padas": sorted(padas.values(), key=lambda x: tuple(int(i) for i in x["pada"].split("."))),
        "autonomy": json.loads(auto.read_text(encoding="utf-8")) if auto.exists() else None,
    }


@app.get("/v1/autonomy/subanta", tags=["coverage"])
def autonomy_subanta(
    stem: str = Query("rAma", description="prātipadika, SLP1"),
    vibhakti: int = Query(1, ge=1, le=8),
    vacana: int = Query(1, ge=1, le=3),
    linga: str = Query("puṃliṅga"),
) -> dict[str, Any]:
    """Derive with *no recipe*: scheduler → resolver → apply_rule. Every step names
    the paribhāṣā layer that chose it."""
    from types import SimpleNamespace

    from tools.autonomy_report import run_autonomously, start_state

    case = SimpleNamespace(kind="subanta", args=(stem, vibhakti, vacana, linga))
    try:
        run = run_autonomously(start_state(case), "", stem, budget=120)
    except Exception as ex:  # unknown stem / tag combination
        raise HTTPException(422, f"{type(ex).__name__}: {ex}") from ex
    return {
        "surface_slp1": run.surface, "surface_dev": slp1_str_to_dev(run.surface),
        "steps": [{"sutra_id": s, "before": b, "after": a, "layer": l, "moved": b != a}
                  for s, b, a, l in run.steps],
    }


@app.get("/v1/autonomy/tinanta", tags=["coverage"])
def autonomy_tinanta(
    dhatu: str = Query("BU", description="dhātu upadeśa, SLP1 (bhvādi, laṭ kartari)"),
    purusha: int = Query(3, ge=1, le=3),
    vacana: int = Query(1, ge=1, le=3),
) -> dict[str, Any]:
    """laṭ kartari with no recipe after vivakṣā has chosen the tiṅ."""
    from types import SimpleNamespace

    from tools.autonomy_report import run_autonomously, start_state

    case = SimpleNamespace(kind="tinanta", args=(dhatu, "laT", purusha, vacana))
    try:
        run = run_autonomously(start_state(case), "", dhatu, budget=120)
    except Exception as ex:
        raise HTTPException(422, f"{type(ex).__name__}: {ex}") from ex
    return {
        "surface_slp1": run.surface, "surface_dev": slp1_str_to_dev(run.surface),
        "steps": [{"sutra_id": s, "before": b, "after": a, "layer": l, "moved": b != a}
                  for s, b, a, l in run.steps],
    }


# ─────────────────────────────────────────────────────────────────
# Library — the Sanskrit literature this machine holds, for reading clients
# (Subhastini, docs/INTEGRATION_CLIENTS.md). Reference text, not engine input.
# ─────────────────────────────────────────────────────────────────

def _library(fn, *args, request: Request | None = None, work_id: str | None = None) -> Any:
    from tools import library_providers as lib

    if work_id and lib.is_local_only(work_id) and request is not None \
            and (request.client is None or request.client.host not in ("127.0.0.1", "::1")):
        raise HTTPException(403, "this text is a local reading copy (All rights reserved); served to this machine only")
    try:
        return fn(*args)
    except KeyError as ex:
        raise HTTPException(404, f"not found: {ex}") from ex


@app.get("/v1/library", tags=["library"])
def library_catalogue() -> dict[str, Any]:
    """Every work the engine can serve, from every provider (Advaita Sharada, Saṃsādhanī, ashtadhyayi.com)."""
    from tools import library_providers as lib

    works = lib.catalogue()
    return {"providers": list(lib.PROVIDERS), "total": len(works), "works": works}


@app.get("/v1/library/search", tags=["library"])
def library_search(q: str = Query(..., min_length=1), limit: int = Query(60, ge=1, le=300),
                   provider: str | None = None) -> dict[str, Any]:
    from tools import library_providers as lib

    hits = lib.search(q, limit, provider)
    return {"q": q, "total": len(hits), "hits": hits}


@app.get("/v1/library/text/{work_id}", tags=["library"])
def library_text(work_id: str, request: Request) -> dict[str, Any]:
    """All items of one work with their full text, for a client's index (Subhastini's concept graph)."""
    from tools import library_providers as lib

    return {"work": work_id, "passages": _library(lib.passages, work_id, request=request, work_id=work_id)}


@app.get("/v1/library/works/{work_id}", tags=["library"])
def library_work(work_id: str, request: Request) -> dict[str, Any]:
    from tools import library_providers as lib

    return _library(lib.work, work_id, request=request, work_id=work_id)


@app.get("/v1/library/works/{work_id}/{section}", tags=["library"])
def library_section(work_id: str, section: str, request: Request) -> dict[str, Any]:
    from tools import library_providers as lib

    return _library(lib.section, work_id, section, request=request, work_id=work_id)


@app.get("/v1/library/works/{work_id}/{section}/{item_id}", tags=["library"])
def library_item(work_id: str, section: str, item_id: str, request: Request) -> dict[str, Any]:
    from tools import library_providers as lib

    return _library(lib.item, work_id, section, item_id, request=request, work_id=work_id)


@app.get("/v1/library/words/{work_id}", tags=["library"])
def library_words_at(work_id: str, chapter: int = Query(..., ge=0), verse: int = Query(..., ge=0)) -> dict[str, Any]:
    """The word analysis of the item holding ``chapter.verse`` (e-reader items group verses: 16.1–3 is one item)."""
    from tools import library_providers as lib

    return _library(lib.words_at, work_id, chapter, verse)


@app.get("/v1/library/words/{work_id}/{section}/{item_id}", tags=["library"])
def library_words(work_id: str, section: str, item_id: str) -> dict[str, Any]:
    """Saṃsādhanī's word-by-word analysis of one item; every word carries the engine's verdict
    (``status: derived`` = the engine re-derives the attested form from the tagged inputs)."""
    from tools import library_providers as lib

    return _library(lib.words, work_id, section, item_id)


@app.get("/coverage", response_class=HTMLResponse, include_in_schema=False)
def coverage_page() -> str:
    return (Path(__file__).parent / "coverage.html").read_text(encoding="utf-8")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def hub() -> str:
    """Local home: every page this machine serves, with no live-site link."""
    return (Path(__file__).parent / "hub.html").read_text(encoding="utf-8")


_DOCS = _ROOT / "docs"
if _DOCS.is_dir():
    app.mount("/pages", StaticFiles(directory=str(_DOCS), html=True), name="pages")
