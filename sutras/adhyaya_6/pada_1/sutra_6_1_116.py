"""
6.1.116  अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च  —  VIDHI

Padaccheda: अव्यात्-अवद्यात्-अवक्रमुः-अव्रत-अयम्-अवन्तु-अवस्युषु च

अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च (6.1.116)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_116_avyAdavady_116"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_116_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avyAdavadyAdavakramuravratAyamavantvavasyuzu ca",
    text_dev              = "अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च",
    padaccheda_dev        = "अव्यात्-अवद्यात्-अवक्रमुः-अव्रत-अयम्-अवन्तु-अवस्युषु च",
    why_dev               = "(सूत्रम् 6.1.116) अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
