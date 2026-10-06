"""
6.3.5  आज्ञायिनि च  —  VIDHI

Padaccheda: आज्ञायिनि च

आज्ञायिनि च (6.3.5)
Pāṭha: ashtadhyayi.com data.txt row i=63005 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_5_AjYAyini_5"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.5", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AjYAyini ca",
    text_dev              = "आज्ञायिनि च",
    samagra_slp1          = "alug uttarapade AjYAyini ca tftIyAyAH manasaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अलुग् उत्तरपदे आज्ञायिनि च तृतीयायाः मनसः",
    padaccheda_dev        = "आज्ञायिनि च",
    why_dev               = "(सूत्रम् 6.3.5) आज्ञायिनि च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
