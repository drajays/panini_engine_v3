# Pāṇini Engine v3 → v4: Final Architecture Plan
## Goal: World's Best Rule-Based Pāṇini Glass-Box Engine

> Every Sanskrit word derivable. Every step auditable. Every sūtra earning its firing.

---

## Vision

The engine derives any Pāṇinian form by simulating the Aṣṭādhyāyī as a
rewrite system. When complete, a classical scholar can read the derivation
trace and recognise each step as a legitimate sūtra application — no
shortcuts, no lookup tables, no hardcoded forms. The `derive()` function
becomes a thin router that hands an initial tape to the autonomous engine
loop and returns the result.

**Definition of Done:**
- `pipelines/tinanta.py` derives every tiṅanta cell via autonomous loop, not
  hardcoded `apply_rule()` scripts.
- All 223 arm reads in `sutras/` are replaced by proper linguistic conditions.
- Every ādeśa substitution uses `adesha_substitute_varnas()` for 1.1.56 inheritance.
- The Tripāḍī phase fires identically for tinanta, subanta, kṛdanta, and taddhita.
- Vibhāṣā rules produce forked states, both branches tested.
- `MAX_DUPLICATE_GROUPS = 0` and `ARM_GATE_BASELINE = 0` (cond) remain passing.

---

## Current State Metrics (baseline 2026-05-30)

| Metric | Value |
|--------|-------|
| Tests passing | 18,580 |
| ARM_GATE_BASELINE (cond) | 0 (clean) |
| Arm reads in act() | 223 across 157 files |
| Direct varnas mutations needing sthanivat | 3 files |
| Cursor-introduced lakāra reads in cond-helpers | 2 files |
| tinanta.py LOC | 4,503 |
| Engine infrastructure already built | phase.py, telemetry.py, resolver.py, scheduler.py, state.clone(), vibhasha_forks, exec_vibhasha.py, sthanivat.py |

The key insight: **the V4 engine infrastructure is embryonic, not absent**.
The work is completing + wiring it, then removing the hardcoded spines that
currently bypass it.

---

## Dependency Graph

```
Phase 0 (Compliance Hotfix)
  └─► Phase 1 (Tripāḍī Abstraction)
        └─► Phase 2 (Telemetry Isolation)
              └─► Phase 3 (Vibhāṣā Fork Manager)
                    └─► Phase 4 (Autonomous Cyclic Loop)   ← needs arm removal
                              └─► Phase 5 (Pipeline Thinning)
                                        └─► Phase 6+ (Completeness)

Phase 0 also unblocks ──► Arm Removal Campaign (parallel to Phases 1–3)
```

---

## Phase 0 — Constitution Compliance Hotfix
**Duration:** 1–2 sessions  
**Prerequisite:** None — do this before anything else.

### 0.1 Sthanivat for whole-term ādeśas (Priority 1 — Correctness)

Three cursor-introduced sutra files do direct `t.varnas = list(...)` mutations
that bypass 1.1.56 inheritance. Fix each by calling `adesha_substitute_varnas()`
from `engine/sthanivat.py`:

**`sutras/adhyaya_2/pada_4/sutra_2_4_37.py`** — `ad` → `ghas` (luṅ):
```python
from engine.sthanivat import DHATUTVA, adesha_substitute_varnas
# Replace: t.varnas = list(parse_slp1_upadesha_sequence("Gas"))
adesha_substitute_varnas(t, "Gas", state, sutra_id="2.4.37",
                         gunadharmas=frozenset({DHATUTVA}))
```
Add `state.samjna_registry["2.4.37_ad_ghas_done"] = True` in act() for
downstream cond() consumers (Phase 3a).

**`sutras/adhyaya_2/pada_4/sutra_2_4_43.py`** — `han` → `vadha` (luṅ):
```python
from engine.sthanivat import DHATUTVA, adesha_substitute_varnas
# Replace: dh.varnas = list(parse_slp1_upadesha_sequence("vadha"))
adesha_substitute_varnas(dh, "vadha", state, sutra_id="2.4.43",
                         gunadharmas=frozenset({DHATUTVA}))
```

