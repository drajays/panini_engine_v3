"""
3.4.81  लिटस्तझयोरेशिरेच्  —  VIDHI (narrow demo)

Demo slice (ईधे):
  In liṭ, replace the 3sg ātmane-pada ending `ta` with `eS`.
  Then `S` is it (1.3.3) and is loped (1.3.9) leaving `e`.

Engine:
  - recipe arms via ``state.meta['3_4_81_lit_esh_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_ta(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() == "ta":
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("lakara_liT"):
        return False
    if not state.meta.get("3_4_81_lit_esh_arm"):
        return False
    return _find_ta(state) is not None


def act(state: State) -> State:
    ti = _find_ta(state)
    if ti is None:
        return state
    pr = state.terms[ti]
    pr.varnas = list(parse_slp1_upadesha_sequence("eS"))
    pr.meta["upadesha_slp1"] = "eS"
    pr.tags.add("upadesha")
    state.meta["3_4_81_lit_esh_arm"] = False
    # record that 1.1.55 was intended for this replacement
    state.meta["1_1_55_anekal_shit_sarvasya_arm"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.81",
    sutra_type=SutraType.VIDHI,
    text_slp1="liTastajhyor eSirec",
    text_dev="लिटस्तझयोरेशिरेच्",
    padaccheda_dev="लिटः / त-झयोः / एशि-रेच्",
    why_dev="लिटि ‘त’ इत्यस्य ‘एश्’ आदेशः (ईधे)।",
    anuvritti_from=("3.4.78",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

