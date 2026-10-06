"""
6.2.167  मुखं स्वाङ्गम्  —  VIDHI

Padaccheda: मुखम् स्वाङ्गम्

मुखं स्वाङ्गम् (6.2.167)
Pāṭha: ashtadhyayi.com data.txt row i=62167 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_167_muKaM_167"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.167", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.167"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.167",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "muKaM svANgam",
    text_dev              = "मुखं स्वाङ्गम्",
    samagra_slp1          = "uttarapadAdiH antaH muKam svANgam bahuvrIhO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः मुखम् स्वाङ्गम् बहुव्रीहौ",
    padaccheda_dev        = "मुखम् स्वाङ्गम्",
    why_dev               = "(सूत्रम् 6.2.167) मुखं स्वाङ्गम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
