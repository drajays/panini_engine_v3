"""
1.2.59  अस्मदो द्वयोश्च  —  VIDHI

*Padaccheda:* **अस्मदः** / **द्वयोः** / **च**

"And for 'asmad' (the first-person pronoun base), [ekasheṣa applies] for
dual (dvayoḥ) also."  This sūtra extends the ekasheṣa rule (1.2.64) to
the asmad pronoun in dual number: when two referents are expressed by asmad,
the ekasheṣa (single-remainder) operation applies in the dual as well.

Operational role (v3):
  - Registers the gate ``1_2_59_asmad_dvayoH`` in both ``paribhasha_gates``
    and ``samjna_registry``.
  - Downstream ekasheṣa processing for asmad consults this gate to confirm
    that dual-number extension is active.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_59_asmad_dvayoH"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.59",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "asmado dvayoS ca",
    text_dev                = "अस्मदो द्वयोश्च",
    padaccheda_dev          = "अस्मदः / द्वयोः / च",
    why_dev                 = (
        "अस्मच्छब्दात् द्वयोः सन्दर्भे च एकशेषः — "
        "अस्मद्-प्रातिपदिकस्य द्विवचनेऽपि एकशेषविधिः प्रवर्तते इति विधिः।"
    ),
    anuvritti_from          = ("1.2.58",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
