# audit/CURSOR_GUARD.md — Cursor hard limits (read before every session)

> **Purpose:** Prevent cursor from shipping changes that break existing tests or
> violate architectural invariants. Each rule below records a real regression
> from a previous cursor session and the structural constraint that prevents it.
> Cursor MUST verify each relevant constraint before committing.

---

## 1. Engine file prohibitions

### 1.1 No hardcoded sūtra IDs in `engine/` except allowlisted files

The auditor at `audit/pipeline_auditor.py` + `tests/unit/test_audit_pipeline_auditor.py`
checks for bare sūtra-ID string literals (matching `^\d+\.\d+\.\d+$`) in `engine/`.

**Currently allowlisted** (see `_ENGINE_LITERAL_SUTRA_ID_ALLOW` in both files):

| File | Allowed IDs | Reason |
|------|-------------|--------|
| `executors/exec_vidhi.py` | `1.3.9` | vacuous it-lopa hook |
| `stubs.py` | `0.0.0` | stub target |
| `adhikara_automation.py` | `1.3.1`, `1.3.9`, `3.1.1`, `3.4.117`, `6.4.1`, `6.4.148` | adhikāra range markers |
| `core_loop.py` | `1.3.28`, `1.3.12`, `1.3.78` | pre-phase it-saṃjñā spine |

**Rule:** If you add `apply_rule("X.Y.Z", …)` calls to a NEW engine file, ALSO add
an allowlist entry in BOTH `audit/pipeline_auditor.py` AND
`tests/unit/test_prakriya_integrity.py`. Otherwise CI fails.

**Verify:** `python3 -m pytest tests/unit/test_audit_pipeline_auditor.py tests/unit/test_prakriya_integrity.py -q`

---

## 2. `engine/subanta_eligibility.py` — `_tinanta_spine_active`

**Invariant:** `_tinanta_spine_active(state)` MUST return `True` when
`state.meta.get("lakara")` is one of the 10 lakāras (or `AsIrliG`).

**Why:** Split-prakriyā pipelines (`pipelines/aBavatAm_split_prakriyas.py`,
`pipelines/akurvAtAm_laG_tanadi_kf.py`, and others) create their own `State`
without `derivation_class: "tinanta"` and without `_derivation` tags, but DO
set `state.meta["lakara"]`. Without this, `tinanta_lakara_placeholder_eligible`
returns False, blocking 3.2.111 and similar lakāra-placeholder rules.

**Current implementation (do not remove the `_LAKARA_VALUES` branch):**
```python
_LAKARA_VALUES = frozenset({
    "laT", "liT", "luT", "lRT", "loT", "liG", "luG", "lRG", "laG", "lRN", "AsIrliG",
})

def _tinanta_spine_active(state: State) -> bool:
    if _derivation_class(state) == "tinanta":
        return True
    if state.meta.get("lakara") in _LAKARA_VALUES:   # ← must stay
        return True
    return any(tag.endswith("_derivation") for t in state.terms for tag in t.tags)
```

**Verify:** `python3 -m pytest tests/unit/test_aBavatAm_split_prakriyas.py tests/unit/test_akurvAtAm_laG_tanadi_kf.py -q`

---

## 3. `sutras/adhyaya_8/pada_2/sutra_8_2_29.py` — pre-merge recipe bypass

**Invariant:** 8.2.29's `cond()` MUST return `True` (independently of tripadi zone)
when `state.meta.get("ashir_8_2_29_recipe")` or `state.meta.get("liG_ad_8_2_29_suw_recipe")` is set.

**Why:** `_derive_ashir_liG` in `pipelines/tinanta.py` calls 8.2.29 PRE-merge
(before `execute_tripadi_phase`). The tripadi zone has not opened yet. If the
recipe bypass is removed, 4 of the 9 āśīr-liṅ cells produce an extra `स्`
(e.g., `भूयास्स्त्` instead of `भूयात्`).

**Current guard (do not remove):**
```python
def cond(state: State) -> bool:
    if state.meta.get("ashir_8_2_29_recipe") or state.meta.get("liG_ad_8_2_29_suw_recipe"):
        return bool(state.terms)
    return tripadi_gate_eligible(state, "8.2.29", gate_key=_GATE_KEY)
```

**Verify:** `python3 -m pytest tests/unit/test_tinanta_bhuyat_ashirling.py tests/unit/test_tinanta_pathati_lat.py -q`

---

