"""
3.1.51  नोनयतिध्वनयत्येलयत्यर्दयतिभ्यः  —  VIDHI

Padaccheda: न ऊनयति-ध्वनयति-एलयति-अर्दयतिभ्यः

Krt suffix rule from dhatu: नोनयतिध्वनयत्येलयत्यर्दयतिभ्यः (51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_51_nonayatiDvan_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_51_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nonayatiDvanayatyelayatyardayatiByaH",
    text_dev              = "नोनयतिध्वनयत्येलयत्यर्दयतिभ्यः",
    padaccheda_dev        = "न ऊनयति-ध्वनयति-एलयति-अर्दयतिभ्यः",
    why_dev               = "धातोः [नोनयतिध्वनयत्येलयत्यर्दयतिभ्यः]-प्रत्ययः विहितः (३.१.51)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