**`sutras/adhyaya_6/pada_4/sutra_6_4_101.py`** — `hi` → `Dhi`/`Qi`:
```python
from engine.sthanivat import TING_PRATYAYATVA, adesha_substitute_varnas
# Both branches:
adesha_substitute_varnas(t, "Di", state, sutra_id="6.4.101",
                         gunadharmas=frozenset({TING_PRATYAYATVA}))
# or:
adesha_substitute_varnas(t, "Qi", state, sutra_id="6.4.101",
                         gunadharmas=frozenset({TING_PRATYAYATVA}))
# Keep t.tags.add("tin_adesha_3_4_78") after — it is an engine-internal tag.
```

Note: `sutras/adhyaya_6/pada_1/sutra_6_1_131.py` uses `left.varnas = [mk("d"), mk("i")]`
as a structural tape truncation (split, not ādeśa) — no change needed; the
`mark_sthanivat_block(u, BLOCK_AL_SAME_SITE)` call already handles it.

### 0.2 Fix Cursor-introduced lakāra reads in cond-helpers

**`sutras/adhyaya_3/pada_1/sutra_3_1_43.py`** — `_cli_insert_index()` reads
`state.meta.get("lakara")`. The correct structural signal is
`state.meta.get("cli_luG_recipe")` which is already the primary gate.
Remove the lakāra read; the cli_luG_recipe check is sufficient.

**`sutras/adhyaya_3/pada_1/sutra_3_1_55.py`** — `_ghas_luG_aG_site()` reads
`state.meta.get("lakara")`. Replace with:
`state.samjna_registry.get("2.4.37_ad_ghas_done")` (set in Phase 0.1 above).
If the `ghas` term is present (`upadesha_slp1 in {"Gas"}`) and cli is present,
luṅ is implied structurally — no coordinate read needed.

### 0.3 Test protocol

```bash
pytest tests/ -x -q                          # all 18,580 pass
pytest tests/constitutional/ -v              # ARM_GATE_BASELINE = 0 remains
pytest tests/unit/test_avaDIt_luN_han.py     # 2.4.43 regression
pytest tests/unit/test_tinanta_ad_lug_kartari.py  # 2.4.37 regression
```

---

## Phase 1 — Universal Tripāḍī Phase
**Duration:** 2–3 sessions  
**Prerequisite:** Phase 0 complete.

### Objective

`engine/phase.py` already defines the three-phase model
(angakarya → sandhi → tripadi). The Tripāḍī rules (8.2.1–8.4.68) are
called piecemeal in tinanta.py via `P00_tripadi_*` canonicals. Extract
this into a proper engine phase module that is universal — identical for
tinanta, subanta, kṛdanta, and taddhita.

### 1.1 Create `engine/phases/tripadi.py`

```python
# engine/phases/tripadi.py
"""
Universal Tripāḍī phase (8.2.1–8.4.68).
Called after _pada_merge() regardless of derivation class.
"""
from engine import apply_rule
from engine.phase import set_phase
from engine.state import State

_TRIPADI_SPINE = [
    "8.2.1",   # asiddha gate + tripadi_zone = True
    "8.2.23",  # saṃyogānta-lopa
    "8.2.29",  # (if applicable)
    "8.2.66",  # ru-ādeśa
    "8.3.15",  # visarga
    "8.3.24",  # anusvāra
    "8.3.59",  # ṣatva (s → ṣ after IK)
    "8.3.60",  # śāsi/vasi/ghasi ṣatva
    "8.4.41",  # (jhal → jaz before śar)
    "8.4.45",  # 
    "8.4.46",  # 
    "8.4.47",  # 
    "8.4.54",  # carc (abhyāsa)
    "8.4.55",  # khari ca (jhal → car before khar)
    "8.4.58",  # anunāsika
    "8.4.62",  # 
    "8.4.63",  # 
    "8.4.65",  # 
    "8.4.66",  # 
    "8.4.68",  # (trace marker)
]

def execute_tripadi_phase(state: State) -> State:
    """
    Apply all Tripāḍī sūtras sequentially.
    The caller is responsible for calling _pada_merge() BEFORE this.
    """
    set_phase(state, "tripadi")
    for sid in _TRIPADI_SPINE:
        state = apply_rule(sid, state)
    return state
```

