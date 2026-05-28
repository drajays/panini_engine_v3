"""
2.3.29  अन्यारादितरर्त्तेदिक्शब्दाञ्चूत्तरपदाजाहियुक्ते  —  VIDHI

Padaccheda: अन्य-आरात्-इतर-ऋते-दिक्शब्द-अञ्चु-उत्तरपद-आच्-आहियुक्ते

anya, arat, itara, rte, dik-words, ancu, ac, ahi take pancami.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_29_anya_arat_dik"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_29_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anyArAditararttedikSabdAYcUttarapadAjAhiyukte",
    text_dev              = "अन्यारादितरर्त्तेदिक्शब्दाञ्चूत्तरपदाजाहियुक्ते",
    padaccheda_dev        = "अन्य-आरात्-इतर-ऋते-दिक्शब्द-अञ्चु-उत्तरपद-आच्-आहियुक्ते",
    why_dev               = "अन्य-आरात्-इतर-ऋते-दिक्-अञ्चु-आच्-आहियुक्ते पञ्चमी (२.३.२९)।",
    anuvritti_from        = ('2.3.28',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
