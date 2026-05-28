"""
3.1.124  ऋहलोर्ण्यत्  —  VIDHI

Padaccheda: ऋ-हलोः ण्यत्

Krt suffix rule from dhatu: ऋहलोर्ण्यत् (124)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_124_fhalorRyat_124"


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
    state.meta["krt_kind"] = "3.1.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fhalorRyat",
    text_dev              = "ऋहलोर्ण्यत्",
    padaccheda_dev        = "ऋ-हलोः ण्यत्",
    why_dev               = "धातोः [ऋहलोर्ण्यत्]-प्रत्ययः विहितः (३.१.124)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
