"""
3.1.5  गुप्तिज्किद्भ्यः सन्  —  VIDHI

Padaccheda: गुप्-तिज्-किद्‍भ्यः सन्

Krt suffix rule from dhatu: गुप्तिज्किद्भ्यः सन् (5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_5_guptijkidBya_5"


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
    state.meta["krt_kind"] = "3.1.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "guptijkidByaH san",
    text_dev              = "गुप्तिज्किद्भ्यः सन्",
    padaccheda_dev        = "गुप्-तिज्-किद्‍भ्यः सन्",
    why_dev               = "धातोः [गुप्तिज्किद्भ्यः सन्]-प्रत्ययः विहितः (३.१.5)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
