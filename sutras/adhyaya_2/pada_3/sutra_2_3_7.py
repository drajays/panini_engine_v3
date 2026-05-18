"""
2.3.7  सप्तमीपञ्चम्यौ कारकमध्ये  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: सप्तमी / पञ्चमी / कारकमध्ये

Śāstra: the seventh (locative/saptamī) and fifth (ablative/pañcamī) vibhaktis
are used in the sense of *kārakamadhe* (intermediate/interval between kārakas
or actions).

Engine: registers the kārakamadhe→saptamī/pañcamī gate. ``cond`` checks only
the gate flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_7_saptami_pancami_karakamadhye"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.7",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "saptamI paYcamyO kArakamaXye",
    text_dev              = "सप्तमीपञ्चम्यौ कारकमध्ये",
    padaccheda_dev        = "सप्तमी / पञ्चम्यौ / कारकमध्ये",
    why_dev               = (
        "कारकमध्ये सप्तमी च पञ्चमी च — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1",),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
