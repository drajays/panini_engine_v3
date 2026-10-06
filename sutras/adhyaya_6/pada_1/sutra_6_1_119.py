"""
6.1.119  अङ्ग इत्यादौ च  —  VIDHI

Padaccheda: अङ्गे इत्यादौ च

अङ्ग इत्यादौ च (6.1.119)
Pāṭha: ashtadhyayi.com data.txt row i=61119 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_119_aNga_119"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.119", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.119"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aNga ityAdO ca",
    text_dev              = "अङ्ग इत्यादौ च",
    samagra_slp1          = "saMhitAyAm aNge ityAdO ca aci prakftyA yajuzi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् अङ्गे इत्यादौ च अचि प्रकृत्या यजुषि",
    padaccheda_dev        = "अङ्गे इत्यादौ च",
    why_dev               = "(सूत्रम् 6.1.119) अङ्ग इत्यादौ च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
