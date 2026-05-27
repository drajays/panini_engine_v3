# audit_tinanta_cursor.md — Rule-based tiṅanta prakriyā audit

> **Parent playbooks:** `audit_claude.md` (why), `audit_cursor.md` (subanta/P0–P5),
> `CONSTITUTION.md` (law). **Coordination:** `audit/RUN_LOG.md` §B claims + §C log.
>
> **Scope:** One canonical spine — `pipelines/tinanta.py::derive()` — for all
> tiṅanta (laṭ … lṛṅ) × prayoga (कर्तरि / कर्मणि / भावे) × puruṣa × vacana.
> No parallel `*_corrected_*` production paths. No new `_arm` gates (Art. 13 §1).

---

## 0. Audit principles (non‑negotiable)

| # | Rule | How we verify |
|---|------|----------------|
| R1 | **Glass box** — every surface step is `apply_rule(sutra_id, state)` | Trace has no pipeline string hacks; SIG edges match sūtra ids |
| R2 | **Mechanical blindness** — `cond()` never reads puruṣa/vacana/gold | `tests/constitutional/test_no_purusha_vacana_in_morphological_ops.py` |
| R3 | **No demo arms in sūtras** — no `P0NN` / `corrected_v2` in `sutras/` | `tests/constitutional/test_no_demo_ids_in_sutra_arm_keys.py` |
| R4 | **Arms are debt** — pipeline `_arm` writes trend to **zero**; net-add forbidden | `grep '_arm"' pipelines/tinanta.py` count tracked weekly |
| R5 | **One spine** — corrected demos merge into `tinanta.py`, then delete demo file | `ls pipelines/*corrected*P0{08..19}*` → 0 |
| R6 | **Sources** — every touched sūtra file gets Art. 14 docstring block | Manual + CI docstring linter (future) |
| R7 | **Oracles are surface-only** — Vidyut / Saṃsādhanī compare output, never copy logic | Document oracle row in test, not in `cond()` |

**Baseline dhātus for matrices (fixed set):**

| SLP1 | Role | Gaṇa | Why |
|------|------|------|-----|
| `BU` | अकर्मक भ्वादि | 1 | Kartari/bhave reference (भवति …) |
| `paci~` | सकर्मक पच् | 1 | Karmaṇi yaḳ spine (dhātupātha upadeśa) |
| `kfvi~` | कृ / क्रि | 8 | Ten-lakāra variety (कुरुते …) |
| `vftu~` | वृत् | 1 | P019 lṛṅ gold — **T3** merge pending |
| `paW` | गति | 1 | Optional; not in upadesha JSON yet |

---

## 1. Phase map (T0–T7)

```
T0 Inventory ──► T1 Coverage matrix ──► T2 Constitutional gates
       │                    │                      │
       └────────────────────┴──────────────────────┤
                                                    ▼
              T7 Web/API ◄── T6 Oracles ◄── T5 Sūtra order ◄── T4 Prayoga depth
                                                    ▲
              T3 P4 merge (P008–P019 demos) ─────────┘
```

| Phase | Goal | Primary files | Est. |
|-------|------|---------------|------|
| **T0** | Baseline counts, arm inventory, prayoga×lakāra dispatch table | `tinanta.py`, `.audit/tinanta_*` | ½ day |
| **T1** | Automated **coverage matrix** (pass/error/NI) | `tests/unit/test_tinanta_matrix_*.py` | 1 day |
| **T2** | Constitutional compliance on tiṅanta path | `tests/constitutional/`, `sutras/` touched by tinanta | 1 day |
| **T3** | Merge **tiṅanta corrected demos** (P008–P019) into canonical spine | `tinanta.py`, delete `*_corrected_P0{08..19}*` | 3–5 days |
| **T4** | **Prayoga** depth: bhāve/karmaṇi 10×9 gold; gaṇa expansion | `tinanta.py`, `tests/unit/` | 1–2 weeks |
| **T5** | Per-lakāra **sūtra-order** audit vs Kāśikā (not Kaumudī order) | `tinanta.py`, `sutras/adhyaya_3/**`, SIG | ongoing |
| **T6** | Oracle spot-check (5–10% matrix cells) | tests only + notes | ½ day / sprint |
| **T7** | Web UI: prayoga on dhātu browser, trace parity | `dhatufilters.html`, `prakriya_tinanta.html` | 1 day |

