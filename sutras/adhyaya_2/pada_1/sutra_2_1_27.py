"""
2.1.27  सामि  —  VIDHI

Padaccheda: सामि

sami (proximity) with subanta forms avyayibhava compound.
Pāṭha: ashtadhyayi.com data.txt row i=21027 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_27_sami"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("avyayibhava" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]             = "2.1.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sAmi",
    text_dev              = "सामि",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA tatpuruzaH sAmi dvitIyA ktena",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा तत्पुरुषः सामि द्वितीया क्तेन",
    padaccheda_dev        = "सामि",
    why_dev               = "सामि-वाचिना सुबन्तेन सह अव्ययीभावः (२.१.२७)।",
    anuvritti_from        = ('2.1.5',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
