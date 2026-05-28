"""
6.3.58  पेषंवासवाहनधिषु च  —  VIDHI

Padaccheda: पेषं-वास-वाहन-धिषु च

पेषंवासवाहनधिषु च (6.3.58)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_58_pezaMvAsav_58"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pezaMvAsavAhanaDizu ca",
    text_dev              = "पेषंवासवाहनधिषु च",
    padaccheda_dev        = "पेषं-वास-वाहन-धिषु च",
    why_dev               = "(सूत्रम् 6.3.58) पेषंवासवाहनधिषु च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
