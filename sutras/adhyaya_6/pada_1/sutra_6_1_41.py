"""
6.1.41  ल्यपि च  —  VIDHI

Padaccheda: ल्यपि च

ल्यपि च (6.1.41)
Pāṭha: ashtadhyayi.com data.txt row i=61041 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_41_lyapi_41"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.41", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lyapi ca",
    text_dev              = "ल्यपि च",
    samagra_slp1          = "lyapi ca samprasAraRam na veYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "ल्यपि च सम्प्रसारणम् न वेञः",
    padaccheda_dev        = "ल्यपि च",
    why_dev               = "(सूत्रम् 6.1.41) ल्यपि च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
