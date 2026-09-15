"""
3.4.87  सेर्ह्यपिच्च  —  VIDHI (*loṭ* *sip* → *hi*)

Sources consulted:
- ashtadhyayi.com data.txt row i=304087
- Kāśikā: लोटि सिप्-स्थाने हि (अपित् — न पित्)
- Cross-validation: tests/unit/test_sthanivat_it_samjna.py

*hi* ādeśa inherits **apit** (not *pit*) from *sip* via **1.1.56** it-sthanivat.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import adesha_substitute_varnas
from phonology.varna import parse_slp1_upadesha_sequence


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "sip":
            continue
        if t.meta.get("source_lakara_upadesha") != "loT":
            continue
        if t.meta.get("P031_3_4_87_hi_done"):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.meta.setdefault("is_apit", True)
    adesha_substitute_varnas(t, "hi", state, sutra_id="3.4.87")
    t.tags.add("tin_adesha_3_4_78")
    t.meta["P031_3_4_87_hi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.87",
    sutra_type=SutraType.VIDHI,
    text_slp1="ser hyapic ca",
    text_dev="सेर्ह्यपिच्च",
    padaccheda_dev="सेः / हि / अपि / च",
    why_dev="लोटि सिप्-स्थाने हि-आदेशः; अपित्-स्थानिवत् (पित् न)।",
    anuvritti_from=("3.4.86",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
