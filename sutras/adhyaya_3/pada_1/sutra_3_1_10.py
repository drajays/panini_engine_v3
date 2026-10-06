"""
3.1.10  उपमानादाचारे  —  VIDHI

Padaccheda: उपमानात् आचारे

Krt suffix rule from dhatu: उपमानादाचारे (10)
Pāṭha: ashtadhyayi.com data.txt row i=31010 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_10_upamAnAdAcAr_10"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.10", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upamAnAdAcAre",
    text_dev              = "उपमानादाचारे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca upamAnAt AcAre karmaRaH vA supaH kyac",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च उपमानात् आचारे कर्मणः वा सुपः क्यच्",
    padaccheda_dev        = "उपमानात् आचारे",
    why_dev               = "धातोः [उपमानादाचारे]-प्रत्ययः विहितः (३.१.10)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
