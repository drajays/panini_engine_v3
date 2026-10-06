"""
3.1.9  काम्यच्च  —  VIDHI

Padaccheda: काम्यच् च

Krt suffix rule from dhatu: काम्यच्च (9)
Pāṭha: ashtadhyayi.com data.txt row i=31009 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_9_kAmyacca_9"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.9", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAmyacca",
    text_dev              = "काम्यच्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kAmyac ca karmaRaH icCAyAM vA supaH AtmanaH kyac",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च काम्यच् च कर्मणः इच्छायां वा सुपः आत्मनः क्यच्",
    padaccheda_dev        = "काम्यच् च",
    why_dev               = "धातोः [काम्यच्च]-प्रत्ययः विहितः (३.१.9)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
