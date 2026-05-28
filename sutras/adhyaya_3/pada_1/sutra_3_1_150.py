"""
3.1.150  आशिषि च  —  VIDHI

Padaccheda: आशिषि च

Krt suffix rule from dhatu: आशिषि च (150)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_150_ASizi_150"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_150_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.150"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.150",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ASizi ca",
    text_dev              = "आशिषि च",
    padaccheda_dev        = "आशिषि च",
    why_dev               = "धातोः [आशिषि च]-प्रत्ययः विहितः (३.१.150)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
