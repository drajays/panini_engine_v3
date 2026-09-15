"""
7.1.86  इतोऽत् सर्वनामस्थाने  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=701086
- Kāśikā: "पन्थाम् इतः अत्"
- Cross-validation: tests/unit/test_sthanivat_al_ashrita_exceptions.py

*it* (इ) → *a* (अ) before sarvanāmasthāna *sup* on *pathin* class stems
(after **7.1.85**).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology import mk


def _site(state: State) -> int | None:
    if state.meta.get("7_1_86_ito_at_done"):
        return None
    if not adhikara_in_effect("7.1.86", state, "6.4.1"):
        if not state.meta.get("sthanivat_lesson_pathin"):
            return None
    for i, t in enumerate(state.terms):
        if "anga" not in t.tags:
            continue
        if not t.varnas:
            continue
        if t.varnas[-1].slp1 != "A":
            continue
        if not t.meta.get("7_1_85_a_adesha"):
            continue
        for vi, v in enumerate(t.varnas):
            if v.slp1 == "i":
                if i + 1 < len(state.terms) and "sup" in state.terms[i + 1].tags:
                    return (i, vi)
        if [v.slp1 for v in t.varnas] == ["p", "a", "T", "i", "A"]:
            return (i, 3)
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    hit = _site(state)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi] = mk("a")
    state.meta["7_1_86_ito_at_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.1.86",
    sutra_type=SutraType.VIDHI,
    text_slp1="ito't sarvanAmasTAne",
    text_dev="इतोऽत् सर्वनामस्थाने",
    padaccheda_dev="इतः अत् सर्वनामस्थाने",
    why_dev="सर्वनामस्थाने इकारस्य अ-आदेशः (पथिन्-श्रेणिः)।",
    anuvritti_from=("7.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
