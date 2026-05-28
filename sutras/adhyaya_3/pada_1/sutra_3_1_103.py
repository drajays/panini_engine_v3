"""
3.1.103  अर्यः स्वामिवैश्ययोः  —  VIDHI

Padaccheda: अर्यः स्वामि-वैश्ययोः

Krt suffix rule from dhatu: अर्यः स्वामिवैश्ययोः (103)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_103_aryaH_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aryaH svAmivESyayoH",
    text_dev              = "अर्यः स्वामिवैश्ययोः",
    padaccheda_dev        = "अर्यः स्वामि-वैश्ययोः",
    why_dev               = "धातोः [अर्यः स्वामिवैश्ययोः]-प्रत्ययः विहितः (३.१.103)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
