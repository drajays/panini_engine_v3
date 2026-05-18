"""
4.4.125  तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः  —  VIDHI

Padaccheda: तद्वान् आसाम् उपधानः मन्त्रः इति इष्टकासु लुक् च मतोः

तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः (4.4.125)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_125_tadvAnAsAm_125"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_125_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadvAnAsAmupaDAno mantra itIzwakAsu luk ca matoH",
    text_dev              = "तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः",
    padaccheda_dev        = "तद्वान् आसाम् उपधानः मन्त्रः इति इष्टकासु लुक् च मतोः",
    why_dev               = "(सूत्रम् 4.4.125) तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
