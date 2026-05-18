"""
1.2.67  पुमान् स्त्रिया  —  VIDHI (SAMJNA gate)

*Padaccheda:* **पुमान्** / **स्त्रिया**

The masculine (pumān) [survives] when paired with a feminine (striyā) in
ekasheṣa.  This sūtra is complementary to 1.2.66: whereas 1.2.66 states
that a feminine behaves like a masculine, 1.2.67 explicitly names the
masculine as the one that is retained.

Operational role (v3):
  - Registers the gate ``1_2_67_pumAn_striyA`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate to confirm the masculine member is
    the ekaśeṣa survivor when masculine and feminine are paired.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_67_pumAn_striyA"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.67",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "pumAn striyA",
    text_dev                = "पुमान् स्त्रिया",
    padaccheda_dev          = "पुमान् / स्त्रिया",
    why_dev                 = (
        "एकशेषे स्त्रिया सह पुमान् शिष्यते — पुंलिङ्गस्य एव ग्रहणं भवति "
        "स्त्रीलिङ्गेन युगले सति। १.२.६६ इत्यस्य पूरकः।"
    ),
    anuvritti_from          = ("1.2.66",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
