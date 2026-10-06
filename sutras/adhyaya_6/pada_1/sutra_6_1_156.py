"""
6.1.156  कारस्करो वृक्षः  —  VIDHI

Padaccheda: कारस्करः वृक्षः

कारस्करो वृक्षः (6.1.156)
Pāṭha: ashtadhyayi.com data.txt row i=61156 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_156_kAraskaro_156"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.156", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.156"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.156",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAraskaro vfkzaH",
    text_dev              = "कारस्करो वृक्षः",
    samagra_slp1          = "saMhitAyAm suwkAtpUrvaH kAraskaraH vfkzaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् सुट्कात्पूर्वः कारस्करः वृक्षः",
    padaccheda_dev        = "कारस्करः वृक्षः",
    why_dev               = "(सूत्रम् 6.1.156) कारस्करो वृक्षः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
