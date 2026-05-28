"""
3.1.80  धिन्विकृण्व्योर च  —  VIDHI

Padaccheda: धिन्वि-कृण्व्योः अ (लुप्तप्रथमान्तनिर्देशः) च

Krt suffix rule from dhatu: धिन्विकृण्व्योर च (80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_80_DinvikfRvyor_80"


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
    state.meta["krt_kind"] = "3.1.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "DinvikfRvyora ca",
    text_dev              = "धिन्विकृण्व्योर च",
    padaccheda_dev        = "धिन्वि-कृण्व्योः अ (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "धातोः [धिन्विकृण्व्योर च]-प्रत्ययः विहितः (३.१.80)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
