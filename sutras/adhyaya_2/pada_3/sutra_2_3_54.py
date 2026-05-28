"""
2.3.54  रुजार्थानां भाववचनानामज्वरेः  —  VIDHI

Padaccheda: रुजा-अर्थानाम् भाव-वचनानाम् अज्वरेः

Disease-words with bhava meaning take sasthi (except jvara).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_54_ruja_bhava"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rujArTAnAM BAvavacanAnAmajvareH",
    text_dev              = "रुजार्थानां भाववचनानामज्वरेः",
    padaccheda_dev        = "रुजा-अर्थानाम् भाव-वचनानाम् अज्वरेः",
    why_dev               = "रुजा-अर्थानाम् भाव-वचनानाम् अज्वरेः (२.३.५४)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
