"""
6.2.169  निष्ठोपमानादन्यतरस्याम्  —  VIDHI

Padaccheda: निष्ठा-उपमानात् अन्यतरस्याम्

निष्ठोपमानादन्यतरस्याम् (6.2.169)
Pāṭha: ashtadhyayi.com data.txt row i=62169 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_169_nizWopamAn_169"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.169", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.169"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.169",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nizWopamAnAdanyatarasyAm",
    text_dev              = "निष्ठोपमानादन्यतरस्याम्",
    samagra_slp1          = "uttarapadAdiH antaH nizWopamAnAt anyatarasyAm bahuvrIhO muKam svANgam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः निष्ठोपमानात् अन्यतरस्याम् बहुव्रीहौ मुखम् स्वाङ्गम्",
    padaccheda_dev        = "निष्ठा-उपमानात् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.2.169) निष्ठोपमानादन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
