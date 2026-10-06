"""
6.1.121  अवपथासि च  —  VIDHI

Padaccheda: अवपथासि च

अवपथासि च (6.1.121)
Pāṭha: ashtadhyayi.com data.txt row i=61121 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_121_avapaTAsi_121"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.121", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avapaTAsi ca",
    text_dev              = "अवपथासि च",
    samagra_slp1          = "saMhitAyAm avapaTAsi ca aci prakftyA yajuzi anudAtte",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् अवपथासि च अचि प्रकृत्या यजुषि अनुदात्ते",
    padaccheda_dev        = "अवपथासि च",
    why_dev               = "(सूत्रम् 6.1.121) अवपथासि च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
