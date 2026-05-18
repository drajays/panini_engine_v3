"""
1.4.10  ह्रस्वं लघु  (hrasvaṃ laghu)  —  SAMJNA

**Pāṭha:** A short (*hrasva*) vowel [syllable] is called *laghu*.

v3: registers the frozenset of SLP1 hrasva vowels under the key ``"laghu"``
in ``state.samjna_registry``.  Fires once (guarded by None-check).

Module-level frozenset per CONSTITUTION Art. 2 / frozenset policy:
  a  — short a
  i  — short i
  u  — short u
  f  — short ṛ (ṛikāra)
  x  — short ḷ (ḷikāra)
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

# SLP1 short (hrasva) vowels
_HRASVA: frozenset = frozenset({"a", "i", "u", "f", "x"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("laghu") is None


def act(state: State) -> State:
    state.samjna_registry["laghu"] = _HRASVA
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.10",
    sutra_type             = SutraType.SAMJNA,
    text_slp1              = "hrasvaM laghu",
    text_dev               = "ह्रस्वं लघु",
    padaccheda_dev         = "ह्रस्वम् / लघु",
    why_dev                = "ह्रस्व-स्वरः लघु-संज्ञकः (अ-इ-उ-ऋ-ऌ)।",
    anuvritti_from         = ("1.4.1",),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
