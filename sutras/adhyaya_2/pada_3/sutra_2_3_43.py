"""
2.3.43  साधुनिपुणाभ्याम् अर्चायां सप्तम्यप्रतेः  —  VIDHI

Padaccheda: साधु-निपुणाभ्याम् अर्चायाम् सप्तमी अ-प्रतेः

sadhu and nipuna in worship context take saptami.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_43_sadhu_nipuna"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sADunipuRAByAm arcAyAM saptamyaprateH",
    text_dev              = "साधुनिपुणाभ्याम् अर्चायां सप्तम्यप्रतेः",
    padaccheda_dev        = "साधु-निपुणाभ्याम् अर्चायाम् सप्तमी अ-प्रतेः",
    why_dev               = "साधु-निपुणाभ्याम् अर्चायाम् सप्तमी (२.३.४३)।",
    anuvritti_from        = ('2.3.36',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
