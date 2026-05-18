"""
3.1.117  विपूयविनीयजित्या मुञ्जकल्कहलिषु  —  VIDHI

Padaccheda: विपूय-विनीय-जित्या मुञ्ज-कल्क-हलिषु

Krt suffix rule from dhatu: विपूयविनीयजित्या मुञ्जकल्कहलिषु (117)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_117_vipUyavinIya_117"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_117_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.117"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vipUyavinIyajityA muYjakalkahalizu",
    text_dev              = "विपूयविनीयजित्या मुञ्जकल्कहलिषु",
    padaccheda_dev        = "विपूय-विनीय-जित्या मुञ्ज-कल्क-हलिषु",
    why_dev               = "धातोः [विपूयविनीयजित्या मुञ्जकल्कहलिषु]-प्रत्ययः विहितः (३.१.117)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
