"""
6.2.38  महान् व्रीह्यपराह्णगृष्टीष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु  —  VIDHI

Padaccheda: महान् व्रीहि-अपराह्ण-गृष्टि-इष्वास-जाबाल-भार-भारत-हैलि-हिल-रौरव-प्रवृद्धेषु

महान् व्रीह्यपराह्णगृष्टीष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु (6.2.38)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_38_mahAn_38"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mahAn vrIhyaparAhRagfzwIzvAsajAbAlaBAraBAratahElihilarOravapravfdDezu",
    text_dev              = "महान् व्रीह्यपराह्णगृष्टीष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु",
    padaccheda_dev        = "महान् व्रीहि-अपराह्ण-गृष्टि-इष्वास-जाबाल-भार-भारत-हैलि-हिल-रौरव-प्रवृद्धेषु",
    why_dev               = "(सूत्रम् 6.2.38) महान् व्रीह्यपराह्णगृष्टीष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
