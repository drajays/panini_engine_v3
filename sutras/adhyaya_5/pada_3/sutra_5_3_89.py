"""
5.3.89  कुत्वा डुपच्  —  VIDHI

Padaccheda: कुत्वा डुपच्

कुत्वा डुपच् (5.3.89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_89_kutvA_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_89_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kutvA qupac",
    text_dev              = "कुत्वा डुपच्",
    padaccheda_dev        = "कुत्वा डुपच्",
    why_dev               = "(सूत्रम् 5.3.89) कुत्वा डुपच्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
