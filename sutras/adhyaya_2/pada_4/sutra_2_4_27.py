"""
2.4.27  पूर्ववदश्ववडवौ  —  VIDHI

Padaccheda: पूर्व-वत् अश्ववडवौ

asva and vadava follow the former member's gender.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_27_asva_vadava_purvavat"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(
        "dvandva_samasa" in t.tags or "samasa_member" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrvavadaSvavaqavO",
    text_dev              = "पूर्ववदश्ववडवौ",
    padaccheda_dev        = "पूर्व-वत् अश्ववडवौ",
    why_dev               = "अश्ववडवौ पूर्व-वत् (२.४.२७)।",
    anuvritti_from        = ('2.4.26',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