**Coordination with Claude (subanta track):**

| Do **not** overlap (Claude §B claim) | Tiṅanta audit **owns** |
|--------------------------------------|-------------------------|
| `webui/static/trace.js`, subanta templates | `pipelines/tinanta.py`, tiṅanta templates, `prakriya_tinanta.html`, `dhatufilters.html` |
| `P01_subanta_bootstrap` body refactor | `P01_samjna_dhatu_class` (already wired) |
| sūtras 1.1.11–1.1.24 subanta cluster | sūtras fired **from** tinanta spines (3.x, 6.x, 7.x, 8.x) when migrating arms |

Shared: `core/canonical_pipelines.py` — **coordinate in §C** before editing blocks used by both.

---

## 2. T0 — Inventory (run once per sprint)

### 2.1 Snapshot tests

```bash
mkdir -p .audit
pytest tests/unit/test_tinanta_*.py -q 2>&1 | tee .audit/tinanta_unit_baseline.txt
python3 -m pytest tests/unit/test_corrected_prakriyas_v2_bundle.py -q \
  -k "P008 or P009 or P010 or P011 or P012 or P013 or P014 or P015 or P016 or P017 or P018 or P019" \
  2>&1 | tee .audit/tinanta_corrected_demo_baseline.txt
```

### 2.2 Arm debt counter

```bash
grep -c '_arm"' pipelines/tinanta.py | tee .audit/tinanta_arm_write_count.txt
grep -oE 'state\.meta\["[^"]*_arm"\]' pipelines/tinanta.py | sort -u > .audit/tinanta_arm_keys.txt
wc -l .audit/tinanta_arm_keys.txt
```

**Current baseline (2026-05-22):** ~134 `_arm` writes in `tinanta.py`; includes
`P031_3_4_87_sip_to_hi_arm` (demo-id — **priority delete**).

### 2.3 Dispatch coverage table (manual seed)

Fill after running matrix script (T1):

| prayoga | laT | liT | luT | lRT | loT | laG | liG | AsIrliG | luG | lRG |
|---------|-----|-----|-----|-----|-----|-----|-----|---------|-----|-----|
| kartari (gaṇa 1) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| karmani | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| bhave | ✓ | ✓ | ? | ? | ? | ? | ? | ? | ✓ | ✓ |

Legend: ✓ = 9 cells derive without `NotImplementedError`; ? = needs gold;
✗ = missing spine.

---

## 3. T1 — Coverage matrix (automated)

**Add:** `tests/unit/test_tinanta_coverage_matrix.py`

```python
# Pseudocode — implement in repo
DHATU_SMOKE = ["BU", "pac", "kf"]
LAKARAS = ["laT","liT","luT","lRT","loT","laG","liG","AsIrliG","luG","lRG"]
PRAYOGAS = ["kartari", "karmani", "bhave"]
PURUSHA = [3, 2, 1]
VACANA = [1, 2, 3]

for dhatu, prayoga, lakara, p, v in product(...):
    try:
        s = derive(dhatu, lakara, prayoga, p, v)
        record("OK", s.flat_dev())
    except NotImplementedError as e:
        record("NI", str(e))
    except Exception as e:
        record("ERR", type(e).__name__)
```

**Acceptance:** CSV/JSON artifact under `.audit/tinanta_matrix_YYYY-MM-DD.json`;
no regressions on previously `OK` cells.

**Priority gold cells (add `tests/unit/test_tinanta_gold_*.py`):**

1. भू × 10 lakāras × kartari — 3sg only (extend `test_tinanta_bhu_ten_lakara_kartari.py`).
2. भू × laT/liT × bhave — 9 cells (`test_tinanta_bhave_lat.py` extended).
3. pac × laT × karmani — 9 cells (क्रियते …).
4. Each P008–P019 demo surface = one regression test **before** merge (T3).

---

## 4. T2 — Constitutional gates

Run every tiṅanta session:

```bash
pytest tests/constitutional/ -q
pytest tests/constitutional/test_no_purusha_vacana_in_morphological_ops.py -v
```

**Tiṅanta-specific grep audits:**

