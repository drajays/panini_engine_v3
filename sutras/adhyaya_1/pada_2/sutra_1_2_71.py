"""
1.2.71  श्वशुरः श्वश्र्वा  —  VIDHI (SAMJNA gate)

*Padaccheda:* **श्वशुरः** / **श्वश्र्वा**

śvaśura (father-in-law) survives as the ekasheṣa remainder when paired
with śvaśrū (mother-in-law).  A specific niyama within the ekasheṣa
framework, analogous to 1.2.70 (pitā mātrā), prescribing that the
masculine in-law form (śvaśuraḥ) wins in the paternal/maternal in-law
pair.

Anuvritti from 1.2.70 carries the pattern of masculine survival in
gender-distinct kinship pairs in ekasheṣa.

Operational role (v3):
  - Registers the gate ``1_2_71_zvaZura_zvaSrvA`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when processing the śvaśura–śvaśrū
    pair in ekasheṣa to select the śvaśura form.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_71_zvaZura_zvaSrvA"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.71",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "zvazuraH zvazrvA",
    text_dev                = "श्वशुरः श्वश्र्वा",
    padaccheda_dev          = "श्वशुरः / श्वश्र्वा",
    why_dev                 = (
        "श्वशुर-श्वश्रू-युगले एकशेषे श्वशुर एव शिष्यते — "
        "श्वश्र्वा सह एकशेषे श्वशुरशब्दस्य ग्रहणम् इति नियमः।"
    ),
    anuvritti_from          = ("1.2.70",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
