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

import sys
from pathlib import Path
from typing import Any, Literal

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sutras  # noqa: F401 — fills SUTRA_REGISTRY
from core.trace_view import enrich_trace, slp1_str_to_dev
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
            "anuvritti_from": s.get("_anuvritti_from", []),
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
    }


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
def subanta(req: SubantaReq) -> dict[str, Any]:
    from pipelines.subanta import derive
    state = _run(derive, req.stem, req.vibhakti, req.vacana, linga=req.linga)
    return _derivation(state, **req.model_dump())


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


def _resolve_dhatu(dhatu: str) -> str:
    """Devanāgarī mūla-dhātu → SLP1 upadeśa; SLP1 passes through untouched."""
    if not any("\u0900" <= c <= "\u097f" for c in dhatu):
        return dhatu                                   # already SLP1
    from pipelines.dhatupatha import _envelope, _payload
    for e in _envelope(_payload())["entries"]:
        if e.get("mula_dhatu_dev", "").strip() == dhatu.strip():
            return e["upadesha_slp1"]
    raise HTTPException(404, f"Devanāgarī dhātu not found: {dhatu}")


@app.post("/v1/tinanta", tags=["tinanta"])
def tinanta(req: TinantaReq) -> dict[str, Any]:
    from pipelines.tinanta import _dhatu_row_by_upadesha, derive
    upadesha = _resolve_dhatu(req.dhatu)
    row = _run(_dhatu_row_by_upadesha, upadesha)
    state = _run(derive, upadesha, req.lakara, req.prayoga, req.purusha, req.vacana)
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
    return {"input": {"dhatu": upadesha, "lakara": lakara, "prayoga": prayoga}, "cells": cells}


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
    krt: Literal["tfc", "Nvul"] = "tfc"


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
        label = row.get("raw_dhatu_after_it_lopa_slp1") or upadesha.rstrip("~").rstrip("\\")
        state = _run(derive_krt, upadesha, krt_upadesha_slp1="Nvul",
                     merge_pratipadika_label=label)
    return _derivation(state, **req.model_dump())


# ─────────────────────────────────────────────────────────────────
# Transliteration (SLP1 ↔ Devanāgarī) — handy for clients
# ─────────────────────────────────────────────────────────────────

@app.get("/v1/translit", tags=["meta"])
def translit(slp1: str) -> dict[str, str]:
    return {"slp1": slp1, "dev": slp1_str_to_dev(slp1)}
