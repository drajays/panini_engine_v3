"""
6.2.146  संज्ञायामनाचितादीनाम्  —  VIDHI

Padaccheda: संज्ञायाम् अनाचित-आदीनाम्

संज्ञायामनाचितादीनाम् (6.2.146)
Pāṭha: ashtadhyayi.com data.txt row i=62146 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_146_saMjYAyAma_146"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.146", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.146"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.146",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAmanAcitAdInAm",
    text_dev              = "संज्ञायामनाचितादीनाम्",
    samagra_slp1          = "uttarapadAdiH antaH saMjYAyAm anAcitAdInAm ktaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः संज्ञायाम् अनाचितादीनाम् क्तः",
    padaccheda_dev        = "संज्ञायाम् अनाचित-आदीनाम्",
    why_dev               = "(सूत्रम् 6.2.146) संज्ञायामनाचितादीनाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
