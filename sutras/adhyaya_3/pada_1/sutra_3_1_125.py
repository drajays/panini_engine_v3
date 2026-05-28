"""
3.1.125  ओरावश्यके  —  VIDHI

Padaccheda: ओः आवश्यके

Krt suffix rule from dhatu: ओरावश्यके (125)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_125_orAvaSyake_125"


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
    state.meta["krt_kind"] = "3.1.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "orAvaSyake",
    text_dev              = "ओरावश्यके",
    padaccheda_dev        = "ओः आवश्यके",
    why_dev               = "धातोः [ओरावश्यके]-प्रत्ययः विहितः (३.१.125)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
