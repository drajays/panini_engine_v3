"""
6.2.168  नाव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः  —  VIDHI

Padaccheda: न अव्यय-दिक्शब्द-गो-महत्-स्थूल-मुष्टि-पृथु-वत्सेभ्यः

नाव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः (6.2.168)
Pāṭha: ashtadhyayi.com data.txt row i=62168 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_168_nAvyayadik_168"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.168", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.168"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.168",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "nAvyayadikSabdagomahatsTUlamuzwipfTuvatseByaH",
    text_dev              = "नाव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः",
    samagra_slp1          = "uttarapadAdiH antaH na avyaya-dikSabda-go-mahat-sTUla-muzwi-pfTu-vatseByaH bahuvrIhO muKam svANgam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः न अव्यय-दिक्शब्द-गो-महत्-स्थूल-मुष्टि-पृथु-वत्सेभ्यः बहुव्रीहौ मुखम् स्वाङ्गम्",
    padaccheda_dev        = "न अव्यय-दिक्शब्द-गो-महत्-स्थूल-मुष्टि-पृथु-वत्सेभ्यः",
    why_dev               = "(सूत्रम् 6.2.168) नाव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
