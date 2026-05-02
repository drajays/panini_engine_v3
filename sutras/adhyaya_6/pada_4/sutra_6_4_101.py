"""
6.4.101  हुझल्भ्यो हेर्धिः  —  VIDHI (narrow: P031 *hi* → *ḍhi*)

After a *jhal*-final *aṅga*, *loṭ* *hi* is replaced by *dhi* (here **Qi** in
engine SLP1 = ढ् + मात्रा *i*, matching *viśiṇḍhi*).

Arms: ``state.meta['P031_6_4_101_hi_to_Qi_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import JHAL
from phonology.varna import parse_slp1_upadesha_sequence


def _find_hi(state: State) -> int | None:
    if not state.meta.get("P031_6_4_101_hi_to_Qi_arm"):
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "hi":
            continue
        if t.meta.get("P031_6_4_101_done"):
            continue
        return i
    return None


def _anga_jhal_final(state: State, hi_idx: int) -> bool:
    if hi_idx < 1:
        return False
    ang = state.terms[hi_idx - 1]
    if "anga" not in ang.tags:
        return False
    if not ang.varnas:
        return False
    return ang.varnas[-1].slp1 in JHAL


def cond(state: State) -> bool:
    hi_i = _find_hi(state)
    if hi_i is None:
        return False
    return _anga_jhal_final(state, hi_i)


def act(state: State) -> State:
    hi_i = _find_hi(state)
    if hi_i is None or not _anga_jhal_final(state, hi_i):
        return state
    t = state.terms[hi_i]
    t.varnas = list(parse_slp1_upadesha_sequence("Qi"))
    t.meta["upadesha_slp1"] = "Qi"
    t.tags.add("tin_adesha_3_4_78")
    t.meta["P031_6_4_101_done"] = True
    state.meta.pop("P031_6_4_101_hi_to_Qi_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.101",
    sutra_type=SutraType.VIDHI,
    text_slp1="huJal-bhyo her dhiH",
    text_dev="हुझल्भ्यो हेर्धिः",
    padaccheda_dev="हुझल्भ्यः / हेः / धिः",
    why_dev="झल्-परत्वे हि-स्थाने ढि-आदेशः — प०३१ (*विशिण्ढि*)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
