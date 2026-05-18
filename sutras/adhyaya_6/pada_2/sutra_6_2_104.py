"""
6.2.104  आचार्योपसर्जनश्चान्तेवासिनि  —  VIDHI

Padaccheda: आचार्योपसर्जनः (सुपां स्थाने सुर्भवतीति --७.१.३९ ; सप्तम्येकवचनस्य स्थाने प्रथमैकवचनम्) च अन्तेवासिनि

आचार्योपसर्जनश्चान्तेवासिनि (6.2.104)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_104_AcAryopasa_104"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_104_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AcAryopasarjanaScAntevAsini",
    text_dev              = "आचार्योपसर्जनश्चान्तेवासिनि",
    padaccheda_dev        = "आचार्योपसर्जनः (सुपां स्थाने सुर्भवतीति --७.१.३९ ; सप्तम्येकवचनस्य स्थाने प्रथमैकवचनम्) च अन्तेवासिनि",
    why_dev               = "(सूत्रम् 6.2.104) आचार्योपसर्जनश्चान्तेवासिनि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
