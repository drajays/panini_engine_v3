"""
6.3.116  नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ  —  VIDHI

Padaccheda: नहि-वृति-वृषि-व्यधि-रुचि-सहि-तनिषु क्वौ

नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ (6.3.116)
Pāṭha: ashtadhyayi.com data.txt row i=63116 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_116_nahivftivf_116"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.116", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nahivftivfzivyaDirucisahitanizu kvO",
    text_dev              = "नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ",
    samagra_slp1          = "uttarapade saMhitAyAm nahi-vfti-vfzi-vyaDi-ruci-sahi-tanizu kvO dIrGaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे संहितायाम् नहि-वृति-वृषि-व्यधि-रुचि-सहि-तनिषु क्वौ दीर्घः",
    padaccheda_dev        = "नहि-वृति-वृषि-व्यधि-रुचि-सहि-तनिषु क्वौ",
    why_dev               = "(सूत्रम् 6.3.116) नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
