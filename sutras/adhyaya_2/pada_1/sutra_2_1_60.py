"""
2.1.60  क्तेन नञ्विशिष्टेनानञ्  —  VIDHI

Padaccheda: क्तेन नञ्-विशिष्टेन अनञ्

kta with nan-visista (negated) form ananna karmadharaya.
Pāṭha: ashtadhyayi.com data.txt row i=21060 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_60_ktena_nana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ktena naYviSizwenAnaY",
    text_dev              = "क्तेन नञ्विशिष्टेनानञ्",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH ktena naY-viSizwena anaY samAnADikaraRena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः क्तेन नञ्-विशिष्टेन अनञ् समानाधिकरणेन",
    padaccheda_dev        = "क्तेन नञ्-विशिष्टेन अनञ्",
    why_dev               = "क्तेन नञ्-विशिष्टेन अनञ् कर्मधारयः (२.1.६०)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
