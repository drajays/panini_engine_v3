"""
2.3.10  पञ्चम्यपाङ्परिभिः  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: पञ्चमी / अपाङ्परिभिः

Śāstra: the fifth vibhakti (ablative/pañcamī) is prescribed when used with
the indeclinables *apa*, *āṅ* (in the sense of a limit), or *pari* (around /
away from).

Engine: registers the apa/āṅ/pari→pañcamī gate. ``cond`` checks only the gate
flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_10_pancami_apa_ang_pari"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.10",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "paYcamyapANparibhiH",
    text_dev              = "पञ्चम्यपाङ्परिभिः",
    padaccheda_dev        = "पञ्चमी / अप-आङ्-परिभिः",
    why_dev               = (
        "अप-आङ्-पर्युपयोगे पञ्चमी-विभक्तिः — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1",),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
