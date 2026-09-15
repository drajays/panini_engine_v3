"""
7.1.85  पथिमथ्यृभुक्षामात्  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=701085
- Kāśikā: "पथिनः प्रथमैकवचने नस्य आः"
- Cross-validation: tests/unit/test_sthanivat_al_ashrita_exceptions.py

Final *n* of *pathin* / *mathin* / … → *ā*; *hal*-antatva of *n* is **not**
extended onto the *ā* ādeśa (*al*-vidhi after *sthānin*).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.sthanivat import BLOCK_AL_AFTER_STHANIN, adesha_substitute_varnas

_PATHIN_STEMS = frozenset({"pathin", "maTin", "fBu", "kzAm"})


def _pathin_anga_index(state: State) -> int | None:
    if state.meta.get("7_1_85_pathin_done"):
        return None
    if not adhikara_in_effect("7.1.85", state, "6.4.1"):
        if not state.meta.get("sthanivat_lesson_pathin"):
            return None
    for i, t in enumerate(state.terms):
        if "anga" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _PATHIN_STEMS:
            if [v.slp1 for v in t.varnas] not in (
                ["p", "a", "T", "i", "n"],
                ["p", "a", "T", "i"],
            ):
                continue
        if not t.varnas or t.varnas[-1].slp1 != "n":
            continue
        if i + 1 >= len(state.terms):
            continue
        if "sup" not in state.terms[i + 1].tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _pathin_anga_index(state) is not None


def act(state: State) -> State:
    i = _pathin_anga_index(state)
    if i is None:
        return state
    anga = state.terms[i]
    base = [v.slp1 for v in anga.varnas[:-1]]
    new_slp1 = "".join(base) + "A"
    adesha_substitute_varnas(
        anga,
        new_slp1,
        state,
        sutra_id="7.1.85",
        sthanivat_block=BLOCK_AL_AFTER_STHANIN,
    )
    anga.meta["7_1_85_a_adesha"] = True
    anga.meta["halantatva_inhibited"] = True
    state.meta["7_1_85_pathin_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.1.85",
    sutra_type=SutraType.VIDHI,
    text_slp1="paTimaTyfBukzAmAt",
    text_dev="पथिमथ्यृभुक्षामात्",
    padaccheda_dev="पथि-मथि-ऋभुक्षाम् आत्",
    why_dev="पथिन्-अन्त्य-नस्य आ-आदेशः; हलन्तत्वम् आ-आदेशे न स्थानिवत्।",
    anuvritti_from=("7.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
