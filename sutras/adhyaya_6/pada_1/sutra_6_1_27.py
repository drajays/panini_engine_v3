"""
6.1.27  शृतं पाके  —  VIDHI

Padaccheda: शृतम् पाके

शृतं पाके (6.1.27)
Pāṭha: ashtadhyayi.com data.txt row i=61027 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_27_SftaM_27"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.27", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SftaM pAke",
    text_dev              = "शृतं पाके",
    samagra_slp1          = "Sftam pAke samprasAraRam nizWAyAm viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "शृतम् पाके सम्प्रसारणम् निष्ठायाम् विभाषा",
    padaccheda_dev        = "शृतम् पाके",
    why_dev               = "(सूत्रम् 6.1.27) शृतं पाके।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
