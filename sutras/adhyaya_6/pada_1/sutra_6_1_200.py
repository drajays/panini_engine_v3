"""
6.1.200  अन्तश्च तवै युगपत्  —  VIDHI

Padaccheda: अन्तः च तवै (लुप्तप्रथमान्तनिर्देशः) युगपत्

अन्तश्च तवै युगपत् (6.1.200)
Pāṭha: ashtadhyayi.com data.txt row i=61200 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_200_antaSca_200"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.200", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.200"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.200",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "antaSca tavE yugapat",
    text_dev              = "अन्तश्च तवै युगपत्",
    samagra_slp1          = "antaH ca tavE yugapat udAttaH AdiH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अन्तः च तवै युगपत् उदात्तः आदिः",
    padaccheda_dev        = "अन्तः च तवै (लुप्तप्रथमान्तनिर्देशः) युगपत्",
    why_dev               = "(सूत्रम् 6.1.200) अन्तश्च तवै युगपत्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
