"""
2.1.52  संख्यापूर्वो द्विगुः  —  VIDHI

Padaccheda: संख्या-पूर्वः द्विगुः

samkhya-purva (numeral-first) compound is called dvigu.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_52_samkhya_dvigu"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_52_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvigu_kind"]             = "2.1.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyApUrvo dviguH",
    text_dev              = "संख्यापूर्वो द्विगुः",
    padaccheda_dev        = "संख्या-पूर्वः द्विगुः",
    why_dev               = "संख्या-पूर्वः द्विगुः समासः (२.१.५२)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
