"""
2.2.38  कडाराः कर्मधारये  —  VIDHI

Padaccheda: कडाराः कर्मधारये

Kadara etc. in karmadharaya compound.
Pāṭha: ashtadhyayi.com data.txt row i=22038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_38_kadara_karmadharaya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.2.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kaqArAH karmaDAraye",
    text_dev              = "कडाराः कर्मधारये",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA kaqArAH karmaDAraye pUrvam vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा कडाराः कर्मधारये पूर्वम् वा",
    padaccheda_dev        = "कडाराः कर्मधारये",
    why_dev               = "कडाराः कर्मधारये (२.२.३८)।",
    anuvritti_from        = ('2.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
