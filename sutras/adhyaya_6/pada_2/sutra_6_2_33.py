"""
6.2.33  परिप्रत्युपापा वर्ज्यमानाहोरात्रावयवेषु  —  VIDHI

Padaccheda: परि-प्रति-उप-अपा वर्ज्यमान-अहोरात्र-अवयवेषु

परिप्रत्युपापा वर्ज्यमानाहोरात्रावयवेषु (6.2.33)
Pāṭha: ashtadhyayi.com data.txt row i=62033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_33_paripratyu_33"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.33", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paripratyupApA varjyamAnAhorAtrAvayavezu",
    text_dev              = "परिप्रत्युपापा वर्ज्यमानाहोरात्रावयवेषु",
    samagra_slp1          = "pari-prati-upa-apAH varjyamAna-ahaH-rAtrAvayavezu prakftyA pUrvapadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "परि-प्रति-उप-अपाः वर्ज्यमान-अहः-रात्रावयवेषु प्रकृत्या पूर्वपदम्",
    padaccheda_dev        = "परि-प्रति-उप-अपा वर्ज्यमान-अहोरात्र-अवयवेषु",
    why_dev               = "(सूत्रम् 6.2.33) परिप्रत्युपापा वर्ज्यमानाहोरात्रावयवेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
