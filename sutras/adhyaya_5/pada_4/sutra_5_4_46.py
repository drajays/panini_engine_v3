"""
5.4.46  अतिग्रहाव्यथनक्षेपेष्वकर्तरि तृतीयायाः  —  VIDHI

Padaccheda: अतिग्रह-अव्यथन-क्षेपेषु अ-कर्तरि तृतीयायाः

अतिग्रहाव्यथनक्षेपेष्वकर्तरि तृतीयायाः (5.4.46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_46_atigrahAvy_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_46_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "atigrahAvyaTanakzepezvakartari tftIyAyAH",
    text_dev              = "अतिग्रहाव्यथनक्षेपेष्वकर्तरि तृतीयायाः",
    padaccheda_dev        = "अतिग्रह-अव्यथन-क्षेपेषु अ-कर्तरि तृतीयायाः",
    why_dev               = "(सूत्रम् 5.4.46) अतिग्रहाव्यथनक्षेपेष्वकर्तरि तृतीयायाः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