The exact spine is determined by running `git grep "apply_rule.*8\.[234]"` 
across all pipelines and canonicals to identify every Tripāḍī rule currently
called. The spine is ordered by sūtra number (Aṣṭādhyāyī krama, Art. 3).

### 1.2 Refactor `_pada_merge` into `engine/phases/pada_merger.py`

`_pada_merge()` is currently duplicated across `pipelines/subanta.py` and
`pipelines/tinanta.py`. It is not a sūtra — it is a structural merger
(recording in trace with `__MERGE__` tag). Move it to:

```python
# engine/phases/pada_merger.py
def pada_merge(state: State) -> State:
    """
    Merge multi-term State into a single pada-tagged Term.
    Records the merge in state.trace with __PADA_MERGE__ status.
    Must be called BEFORE execute_tripadi_phase().
    """
```

### 1.3 Update all callers

Replace every `P00_tripadi_*` canonical call and inline `apply_rule("8.2.1", ...)` 
sequence in tinanta.py, subanta.py, krdanta.py with:

```python
from engine.phases.pada_merger import pada_merge
from engine.phases.tripadi import execute_tripadi_phase

# At derivation end:
pada_merge(state)
execute_tripadi_phase(state)
```

This eliminates ~15 unique `P00_tripadi_*` canonical variants and consolidates
all Tripāḍī logic into one auditable module.

### 1.4 Test protocol

```bash
pytest tests/ -q                             # all 18,580 pass
pytest tests/constitutional/test_no_new_duplicates.py  # MAX=0 remains
```

---

## Phase 2 — Telemetry Isolation (Orthogonal Observer)
**Duration:** 1–2 sessions  
**Prerequisite:** Phase 1 (cleaner state flow makes tracing easier).

### Objective

`engine/telemetry.py` already provides a `ContextVar`-based hook. The
dispatcher already calls `notify_apply_rule_end`. The remaining work:

1. Audit all non-dispatcher code that appends directly to `state.trace`.
2. Replace manual trace appends in pipeline structural merges with a
   canonical `state.emit_structural(label, before, after, why)` method.
3. Expand the TraceBuilder to capture structural events separately from
   sūtra events, so downstream tools can distinguish sūtra applications
   from pipeline housekeeping.

### 2.1 Add `State.emit_structural()`

```python
# In engine/state.py
def emit_structural(
    self,
    label: str,       # e.g. "__PADA_MERGE__", "__KRT_MERGE__"
    form_before: str,
    form_after: str,
    why_dev: str,
) -> None:
    """Record a non-sūtra structural step in trace."""
    self.trace.append({
        "sutra_id":    label,
        "sutra_type":  "STRUCTURAL",
        "type_label":  label,
        "form_before": form_before,
        "form_after":  form_after,
        "why_dev":     why_dev,
        "status":      "APPLIED",
    })
```

All `state.trace.append({...})` calls in `pada_merge`, `_krt_merge`,
`_pada_merge` etc. are replaced with `state.emit_structural(...)`.

### 2.2 Expand TraceBuilder

```python
# engine/telemetry.py (addition)
class TraceBuilder:
    """Observer that builds a structured prakriyā from events."""
    def __init__(self):
        self.sutra_steps: list[dict] = []
        self.structural_steps: list[dict] = []
    
    def on_apply_rule(self, from_id, to_id, state):
        """Called by notify_apply_rule_end for every apply_rule() call."""
        if state.trace:
            last = state.trace[-1]
            if last.get("sutra_type") == "STRUCTURAL":
                self.structural_steps.append(last)
            else:
                self.sutra_steps.append(last)
    
    def full_trace(self) -> list[dict]:
        return sorted(
            self.sutra_steps + self.structural_steps,
            key=lambda s: s.get("_seq", 0)
        )
```

### 2.3 Test protocol

Backward replayability (Art. 9) must still pass:
```bash
python tools/replay_trace.py pipelines/tinanta.py derive ada~ liT kartari 3 2
pytest tests/ -q
```

---

