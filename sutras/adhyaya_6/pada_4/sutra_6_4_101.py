"""
6.4.101  हुझल्भ्यो हेर्धिः  —  VIDHI (narrow: P031 *hi* → *ḍhi*)

After a *jhal*-final *aṅga*, *loṭ* *hi* is replaced by *dhi* (here **Qi** in
engine SLP1 = ढ् + मात्रा *i*, matching *viśiṇḍhi*).

Arms: ``state.meta['P031_6_4_101_hi_to_Qi_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import TING_PRATYAYATVA, adesha_substitute_varnas
from phonology.pratyahara import JHAL


def _find_hi(state: State) -> int | None:
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
    ang_final = state.terms[hi_i - 1].varnas[-1].slp1
    # Dental *aṅga* (*ad* … अद्धि): *Dhi*; else P031 *Qi* (ढि, *viśiṇḍhi*).
    if ang_final == "d":
        adesha_substitute_varnas(
            t, "Di", state,
            sutra_id="6.4.101",
            gunadharmas=frozenset({TING_PRATYAYATVA}),
        )
    else:
        adesha_substitute_varnas(
            t, "Qi", state,
            sutra_id="6.4.101",
            gunadharmas=frozenset({TING_PRATYAYATVA}),
        )
    t.tags.add("tin_adesha_3_4_78")
    t.meta["P031_6_4_101_done"] = True
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
