"""
3.4.35  शुष्कचूर्णरूक्षेषु पिषः  —  VIDHI

Padaccheda: शुष्क-चूर्ण-रूक्षेषु पिषः

krt-suffix rule: शुष्कचूर्णरूक्षेषु पिषः
Pāṭha: ashtadhyayi.com data.txt row i=34035 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_35_SuzkacUrRa_35"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.35", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SuzkacUrRarUkzezu pizaH",
    text_dev              = "शुष्कचूर्णरूक्षेषु पिषः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Suzka-cUrRa-rUkzezu pizaH kft Ramul karmaRi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः शुष्क-चूर्ण-रूक्षेषु पिषः कृत् णमुल् कर्मणि",
    padaccheda_dev        = "शुष्क-चूर्ण-रूक्षेषु पिषः",
    why_dev               = "धातोः प्रत्ययः (३.4.35)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
