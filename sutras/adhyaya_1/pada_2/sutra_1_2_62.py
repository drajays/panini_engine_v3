"""
1.2.62  विशाखयोश्च  —  VIDHI (SAMJNA gate)

*Padaccheda:* **विशाखयोः** / **च**

And for "viśākhā" — another nakṣatra pair — the same plural/dual
treatment applies (anuvritti of the ekaśeṣa/bahuvacanam rule from
1.2.60).  The particle "ca" (and) draws in the earlier rule by
continuation.

Operational role (v3):
  - Registers the gate ``1_2_62_viSAkhayoH`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when applying plural/ekaśeṣa
    treatment to the nakṣatra name "viśākhā".

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_62_viSAkhayoH"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.62",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "vizAKayoH ca",
    text_dev                = "विशाखयोश्च",
    padaccheda_dev          = "विशाखयोः / च",
    why_dev                 = (
        "विशाखा-नक्षत्रयुगलस्यापि एकशेष-बहुवचन-विधिः अनुवर्तते — "
        "च-शब्देन फल्गुनी-प्रोष्ठपदयोः समं विशाखयोरपि ग्रहणम्।"
    ),
    anuvritti_from          = ("1.2.60",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
