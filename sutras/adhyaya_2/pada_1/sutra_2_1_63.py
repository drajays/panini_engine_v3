"""
2.1.63  कतरकतमौ जातिपरिप्रश्ने  —  VIDHI

Padaccheda: कतर-कतमौ जाति-परिप्रश्ने

katara, katama in jati-question context form karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_63_katara_jati"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_63_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "katarakatamO jAtiparipraSne",
    text_dev              = "कतरकतमौ जातिपरिप्रश्ने",
    padaccheda_dev        = "कतर-कतमौ जाति-परिप्रश्ने",
    why_dev               = "कतर-कतमौ जाति-परिप्रश्ने कर्मधारये (२.१.६३)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