```bash
# Demo ids inside tinanta pipeline
grep -n 'P0[0-9][0-9]_\|corrected_v2' pipelines/tinanta.py

# Surface/gold reads in sutras used by tinanta (sample)
grep -rln 'data/reference\|flat_dev\|gold' sutras/adhyaya_3/ sutras/adhyaya_7/
```

**Sūtra arms gated only on `state.meta[*_arm]` along tinanta spine** — migrate per
`audit_cursor.md` §5.3 (same template as 6.1.97). Priority order for tinanta:

1. `3_1_68_kartari_recipe` — replace with Term tags (`vikarana`, `kartari_laT_ready`).
2. `tin_adesha_pending` / `tin_adesha_slp1` — structural tiṅ ādeśa state (meta OK if not `_arm`).
3. Lakāra-specific arms (`3_3_162_loT_arm`, `3_2_110_luG_arm`, …) — **one lakāra per PR**.
4. Delete `P031_*` demo arms.

---

## 5. T3 — P4 tinānta batch: merge corrected demos (P008–P019)

**Source of truth for gold surfaces:**
`data/reference/corrected_prakriyas_v2/prakriyas_corrected_v2.json`

| ID | Pipeline file | Lakāra / note | Merge target |
|----|---------------|---------------|--------------|
| P008 | `Aste_lat_Ada_corrected_P008_demo.py` | laṭ, आद् | `_derive_laT` / ada spine |
| P009 | (bundle only) | — | locate in JSON, map to spine |
| P010 | `Ayacchate_lat_yam_corrected_P010_demo.py` | laṭ, yam | laṭ + ātmanepada |
| P011 | `utkurute_*`, `upaskurute_*` | laṭ, upasarga | `derive(..., upasargas=)` |
| P012 | `apajAnIte_lat_apa_jYA_corrected_P012_demo.py` | laṭ, apa | upasarga + laṭ |
| P013 | `zuSrUzate_san_Sru_corrected_P013_demo.py` | laṭ, san | san/śru spine in laṭ |
| P014 | `IkzAYcakre_lit_Ikz_kf_corrected_P014_demo.py` | liṭ | `_derive_lit` |
| P015 | `pAyayate_pa_Nic_corrected_P015_demo.py` | laṭ, ṇic | causative spine |
| P016 | `lohitAyati_lat_lohita_kyaz_corrected_P016_demo.py` | laṭ | denominative |
| P017 | `pawapawAyati_anukaraNa_corrected_P017_demo.py` | laṭ, āmreḍita | 6.1.1 + 6.1.97 (done) |
| P018 | `vyadyutat_*`, `vyadyotizwa_*` | luṅ | `_derive_luG` |
| P019 | `avartsyat_lRG_vf_corrected_P019_demo.py` | lṛṅ | `_derive_lRG` |

**Per-demo procedure (same as `audit_cursor.md` §6.2):**

1. `diff` demo vs relevant `_derive_*` section in `tinanta.py`.
2. If demo adds missing `apply_rule` calls → insert into canonical spine in **Aṣṭādhyāyī order**.
3. If demo only adds `_arm` → fix **sūtra** `cond()` (T2), then merge spine.
4. Port test from `test_corrected_prakriyas_v2_bundle.py` to `test_tinanta_gold_<name>.py`.
5. Delete demo pipeline; remove from `webui/app.py` / streamlit selectors.
6. §C log + §B release.

**Batch order (lowest risk first):** P019 → P008 → P010 → P012 → P014 → P018 → P015 → P016 → P011 → P013 (san is heavy).

---

## 6. T4 — Prayoga & gaṇa depth

### 6.1 Bhāve (भावे)

- **Done:** laṭ/liṭ dispatch, lṛṅ karmaṇi-style; smoke tests.
- **Todo:** 9×10 gold table for `BU` bhave; dedicated spines for loṭ / āśīr-liṅ if
  karmaṇi clone is wrong (audit trace for भवतु, भूयात्).
- **Rule check:** 3.4.69 → ātmanepada only; no karmaṇi yaḵ — verify `cond()` on
  3.1.66/3.1.68 use Term tags, not `prayoga` meta inside sūtras.

### 6.2 Karmaṇi (कर्मणि)

- **Done:** all 10 lakāras dispatched in `derive()`.
- **Todo:** pac (or `kf`) 9×10 gold; verify yaḳ + ātmanepada tin after lopa per cell.

### 6.3 Kartari other gaṇas

