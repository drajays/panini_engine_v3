"""
3.2.104  जीर्यतेरतृन्  —  VIDHI

Padaccheda: जीर्यतेः अतृन्

krt-suffix rule: जीर्यतेरतृन् (104)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_104_jIryaterat_104"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_104_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jIryateratfn",
    text_dev              = "जीर्यतेरतृन्",
    padaccheda_dev        = "जीर्यतेः अतृन्",
    why_dev               = "धातोः कृत्-प्रत्ययः [जीर्यतेरतृन्] विहितः (३.२.104)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
