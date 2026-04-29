"""
2.2.20  अमेवाव्ययेन  —  VIDHI (narrow v3 demo slice)

User note (``कृन्मेजन्तः.md``): when a kṛn/mejanta-derived avyaya is **am-anta**,
it forms a samāsa with its upapada (here, saptamī-stha upapada) to yield a single
computational block (e.g. स्वादु + (कारम्) → स्वादुकारम्).

This file implements a *minimal* structural merge:
  - left term: tagged ``upapada`` (upapada-saṃjñā already assigned by upstream)
  - right term: an ``avyaya`` kṛdanta block ending in ``m`` (am-anta)
  - action: merge into one ``prakriti`` term carrying ``prātipadika``/``anga`` + ``avyaya``.

This is adequate for demos where the goal is to show 1.1.39 → 2.2.20 → 2.4.82.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term


def _find(state: State):
    if len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        up = state.terms[i]
        nxt = state.terms[i + 1]
        if "upapada" not in up.tags:
            continue
        if "avyaya" not in nxt.tags:
            continue
        if nxt.kind != "pratyaya":
            continue
        if not nxt.varnas or nxt.varnas[-1].slp1 != "m":
            continue
        if state.meta.get("2_2_20_ameva_avyayena_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    up = state.terms[i]
    pr = state.terms[i + 1]
    merged_varnas = [v.clone() for v in up.varnas] + [v.clone() for v in pr.varnas]
    merged = Term(
        kind="prakriti",
        varnas=merged_varnas,
        tags={"prātipadika", "anga", "avyaya"},
        meta={"upadesha_slp1": "".join(v.slp1 for v in merged_varnas)},
    )
    before = state.flat_slp1()
    state.terms = state.terms[:i] + [merged] + state.terms[i + 2 :]
    state.meta["2_2_20_ameva_avyayena_done"] = True
    state.trace.append({
        "sutra_id": "__2_2_20_MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "अमेव-अव्यय-समासः",
        "form_before": before,
        "form_after": state.flat_slp1(),
        "why_dev": "अमन्त-अव्ययेन उपपदस्य समासः (संरचनात्मकं, न सूत्रम्)।",
        "status": "APPLIED",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.2.20",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1      = "ameva avyayena",
    text_dev       = "अमेवाव्ययेन",
    padaccheda_dev = "अम् एव / अव्ययेन",
    why_dev        = "अमन्त-अव्ययेन सह उपपदस्य समासः (कृन्मेजन्त-प्रसङ्गे)।",
    anuvritti_from = ("2.2.19",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

