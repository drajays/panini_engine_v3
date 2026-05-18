"""
1.4.107  अस्मद्युत्तमः  —  VIDHI

Padaccheda: अस्मदि ७/१ उत्तमः १/१

The word/form relating to asmad (first person) is called uttama
(first person marker).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "1_4_107_asmad_uttama"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("1_4_107_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["purusa_kind"]         = "1.4.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.4.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asmadyuttamaH",
    text_dev              = "अस्मद्युत्तमः",
    padaccheda_dev        = "अस्मदि ७/१ उत्तमः १/१",
    why_dev               = "अस्मच्छब्दे अर्थे उत्तम-पुरुष-संज्ञा (१.४.१०७)।",
    anuvritti_from        = ("1.4.105",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
