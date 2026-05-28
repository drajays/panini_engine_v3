"""
3.1.136  आतश्चोपसर्गे  —  VIDHI

Padaccheda: आतः च उपसर्गे

Krt suffix rule from dhatu: आतश्चोपसर्गे (136)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_136_AtaScopasarg_136"


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
    state.meta["krt_kind"] = "3.1.136"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.136",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtaScopasarge",
    text_dev              = "आतश्चोपसर्गे",
    padaccheda_dev        = "आतः च उपसर्गे",
    why_dev               = "धातोः [आतश्चोपसर्गे]-प्रत्ययः विहितः (३.१.136)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
