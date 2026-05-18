"""
8.4.4  वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः  —  VIDHI

Padaccheda: वनम् (षष्ठीस्थाने व्यत्ययेन प्रथमा) पुरगा-मिश्रका-सिध्रका-शारिका-कोटरा-अग्रेभ्यः

वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः (8.4.4)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_4_vanaM_4"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_4_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vanaM puragAmiSrakAsiDrakASArikAkowarA'greByaH",
    text_dev              = "वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः",
    padaccheda_dev        = "वनम् (षष्ठीस्थाने व्यत्ययेन प्रथमा) पुरगा-मिश्रका-सिध्रका-शारिका-कोटरा-अग्रेभ्यः",
    why_dev               = "(सूत्रम् 8.4.4) वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
