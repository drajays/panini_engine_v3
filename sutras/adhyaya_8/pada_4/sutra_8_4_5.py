"""
8.4.5  प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपियूक्षाभ्योऽसंज्ञायामपि  —  VIDHI

Padaccheda: प्र-निः-अन्तः-शर-इक्षु-प्लक्ष-आम्र-कार्ष्य-खदिर-पियूक्षाभ्यः अ-संज्ञायाम् अपि

प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपियूक्षाभ्योऽसंज्ञायामपि (8.4.5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_5_praniranta_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pranirantaHSarekzuplakzAmrakArzyaKadirapiyUkzAByo'saMjYAyAmapi",
    text_dev              = "प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपियूक्षाभ्योऽसंज्ञायामपि",
    padaccheda_dev        = "प्र-निः-अन्तः-शर-इक्षु-प्लक्ष-आम्र-कार्ष्य-खदिर-पियूक्षाभ्यः अ-संज्ञायाम् अपि",
    why_dev               = "(सूत्रम् 8.4.5) प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपियूक्षाभ्योऽसंज्ञायामपि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
