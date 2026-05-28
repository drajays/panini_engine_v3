"""
3.1.74  श्रुवः शृ च  —  VIDHI

Padaccheda: श्रुवः शृ (लुप्तप्रथमान्तनिर्देशः) च

Krt suffix rule from dhatu: श्रुवः शृ च (74)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_74_SruvaH_74"


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
    state.meta["krt_kind"] = "3.1.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SruvaH Sf ca",
    text_dev              = "श्रुवः शृ च",
    padaccheda_dev        = "श्रुवः शृ (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "धातोः [श्रुवः शृ च]-प्रत्ययः विहितः (३.१.74)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
