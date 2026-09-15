"""
3.1.28  गुपूधूपविच्छिपणिपनिभ्य आयः  —  VIDHI

Padaccheda: गुपू-धूप-विच्छि-पणि-पनिभ्यः आयः

Krt suffix rule from dhatu: गुपूधूपविच्छिपणिपनिभ्य आयः (28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_28_gupUDUpavicC_28"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.28", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gupUDUpavicCipaRipaniBya AyaH",
    text_dev              = "गुपूधूपविच्छिपणिपनिभ्य आयः",
    padaccheda_dev        = "गुपू-धूप-विच्छि-पणि-पनिभ्यः आयः",
    why_dev               = "धातोः [गुपूधूपविच्छिपणिपनिभ्य आयः]-प्रत्ययः विहितः (३.१.28)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
