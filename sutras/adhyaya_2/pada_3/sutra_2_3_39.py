"""
2.3.39  स्वामीश्वराधिपतिदायादसाक्षिप्रतिभूप्रसूतैश्च  —  VIDHI

Padaccheda: स्वामि-ईश्वर-अधिपति-दायाद-साक्षि-प्रतिभू-प्रसूतैः च

svami, isvara, adhipati etc. take sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_39_svami_isvara"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_39_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svAmISvarADipatidAyAdasAkzipratiBUprasUtESca",
    text_dev              = "स्वामीश्वराधिपतिदायादसाक्षिप्रतिभूप्रसूतैश्च",
    padaccheda_dev        = "स्वामि-ईश्वर-अधिपति-दायाद-साक्षि-प्रतिभू-प्रसूतैः च",
    why_dev               = "स्वामि-ईश्वर-अधिपति-दायाद-साक्षि-प्रतिभू-प्रसूतैः च षष्ठी (२.३.३९)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
