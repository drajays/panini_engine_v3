"""asmad / yuzmad stem-prefix helpers for the 7.2.86–97 ādeśas (the stem is replaced up to its final ``ad``)."""
from __future__ import annotations

from phonology.varna import parse_slp1_upadesha_sequence

PRONOUN_PREFIX = {"asmad": "asm", "yuzmad": "yuzm"}


def stem_key(t) -> str:
    return (t.meta.get("upadesha_slp1") or "").strip()


def prefix_len(t) -> int:
    """Length of the replaceable prefix (asm / yuzm) if the Term currently starts with it, else 0."""
    p = PRONOUN_PREFIX.get(stem_key(t))
    if not p or [v.slp1 for v in t.varnas[: len(p)]] != list(p):
        return 0
    return len(p)


def replace_prefix(t, new_slp1: str) -> None:
    t.varnas = list(parse_slp1_upadesha_sequence(new_slp1)) + list(t.varnas[prefix_len(t):])
