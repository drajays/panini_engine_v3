"""
6.2.188  अधेरुपरिस्थम्  —  VIDHI

Padaccheda: अधेः उपरिस्थम्

अधेरुपरिस्थम् (6.2.188)
Pāṭha: ashtadhyayi.com data.txt row i=62188 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_188_aDeruparis_188"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.188", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.188"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.188",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDeruparisTam",
    text_dev              = "अधेरुपरिस्थम्",
    samagra_slp1          = "uttarapadAdiH antaH aDeH uparisTam upasargAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः अधेः उपरिस्थम् उपसर्गात्",
    padaccheda_dev        = "अधेः उपरिस्थम्",
    why_dev               = "(सूत्रम् 6.2.188) अधेरुपरिस्थम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
