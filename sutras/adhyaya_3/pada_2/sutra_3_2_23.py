"""
3.2.23  न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु  —  VIDHI

Padaccheda: न शब्द-श्लोक-कलह-गाथा-वैर-चाटु-सूत्र-मन्त्र-पदेषु

krt-suffix rule: न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु (23)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_23_na_23"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_23_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na SabdaSlokakalahagATAvEracAwusUtramantrapadezu",
    text_dev              = "न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु",
    padaccheda_dev        = "न शब्द-श्लोक-कलह-गाथा-वैर-चाटु-सूत्र-मन्त्र-पदेषु",
    why_dev               = "धातोः कृत्-प्रत्ययः [न शब्दश्लोककलहगाथावैरचाटुसूत्रमन्त्रपदेषु] विहितः (३.२.23)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
