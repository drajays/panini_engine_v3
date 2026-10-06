"""
6.1.190  अनुदात्ते च  —  VIDHI

Padaccheda: अनुदात्ते च

अनुदात्ते च (6.1.190)
Pāṭha: ashtadhyayi.com data.txt row i=61190 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_190_anudAtte_190"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.190", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.190"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.190",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anudAtte ca",
    text_dev              = "अनुदात्ते च",
    samagra_slp1          = "anudAtte ca udAttaH la-sArvaDAtukam AdiH aByastAnAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अनुदात्ते च उदात्तः ल-सार्वधातुकम् आदिः अभ्यस्तानाम्",
    padaccheda_dev        = "अनुदात्ते च",
    why_dev               = "(सूत्रम् 6.1.190) अनुदात्ते च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
