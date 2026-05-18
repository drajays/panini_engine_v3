"""
1.2.70  पिता मात्रा  —  VIDHI (SAMJNA gate)

*Padaccheda:* **पिता** / **मात्रा**

pitṛ (father) survives as the ekasheṣa remainder when paired with mātṛ
(mother).  This is a specific exception to the general ekasheṣa rule of
1.2.64, prescribing that the masculine form (pitā) wins in the
father–mother pair — contra the general principle where either could
survive.

Anuvritti from 1.2.68 carries the ekasheṣa context of gender-distinct
kinship pairs.

Operational role (v3):
  - Registers the gate ``1_2_70_pitA_mAtrA`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when processing the pitṛ–mātṛ
    pair in ekasheṣa to select the pitṛ form.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_70_pitA_mAtrA"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.70",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "pitA mAtrA",
    text_dev                = "पिता मात्रा",
    padaccheda_dev          = "पिता / मात्रा",
    why_dev                 = (
        "पितृ-मातृ-युगले एकशेषे पिता एव शिष्यते — "
        "मातृशब्देन सह एकशेषे पितृशब्दस्य ग्रहणम् इति नियमः।"
    ),
    anuvritti_from          = ("1.2.68",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
