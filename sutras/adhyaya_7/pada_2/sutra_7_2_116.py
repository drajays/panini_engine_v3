"""
7.2.116  अतो उपधायाः  —  VIDHI

Operational role (v3.8, kṛt Nvul agent nouns like पाचक):
  When a dhātu has upadhā 'a' and the following pratyaya is **ṇit**,
  apply vṛddhi to that upadhā:

  pac + (ṇit-pratyaya) → pAc ...

We implement narrowly:
  - first term is dhātu
  - last term is kṛt pratyaya whose recorded it-markers contain 'N'
  - dhātu ends with a consonant, and the vowel immediately before that
    consonant is 'a' → replace it with 'A'
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk, HAL


def _find_upadha_a(state: State):
    if len(state.terms) < 2:
        return None
    dhatu = state.terms[0]
    pr    = state.terms[-1]
    if "dhatu" not in dhatu.tags:
        return None
    if "krt" not in pr.tags:
        return None
    itm = pr.meta.get("it_markers", set())
    if not isinstance(itm, set) or not ("N" in itm or "R" in itm):
        return None
    if dhatu.meta.get("upadha_vrddhi_done"):
        return None
    if len(dhatu.varnas) < 2:
        return None
    if dhatu.varnas[-1].slp1 not in HAL:
        return None
    # Upadhā = vowel before final consonant in this minimal model.
    if dhatu.varnas[-2].slp1 != "a":
        return None
    return (0, len(dhatu.varnas) - 2)


def cond(state: State) -> bool:
    return _find_upadha_a(state) is not None


def act(state: State) -> State:
    hit = _find_upadha_a(state)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi] = mk("A")
    state.terms[ti].meta["upadha_vrddhi_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.116",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ata upadhAyAH (Nit pare)",
    text_dev       = "अतो उपधायाः",
    padaccheda_dev = "अतः उपधायाः",
    why_dev        = "णित्-प्रत्यये परे धातोः उपधास्थ-अकारस्य वृद्धि (पच् → पाच्)।",
    anuvritti_from = ("1.1.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

