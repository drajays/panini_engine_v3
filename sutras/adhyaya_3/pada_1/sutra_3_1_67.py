"""
3.1.67  सार्वधातुके यक्  —  VIDHI

Padaccheda: सार्वधातुके यक्

yak vikaraṇa in sārvadhātuka (karmani/bhāva) context. Structurally:
all karmani pipelines tag the dhātu with "bhava_karma_usage" before this.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_67_sArvaDAtuke_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: karmani/bhāva pipeline tags dhātu "bhava_karma_usage"
    if any("bhava_karma_usage" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_1_67_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sArvaDAtuke yak",
    text_dev              = "सार्वधातुके यक्",
    padaccheda_dev        = "सार्वधातुके यक्",
    why_dev               = "धातोः [सार्वधातुके यक्]-प्रत्ययः विहितः (३.१.67)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
