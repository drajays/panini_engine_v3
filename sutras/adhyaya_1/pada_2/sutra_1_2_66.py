"""
1.2.66  स्त्री पुंवच्च  —  VIDHI (SAMJNA gate)

*Padaccheda:* **स्त्री** / **पुंवत्** / **च**

And a feminine [word] acts like a masculine [word in ekasheṣa context].
When ekasheṣa pairs a masculine and feminine form, the masculine survives.
The particle "ca" (and) draws in the anuvritti from the preceding rules.

Operational role (v3):
  - Registers the gate ``1_2_66_strI_puMvat`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when determining which form survives
    in ekasheṣa between masculine and feminine members of a pair.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import accent_paribhasha_gate_eligible

_GATE_KEY = "1_2_66_strI_puMvat"


def cond(state: State) -> bool:
    return accent_paribhasha_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.66",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "strI puMvac ca",
    text_dev                = "स्त्री पुंवच्च",
    padaccheda_dev          = "स्त्री / पुंवत् / च",
    why_dev                 = (
        "एकशेषे स्त्री पुंवत् भवति — पुंलिङ्गः एव शिष्यते स्त्रीलिङ्गेन सह युगले। "
        "च-शब्देन पूर्वनियमस्यानुवृत्तिः।"
    ),
    anuvritti_from          = ("1.2.64",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
