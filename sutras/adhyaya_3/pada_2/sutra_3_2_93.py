"""
3.2.93  कर्मणीनिर्विक्रियः  —  VIDHI

Padaccheda: कर्मणि इनि (लुप्तप्रथमान्तनिर्देशः) विक्रियः

krt-suffix rule: कर्मणीनिर्विक्रियः (93)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_93_karmaRInir_93"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.93"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRInirvikriyaH",
    text_dev              = "कर्मणीनिर्विक्रियः",
    padaccheda_dev        = "कर्मणि इनि (लुप्तप्रथमान्तनिर्देशः) विक्रियः",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्मणीनिर्विक्रियः] विहितः (३.२.93)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
