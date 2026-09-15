"""
core/phases/tripadi — Universal Tripāḍī phase (8.2.1–8.4.68).

``execute_tripadi_phase(state)`` replaces all ``P00_tripadi_*`` canonical
fragments and inline ``apply_rule("8.2.x", …)`` sequences that were
previously duplicated across pipelines.  Call it AFTER ``pada_merge()``.

Design
------
* The spine contains only rules whose ``cond()`` is safe to call unconditionally
  after a pada-merge: they either have idempotency guards, narrow phonological
  conditions that naturally skip, or arm-gated conditions that skip when the arm
  is absent.
* Rules with overly broad ``cond()`` implementations that cause false positives
  on merged padas are kept OUT of the spine and called explicitly by pipelines:
    - 8.3.59  ādeśapratyayayoḥ: lookahead ``hal+s+IK`` fires on laṭ ``adsi`` → wrong ṣatva
    - 8.2.29  skoḥ saṃyogādyoranteṣu: fires vacuously on merged padas
    - 8.4.46/47 anunāsika dvitva: too broad for post-merge pada
    - 8.2.108  yar gemination: needs exhaustive loop (P00_tripadi_yar_anaci_dvitva_spine)
* Phase-4 upgrade: once arm removal is complete and all ``cond()`` are purely
  structural, this fixed spine will be replaced by the scheduler-driven loop
  in ``engine/core_loop.py``.
"""
from __future__ import annotations

import sutras  # noqa: F401 — ensures all sūtras are registered

from engine import apply_rule
from engine.state import State


_TRIPADI_SPINE: tuple[str, ...] = (
    # ── 8.2 — Asiddha gate + pada-final operations ──────────────────────────
    "8.2.1",    # pūrvatrāsiddham — opens Tripāḍī zone (idempotent gate)
    "8.2.23",   # saṃyogāntalopa — drops final cluster (ant→an)
    "8.2.39",   # jhal padānte → jaś (t→d at word-end)
    "8.2.66",   # sasajuṣo ruḥ — s→r at word-end
    # ── 8.3 — visarga, ṣatva ────────────────────────────────────────────────
    "8.3.15",   # khari visarjanīyaḥ — r→ḥ
    "8.3.24",   # naścopādhā anusvāraḥ — n→M before consonant
    "8.3.59",   # ādeśasya — ṣatva after IK in pratyaya-s (fixed: IK not word-final guard)
    "8.3.60",   # śāsi/vasi/ghasi ṣatva (idempotent: 8_3_60_satva_done flag)
    # ── 8.4 — assimilation ──────────────────────────────────────────────────
    "8.4.41",   # ṣṭunā ṣṭuḥ — ṣ+t→ṣ+ṭ (structural; arm-guarded for edge cases)
    "8.4.54",   # abhyāse carc — jhal→jaś in abhyāsa (idempotent: 8_4_54_carc_done)
    "8.4.55",   # khari ca — jhal→car before khar (idempotent: 8_4_55_khari_ca_done)
    "8.4.56",   # vāvasāne — jaś→car at pause (idempotent: gate)
    "8.4.58",   # anunāsika ca
    "8.4.68",   # a-a padānte — trace marker (idempotent gate)
)


def execute_tripadi_phase(state: State) -> State:
    """
    Apply the core Tripāḍī spine sequentially.

    Must be called AFTER ``pada_merge()``.  Pre-merge rules (8.2.1, 8.4.54)
    may be called explicitly by the pipeline before the merge; they will SKIP
    here due to their idempotency guards.

    Rules excluded from the spine (call explicitly when needed):
      8.2.29  — fires vacuously on merged padas; call pre-merge in āśīr-liṅ
      8.4.46/47 — dvitva gemination; needs scope guard
      8.2.108 — yar gemination; needs exhaustive loop

    Returns ``state`` (mutated in place, also returned for chaining).
    """
    for sid in _TRIPADI_SPINE:
        state = apply_rule(sid, state)
    return state
