"""
1.1.25  ḍati ca  —  SAMJNA

*Anuvṛtti*: saṃkhyā (1.1.23), ṣaṭ (1.1.24).

**Pāṭha:** *ḍa*+*ti* (i.e. kati-class interrogatives formed with the *ḍa*-suffix)
also (*ca*) receive the *ṣaṭ*-saṃjñā — as an extension of **1.1.24** beyond
*ṣ*/*ṇ*-ending numerals.

v3: ``samjna_registry['zaW_qati']`` registers the singleton frozenset ``{'kati'}``
once (R2 idempotent guard).  Terms with ``upadesha_slp1 == 'kati'`` and the
*saṃkhyā* tag-complex are stamped ``zat_samjna`` so downstream *ṣaṭ*-sensitive
rules (e.g. tṛtīyā-*ā*-plurals) can test the tag without re-reading the
registry.

Mechanical blindness (CONSTITUTION Art. 2):
  - ``cond`` reads only ``Term.meta['upadesha_slp1']``, Term.tags, and
    ``samjna_registry`` — no paradigm coordinates, no Devanāgarī strings.
"""
from __future__ import annotations

from typing import FrozenSet

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from sutras.adhyaya_1.pada_1 import sutra_1_1_23 as s1123
from sutras.adhyaya_1.pada_1 import sutra_1_1_24 as s1124

# SLP1 prātipadika for the ḍati-class: kim + ḍa-suffix → kati.
QATI_SET_SLP1: FrozenSet[str] = frozenset({"kati"})

# Registry key for the ḍati branch of ṣaṭ-saṃjñā.
ZAT_QATI_KEY: str = "zaW_qati"


def _zat_qati_registered(state: State) -> bool:
    return state.samjna_registry.get(ZAT_QATI_KEY) == QATI_SET_SLP1


def _eligible(state: State):
    """Yield Terms that are saṃkhyā-aṅga with upadesha_slp1 'kati' not yet tagged."""
    for t in state.terms:
        if "anga" not in t.tags:
            continue
        upa = t.meta.get("upadesha_slp1")
        if upa not in QATI_SET_SLP1:
            continue
        if "zat_samjna" in t.tags:
            continue
        yield t


def cond(state: State) -> bool:
    # Requires both 1.1.23 (saṃkhyā) and 1.1.24 (ṣaṭ) to be registered first.
    if not s1123.sankhya_samjna_1_1_23_is_registered(state):
        return False
    if not s1124.zat_samjna_is_registered(state):
        return False
    # Idempotent: once the registry entry is set, skip.
    if _zat_qati_registered(state):
        return False
    return True


def act(state: State) -> State:
    # Register the ḍati branch.
    state.samjna_registry[ZAT_QATI_KEY] = QATI_SET_SLP1
    # Tag any already-present kati-aṅga Terms.
    for t in _eligible(state):
        t.tags.add("zat_samjna")
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.25",
    sutra_type     = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1      = "qati ca",
    text_dev       = "डति च",
    padaccheda_dev = "डति / च (षट्-संज्ञा)",
    why_dev        = "डति (कति-आदि) च षट्-संज्ञकम् — १.१.२३-२४-अनुवृत्त्या।",
    anuvritti_from = ("1.1.23", "1.1.24"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
