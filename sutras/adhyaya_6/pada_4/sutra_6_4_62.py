"""
6.4.62  स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च  —  VIDHI

Padaccheda: स्य-सिच्-सीयुट्‍-तासिषु भाव-कर्म्मणोः उपदेशे अच्-हन-ग्रह-दृशाम् वा चिण्-वत् इट् च

स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च (6.4.62)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_62_syasicsIyu_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_62_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "syasicsIyuwtAsizu BAvakarmaRorupadeSe'jJanagrahadfSAM vA ciRvadiw ca",
    text_dev              = "स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च",
    padaccheda_dev        = "स्य-सिच्-सीयुट्‍-तासिषु भाव-कर्म्मणोः उपदेशे अच्-हन-ग्रह-दृशाम् वा चिण्-वत् इट् च",
    why_dev               = "(सूत्रम् 6.4.62) स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा चिण्वदिट् च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
