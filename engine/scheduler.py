"""
engine/scheduler.py — Candidate enumeration.
──────────────────────────────────────────────

For "autonomous" derivation (no recipe list), the scheduler asks:
  "Which sūtras in the registry would fire on this state RIGHT NOW?"

It returns the list of ids whose `cond(state)` returns True AND which
are not blocked / frozen / asiddha.

If exactly one candidate remains, fire it.
If zero,   derivation has halted.
If more,   pass to engine/resolver.py.

This module is OPTIONAL for pipeline-driven derivations (which call
apply_rule() in a fixed order).  It is USED by tests that verify the
engine can reach a gold form autonomously.

Scheduler discipline (Phase 4):
  The autonomous loop only considers VIDHI, NIYAMA, VIBHASHA, and SAMJNA
  sūtras.  The others are excluded for these reasons:

  PARIBHASHA  — interpretive meta-rules (paribhāṣā gates) that are always
                active as background principles; they are not "fired" by
                the autonomous loop — they are consulted by other sūtras.

  ADHIKARA    — scope-management sūtras that open/close adhikāra stacks;
                these require pipeline context to know when to open and
                are handled by the recipe spine, not the loop.

  ANUVADA     — trace/restatement sūtras; no tape change, recipe-only.

  NIPATANA    — exceptional form stamps; require pipeline context.

  ATIDESHA    — analogical extension rules; handled by atidesha executor
                when explicitly invoked.

  PRATISHEDHA — blocking rules; consulted via state.blocked_sutras gate,
                not enumerated as candidates.
"""
from __future__ import annotations

from typing import List

from engine.gates      import (
    asiddha_violates,
    is_blocked,
    is_frozen_by_nipatana,
    is_tripadi,
)
from engine.phase      import sutra_in_phase
from engine.registry   import SUTRA_REGISTRY
from engine.state      import State
from engine.sutra_type import SutraType

# Sūtra types the autonomous loop considers.
_LOOP_TYPES: frozenset[SutraType] = frozenset({
    SutraType.VIDHI,
    SutraType.NIYAMA,
    SutraType.VIBHASHA,
    SutraType.SAMJNA,
})

# Multi-term ranges: sūtras that require ≥2 terms on the tape.
# Skip them when the tape has < 2 terms (nothing to junction/compound/assign).
#
# 2.1.1–2.1.72   samāsa (compound formation) — prātipadika + case relation
# 2.2.1–2.2.38   samāsa sub-types — multi-member compound context
# 2.3.1–2.3.73   kāraka vibhakti — noun + vibhakti assignment context
# 6.1.1–6.1.229  vowel-consonant junction (saṃhitā) — inter-term boundary
# 6.2.1–6.2.199  accentuation (svara) — compound/prātipadika+sup boundary
# 6.3.1–6.3.999  sandhi in samāsa/taddhita — compound boundary
#
# 6.2.*/6.3.* additionally require a PRĀTIPADIKA term — they are for nominal
# (subanta) sandhi, not tinanta (dhātu+vikaraṇa+tiṅ) context.
_MULTI_TERM_RANGES: tuple[tuple[tuple[int, ...], tuple[int, ...]], ...] = (
    ((2, 1, 1), (2, 1, 72)),
    ((2, 2, 1), (2, 2, 38)),
    ((2, 3, 1), (2, 3, 73)),
    ((6, 1, 1), (6, 1, 229)),
    ((6, 2, 1), (6, 2, 199)),
    ((6, 3, 1), (6, 3, 999)),
)

# Ranges that additionally require a prātipadika on the tape.
# Even when ≥2 terms are present (dhātu+vikaraṇa+tiṅ), samāsa-sandhi sūtras
# don't apply to tinanta spines.
_PRATIPADIKA_REQUIRED_RANGES: tuple[tuple[tuple[int, ...], tuple[int, ...]], ...] = (
    ((6, 2, 1), (6, 2, 199)),
    ((6, 3, 1), (6, 3, 999)),
    ((2, 1, 1), (2, 1, 72)),
    ((2, 2, 1), (2, 2, 38)),
    ((2, 3, 1), (2, 3, 73)),
)


