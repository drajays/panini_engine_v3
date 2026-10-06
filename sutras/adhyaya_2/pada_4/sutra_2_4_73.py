"""
2.4.73  बहुलं छन्दसि  —  VIDHI

Padaccheda: बहुलम् छन्दसि

Bahulam (varied) in chandas context.
Pāṭha: ashtadhyayi.com data.txt row i=24073 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_73_bahulam_chandas_73"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_73_chandas_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.73"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahulaM Candasi",
    text_dev              = "बहुलं छन्दसि",
    samagra_slp1          = "bahulam Candasi luk adi-praBftiByaH SapaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "बहुलम् छन्दसि लुक् अदि-प्रभृतिभ्यः शपः",
    padaccheda_dev        = "बहुलम् छन्दसि",
    why_dev               = "बहुलम् छन्दसि (२.४.७३)।",
    anuvritti_from        = ('2.4.72',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