## Phase 3 — Vibhāṣā Fork Manager
**Duration:** 2–3 sessions  
**Prerequisite:** Phase 2 complete (clean telemetry makes fork tracing possible).

### Objective

The engine currently has `state.vibhasha_forks` (list), `state.clone()` (deep copy),
and `engine/executors/exec_vibhasha.py`. These are not yet connected to produce
parallel derivation branches. Complete the fork mechanism.

### 3.1 Implement deep-isolated `state.fork()`

`state.clone()` exists but shares list references for complex nested objects.
Verify and strengthen:

```python
# engine/state.py
def fork(self) -> "State":
    """
    Create a parallel derivation branch.
    The fork shares nothing mutable with the original after creation.
    All varṇa tapes, term tags, meta dicts are deep-copied.
    The vibhasha_forks list on both states remains independent.
    """
    import copy
    s = copy.deepcopy(self)
    s.vibhasha_forks = []       # forks don't inherit prior fork list
    s.meta["forked_from"] = id(self)
    return s
```

Write `tests/unit/test_vibhasha_forking.py`:
```python
def test_fork_tape_isolation():
    """Mutation of primary must not leak into fork."""
    s = State(terms=[Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})], ...)
    fork = s.fork()
    s.terms[0].varnas[0] = mk("b")
    assert fork.terms[0].varnas[0].slp1 == "a"   # not "b"

def test_fork_meta_isolation():
    s = State(terms=[], meta={"x": 1}, ...)
    fork = s.fork()
    s.meta["x"] = 99
    assert fork.meta["x"] == 1
```

### 3.2 Complete `exec_vibhasha.py`

```python
# engine/executors/exec_vibhasha.py (completion)
def exec_vibhasha(rec, state: State) -> State:
    """
    VIBHASHA: optional rule. Fork state.
    Primary: applies the rule.
    Fork: skips it (the "na" alternative).
    Both are registered in state.vibhasha_forks for downstream audit.
    """
    fork = state.fork()
    fork.meta[f"{rec.sutra_id}_skipped_vibhasha"] = True
    state.vibhasha_forks.append(fork)
    
    # Apply to primary
    state = rec.act(state)
    state.meta[f"{rec.sutra_id}_applied_vibhasha"] = True
    return state
```

### 3.3 Change `sutra_6_4_38.py` to `SutraType.VIBHASHA`

This is the first concrete use of the fork manager. 6.4.38 is "vā" (optional).
Change its `sutra_type` to `SutraType.VIBHASHA`, remove the arm guard.
Verify both forks (with and without m-lopa) in `tests/unit/test_lyap_vibhasha.py`.

### 3.4 Test protocol

```bash
pytest tests/unit/test_vibhasha_forking.py    # new test
pytest tests/ -q                              # all 18,580+ pass
```

---

## Phase 4 — Autonomous Cyclic Engine Loop + Arm Removal Campaign
**Duration:** 5–8 sessions (the hardest phase)  
**Prerequisite:** Phases 1–3 complete. Arm removal must track alongside this.

### Objective

Replace hardcoded `apply_rule()` scripts with a `while` loop driven by
`engine/scheduler.py` + `engine/resolver.py`. This is only possible when
sutra `cond()` functions are general enough to fire based on pure linguistic
state — not arm flags. The arm removal campaign runs in parallel.

### 4.1 Create `engine/core_loop.py`

```python
# engine/core_loop.py
"""
run_sapadasaptadhyayi(state) — Autonomous derivation loop.

Drives the Sapāda-Saptādhyāyī (adhyāyas 1.1 through 7.4 + 8.1)
phase of derivation. Stops before the Tripāḍī phase (8.2+).

The loop:
  1. Ask scheduler for eligible sūtras.
  2. If zero: convergence — break.
  3. If one: fire it.
  4. If many: resolver picks the winner (SOI/DOI + conflict table).
  5. Repeat.
  
Vibhāṣā rules produce forks (handled by exec_vibhasha).
Max iterations: 500 (safety, raises ConvergenceError if hit).
"""
from __future__ import annotations
from engine.scheduler import enumerate_candidates
from engine.resolver  import resolve
from engine import apply_rule
from engine.state import State

MAX_ITERATIONS = 500

class ConvergenceError(RuntimeError):
    pass

def run_sapadasaptadhyayi(state: State) -> State:
    for _ in range(MAX_ITERATIONS):
        candidates = enumerate_candidates(state)
        if not candidates:
            break
        winner = candidates[0] if len(candidates) == 1 else resolve(candidates, state)
        state = apply_rule(winner, state)
    else:
        raise ConvergenceError(f"No convergence after {MAX_ITERATIONS} iterations")
    return state
```