def _id_tuple(sid: str) -> tuple[int, ...]:
    return tuple(int(p) for p in sid.split("."))


def _needs_multi_term(sid: str, state: State) -> bool:
    """
    Return True when the sūtra cannot fire on the current tape.

    Two guards:
      1. Single-term gate: sūtras that need ≥2 terms (sandhi/samāsa/kāraka)
         are skipped when the tape has fewer than 2 terms.
      2. Prātipadika gate: samāsa/svara/nominal-sandhi sūtras (6.2.*/6.3.*,
         2.1-2.3.*) are skipped unless a prātipadika term is on the tape.
         This prevents tinanta spines (dhātu+vikaraṇa+tiṅ) from spuriously
         matching these sūtras after vikaraṇa insertion adds a 3rd term.
    """
    nterms = len(state.terms)
    t = _id_tuple(sid)

    # Single-term check: skip if less than 2 terms
    if nterms < 2:
        return any(lo <= t <= hi for lo, hi in _MULTI_TERM_RANGES)

    # Prātipadika gate: for ranges that need compound/nominal context
    if any(lo <= t <= hi for lo, hi in _PRATIPADIKA_REQUIRED_RANGES):
        return not any("prātipadika" in term.tags for term in state.terms)

    return False


def _skip_krt_window(sid: str, state: State) -> bool:
    """
    Prayoga-class fast path: skip adhyāya 3.2/3.3 kṛt windows on tinanta
    spines unless ``krdanta_pending`` is on the tape.
    """
    t = _id_tuple(sid)
    if not ((3, 2, 1) <= t <= (3, 3, 999)):
        return False
    dc = (state.meta.get("derivation_class") or "").strip()
    if dc != "tinanta":
        return False
    if any("krdanta_pending" in term.tags for term in state.terms):
        return False
    return True


def _in_scheduler_phase(sid: str, state: State) -> bool:
    """Phase-scoped enumeration — only sūtras in the current phase window."""
    phase = getattr(state, "phase", "angakarya") or "angakarya"
    if phase == "tripadi":
        return is_tripadi(sid)
    return sutra_in_phase(sid, phase)


def enumerate_candidates(state: State) -> List[str]:
    """
    Return sūtra ids whose cond(state) fires on the current state and
    which are not ruled out by gates.  Deterministic: sorted by id.

    Only VIDHI, NIYAMA, VIBHASHA, and SAMJNA sūtras are enumerated —
    PARIBHASHA, ADHIKARA, ANUVADA, NIPATANA, ATIDESHA, and PRATISHEDHA
    are excluded (see module docstring for rationale).

    Bidirectional Tripāḍī isolation (scheduler-only — the dispatcher
    allows explicit recipe calls outside this gate):
      • Outside Tripāḍī zone: skip Tripāḍī sūtras (8.2.1–8.4.68).
      • Inside Tripāḍī zone: asiddha_violates() skips non-Tripāḍī sūtras.

    Saṃhitā heuristic: 6.1.1–6.1.229 require ≥2 tape terms (inter-term
    junction needed); skip them when tape has < 2 terms.

    Phase-scoped pools: only sūtras whose id falls in ``state.phase`` window
    are enumerated (see ``engine/phase.py``).
    """
    out = []
    in_tripadi = state.tripadi_zone
    for sid, rec in SUTRA_REGISTRY.items():
        if rec.sutra_type not in _LOOP_TYPES:
            continue
        if not _in_scheduler_phase(sid, state):
            continue
        if _skip_krt_window(sid, state):
            continue
        # Bidirectional Tripāḍī isolation in the scheduler.
        if not in_tripadi and is_tripadi(sid):
            continue
        # Multi-term heuristic: skip sandhi/svara/samāsa sūtras when < 2 terms.
        if _needs_multi_term(sid, state):
            continue
        if is_blocked(sid, state):
            continue
        if asiddha_violates(sid, state):
            continue
        if is_frozen_by_nipatana(rec.sutra_type, state):
            continue
        try:
            if rec.cond is not None and rec.cond(state):
                out.append(sid)
        except Exception:
            # A cond() that raises on this state simply doesn't apply.
            pass
    out.sort(key=lambda s: tuple(int(p) for p in s.split(".")))
    return out
