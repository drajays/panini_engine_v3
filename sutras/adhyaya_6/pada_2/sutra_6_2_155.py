"""
6.2.155  नञो गुणप्रतिषेधे सम्पाद्यर्हहितालमर्थास्तद्धिताः  —  VIDHI

Padaccheda: नञः गुणप्रतिषेधे सम्पादी-अर्ह-हित-अलम्-अर्थाः तद्धिताः

नञो गुणप्रतिषेधे सम्पाद्यर्हहितालमर्थास्तद्धिताः (6.2.155)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_155_naYo_155"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_155_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.155"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.155",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naYo guRapratizeDe sampAdyarhahitAlamarTAstadDitAH",
    text_dev              = "नञो गुणप्रतिषेधे सम्पाद्यर्हहितालमर्थास्तद्धिताः",
    padaccheda_dev        = "नञः गुणप्रतिषेधे सम्पादी-अर्ह-हित-अलम्-अर्थाः तद्धिताः",
    why_dev               = "(सूत्रम् 6.2.155) नञो गुणप्रतिषेधे सम्पाद्यर्हहितालमर्थास्तद्धिताः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
