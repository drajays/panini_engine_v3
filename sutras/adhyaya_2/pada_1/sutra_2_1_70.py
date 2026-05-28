"""
2.1.70  कुमारः श्रमणाऽऽदिभिः  —  VIDHI

Padaccheda: कुमारः श्रमणा-आदिभिः

kumara with sramana etc. forms karmadharaya compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_70_kumara_sramana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kumAraH SramaRA''diBiH",
    text_dev              = "कुमारः श्रमणाऽऽदिभिः",
    padaccheda_dev        = "कुमारः श्रमणा-आदिभिः",
    why_dev               = "कुमारः श्रमण-आदिभिः सह कर्मधारयः (२.१.७०)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
