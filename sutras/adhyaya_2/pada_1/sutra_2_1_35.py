"""
2.1.35  भक्ष्येण मिश्रीकरणम्  —  VIDHI

Padaccheda: भक्ष्येण मिश्री-करणम्

Food-mixing context (bhaksya + misrikarana) forms tatpurusha.
Pāṭha: ashtadhyayi.com data.txt row i=21035 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_35_bhaksya_misra"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BakzyeRa miSrIkaraRam",
    text_dev              = "भक्ष्येण मिश्रीकरणम्",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH BakzyeRa miSrIkaraRam tftIyA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः भक्ष्येण मिश्रीकरणम् तृतीया",
    padaccheda_dev        = "भक्ष्येण मिश्री-करणम्",
    why_dev               = "भक्ष्येण मिश्रीकरण-वाचिना सह तत्पुरुषः (२.१.३५)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
