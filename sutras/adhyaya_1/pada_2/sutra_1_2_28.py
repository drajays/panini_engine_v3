"""
1.2.28  अचश्च  (acaś ca)  —  SAMJNA

Anuvṛtti: ūkāla (vowel-quantity classification) from 1.2.27.

Meaning: And vowels (ac) [participate in the three-fold quantity
classification — hrasva/dīrgha/pluta]. This sūtra extends and
reinforces the vowel-duration saṃjñā of 1.2.27 by explicitly stating
that ALL ac (vowels) participate in the hrasva / dīrgha / pluta
classification scheme.

The word "ca" (and) links this to the prior sūtra (1.2.27) by anuvṛtti,
affirming that the quantity-classification framework is not limited to
special contexts but applies universally to all ac phonemes.

Engine:
  - Gate-style idempotent SAMJNA.
  - cond: fire only if paribhasha_gates["1_2_28_acaS_ca"] is not True.
  - act: set paribhasha_gates["1_2_28_acaS_ca"] = True;
         set samjna_registry["1_2_28_acaS_ca"] = True; return state.
  - r1_form_identity_exempt=True: no surface string changes.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    """Idempotent guard — fire only if the ac-quantity gate is not yet set."""
    return state.paribhasha_gates.get("1_2_28_acaS_ca") is not True


def act(state: State) -> State:
    """Register the ac-quantity gate. No varṇa mutation."""
    state.paribhasha_gates["1_2_28_acaS_ca"] = True
    state.samjna_registry["1_2_28_acaS_ca"] = True
    return state


_WHY_DEV = (
    "अच् (स्वर) च ऊकाल-त्रिकः — ह्रस्व-दीर्घ-प्लुत-भेदेन सर्वे स्वराः वर्गीकृताः। "
    "'च' इत्यनेन १.२.२७-तः अनुवृत्तिः — सर्वेषाम् अचां मात्रा-संज्ञा प्रवर्तते।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.28",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "acaS ca",
    text_dev                = "अचश्च",
    padaccheda_dev          = "अचः / च",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.27",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
