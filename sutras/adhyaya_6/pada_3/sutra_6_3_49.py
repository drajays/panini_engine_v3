"""
6.3.49  विभाषा चत्वारिंशत्प्रभृतौ सर्वेषाम्  —  VIDHI

Padaccheda: विभाषा चत्वारिंशत्-प्रभृतौ सर्वेषाम्

विभाषा चत्वारिंशत्प्रभृतौ सर्वेषाम् (6.3.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_49_viBAzA_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA catvAriMSatpraBftO sarvezAm",
    text_dev              = "विभाषा चत्वारिंशत्प्रभृतौ सर्वेषाम्",
    padaccheda_dev        = "विभाषा चत्वारिंशत्-प्रभृतौ सर्वेषाम्",
    why_dev               = "(सूत्रम् 6.3.49) विभाषा चत्वारिंशत्प्रभृतौ सर्वेषाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
