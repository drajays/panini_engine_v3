"""
5.2.18  गोष्ठात् खञ् भूतपूर्वे  —  VIDHI

Padaccheda: गोष्ठात् खञ् भूतपूर्वे

गोष्ठात् खञ् भूतपूर्वे (5.2.18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_18_gozWAt_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_18_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gozWAt KaY BUtapUrve",
    text_dev              = "गोष्ठात् खञ् भूतपूर्वे",
    padaccheda_dev        = "गोष्ठात् खञ् भूतपूर्वे",
    why_dev               = "(सूत्रम् 5.2.18) गोष्ठात् खञ् भूतपूर्वे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
