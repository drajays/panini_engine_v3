"""
2.1.56  उपमितं व्याघ्रादिभिः सामान्याप्रयोगे  —  VIDHI

Padaccheda: उपमितम् व्याघ्र-आदिभिः सामान्य-अप्रयोगे

upamita with vyaghra etc. in non-samanya use forms karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_56_upamita_vyaghra"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upamitaM vyAGrAdiBiH sAmAnyAprayoge",
    text_dev              = "उपमितं व्याघ्रादिभिः सामान्याप्रयोगे",
    padaccheda_dev        = "उपमितम् व्याघ्र-आदिभिः सामान्य-अप्रयोगे",
    why_dev               = "उपमितं व्याघ्र-आदिभिः सामान्य-अप्रयोगे कर्मधारयः (२.१.५६)।",
    anuvritti_from        = ('2.1.55',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