### 4.2 Arm Removal Campaign (parallel track)

The autonomous loop is useless while 223 arm reads exist — arms are the reason
the loop can't fire rules on its own. Remove them in priority order:

**Batch A — Cursor-introduced (7 files, ~3 sessions):**

| Sūtra | Arm | Replacement |
|-------|-----|-------------|
| 3.1.32 | `P025/kath_3_1_32_arm` | `"prātipadika" in ang.tags and "sanadi" not in ang.tags` |
| 3.4.92 | `3_4_92_loT_uttama_arm` | `upadesha_slp1 in {"ni", "vas", "mas"}` (structural uttama identity) |
| 3.4.92 | `3_4_92_loT_karmani_arm` | `t.meta.get("3_4_93_done")` + final-E check |
| 6.1.70 | `P029_6_1_70_vy_lopa_arm` | Unified done-key `6_1_70_y_before_v_done` |
| 6.4.48 | `kath_6_4_48_arm` | `"prātipadika" in ang.tags and _nic_i_follows(...)` |
| 6.4.48 | `han_6_4_48_arm` | Merge `_han_vadh_site` into default `_site` routing |
| 7.2.103 | `P028_7_2_103_kim_kah_arm` | `upadesha_slp1 == "kim"` + next-sup check (already structural) |
| 7.2.7 | `7_2_7_luN_it_vrddhi_arm` | Remove; `_matches_sic_it` structural check is sufficient |
| 7.2.7 | `7_2_7_anga_vrddhi_arm` | Remove; `_anga_vrddhi_blocked` gate is sufficient |

For each: remove the arm write from the calling pipeline in the same commit.
Run `git grep <arm_key>` to confirm zero references remain.

**Batch B — Highest-count legacy files (~5 sessions):**

Target the 20 files with most arm reads:
7_4_59 (8), 8_4_66 (6), 6_1_198 (4), 6_4_48 (4), 7_4_60 (4), 8_4_55 (4),
3_4_114 (3), 6_1_70 (3), 7_1_28 (3), 2_3_48 (4)...

For each, determine the correct linguistic predicate (upadeśa identity,
saṃjñā registry entry, prior-rule completion flag, phonemic condition)
and replace. The ratchet rule: **each commit touching a sūtra file must
reduce total arm count by ≥1**.

**Batch C — Remaining 130+ files** — tracked as ongoing debt, reduced
session-by-session via the ratchet rule.

### 4.3 `engine/nimitta_predicates.py` — Structural Signal Library

Build a shared module of re-usable linguistic predicates to replace
per-sūtra ad hoc meta reads:

```python
# engine/nimitta_predicates.py
def is_ardhadhatuka_following(state, anga_idx: int) -> bool:
    """True when the term at anga_idx+1 is an ardha-dhātuka pratyaya."""

def is_sarvadhatuka_following(state, anga_idx: int) -> bool:
    """True when the term at anga_idx+1 carries the sārvadhatuka tag."""

def dhatu_upadesha(state, idx: int) -> str | None:
    """Return upadesha_slp1 of the dhātu term at idx, or None."""

def has_it_samjna(state, idx: int, key: str) -> bool:
    """True when the term at idx carries the given it-saṃjñā."""

def is_ngit_tin(state, idx: int) -> bool:
    """True when tiṅ ādeśa at idx is n-git (not k-git, not pit)."""
```

### 4.4 Test Strategy for Phase 4

Do NOT gut the pipelines yet (that is Phase 5). Instead, run both paths
side-by-side:

