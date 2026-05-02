"""
3.4.82  परस्मैपदानां णलतुसुस्थलथुसणल्वमाः  —  VIDHI (narrow demo)

Demo slice (विभिदतुः):
  In liṭ, for parasmaipada 3rd dual, replace `tas` with `atus`.

Teaching JSON **P036** (*nināya*): in liṭ, for parasmaipada 3rd singular, replace
``tip``/``ti`` (after **3.4.78**) with ``ṇal`` (machine ``Nal``).

Engine:
  • *atus*: ``state.meta['3_4_82_lit_atus_arm']`` + ``tas`` from **3.4.78**.
  • **P036**: ``state.meta['P036_3_4_82_lit_Nal_arm']`` + ``tip``/``ti`` *tiṅ* row.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _find_tas(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "tas":
            return i
    return None


def _find_lit_tip(state: State) -> int | None:
    if not state.meta.get("P036_3_4_82_lit_Nal_arm"):
        return None
    if not state.meta.get("lakara_liT"):
        return None
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"tip", "ti"}:
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("lakara_liT"):
        return False
    if state.meta.get("3_4_82_lit_atus_arm"):
        return _find_tas(state) is not None
    if state.meta.get("P036_3_4_82_lit_Nal_arm"):
        return _find_lit_tip(state) is not None
    return False


def act(state: State) -> State:
    if state.meta.get("P036_3_4_82_lit_Nal_arm"):
        ti = _find_lit_tip(state)
        if ti is None:
            return state
        nal = Term(
            kind="pratyaya",
            varnas=list(parse_slp1_upadesha_sequence("Nal")),
            tags={"pratyaya", "tin", "ardhadhatuka", "upadesha"},
            meta={"upadesha_slp1": "Nal", "lit_Nal": True},
        )
        # **1.3.9** *it*-lopa on ``ṇal`` requires the final ``l`` to carry an *it* tag
        # (``parse_slp1_upadesha_sequence`` does not mark ``Nal`` like ``tip``).
        if nal.varnas and nal.varnas[-1].slp1 == "l":
            nal.varnas[-1].tags.add("it_candidate_halantyam")
        state.terms[ti] = nal
        state.meta["P036_3_4_82_lit_Nal_arm"] = False
        return state
    ti = _find_tas(state)
    if ti is None:
        return state
    atus = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("atus")),
        tags={"pratyaya", "tin", "ardhadhatuka"},
        meta={"upadesha_slp1": "atus", "lit_atus": True},
    )
    state.terms[ti] = atus
    state.meta["3_4_82_lit_atus_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.82",
    sutra_type=SutraType.VIDHI,
    text_slp1="parasmaipadAnAm Ralatusu... (narrow)",
    text_dev="परस्मैपदानां णलतुसुस्थलथुसणल्वमाः",
    padaccheda_dev="परस्मैपदानाम् / णल-तुसु-स्थ-लथुस्-णल्-वमाः",
    why_dev="लिटि परस्मैपदे तस् → अतुस्; एकवचने तिप् → णल् (प०३६)।",
    anuvritti_from=("3.4.78",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