## 4. `sutras/adhyaya_1/pada_1/sutra_1_1_18.py` — no longer bootstraps on bare state

**New behavior (cursor's correct change):** 1.1.18 fires ONLY when a term ending
in `u` is followed by an *iti* term (`i-t-i`). The old "bootstrap" (firing on any
state to set its gate) was removed.

**Consequence:** The `test_gate_idempotent` test was updated to use a `u+iti`
context. The sig_applied_paths_baseline was regenerated WITHOUT 1.1.18 in subanta
paths (which is linguistically correct — rāma-pullinga has no u+iti).

**Do NOT restore the old bootstrap:** restoring `return GATE_KEY not in state.paribhasha_gates`
would re-introduce 1.1.18 as a false positive on the bare-BU probe, breaking the
raw FP=0 ratchet.

**Verify:** `python3 -m pytest tests/unit/test_sutra_1_1_18_Um.py tests/regression/test_sig_baseline.py tests/regression/test_sig_sequence_groups.py -q`

---

## 5. Regression baseline files — freeze protocol

Three frozen files must stay consistent with the engine's actual derivation paths:

| File | What it locks | How to update |
|------|--------------|---------------|
| `tests/regression/sig_applied_paths_baseline.json` | sūtra path for each rāma-pullinga cell | Re-run `python3 tools/regenerate_sig_artifacts.py` or the inline script in §C of RUN_LOG |
| `tests/regression/sig_sequence_groups_baseline.json` | contiguous sūtra subsequences in subanta | Edit JSON directly; remove/add sequences |
| `audit/cond_discipline_auditor.py` ratchet | raw/filtered VIDHI FP counts | `python3 audit/cond_discipline_auditor.py --status` then update `_BASELINE` dict |

**Rule:** If you change a `cond()` that was part of the rāma-pullinga path,
run `tests/regression/test_sig_baseline.py` before committing. If it fails, either
restore the path or regenerate the baseline AND justify in `audit/RUN_LOG.md §C`.

---

## 6. BU-probe FP ratchet — must not regress

The cond discipline auditor baseline is ratcheted. You may NOT merge a change that
raises the raw VIDHI FP count on the BU probe above the current frozen value.

Check: `python3 audit/cond_discipline_auditor.py --status`

If a VIDHI cond migration causes FP to rise, the migration is incomplete — fix the
`cond()` before committing.

---

## 7. `pipelines/tinanta.py` `derive()` — `derivation_class` required

The `State` built at the top of `derive()` MUST include:
```python
meta={"prayoga": prayoga, "derivation_class": "tinanta"}
```

Without `"derivation_class": "tinanta"`, `_tinanta_spine_active()` returns False
for the BU-probe tape, causing `tinanta_lakara_placeholder_eligible` and
`tin_pratyaya_gate_eligible` to reject most tinanta rules.

**Verify:** `python3 -m pytest tests/unit/test_tinanta_bhuyat_ashirling.py -q`

---

## 8. Shared-file coordination (see also §I of RUN_LOG.md)

Files that both agents touch — always check §B before editing:

| File | Rules |
|------|-------|
| `engine/scheduler.py` | Do NOT revert phase pools or pratipadika gate (cursor); do NOT revert type/tripadi filters (claude) |
| `engine/phase.py` | cursor owns; claude: read before any transition change |
| `engine/core_loop.py` | cursor owns |
| `engine/subanta_eligibility.py` | cursor owns; claude may add `_tinanta_spine_active` fallbacks but must keep `_LAKARA_VALUES` branch |
| `sutras/adhyaya_3/**` | cursor owns batch krt_eligibility migration; do NOT add `any(dhatu)` stubs back |
| `tests/regression/sig_applied_paths_baseline.json` | regenerate if path changes; always justify in RUN_LOG |

---

## CI gate — run before every commit

```bash
python3 -m pytest \
  tests/unit/test_audit_pipeline_auditor.py \
  tests/unit/test_prakriya_integrity.py \
  tests/unit/test_sutra_1_1_18_Um.py \
  tests/regression/test_sig_baseline.py \
  tests/regression/test_sig_sequence_groups.py \
  tests/constitutional/test_vidhi_cond_discipline.py \
  tests/unit/test_tinanta_bhuyat_ashirling.py \
  tests/unit/test_aBavatAm_split_prakriyas.py \
  tests/unit/test_akurvAtAm_laG_tanadi_kf.py \
  -q
```

All must pass (or be pre-existing xfail). 0 unexpected failures = safe to commit.
