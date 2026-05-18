"""
1.4.12  दीर्घं च  (dīrghaṃ ca)  —  SAMJNA

**Pāṭha:** A long (*dīrgha*) vowel is also (*ca*) *guru* [by anuvritti from
1.4.11].

v3: registers the frozenset of SLP1 dīrgha (long) vowels under
``"guru_dirgha"`` in ``state.samjna_registry``.  Fires once (guarded by
None-check).

Module-level frozenset per CONSTITUTION frozenset policy:
  A — long ā
  I — long ī
  U — long ū
  F — long ṝ
  X — long ḹ
  e — e (always long in Pāṇini)
  E — ai
  o — o
  O — au
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

# SLP1 dīrgha (long / guru by nature) vowels
_DIRGHA: frozenset = frozenset({"A", "I", "U", "F", "X", "e", "E", "o", "O"})


def cond(state: State) -> bool:
    return state.samjna_registry.get("guru_dirgha") is None


def act(state: State) -> State:
    state.samjna_registry["guru_dirgha"] = _DIRGHA
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.12",
    sutra_type             = SutraType.SAMJNA,
    text_slp1              = "dIrghaM ca",
    text_dev               = "दीर्घं च",
    padaccheda_dev         = "दीर्घम् / च",
    why_dev                = "दीर्घ-स्वरोऽपि गुरु-संज्ञकः (आ-ई-ऊ-ॠ-ॡ-ए-ऐ-ओ-औ)।",
    anuvritti_from         = ("1.4.1", "1.4.10", "1.4.11"),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
