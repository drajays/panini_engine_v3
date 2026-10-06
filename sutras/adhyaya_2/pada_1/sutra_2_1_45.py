"""
2.1.45  क्तेनाहोरात्रावयवाः  —  VIDHI

Padaccheda: क्तेन अहो-रात्र-अवयवाः

kta with ahoraatra-avayava (day-parts) forms tatpurusha compound.
Pāṭha: ashtadhyayi.com data.txt row i=21045 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_45_ktena_ahoratri"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ktenAhorAtrAvayavAH",
    text_dev              = "क्तेनाहोरात्रावयवाः",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH ktena ahorAtra-avayavAH saptamI",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः क्तेन अहोरात्र-अवयवाः सप्तमी",
    padaccheda_dev        = "क्तेन अहो-रात्र-अवयवाः",
    why_dev               = "क्तेन अहोरात्र-अवयव-वाचिनां सह तत्पुरुषः (२.१.४५)।",
    anuvritti_from        = ('2.1.22',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
