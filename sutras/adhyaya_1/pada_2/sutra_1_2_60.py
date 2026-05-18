"""
1.2.60  फल्गुनीप्रोष्ठपदानां च नक्षत्रे  —  VIDHI (SAMJNA gate)

*Padaccheda:* **फल्गुनी-प्रोष्ठपदानाम्** / **च** / **नक्षत्रे**

For the nakṣatra (asterism) names "phalgunī" and "proṣṭhapada" — when
used in the sense of the nakṣatra pair — they receive plural/ekaśeṣa
treatment.  This is a Vedic and astronomical rule extending the
bahuvacanam principle of 1.2.58 to these specific star-pair names.

Operational role (v3):
  - Registers the gate ``1_2_60_palgUni_proSTapada`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when processing the nakṣatra names
    phalgunī and proṣṭhapada for plural/ekaśeṣa agreement.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_60_palgUni_proSTapada"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.60",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "PalgUnI-proWTapadAnAM ca nakzatre",
    text_dev                = "फल्गुनीप्रोष्ठपदानां च नक्षत्रे",
    padaccheda_dev          = "फल्गुनी-प्रोष्ठपदानाम् / च / नक्षत्रे",
    why_dev                 = (
        "फल्गुनी-प्रोष्ठपदयोः नक्षत्रनाम्नोः युगलविवक्षायां बहुवचनम् एकशेषश्च — "
        "नक्षत्रयुगलस्य एकशेष-विषये एतयोः विशेषविधिः।"
    ),
    anuvritti_from          = ("1.2.58",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
