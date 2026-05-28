"""
3.1.127  आनाय्योऽनित्ये  —  VIDHI

Padaccheda: आनाय्यः अनित्ये

Krt suffix rule from dhatu: आनाय्योऽनित्ये (127)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_127_AnAyyonitye_127"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_127_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AnAyyo'nitye",
    text_dev              = "आनाय्योऽनित्ये",
    padaccheda_dev        = "आनाय्यः अनित्ये",
    why_dev               = "धातोः [आनाय्योऽनित्ये]-प्रत्ययः विहितः (३.१.127)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
