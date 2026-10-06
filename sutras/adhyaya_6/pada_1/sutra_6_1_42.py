"""
6.1.42  ज्यश्च  —  VIDHI

Padaccheda: ज्यः च

ज्यश्च (6.1.42)
Pāṭha: ashtadhyayi.com data.txt row i=61042 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_42_jyaSca_42"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.42", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jyaSca",
    text_dev              = "ज्यश्च",
    samagra_slp1          = "jyaH ca samprasAraRam na lyapi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "ज्यः च सम्प्रसारणम् न ल्यपि",
    padaccheda_dev        = "ज्यः च",
    why_dev               = "(सूत्रम् 6.1.42) ज्यश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