```python
# tests/unit/test_autonomous_vs_recipe.py
def test_lat_bhu_autonomous_matches_recipe():
    recipe_state  = derive("BU", "laT", "kartari", 3, 1)  # existing recipe
    auto_state    = derive_autonomous("BU", "laT", "kartari", 3, 1)  # new loop
    assert recipe_state.flat_dev() == auto_state.flat_dev()
```

Start with the simplest derivation (BU laT 3.1), then expand coverage.
The autonomous path is correct when it matches all recipe outputs.

### 4.5 Test protocol

```bash
pytest tests/ -q                                    # 18,580+ pass
pytest tests/unit/test_autonomous_vs_recipe.py      # new test
python3 -c "
from engine.scheduler import enumerate_candidates
from engine.state import State
# Verify scheduler finds zero candidates on a fully-derived state
"
```

---

## Phase 5 — Pipeline Thinning
**Duration:** 3–5 sessions  
**Prerequisite:** Phase 4 autonomous loop handles ≥90% of tinanta forms autonomously.

### Objective

Gut `pipelines/tinanta.py` from 4,503 lines to ~200 lines. The pipeline
becomes a pure tape initializer + router.

### 5.1 Extract test fixtures

```python
# tests/fixtures/tinanta_paradigms.py
"""Gold paradigm fixtures used by tinanta tests."""
BHU_LAT_KARTARI_PARASMAI = {
    (3, 1): "भवति",
    (3, 2): "भवतः",
    ...
}
```

Move all `derive_*` wrapper functions from the bottom of tinanta.py here.

### 5.2 Thin `derive()` to a router

```python
# pipelines/tinanta.py (post-Phase-5)
def derive(upadesha, lakara, pada, purusha, vacana) -> State:
    """
    Thin router. Initializes tape, calls autonomous loop + Tripāḍī phase.
    """
    dhatu = _fetch_dhatu(upadesha)          # dhatupatha lookup
    state = _build_initial_state(dhatu, lakara, pada, purusha, vacana)
    state = run_sapadasaptadhyayi(state)    # autonomous loop
    pada_merge(state)                       # structural merger
    state = execute_tripadi_phase(state)   # Tripāḍī phase
    return state
```

Delete all `_derive_laT_*`, `_derive_liT_*`, etc. functions. The
engine loop handles these dynamically.

### 5.3 Handle known autonomous gaps with bridge recipes

During Phase 4, some derivation paths will not yet be fully autonomous
(complex pratyaya selection, liṭ reduplication, etc.). For these, keep
a **bridge recipe** file:

```python
# pipelines/recipes/tinanta_bridges.py
"""
Temporary bridge recipes for derivation paths not yet autonomous.
Each bridge registers a recipe with the core_loop to handle its case.
Remove as the autonomous loop handles each case.
"""
```

This avoids breaking the test suite during the transition.

---

## Phase 6+ — Completeness Roadmap

Once the engine is architecturally sound (Phases 0–5), expand coverage:

| Phase | Scope | Key Sūtras |
|-------|-------|-----------|
| 6 | Complete tiṅanta matrix | All 10 lakāras × 9 cells × parasmai + ātmane + karmani |
| 7 | Kṛdanta universalization | kṛt pratyayas: ktvā, lyap, tumun, ṇamul, śatṛ, śānac, kta, ktavatu... |
| 8 | Subanta universalization | All 8 vibhaktis × 3 vacanas × all stem classes |
| 9 | Samāsa | Dvandva, tatpuruṣa, karmadhāraya, bahuvrīhi, avyayībhāva |
| 10 | Taddhita | Apatya, sāmānya, mātrā taddhitas |
| 11 | Vākyaprakaraṇa | Kārakaviveka, anvaya |
| 12 | Audit Completeness | Kāśikā-verified trace for 1000 canonical forms |

---

## Arm Removal Ratchet Rule

> **Every commit that modifies a sūtra file MUST reduce the total arm count by ≥1.**
> No new arms may be written anywhere in `sutras/`.
> Target: 223 → 0 over the course of Phases 4–6.

Track progress in `audit/RUN_LOG.md` after each session:
```
2026-05-30  arm_count=223  (baseline)
YYYY-MM-DD  arm_count=N    (after session)
```

