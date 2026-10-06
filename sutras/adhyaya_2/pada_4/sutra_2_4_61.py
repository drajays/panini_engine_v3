"""
2.4.61  न तौल्वलिभ्यः  —  VIDHI

Padaccheda: न तौल्वलिभ्यः

NOT from taulvali etc.
Pāṭha: ashtadhyayi.com data.txt row i=24061 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_61_na_taulvali"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_61_yuna_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.61",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na tOlvaliByaH",
    text_dev              = "न तौल्वलिभ्यः",
    samagra_slp1          = "na tOlvaliByaH yUni luk",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "न तौल्वलिभ्यः यूनि लुक्",
    padaccheda_dev        = "न तौल्वलिभ्यः",
    why_dev               = "न तौल्वलिभ्यः (२.४.६१)।",
    anuvritti_from        = ('2.4.58',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
