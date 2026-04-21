"""
1.2.46  कृत्तद्धितसमासाश्च  —  SAMJNA

A stem formed by a kṛt / taddhita affix (or a compound) is called
*prātipadika* — licensing sup attachment under ``4.1.1`` / ``4.1.2``.

Engine: fires once a kṛt-augmented dhātu shape is ready (after ``7.2.116`` on
the agent-noun path); registry flag for trace only.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    if "dhatu" not in state.terms[0].tags:
        return False
    if "krt" not in state.terms[-1].tags:
        return False
    if state.samjna_registry.get("1.2.46_krit_pratipadika"):
        return False
    t0 = state.terms[0]
    pr = state.terms[-1]
    if t0.meta.get("upadha_vrddhi_done") is True:
        return True
    if t0.meta.get("aco_nniti_vrddhi_done") is True:
        return True
    # tṛc / 7.3.84 guṇa on aṅga (e.g. चि → चे before ``tf``).
    if t0.meta.get("anga_guna_7_3_84") is True and "krt" in pr.tags:
        return True
    return False


def act(state: State) -> State:
    state.samjna_registry["1.2.46_krit_pratipadika"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.2.46",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "kft-taddhita-samAsAH ca",
    text_dev       = "कृत्तद्धितसमासाश्च",
    padaccheda_dev = "कृत्-तद्धित-समासाः च (प्रातिपदिकम्)",
    why_dev        = "कृत्-तद्धित-समासान्ताः शब्दाः प्रातिपदिक-संज्ञकाः।",
    anuvritti_from = ("1.2.45",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
