"""phonology/stem_input.py — prātipadika input normalization utilities."""
from __future__ import annotations

from phonology.tokenizer import devanagari_to_slp1_flat

_DEVA_START = 0x0900
_DEVA_END = 0x097F


def _has_devanagari(s: str) -> bool:
    return any(_DEVA_START <= ord(c) <= _DEVA_END for c in s)


def _has_latin_letters(s: str) -> bool:
    return any("A" <= c <= "Z" or "a" <= c <= "z" for c in s)


def normalize_pratipadika_input(raw: str) -> str:
    """Return canonical SLP1 stem from either Devanāgarī or SLP1 input."""
    s = raw.strip()
    if not s:
        return ""
    dev = _has_devanagari(s)
    lat = _has_latin_letters(s)
    if dev and lat:
        raise ValueError(
            "एक ही इनपुट में देवनागरी और लैटिन (SLP1) मिलाकर न लिखें — "
            "या तो केवल `राम` जैसा देवनागरी, या केवल `rAma` जैसा SLP1।"
        )
    if dev:
        return devanagari_to_slp1_flat(s)
    return s


def stem_slp1_to_display_devanagari(stem_slp1: str) -> str:
    """Convert SLP1 prātipadika to display Devanāgarī."""
    from phonology.joiner import slp1_to_devanagari
    from pipelines.subanta import build_initial_state

    s0 = build_initial_state(stem_slp1, 1, 1)
    if not s0.terms:
        return ""
    return slp1_to_devanagari(s0.terms[0].varnas)
