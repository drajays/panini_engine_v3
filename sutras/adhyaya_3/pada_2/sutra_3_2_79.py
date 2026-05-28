"""
3.2.79  कर्तर्युपमाने  —  VIDHI

Padaccheda: कर्तरि उपमाने

krt-suffix rule: कर्तर्युपमाने (79)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_79_kartaryupa_79"


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
    state.meta["krt_kind"] = "3.2.79"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.79",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kartaryupamAne",
    text_dev              = "कर्तर्युपमाने",
    padaccheda_dev        = "कर्तरि उपमाने",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्तर्युपमाने] विहितः (३.२.79)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