---

## Sutra Architecture Decision Rules

When implementing or refactoring any sūtra, apply these in order:

1. **Can the condition be expressed as a phonemic predicate?** (varṇa SLP1,
   pratyāhāra membership, upadeśa identity) → Write it. No arm needed.

2. **Can it use a saṃjñā registry entry?** (e.g. `state.samjna_registry.get("2.4.37_ad_ghas_done")`) → Use that. Prefer completion flags over arms.

3. **Can it use an it-saṃjñā or tag?** (kit, Nit, ṇit, pit, apit; dhātu,
   aṅga, pratyaya, pada) → Use that. Tags are structural.

4. **Is it a vibhāṣā (optional) rule?** → `SutraType.VIBHASHA`. Let
   `exec_vibhasha.py` fork the state. No arm.

5. **Would the correct condition require a lakāra/puruṣa/vacana coordinate?** → STOP.
   This is an Art. 2 violation. Find the structural signal instead.
   (Tip: the lakāra coordinate is a proxy for a structural saṃjñā.
   `laṅ` = `anadyatana_bhūta_saṃjñā`, `liṭ` = `parokṣa_saṃjñā`, etc.)

6. **Arms in `act()` are debt, not violations.** They may remain temporarily
   while the proper condition is being developed. But they MUST be removed
   before any derivation path becomes part of the autonomous loop.

---

## Testing Strategy

### Test tiers

| Tier | What it tests | When it runs |
|------|--------------|--------------|
| Constitutional | Art. 2, 11, 13 §1 — no arms in cond, no vibhakti reads, no duplicates | Every commit |
| Unit | Individual sutra cond/act on constructed states | Every commit |
| Pipeline | Full derive() for specific forms (gold comparison) | Every commit |
| Paradigm | All cells of a full paradigm (8×3 subanta, 9-cell tiṅanta) | Pre-merge |
| Autonomous | run_sapadasaptadhyayi() matches recipe output | Phase 4+ |
| Kāśikā | 1000 canonical forms from Kāśikā commentary | Phase 12 |

### Safety invariants

After every session:
```bash
pytest tests/ --tb=short -q        # zero failures
pytest tests/constitutional/ -v    # ARM_GATE_BASELINE=0, MAX_DUPLICATES=0
python tools/replay_trace.py ...   # Art. 9 backward replayability
```

---

## File Map: New Files Created

```
engine/
  phases/
    __init__.py
    tripadi.py          # Phase 1: universal Tripāḍī phase
    pada_merger.py      # Phase 1: universal _pada_merge
  core_loop.py          # Phase 4: autonomous cyclic loop
  nimitta_predicates.py # Phase 4: structural signal library

tests/
  unit/
    test_vibhasha_forking.py     # Phase 3
    test_autonomous_vs_recipe.py # Phase 4
  fixtures/
    tinanta_paradigms.py         # Phase 5

pipelines/
  recipes/
    tinanta_bridges.py           # Phase 5 (temporary, delete when done)

audit/
  arm_inventory.json             # Phase 4: arm removal tracking
```

---

## Success Metrics

| Milestone | Metric |
|-----------|--------|
| Phase 0 done | 3 sthanivat fixes merged; 2 lakāra reads removed; all tests pass |
| Phase 1 done | `engine/phases/tripadi.py` exists; P00_tripadi_* canonicals deleted |
| Phase 2 done | Zero `state.trace.append()` calls outside `state.emit_structural()` |
| Phase 3 done | `test_vibhasha_forking.py` passes; 6.4.38 is VIBHASHA type |
| Phase 4 partial | Autonomous loop derives BU laT/liT/laṅ correctly; arm count < 150 |
| Phase 4 complete | Autonomous loop matches recipe output for all 18,580+ test forms |
| Phase 5 done | tinanta.py < 300 LOC; all pipeline spines deleted |
| Final | arm_count = 0; every form derives autonomously; Kāśikā audit green |

---

*This plan is the working constitution for Pāṇini Engine v4.*  
*Update the metrics table after each session. Ratchet the arm count down.*  
*The engine is done when a Sanskrit scholar can read any trace and nod.*
