"""
6.2.129  कूलसूदस्थलकर्षाः संज्ञायाम्  —  VIDHI

Padaccheda: कूल-सूद-स्थल-कर्षाः संज्ञायाम्

कूलसूदस्थलकर्षाः संज्ञायाम् (6.2.129)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_129_kUlasUdasT_129"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.129"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.129",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kUlasUdasTalakarzAH saMjYAyAm",
    text_dev              = "कूलसूदस्थलकर्षाः संज्ञायाम्",
    padaccheda_dev        = "कूल-सूद-स्थल-कर्षाः संज्ञायाम्",
    why_dev               = "(सूत्रम् 6.2.129) कूलसूदस्थलकर्षाः संज्ञायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
