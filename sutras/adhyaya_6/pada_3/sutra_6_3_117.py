"""
6.3.117  वनगिर्योः संज्ञायां कोटरकिंशुलकादीनाम्  —  VIDHI

Padaccheda: वन-गिर्योः संज्ञायाम् कोटर-किंशुलक-आदीनाम्

वनगिर्योः संज्ञायां कोटरकिंशुलकादीनाम् (6.3.117)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_117_vanagiryoH_117"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_117_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.117"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vanagiryoH saMjYAyAM kowarakiMSulakAdInAm",
    text_dev              = "वनगिर्योः संज्ञायां कोटरकिंशुलकादीनाम्",
    padaccheda_dev        = "वन-गिर्योः संज्ञायाम् कोटर-किंशुलक-आदीनाम्",
    why_dev               = "(सूत्रम् 6.3.117) वनगिर्योः संज्ञायां कोटरकिंशुलकादीनाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
