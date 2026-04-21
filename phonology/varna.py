"""
phonology/varna.py — canonical SLP1 ↔ Devanāgarī mappings + mk() factory.
─────────────────────────────────────────────────────────────────────────

SOURCE OF TRUTH for phoneme → Devanāgarī surface.  Every Varna built
via mk() automatically gets its `dev` set from these tables, so we
never carry inconsistent (slp1, dev) pairs.

Convention:
  • A consonant Varna's `dev` is ALWAYS halanta form (क् not क).
  • A vowel Varna's `dev` is the STANDALONE form (अ not ा).
  • An inherent-'a' after a consonant is Varna(slp1='a', dev='').
"""
from __future__ import annotations

from engine.state import Varna  # re-export for sūtras; no engine runtime used


AC_DEV = {
    "a": "अ", "A": "आ",
    "i": "इ", "I": "ई",
    "u": "उ", "U": "ऊ",
    "f": "ऋ", "F": "ॠ",
    "x": "ऌ", "X": "ॡ",
    "e": "ए", "E": "ऐ",
    "o": "ओ", "O": "औ",
}


HAL_DEV = {
    "k": "क्", "K": "ख्", "g": "ग्", "G": "घ्", "N": "ङ्",
    "c": "च्", "C": "छ्", "j": "ज्", "J": "झ्", "Y": "ञ्",
    "w": "ट्", "W": "ठ्", "q": "ड्", "Q": "ढ्", "R": "ण्",
    "t": "त्", "T": "थ्", "d": "द्", "D": "ध्", "n": "न्",
    "p": "प्", "P": "फ्", "b": "ब्", "B": "भ्", "m": "म्",
    "y": "य्", "v": "व्", "r": "र्", "l": "ल्",
    "S": "श्", "z": "ष्", "s": "स्",
    "h": "ह्",
}


AC_MATRA = {
    "a": "",    "A": "ा",
    "i": "ि",   "I": "ी",
    "u": "ु",   "U": "ू",
    "f": "ृ",   "F": "ॄ",
    "x": "ॢ",   "X": "ॣ",
    "e": "े",   "E": "ै",
    "o": "ो",   "O": "ौ",
}


HAL_BASE = {k: v[:-1] for k, v in HAL_DEV.items()}


# Anusvāra / visarga are represented by special slp1 chars:
#   'M' → anusvāra ं,    'H' → visarga ः
SPECIAL_DEV = {
    "M": "ं",
    "H": "ः",
}


def mk(slp1: str, *tags: str) -> Varna:
    """
    Build a Varna from an SLP1 letter with auto-derived Devanāgarī.

    >>> mk('r').slp1, mk('r').dev
    ('r', 'र्')
    >>> mk('A').slp1, mk('A').dev
    ('A', 'आ')
    >>> mk('a').dev
    'अ'
    """
    if slp1 in AC_DEV:
        dev = AC_DEV[slp1]
    elif slp1 in HAL_DEV:
        dev = HAL_DEV[slp1]
    elif slp1 in SPECIAL_DEV:
        dev = SPECIAL_DEV[slp1]
    else:
        raise ValueError(f"unknown SLP1 phoneme: {slp1!r}")
    return Varna(slp1=slp1, dev=dev, tags=set(tags))


def mk_inherent_a() -> Varna:
    """Inherent-a after a consonant: slp1='a', dev=''."""
    return Varna(slp1="a", dev="", tags=set())


def parse_slp1_upadesha_sequence(slp1_seq: str) -> list:
    """
    Parse SLP1 upadeśa where a standalone ``~`` marks anunāsika on the nearest
    preceding vowel (same information as Devanagari candrabindu ``ँ`` in
    ``devanagari_to_varnas``).

    Examples:
      * ``qupac~z`` → ``… a(anunāsika), c, …`` (the ``~`` applies to the ``a``).
      * Inventory ``s~`` (सुँ) → ``[s, u(anunāsika)]`` (no vowel precedes ``~``).

    This must stay aligned with ``phonology.tokenizer.devanagari_to_slp1_flat``,
    which emits ``~`` after vowel letters that carry the ``anunasika`` tag.
    """
    from phonology.pratyahara import AC, HAL

    if slp1_seq == "s~":
        return [mk("s"), mk("u", "anunasika")]
    varnas: list = []
    i = 0
    while i < len(slp1_seq):
        ch = slp1_seq[i]
        if ch == "~":
            for j in range(len(varnas) - 1, -1, -1):
                if varnas[j].slp1 in AC:
                    varnas[j].tags.add("anunasika")
                    break
            i += 1
            continue
        if ch == "a" and varnas and varnas[-1].slp1 in HAL:
            v = mk_inherent_a()
        else:
            v = mk(ch)
        varnas.append(v)
        i += 1
    return varnas


def mk_upadesha(slp1_seq: str) -> list:
    """
    Build a raw upadeśa varṇa list from a SLP1 string.
    Used by sutras/adhyaya_4/pada_1/sutra_4_1_2.py (sup inventory) and
    the dhātupāṭha loader.
    """
    return parse_slp1_upadesha_sequence(slp1_seq)
