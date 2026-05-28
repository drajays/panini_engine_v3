"""
3.1.104  उपसर्या काल्या प्रजने  —  VIDHI

Padaccheda: उपसर्या काल्या प्रजने

Krt suffix rule from dhatu: उपसर्या काल्या प्रजने (104)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_104_upasaryA_104"


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
    state.meta["krt_kind"] = "3.1.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasaryA kAlyA prajane",
    text_dev              = "उपसर्या काल्या प्रजने",
    padaccheda_dev        = "उपसर्या काल्या प्रजने",
    why_dev               = "धातोः [उपसर्या काल्या प्रजने]-प्रत्ययः विहितः (३.१.104)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
