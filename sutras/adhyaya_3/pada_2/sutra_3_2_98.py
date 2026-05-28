"""
3.2.98  पञ्चम्यामजातौ  —  VIDHI

Padaccheda: पञ्चम्याम् अ-जातौ

krt-suffix rule: पञ्चम्यामजातौ (98)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_98_paYcamyAma_98"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_98_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paYcamyAmajAtO",
    text_dev              = "पञ्चम्यामजातौ",
    padaccheda_dev        = "पञ्चम्याम् अ-जातौ",
    why_dev               = "धातोः कृत्-प्रत्ययः [पञ्चम्यामजातौ] विहितः (३.२.98)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
