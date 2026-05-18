"""
2.1.31  पूर्वसदृशसमोनार्थकलहनिपुणमिश्रश्लक्ष्णैः  —  VIDHI

Padaccheda: पूर्व-सदृश-सम-ऊनार्थ-कलह-निपुण-मिश्र-श्लक्ष्णैः

purva, sadrsa, sama etc. with tritiya form karmadharaya compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_31_purva_sadrsa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrvasadfSasamonArTakalahanipuRamiSraSlakzREH",
    text_dev              = "पूर्वसदृशसमोनार्थकलहनिपुणमिश्रश्लक्ष्णैः",
    padaccheda_dev        = "पूर्व-सदृश-सम-ऊनार्थ-कलह-निपुण-मिश्र-श्लक्ष्णैः",
    why_dev               = "पूर्व-सदृश-आदिभिः तृतीयान्तस्य सह कर्मधारयः (२.१.३१)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
