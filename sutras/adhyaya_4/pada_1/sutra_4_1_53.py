"""
4.1.53  अस्वाङ्गपूर्वपदाद्वा  —  VIDHI

Padaccheda: अ-स्वाङ्ग-पूर्वपदात् वा

अस्वाङ्गपूर्वपदाद्वा (4.1.53)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_53_asvANgapUr_53"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_53_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asvANgapUrvapadAdvA",
    text_dev              = "अस्वाङ्गपूर्वपदाद्वा",
    padaccheda_dev        = "अ-स्वाङ्ग-पूर्वपदात् वा",
    why_dev               = "(सूत्रम् 4.1.53) अस्वाङ्गपूर्वपदाद्वा।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
