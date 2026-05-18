"""
1.2.52  विशेषणानां चाजातेः  —  NIYAMA

*Padaccheda:* **विशेषणानाम्** / **च** / **अजातेः**

Of *viśeṣaṇas* (adjectives / qualifiers) — but NOT when they denote
*jāti* (genus / natural class) — [the *ekasheṣa* rule from 1.2.64
applies].  This is a *niyama* restricting ekasheṣa: adjectival forms
undergo single-remainder treatment only when they do NOT refer to the
genus/class itself.

Anuvṛtti: *ekasheṣa* from the 1.2.64 region.

Operational role (v3):
  - Registers the gate ``1_2_52_viSezaNA_ajAteH`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream ekasheṣa recipes consult this gate to decide whether
    adjectival-qualifier forms are eligible for single-remainder
    reduction (excluding jāti-denotation contexts).

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_52_viSezaNA_ajAteH"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.52",
    sutra_type              = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1               = "viSezaRARAM cAjAteH",
    text_dev                = "विशेषणानां चाजातेः",
    padaccheda_dev          = "विशेषणानाम् / च / अजातेः",
    why_dev                 = (
        "विशेषणानां जातिवाचित्वं विना एकशेषो विधीयते — "
        "जातिबोधके विशेषणे तु एकशेषो न भवति इति नियमः।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
