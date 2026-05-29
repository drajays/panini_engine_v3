"""
3.4.81  लिटस्तझयोरेशिरेच्  —  VIDHI

In liṭ:
  - ātmanepada 3sg `ta` → `eS` (eŚ after IT-lopa = e)
  - ātmanepada 3pl `Ja` (jha) → `irec` (iReC after IT-lopa = ire)

Engine: recipe arms via ``state.meta['liT_esh_recipe']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_ta_or_Ja(state: State):
    """Return (index, kind) where kind in {'ta', 'Ja'}."""
    for i, t in enumerate(state.terms):
        if "pratyaya" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "ta":
            return (i, "ta")
        if up == "Ja":
            return (i, "Ja")
    return None


def cond(state: State) -> bool:
    if not state.meta.get("lakara_liT"):
        return False
    if not state.meta.get("liT_esh_recipe"):
        return False
    return _find_ta_or_Ja(state) is not None


def act(state: State) -> State:
    hit = _find_ta_or_Ja(state)
    if hit is None:
        return state
    ti, kind = hit
    pr = state.terms[ti]
    if kind == "ta":
        pr.varnas = list(parse_slp1_upadesha_sequence("eS"))
        pr.meta["upadesha_slp1"] = "eS"
    else:  # Ja → irec
        pr.varnas = list(parse_slp1_upadesha_sequence("irec"))
        pr.meta["upadesha_slp1"] = "irec"
    pr.tags.add("upadesha")
    state.meta["liT_esh_recipe"] = False
    state.meta["anekal_shit_recipe"] = True
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

