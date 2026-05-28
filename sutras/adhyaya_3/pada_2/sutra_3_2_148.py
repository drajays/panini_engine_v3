"""
3.2.148  चलनशब्दार्थादकर्मकाद्युच्  —  VIDHI

Padaccheda: चलन-शब्द-अर्थात् अकर्मकात् युच्

krt-suffix rule: चलनशब्दार्थादकर्मकाद्युच् (148)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_148_calanaSabd_148"


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
    state.meta["krt_kind"] = "3.2.148"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.148",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "calanaSabdArTAdakarmakAdyuc",
    text_dev              = "चलनशब्दार्थादकर्मकाद्युच्",
    padaccheda_dev        = "चलन-शब्द-अर्थात् अकर्मकात् युच्",
    why_dev               = "धातोः कृत्-प्रत्ययः [चलनशब्दार्थादकर्मकाद्युच्] विहितः (३.२.148)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
