"""
1.2.44  एकविभक्ति चापूर्वनिपाते  —  PARIBHASHA

*Padaccheda:* **एकविभक्ति** / **च** / **अपूर्वनिपाते**

A word that occurs in a single case-ending (*ekavibhakti*) and is NOT used
as the prior member (*pūrva-nipāta*) of a compound [is to be treated as an
*avyaya*].  This paribhāṣā extends the avyaya saṃjñā to words that are
fixed to one case-form and are not first-members of samāsas.

Operational role (v3):
  - Registers the interpretive gate ``1_2_44_ekavibhakti_apUrvanipAte`` in
    both ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream recipes consult this gate before applying single-vibhakti
    / non-pūrvanipāta avyaya treatment.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_44_ekavibhakti_apUrvanipAte"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.44",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "ekaviBakti cApUrvanipAte",
    text_dev                = "एकविभक्ति चापूर्वनिपाते",
    padaccheda_dev          = "एकविभक्ति / च / अपूर्वनिपाते",
    why_dev                 = (
        "एकविभक्त्यन्तं अपूर्वनिपातञ्च शब्दं अव्ययसंज्ञकं विदधाति "
        "— यत् एकस्यां विभक्तौ एव प्रयुज्यते न तु समासे पूर्वपदम्।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
