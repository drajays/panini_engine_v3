"""
3.1.46  श्लिष आलिङ्गने  —  VIDHI

Padaccheda: श्लिषः आलिङ्गने

Krt suffix rule from dhatu: श्लिष आलिङ्गने (46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_46_Sliza_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_46_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Sliza AliNgane",
    text_dev              = "श्लिष आलिङ्गने",
    padaccheda_dev        = "श्लिषः आलिङ्गने",
    why_dev               = "धातोः [श्लिष आलिङ्गने]-प्रत्ययः विहितः (३.१.46)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
