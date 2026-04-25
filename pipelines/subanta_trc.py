"""
pipelines/subanta_trc.py — nominal singular recipe for **tṛc** stems (चेता-पथ).

Uses ``state.meta['trc_nom_sg_pipeline']`` so 7.1.94 / 6.4.11 / 6.1.66 / 8.2.7
self-gate without reading vibhakti in sūtra cond().

This is a **pipeline** only; it does not change dispatcher semantics.
"""
from __future__ import annotations

from typing import List

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term

from pipelines.subanta import build_initial_state


def _pada_merge(state: State) -> None:
    if not state.terms:
        return
    all_varnas: List = []
    for t in state.terms:
        all_varnas.extend(t.varnas)
    pada = Term(kind="pada", varnas=all_varnas, tags={"pada"}, meta={})
    state.terms = [pada]
    state.trace.append({
        "sutra_id"    : "__MERGE__",
        "sutra_type"  : "STRUCTURAL",
        "type_label"  : "पद-मेलनम्",
        "form_before" : state.flat_slp1(),
        "form_after"  : state.flat_slp1(),
        "why_dev"     : "तृच्-सुबन्त — पद-संयोजनम् (संरचनात्मकम्)।",
        "status"      : "APPLIED",
    })


def derive_trc_nom_sg(
    stem_slp1: str,
    *,
    vibhakti: int = 1,
    vacana: int = 1,
    linga: str = "pulliṅga",
) -> State:
    """
    Subanta slice for a **tṛc** stem (e.g. ``cetf``) + ``su`` → ``cetA`` surface.
    """
    s = build_initial_state(stem_slp1, vibhakti, vacana, linga)
    s.meta["trc_nom_sg_pipeline"] = True
    if s.terms:
        s.terms[0].meta["trc_rikaranta"] = True

    s = apply_rule("1.4.14", s)
    s = apply_rule("4.1.1", s)
    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.73", s)
    s = apply_rule("1.1.2", s)
    s = apply_rule("1.1.3", s)
    s = apply_rule("1.1.7", s)
    s = apply_rule("1.1.60", s)  # *lopa* saṃjñā
    s = apply_rule("1.1.61", s)  # *luk* / *ślu* / *lup*
    s = apply_rule("1.1.62", s)  # *pratyayalope pratyayalakṣaṇam*
    s = apply_rule("1.1.63", s)  # *na lumatā … aṅgasya pratyayalakṣaṇam*
    s = apply_rule("1.1.8", s)
    s = apply_rule("1.1.9", s)
    s = apply_rule("1.1.10", s)
    s = apply_rule("1.1.11", s)
    s = apply_rule("1.1.12", s)
    s = apply_rule("1.1.13", s)
    s = apply_rule("1.1.14", s)
    s = apply_rule("1.1.100", s)
    s = apply_rule("1.1.15", s)
    s = apply_rule("1.1.16", s)
    s = apply_rule("1.1.17", s)
    s = apply_rule("1.1.18", s)
    s = apply_rule("1.1.19", s)
    s = apply_rule("1.1.20", s)
    s = apply_rule("1.1.21", s)
    s = apply_rule("1.1.46", s)
    s = apply_rule("1.1.22", s)
    s = apply_rule("1.1.23", s)
    s = apply_rule("1.1.24", s)
    s = apply_rule("4.1.2", s)

    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.4", s)
    s = apply_rule("1.3.5", s)
    s = apply_rule("1.3.6", s)
    s = apply_rule("1.3.7", s)
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.3.10", s)

    s = apply_rule("6.4.1", s)
    s = apply_rule("7.1.94", s)
    s = apply_rule("6.4.11", s)
    s = apply_rule("6.1.66", s)

    _pada_merge(s)

    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.7", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    s = apply_rule("8.3.59", s)
    s = apply_rule("8.4.1", s)
    s = apply_rule("8.4.2", s)
    return s
