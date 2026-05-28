"""
3.2.121  नन्वोर्विभाषा  —  VIDHI

Padaccheda: नन्वोः विभाषा

krt-suffix rule: नन्वोर्विभाषा (121)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_121_nanvorviBA_121"


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
    state.meta["krt_kind"] = "3.2.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nanvorviBAzA",
    text_dev              = "नन्वोर्विभाषा",
    padaccheda_dev        = "नन्वोः विभाषा",
    why_dev               = "धातोः कृत्-प्रत्ययः [नन्वोर्विभाषा] विहितः (३.२.121)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
