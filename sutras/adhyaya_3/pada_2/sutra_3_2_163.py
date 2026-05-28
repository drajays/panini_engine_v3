"""
3.2.163  इण्नश्जिसर्त्तिभ्यः क्वरप्  —  VIDHI

Padaccheda: इण्-नश्-जि-सर्त्तिभ्यः क्वरप्

krt-suffix rule: इण्नश्जिसर्त्तिभ्यः क्वरप् (163)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_163_iRnaSjisar_163"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_163_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.163"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.163",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iRnaSjisarttiByaH kvarap",
    text_dev              = "इण्नश्जिसर्त्तिभ्यः क्वरप्",
    padaccheda_dev        = "इण्-नश्-जि-सर्त्तिभ्यः क्वरप्",
    why_dev               = "धातोः कृत्-प्रत्ययः [इण्नश्जिसर्त्तिभ्यः क्वरप्] विहितः (३.२.163)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
