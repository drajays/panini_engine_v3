"""
3.2.46  संज्ञायां भृतॄवृजिधारिसहितपिदमः  —  VIDHI

Padaccheda: संज्ञायाम् भृ-तॄ-वृ-जि-धारि-सहि-तपि-दमः

krt-suffix rule: संज्ञायां भृतॄवृजिधारिसहितपिदमः (46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_46_saMjYAyAM_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_46_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAM BftFvfjiDArisahitapidamaH",
    text_dev              = "संज्ञायां भृतॄवृजिधारिसहितपिदमः",
    padaccheda_dev        = "संज्ञायाम् भृ-तॄ-वृ-जि-धारि-सहि-तपि-दमः",
    why_dev               = "धातोः कृत्-प्रत्ययः [संज्ञायां भृतॄवृजिधारिसहितपिदमः] विहितः (३.२.46)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
