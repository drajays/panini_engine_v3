"""
pipelines/preflight_lopa_samjna.py — shared **1.1.60**–**1.1.63** *prayoga* block.

Several recipes need the same *lopa* / *luk*–*ślu*–*lup* *saṃjñā* / *pratyayalakṣaṇa*
*paribhāṣā* *śr̥ṅkhalā* in identical order.  Centralizing preserves one canonical
sequence; **sūtra* logic* remains in ``sutras/``; this module only *schedules*
``apply_rule`` calls.
"""
from __future__ import annotations

from engine       import apply_rule
from engine.state import State

# *sthāne adarśanam* (1.1.60) → *luk*–*ślu*–*lup* (1.1.61) → *pratyayalakṣaṇam* (1.1.62)
# → *na lumat…* (1.1.63) — *subanta* preflight align *krdanta* / *subanta_trc*.
PREFLIGHT_LOPA_LUK_1_1_6X: tuple[str, ...] = (
    "1.1.60",
    "1.1.61",
    "1.1.62",
    "1.1.63",
)


def apply_preflight_luk_samjna_block(s: State) -> State:
    for sid in PREFLIGHT_LOPA_LUK_1_1_6X:
        s = apply_rule(sid, s)
    return s
