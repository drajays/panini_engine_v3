"""
3.1.142  दुन्योरनुपसर्गे  —  VIDHI

Padaccheda: दु-न्योः अन्-उपसर्गे

Krt suffix rule from dhatu: दुन्योरनुपसर्गे (142)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_142_dunyoranupas_142"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_142_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.142"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.142",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dunyoranupasarge",
    text_dev              = "दुन्योरनुपसर्गे",
    padaccheda_dev        = "दु-न्योः अन्-उपसर्गे",
    why_dev               = "धातोः [दुन्योरनुपसर्गे]-प्रत्ययः विहितः (३.१.142)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
