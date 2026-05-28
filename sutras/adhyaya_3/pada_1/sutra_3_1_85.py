"""
3.1.85  व्यत्ययो बहुलम्  —  VIDHI

Padaccheda: व्यत्ययः बहुलम्

Krt suffix rule from dhatu: व्यत्ययो बहुलम् (85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_85_vyatyayo_85"


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
    state.meta["krt_kind"] = "3.1.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vyatyayo bahulam",
    text_dev              = "व्यत्ययो बहुलम्",
    padaccheda_dev        = "व्यत्ययः बहुलम्",
    why_dev               = "धातोः [व्यत्ययो बहुलम्]-प्रत्ययः विहितः (३.१.85)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
