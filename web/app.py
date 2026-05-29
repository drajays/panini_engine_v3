"""web/app.py — Panini Engine v3 web UI (FastAPI + Jinja2 + HTMX)."""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure repo root is on the path so engine imports work
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import sutras  # noqa: F401 — loads all registered sutras

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated

from display import (
    build_paradigm_table,
    prepare_trace,
    slp1_to_deva,
    VIBHAKTI_LABELS,
    VACANA_LABELS,
)

app = FastAPI(title="Panini Engine v3", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")
templates.env.globals["slp1_to_deva"] = slp1_to_deva
templates.env.globals["VIBHAKTI_LABELS"] = VIBHAKTI_LABELS
templates.env.globals["VACANA_LABELS"] = VACANA_LABELS


# ── Home ──────────────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ── Paradigm 8×3 ─────────────────────────────────────────────────────────────
@app.get("/paradigm", response_class=HTMLResponse)
async def paradigm_page(request: Request):
    return templates.TemplateResponse("paradigm.html", {
        "request": request, "table": None, "stem": "", "linga": "pulliṅga",
    })


@app.post("/paradigm/derive", response_class=HTMLResponse)
async def paradigm_derive(
    request: Request,
    stem: Annotated[str, Form()],
    linga: Annotated[str, Form()] = "pulliṅga",
):
    error = None
    table = None
    try:
        table = build_paradigm_table(stem.strip(), linga)
    except Exception as e:
        error = str(e)
    return templates.TemplateResponse("_paradigm_table.html", {
        "request": request, "table": table, "stem": stem, "linga": linga, "error": error,
    })


@app.post("/paradigm/cell", response_class=HTMLResponse)
async def paradigm_cell(
    request: Request,
    stem: Annotated[str, Form()],
    linga: Annotated[str, Form()] = "pulliṅga",
    vi: Annotated[int, Form()] = 1,
    va: Annotated[int, Form()] = 1,
    surface_only: Annotated[str, Form()] = "false",
):
    error = None
    steps = []
    final_form = ""
    try:
        import sutras as _s  # noqa
        from pipelines.subanta import derive
        state = derive(stem.strip(), vi, va, linga)
        final_form = state.flat_slp1()
        steps = prepare_trace(state.trace, surface_only == "true")
    except Exception as e:
        error = str(e)
    return templates.TemplateResponse("_trace.html", {
        "request": request, "steps": steps, "final_form": final_form,
        "final_deva": slp1_to_deva(final_form), "error": error,
        "title": f"{VIBHAKTI_LABELS[vi-1]} {VACANA_LABELS[va-1]}",
    })


# ── Tiṅanta ───────────────────────────────────────────────────────────────────
@app.get("/tinanta", response_class=HTMLResponse)
async def tinanta_page(request: Request):
    from pipelines.dhatupatha import list_tfc_demo_ids
    try:
        dhatus = list_tfc_demo_ids()
    except Exception:
        dhatus = []
    return templates.TemplateResponse("tinanta.html", {
        "request": request, "dhatus": dhatus,
        "LAKARAS": ["laT", "liT", "luT", "lṛT", "leT", "loT", "laṅ", "liṅ", "luṅ", "lṛṅ"],
        "PADAS": ["kartari", "karmani"],
        "PURUSHAS": [("3rd", 3), ("2nd", 2), ("1st", 1)],
        "VACANAS": [("sg", 1), ("du", 2), ("pl", 3)],
    })


@app.post("/tinanta/derive", response_class=HTMLResponse)
async def tinanta_derive(
    request: Request,
    dhatu: Annotated[str, Form()],
    lakara: Annotated[str, Form()] = "laT",
    pada: Annotated[str, Form()] = "kartari",
    purusha: Annotated[int, Form()] = 3,
    vacana: Annotated[int, Form()] = 1,
    surface_only: Annotated[str, Form()] = "false",
):
    error = None
    steps = []
    final_form = ""
    try:
        from pipelines.tinanta import derive
        state = derive(dhatu.strip(), lakara, pada, purusha, vacana)
        final_form = state.flat_slp1()
        steps = prepare_trace(state.trace, surface_only == "true")
    except Exception as e:
        error = str(e)
    return templates.TemplateResponse("_trace.html", {
        "request": request, "steps": steps, "final_form": final_form,
        "final_deva": slp1_to_deva(final_form), "error": error,
        "title": f"{dhatu} {lakara} {pada} {purusha}p {vacana}v",
    })


# ── Kṛdanta ───────────────────────────────────────────────────────────────────
@app.get("/krdanta", response_class=HTMLResponse)
async def krdanta_page(request: Request):
    return templates.TemplateResponse("krdanta.html", {"request": request})


@app.post("/krdanta/derive", response_class=HTMLResponse)
async def krdanta_derive(
    request: Request,
    dhatu: Annotated[str, Form()],
    krt_type: Annotated[str, Form()] = "nvul",
    surface_only: Annotated[str, Form()] = "false",
):
    error = None
    steps = []
    final_form = ""
    try:
        from pipelines.krdanta import derive_krt, build_dhatu_state_from_varnas
        from phonology.tokenizer import devanagari_to_varnas
        from pipelines.dhatupatha import get_dhatu_row

        row = get_dhatu_row(dhatu.strip())
        varnas = devanagari_to_varnas(row["upadesha_dev"]) if row else None
        krt_state = derive_krt(build_dhatu_state_from_varnas(varnas or []), krt_type)
        final_form = krt_state.flat_slp1()
        steps = prepare_trace(krt_state.trace, surface_only == "true")
    except Exception as e:
        error = str(e)
    return templates.TemplateResponse("_trace.html", {
        "request": request, "steps": steps, "final_form": final_form,
        "final_deva": slp1_to_deva(final_form), "error": error,
        "title": f"कृदन्त: {dhatu} + {krt_type}",
    })


# ── Special stems (ghi/sarva/tad) ────────────────────────────────────────────
@app.get("/special", response_class=HTMLResponse)
async def special_page(request: Request):
    return templates.TemplateResponse("special.html", {"request": request})


@app.post("/special/derive", response_class=HTMLResponse)
async def special_derive(
    request: Request,
    stem_type: Annotated[str, Form()] = "hari",
):
    error = None
    table = None
    try:
        table = build_paradigm_table(stem_type, "pulliṅga")
    except Exception as e:
        error = str(e)
    return templates.TemplateResponse("_paradigm_table.html", {
        "request": request, "table": table, "stem": stem_type,
        "linga": "pulliṅga", "error": error,
    })


# ── Devendra / Suryodaya ─────────────────────────────────────────────────────
@app.get("/devendra", response_class=HTMLResponse)
async def devendra_page(request: Request):
    results = {}
    try:
        from pipelines.devendra import DEVENDRA, SURYODAYA, derive_demo
        for key, demo in [("devendra", DEVENDRA), ("suryodaya", SURYODAYA)]:
            state = derive_demo(demo)
            results[key] = {
                "form": state.flat_slp1(),
                "deva": slp1_to_deva(state.flat_slp1()),
                "steps": prepare_trace(state.trace, False),
                "steps_surface": prepare_trace(state.trace, True),
            }
    except Exception as e:
        results["error"] = str(e)
    return templates.TemplateResponse("devendra.html", {
        "request": request, "results": results,
    })


# ── Dik-samāsa + caturthi ────────────────────────────────────────────────────
@app.get("/dik", response_class=HTMLResponse)
async def dik_page(request: Request):
    results = {}
    try:
        from pipelines.dik_uttarapurva import caturthi_preset, capture_caturthi_prakriya_stdout
        from pipelines.dik_caturthi_glassbox_text import glass_rows, GLASS_HEADER
        for pid in ["uttarapurva", "dakshinapurva"]:
            try:
                preset = caturthi_preset(pid)
                state = preset()
                results[pid] = {
                    "form": state.flat_slp1(),
                    "deva": slp1_to_deva(state.flat_slp1()),
                    "steps": prepare_trace(state.trace, False),
                }
            except Exception as e:
                results[pid] = {"error": str(e)}
    except Exception as e:
        results["error"] = str(e)
    return templates.TemplateResponse("dik.html", {"request": request, "results": results})
