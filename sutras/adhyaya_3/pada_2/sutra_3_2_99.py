"""
3.2.99  उपसर्गे च संज्ञायाम्  —  VIDHI

Padaccheda: उपसर्गे च संज्ञायाम्

krt-suffix rule: उपसर्गे च संज्ञायाम् (99)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_99_upasarge_99"


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
    state.meta["krt_kind"] = "3.2.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasarge ca saMjYAyAm",
    text_dev              = "उपसर्गे च संज्ञायाम्",
    padaccheda_dev        = "उपसर्गे च संज्ञायाम्",
    why_dev               = "धातोः कृत्-प्रत्ययः [उपसर्गे च संज्ञायाम्] विहितः (३.२.99)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
