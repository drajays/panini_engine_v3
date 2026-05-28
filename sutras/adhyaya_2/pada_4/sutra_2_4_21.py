"""
2.4.21  उपज्ञोपक्रमं तदाद्याचिख्यासायाम्  —  VIDHI

Padaccheda: उपज्ञा-उपक्रमम् तदाद्याचिख्यासायाम्

upajña and upakrama in 'desiring to teach' context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_21_upajna_upakrama"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.21", state, "2.4.19")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upajYopakramaM tadAdyAciKyAsAyAm",
    text_dev              = "उपज्ञोपक्रमं तदाद्याचिख्यासायाम्",
    padaccheda_dev        = "उपज्ञा-उपक्रमम् तदाद्याचिख्यासायाम्",
    why_dev               = "उपज्ञा-उपक्रमम् तदाद्याचिख्यासायाम् (२.४.२१)।",
    anuvritti_from        = ('2.4.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
