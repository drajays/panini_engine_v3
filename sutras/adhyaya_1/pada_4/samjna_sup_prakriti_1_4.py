"""
Shared predicates for **1.4.16–1.4.18** (*pada* / *bha* on *prakṛti* before *sup*).

Not a sūtra module (no ``SutraRecord``) — excluded from the ``sutra_*.py`` loader.
"""
from __future__ import annotations

from engine.state import Term
from phonology.pratyahara import AC, YAN
from phonology.varna import HAL_DEV

# Same loose *yaci* onset as **1.4.18** (*ac* ∪ *yaṭ* ∪ śaṭ sparśa in SLP1).
_YACI_HAL = frozenset(YAN) | frozenset({"S", "z", "s", "h"})

_PU_STRI_SARVANAMASTHANA = frozenset({"s~", "O", "jas", "am", "Ow"})
_NAPUMS_SARVANAMASTHANA = frozenset({"jas", "Sas"})


def is_sarvanamasthana_sup(pr: Term, anga: Term) -> bool:
    if "sarvanamasthana" in pr.tags:
        return True
    u = pr.meta.get("upadesha_slp1")
    if u == "Si":
        return True
    if not u:
        return False
    if "napuṃsaka" in anga.tags:
        return u in _NAPUMS_SARVANAMASTHANA
    return u in _PU_STRI_SARVANAMASTHANA


def yaci_onset_loose(pr: Term) -> bool:
    """*Yaci* as in **1.4.18** (post-*it* ``Term.varnas``)."""
    if not pr.varnas:
        return False
    ch = pr.varnas[0].slp1
    return ch in AC or ch in _YACI_HAL


def raw_upadesha_first_slp1(raw: str) -> str | None:
    if not raw:
        return None
    return raw[0]


def yaci_onset_strict_siti(raw: str) -> bool:
    """
    *Yaci* narrow slice for **1.4.16** (*siti ca*): *yaṭ* (**y/v/r/l**) or vowel,
    excluding ś/ṣ/s/h — so **śas** (**Sas**) does not block **bha** here.
    """
    ch = raw_upadesha_first_slp1(raw)
    if ch is None:
        return False
    return ch in AC or ch in YAN


def raw_final_is_hal_s(raw: str) -> bool:
    """True if raw *sup* upadeśa ends in dental ``s`` (a typical *it* *hal*)."""
    if not raw:
        return False
    last = raw[-1]
    return last == "s" and last in HAL_DEV


def is_siti_pada_context(pr: Term, anga: Term) -> bool:
    """**1.4.16** — *siti* + *asarvanāmasthāna* *svādi* (*ca* extends **1.4.14** *pada*)."""
    if "sup" not in pr.tags or "anga" not in anga.tags:
        return False
    if is_sarvanamasthana_sup(pr, anga):
        return False
    raw = pr.meta.get("upadesha_slp1") or ""
    if not raw_final_is_hal_s(raw):
        return False
    return yaci_onset_strict_siti(raw)


def is_asarvanamasthana_svadi_sup(pr: Term, anga: Term) -> bool:
    """**1.4.17** — *svādiṣv asarvanāmasthāne* (no *yaci* condition)."""
    return (
        "sup" in pr.tags
        and "anga" in anga.tags
        and not is_sarvanamasthana_sup(pr, anga)
    )
