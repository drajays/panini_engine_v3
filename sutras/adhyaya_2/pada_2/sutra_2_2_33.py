"""
2.2.33  अजाद्यदन्तम्  —  VIDHI

Padaccheda: अजादि-अदन्तम्

Ajadi and adanta also in dvandva context.
Pāṭha: ashtadhyayi.com data.txt row i=22033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_33_ajadi_adanta"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("dvandva" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.2.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ajAdyadantam",
    text_dev              = "अजाद्यदन्तम्",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA ac-Adi-at-antam pUrvam dvandve",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा अच्-आदि-अत्-अन्तम् पूर्वम् द्वन्द्वे",
    padaccheda_dev        = "अजादि-अदन्तम्",
    why_dev               = "अजादि-अदन्तं च (२.२.३३)।",
    anuvritti_from        = ('2.2.32',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
