"""
2.3.18  कर्तृकरणयोस्तृतीया  —  VIDHI

Padaccheda: कर्त्तृ-करणयोः तृतीया

Tritiya marks kartri and karana roles.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_18_kartru_tritiya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kartfkaraRayostftIyA",
    text_dev              = "कर्तृकरणयोस्तृतीया",
    padaccheda_dev        = "कर्त्तृ-करणयोः तृतीया",
    why_dev               = "कर्तृ-करणयोः तृतीया (२.३.१८)।",
    anuvritti_from        = ('2.3.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
