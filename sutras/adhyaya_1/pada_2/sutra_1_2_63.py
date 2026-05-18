"""
1.2.63  तिष्यपुनर्वस्वोर्नक्षत्रद्वन्द्वे बहुवचनस्य द्विवचनं नित्यम्  —  VIDHI (SAMJNA gate)

*Padaccheda:* **तिष्यपुनर्वस्वोः** / **नक्षत्रद्वन्द्वे** / **बहुवचनस्य** / **द्विवचनम्** / **नित्यम्**

For the nakṣatra-dvandva compounds of "tiṣya" and "punarvasu", the dual
(dvivacana) is always used instead of the plural (bahuvacana).  This is a
Vedic grammatical rule (nityam — always) for these specific nakṣatra names.

Operational role (v3):
  - Registers the gate ``1_2_63_tizya_punarvasu_dvivacana`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when replacing bahuvacana with
    dvivacana for the nakṣatra names tiṣya and punarvasu.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_63_tizya_punarvasu_dvivacana"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.63",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "tizya-punarvasvornakzatra-dvandve bahuvacanasya dvivacanam nityam",
    text_dev                = "तिष्यपुनर्वस्वोर्नक्षत्रद्वन्द्वे बहुवचनस्य द्विवचनं नित्यम्",
    padaccheda_dev          = "तिष्यपुनर्वस्वोः / नक्षत्रद्वन्द्वे / बहुवचनस्य / द्विवचनम् / नित्यम्",
    why_dev                 = (
        "तिष्य-पुनर्वसु-नक्षत्रयोः द्वन्द्वे बहुवचनस्य स्थाने द्विवचनं नित्यं भवति — "
        "पुनर्वसू इत्येव, न पुनर्वसवः इति।"
    ),
    anuvritti_from          = ("1.2.60",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
