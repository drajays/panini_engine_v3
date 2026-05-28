"""
2.3.69  न लोकाव्ययनिष्ठाखलर्थतृनाम्  —  VIDHI

Padaccheda: न ल-उ-उक-अव्यय-निष्ठा-खल्-अर्थतृनाम्

NOT for luk, avyaya, nistha, khal, artha-trn.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_69_na_lok_avyaya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na lokAvyayanizWAKalarTatfnAm",
    text_dev              = "न लोकाव्ययनिष्ठाखलर्थतृनाम्",
    padaccheda_dev        = "न ल-उ-उक-अव्यय-निष्ठा-खल्-अर्थतृनाम्",
    why_dev               = "न लक-अव्यय-निष्ठा-खल्-अर्थतृनाम् (२.३.६९)।",
    anuvritti_from        = ('2.3.65',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
