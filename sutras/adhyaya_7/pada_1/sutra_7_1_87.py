"""
7.1.87  थो न्थः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=71087
- Kāśikā: "पन्थाः थः न्थः"
- Cross-validation: tests/unit/test_sthanivat_al_ashrita_exceptions.py

*th* (थ) → *nth* (न्थ्) in *pathin* class stems before sarvanāmasthāna *sup*.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.declension import anga_and_sup, is_stem
from engine.state import State
from phonology import mk


def _site_real(state: State):
    """थो न्थः — पथिन् / मथिन् before a sarvanāmasthāna sup: the th becomes nth (पन्थाः, मन्थानौ); ऋभुक्षिन् has no th."""
    hit = anga_and_sup(state, "7.1.87")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "paTin", "maTin", tadanta=True) or "sarvanamasthana" not in sup.tags or anga.meta.get("7_1_87_done"):
        return None
    for vi, v in enumerate(anga.varnas):
        if v.slp1 == "T":
            return anga, vi
    return None


def _site(state: State) -> int | None:
    if state.meta.get("7_1_87_tho_ntha_done"):
        return None
    if not adhikara_in_effect("7.1.87", state, "6.4.1"):
        if not state.meta.get("sthanivat_lesson_pathin"):
            return None
    for i, t in enumerate(state.terms):
        if "anga" not in t.tags:
            continue
        for vi, v in enumerate(t.varnas):
            if v.slp1 != "T":
                continue
            if i + 1 >= len(state.terms) or "sup" not in state.terms[i + 1].tags:
                continue
            if t.meta.get("7_1_85_a_adesha") or state.meta.get("sthanivat_lesson_pathin"):
                return (i, vi)
    return None


def cond(state: State) -> bool:
    return _site(state) is not None or _site_real(state) is not None


def act(state: State) -> State:
    real = _site_real(state)
    if real is not None:
        anga, vi = real
        anga.varnas[vi:vi + 1] = [mk("n"), mk("T")]
        anga.meta["7_1_87_done"] = True
        return state
    hit = _site(state)
    if hit is None:
        return state
    ti, vi = hit
    t = state.terms[ti]
    t.varnas[vi : vi + 1] = [mk("n"), mk("T")]
    state.meta["7_1_87_tho_ntha_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.1.87",
    sutra_type=SutraType.VIDHI,
    text_slp1="To nTaH",
    text_dev="थो न्थः",
    samagra_slp1="paTi-maTi-fBukzAmaNgasya TaH sarvanAmasTAne nTaH",
    samagra_dev="पथि-मथि-ऋभुक्षामङ्गस्य थः सर्वनामस्थाने न्थः",
    padaccheda_dev="थः न्थः",
    why_dev="पथिन्-श्रेण्यां थकारस्य न्थ्-आदेशः।",
    anuvritti_from=("7.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
