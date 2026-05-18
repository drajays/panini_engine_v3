"""
7.3.1  देविकाशिंशपादित्यवाड्दीर्घसत्रश्रेयसामात्  —  VIDHI

Padaccheda: देविका-शिंशपा-दित्यवाट्-दीर्घसत्र-श्रेयसाम् आत्

देविकाशिंशपादित्यवाड्दीर्घसत्रश्रेयसामात् (7.3.1)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_1_devikASiMS_1"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_1_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.1"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.1",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "devikASiMSapAdityavAqdIrGasatraSreyasAmAt",
    text_dev              = "देविकाशिंशपादित्यवाड्दीर्घसत्रश्रेयसामात्",
    padaccheda_dev        = "देविका-शिंशपा-दित्यवाट्-दीर्घसत्र-श्रेयसाम् आत्",
    why_dev               = "(सूत्रम् 7.3.1) देविकाशिंशपादित्यवाड्दीर्घसत्रश्रेयसामात्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
