"""
3.1.66  चिण् भावकर्मणोः  —  VIDHI

Padaccheda: चिण् भाव-कर्मणोः

ciṇ suffix in bhāva/karmani context. Structurally: all karmani pipelines
tag the dhātu with "bhava_karma_usage" before calling this sūtra.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_66_ciR_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: karmani/bhāva pipeline tags dhātu "bhava_karma_usage"
    if any("bhava_karma_usage" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("ciN_recipe"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ciR BAvakarmaRoH",
    text_dev              = "चिण् भावकर्मणोः",
    padaccheda_dev        = "चिण् भाव-कर्मणोः",
    why_dev               = "धातोः [चिण् भावकर्मणोः]-प्रत्ययः विहितः (३.१.66)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
