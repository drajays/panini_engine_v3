"""
4.3.72  द्व्यजृद्ब्राह्मणर्क्प्रथमाध्वरपुरश्चरणनामाख्याताट्ठक्  —  VIDHI

Padaccheda: द्वि-अच्-ऋत्-ब्राह्मण-ऋक्-प्रथम-अध्वर-पुरश्चरण-नाम-आख्यातात् ठक्

द्व्यजृद्ब्राह्मणर्क्प्रथमाध्वरपुरश्चरणनामाख्याताट्ठक् (4.3.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_72_dvyajfdbrA_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.72", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvyajfdbrAhmaRarkpraTamADvarapuraScaraRanAmAKyAtAwWak",
    text_dev              = "द्व्यजृद्ब्राह्मणर्क्प्रथमाध्वरपुरश्चरणनामाख्याताट्ठक्",
    padaccheda_dev        = "द्वि-अच्-ऋत्-ब्राह्मण-ऋक्-प्रथम-अध्वर-पुरश्चरण-नाम-आख्यातात् ठक्",
    why_dev               = "(सूत्रम् 4.3.72) द्व्यजृद्ब्राह्मणर्क्प्रथमाध्वरपुरश्चरणनामाख्याताट्ठक्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
