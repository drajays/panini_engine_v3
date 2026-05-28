"""
3.1.83  हलः श्नः शानज्झौ  —  VIDHI

Padaccheda: हलः श्नः शानच् हौ

Krt suffix rule from dhatu: हलः श्नः शानज्झौ (83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_83_halaH_83"


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
    state.meta["krt_kind"] = "3.1.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "halaH SnaH SAnajJO",
    text_dev              = "हलः श्नः शानज्झौ",
    padaccheda_dev        = "हलः श्नः शानच् हौ",
    why_dev               = "धातोः [हलः श्नः शानज्झौ]-प्रत्ययः विहितः (३.१.83)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
