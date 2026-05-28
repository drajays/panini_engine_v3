"""
7.2.5  ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम्  —  VIDHI

Padaccheda: ह्-म्-य्-अन्त-क्षण-श्वस-जागृ-णि-श्वि-एदिताम्

ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम् (7.2.5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_5_hmyantakza_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.5", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_2_5_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hmyantakzaRaSvasajAgfRiSvyeditAm",
    text_dev              = "ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम्",
    padaccheda_dev        = "ह्-म्-य्-अन्त-क्षण-श्वस-जागृ-णि-श्वि-एदिताम्",
    why_dev               = "(सूत्रम् 7.2.5) ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