- `_derive_laT` tail: gaṇa ≠ 1 raises `NotImplementedError` — track per-gaṇa
  spines as separate T4 epics (2nd gaṇa, 8th gaṇa, …).

---

## 7. T5 — Sūtra-order audit (per lakāra)

For each `_derive_<lakara>()`:

1. Export trace sutra-id list for BU 3sg kartari.
2. Compare to Kāśikā prakriyā on [ashtadhyayi.com](https://ashtadhyayi.com) (human step).
3. Flag **order inversions** (esp. tripāḍī: 8.2.x before 3.4.77 re-fire).
4. Optional: `make sig-snapshot` diff — fewer spurious 1.1.x edges after subanta split.

**Already audited in engine:** laṭ kartari bhvādi (spec steps in `derive()` comments);
extend comments to other lakāras as they are gold-certified.

---

## 8. T6 — Oracle cross-validation (surface only)

- Sample 5% of T1 matrix `OK` cells.
- Compare Devanāgarī to [Vidyullekha](https://ambuda-org.github.io/vidyullekha/) or
  Saṃsādhanī tinanta analyzer.
- Mismatch protocol: file `tests/regression/test_tinanta_oracle_<dhatu>_<lakara>.py`
  with `pytest.mark.xfail` until sūtra fix lands — **never** patch surface in pipeline.

---

## 9. T7 — Web UI & API

| Item | Status | Task |
|------|--------|------|
| Dhātu browser + full trace on click | ✓ shipped | — |
| Prayoga toggle on paradigm grid | todo | kartari / karmani / bhave → `/api/tinanta/all_lakara` |
| Deep link `/prakriya/tinanta?...` | ✓ | extend query params for prayoga |
| Default RUPA filter on tiṅanta pages | ✓ | keep parity if `trace.js` changes (Claude P0) |

---

## 10. Session workflow (Cursor / Claude)

1. Read `audit/RUN_LOG.md` §B + §C.
2. Pick phase Tn; add §B row: `cursor | Tn <name> | <files> | in-progress`.
3. Execute acceptance tests for that phase only.
4. Append §C (what / why / tests / next).
5. Set claim `released`.

**Commit message format:** `audit T3: merge P019 lṛṅ spine into tinanta.py`

---

## 11. Immediate next actions (Cursor plan — no user input required)

| Order | Action | §B claim files |
|-------|--------|----------------|
| 1 | Add `tests/unit/test_tinanta_coverage_matrix.py` (T1) | `tests/unit/test_tinanta_coverage_matrix.py` |
| 2 | T3 start: merge **P019** (`avartsyat_lRG`) — smallest lṛṅ gold | `tinanta.py`, `pipelines/avartsyat_*` |
| 3 | T3: **P008** `Aste` laṭ | same pattern |
| 4 | T4: extend bhāve 9-cell gold for laṭ + liṭ | `tests/unit/test_tinanta_bhave_*.py` |
| 5 | T2: remove `P031_3_4_87_sip_to_hi_arm` from `tinanta.py` + fix 3.4.87 `cond` | `tinanta.py`, `sutras/.../sutra_3_4_87.py` |

**Defer until Claude releases `canonical_pipelines.py`:** luk arms (P3 group 2) affecting
shared preflight — unless tinanta-only arm.

---

## 12. Done criteria (entire tiṅanta audit)

- [ ] T1 matrix: kartari × 6 dhātus × 10 lakāras × 9 cells ≥ 95% `OK` for bhvādi set.
- [ ] T1 matrix: karmani + bhave ≥ 90% `OK` on `BU` + `pac`.
- [ ] T3: zero `pipelines/*corrected_P0{08..19}*_demo.py`.
- [ ] T2: `tinanta.py` `_arm` writes reduced by ≥ 80% vs T0 baseline.
- [ ] T2: zero `P0NN` strings in `pipelines/tinanta.py`.
- [ ] T4: regression files for each prayoga × reference dhātu (minimum 3 gold cells per lakāra).
- [ ] T6: oracle spot-check log in `.audit/tinanta_oracle_notes.md`.
- [ ] T7: dhātu browser supports prayoga filter + full prakriyā for all three.

When all boxes checked, add §C entry: **「Tiṅanta audit complete」** and archive
`.audit/tinanta_matrix_*` to release tag.
