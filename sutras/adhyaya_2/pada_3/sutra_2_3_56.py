"""
2.3.56  जासिनिप्रहणनाटक्राथपिषां हिंसायाम्  —  VIDHI

Padaccheda: जासि-नि-प्र-हण-नाट-क्राथ-पिषाम् हिंसायाम्

jasi, ni, pra, han, nat, krath, pis in violence context take sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_56_jasi_himsa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_56_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAsiniprahaRanAwakrATapizAM hiMsAyAm",
    text_dev              = "जासिनिप्रहणनाटक्राथपिषां हिंसायाम्",
    padaccheda_dev        = "जासि-नि-प्र-हण-नाट-क्राथ-पिषाम् हिंसायाम्",
    why_dev               = "जासि-नि-प्र-हण-नाट-क्राथ-पिषाम् हिंसायाम् (२.३.५६)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
