"""
2.4.41  वेञो वयिः  —  VIDHI

Padaccheda: वेञः वयिः

vij root is replaced by vayi.
Pāṭha: ashtadhyayi.com data.txt row i=24041 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_41_vena_vayi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.41", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.41"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.41",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "veYo vayiH",
    text_dev              = "वेञो वयिः",
    samagra_slp1          = "ArDaDAtuke veYaH vayiH liwi anyatarasyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आर्धधातुके वेञः वयिः लिटि अन्यतरस्याम्",
    padaccheda_dev        = "वेञः वयिः",
    why_dev               = "वेञः वयिः (२.४.४१)।",
    anuvritti_from        = ('2.4.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
