"""
phonology/gostriyor_upasarjana.py — pure helpers for **1.2.48** *gostriyor
upasarjanasya* (hrasva on *prātipadika* when the *upasarjana* is *go* or ends
in a *strī*-pratyaya-class surface).

No ``State`` / ``Term`` imports: callers pass ``List[Varna]`` only.
"""
from __future__ import annotations

from typing import List, Optional

from phonology.varna import Varna, mk


def flat_slp1(varnas: List[Varna]) -> str:
    return "".join(v.slp1 for v in varnas)


def ends_with_go_component(flat: str) -> bool:
    """True if the flat string ends in the *go* sequence ``…go`` (SLP1)."""
    return len(flat) >= 2 and flat.endswith("go")


def strI_final_dirgha_applicable(flat: str) -> bool:
    """Final letter is a *dirgha* vowel classically shortened under 1.2.48."""
    return bool(flat) and flat[-1] in ("A", "I", "U")


_DIRGHA_TO_HRASVA = {"A": "a", "I": "i", "U": "u"}


def apply_go_hrasva(varnas: List[Varna]) -> Optional[List[Varna]]:
    """
    *go* → *gu* style: final ``o`` after ``g`` becomes ``u`` (citra-go → citra-gu).
    Returns a new list or ``None`` if inapplicable.
    """
    flat = flat_slp1(varnas)
    if not ends_with_go_component(flat):
        return None
    out = [v.clone() for v in varnas]
    last = out[-1]
    if last.slp1 != "o":
        return None
    nv = mk("u")
    nv.tags = set(last.tags)
    out[-1] = nv
    return out


def apply_strI_pratyaya_final_hrasva(varnas: List[Varna]) -> Optional[List[Varna]]:
    """
    Final *dirgha* ``A`` / ``I`` / ``U`` → hrasa ``a`` / ``i`` / ``u``
    (e.g. *atikhATvA* → *atikhATva*, *nirvArANasI* style *I* → *i*).
    """
    flat = flat_slp1(varnas)
    if not strI_final_dirgha_applicable(flat):
        return None
    last = varnas[-1]
    short = _DIRGHA_TO_HRASVA.get(last.slp1)
    if short is None:
        return None
    out = [v.clone() for v in varnas]
    nv = mk(short)
    nv.tags = set(last.tags)
    out[-1] = nv
    return out
