"""
1.1.24  (ṣṇāntā ṣaṭ)  —  SAMJNA; *devanāgarī* = ``_TEXT_DEV`` (ashtadhyayi *i* 11024 *s* line).

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11024):** under *anuvṛtti* of *saṅkhyā* from **1.1.23**
(``an`` = ``संख्या``), a numeral (*saṅkhyā*) that is *ṣ*-ending or *ṇ*-ending (*ṣṇānta*) receives
the technical name *ṣaṭ*.

v3: ``samjna_registry['zaW']`` registers the **ending-set** (SLP1) ``{'z', 'n'}`` once (R2), and
``sankhya_pratipadika_is_zananta`` provides the operational membership test without consulting any
gold lists (CONSTITUTION Art. 2 / Art. 6).  This file does not mutate any ``Term``.
"""
from __future__ import annotations

from typing import FrozenSet

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from sutras.adhyaya_1.pada_1 import sutra_1_1_23 as s1123

# SLP1 endings: z = ष्, n = न् (the rule's *ṣṇānta* locus).
ZANANTA_ENDINGS_SLP1: FrozenSet[str] = frozenset({"z", "n"})

# Registry key: ṣaṭ = zaW (W = ट्).
ZAT_KEY: str = "zaW"

# Exact ``s`` (i=11024).
_TEXT_DEV: str = "ष्णान्ता षट्"


def zat_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get(ZAT_KEY) == ZANANTA_ENDINGS_SLP1


def sankhya_pratipadika_is_zananta(pratipadika_slp1: str) -> bool:
    """True iff this (SLP1) stem ends in **z** or **n** (ṣ/ṇ-anta)."""
    s = pratipadika_slp1.strip()
    if not s:
        return False
    return s[-1] in ZANANTA_ENDINGS_SLP1


def cond(state: State) -> bool:
    # Only meaningful under *saṅkhyā* anuvṛtti (1.1.23), and idempotent.
    if not s1123.sankhya_samjna_1_1_23_is_registered(state):
        return False
    return not zat_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry[ZAT_KEY] = ZANANTA_ENDINGS_SLP1
    return state


_WHY = (
    "संख्या-शब्देषु ष-ण-अन्तेषु, 'षट्' इति संज्ञा (१.१.२३-अनुवृत्त्या)।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.24",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "zRAntA zaW",
    text_dev       = _TEXT_DEV,
    padaccheda_dev = "ष्णान्ता / षट्",
    why_dev        = _WHY,
    anuvritti_from = ("1.1.23",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

