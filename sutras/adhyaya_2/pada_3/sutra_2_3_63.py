"""
2.3.63  यजेश्च करणे  —  VIDHI

Padaccheda: यजेः च करणे

yaj root also takes tritiya for karana.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_63_yajeh_karane"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_63_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yajeSca karaRe",
    text_dev              = "यजेश्च करणे",
    padaccheda_dev        = "यजेः च करणे",
    why_dev               = "यजेः च करणे (२.३.६३)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
