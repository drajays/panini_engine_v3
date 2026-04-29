"""
3.4.82  परस्मैपदानां णलतुसुस्थलथुसणल्वमाः  —  VIDHI (narrow demo)

Demo slice (विभिदतुः):
  In liṭ, for parasmaipada 3rd dual, replace `tas` with `atus`.

Engine:
  - expects `tas` already produced by **3.4.78** (via canonical tin-ādeśa slice)
    with ``state.meta['tin_adesha_slp1'] == 'tas'``.
  - applies only when ``state.meta['lakara_liT']`` is True and recipe arms via
    ``state.meta['3_4_82_lit_atus_arm']``.
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


def cond(state: State) -> bool:
    if not state.meta.get("lakara_liT"):
        return False
    if not state.meta.get("3_4_82_lit_atus_arm"):
        return False
    return _find_tas(state) is not None


def act(state: State) -> State:
    ti = _find_tas(state)
    if ti is None:
        return state
    atus = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("atus"),
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
    why_dev="लिटि परस्मैपदे तस् → अतुस् (विभिदतुः)।",
    anuvritti_from=("3.4.78",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

