# Handover — LK case gate rulings (cursor, 2026-11-14)

For the agent that picks this up. Law: `CONSTITUTION.md`. Entry point: `AGENTS.md`. The rulings and their reasoning are in
`audit/LK_GATE_RULINGS_2026-11-14.md`; this file covers state, files and next steps.

## 0. Read first: what state the work is in

- **Nothing is committed.** All the work is uncommitted changes on the owner's machine, on top of commit `3c03d3ab`
  (38 paths in `git status`). A cloud agent cloning the remote **will not see any of it** until the owner commits and
  pushes. If the files listed in §3 are missing, stop and ask the owner to push.
- **The brain is local only.** The brain rulings R-012, R-013 and R-014 were written to
  `~/data-master/ashtadhyayi-ai/rulings/` and are not committed in that repo either. `tests/constitutional/test_brain_rulings_mirror.py`
  skips when the brain is absent, so a cloud machine without it will not check the SC-008..010 mirror.
- **Full suite, aborted.** The full suite plus the firing-ledger rebuild
  (`LK=1 .venv/bin/python -m tools.firing_coverage -n8 -p no:cacheprovider --durations=25`) was **stopped by the owner at
  99%**:
  - Before the stop, **2 failures** showed up; which tests they were is unknown.
  - At the stop, 3 workers went down, giving 3 more F marks that are not real failures.
  - No summary was printed and **no new ledger was written**: `sig/firing_coverage.json` is still dated 2026-11-12.
  - Rerun it, or run the test files touched by the change (§5), to find the 2 failures.
- **Claims released for handoff.** cursor's seven claims are released (`make claims` shows none). Claim your own scope
  before editing: `AGENT=claude make claim ID=… SCOPE="…"`.

## 1. The four rulings, in short (the owner's questions)

| Question | Ruling | Where it is implemented |
|---|---|---|
| Q1: right form, sūtra not fired | The trace is required (Art. 0, 16). It is never a pass, never "redundant". It is reported as the FAIL sub-kind `not_fired`. | `tools/lk_cases.py` (`sub_kind`, `summary`) |
| Q2: the three owner cases | None is a conflict with the Kāśikā; all three were mistyped fixtures. | brain R-012/013/014 → `docs/SOURCE_CONFLICTS.md` SC-008/009/010; fixtures a7/a8 |
| Q3: counts | The LK grade **replaces the "named in tests ≥5×" proxy**, not the ledger. An LK FAIL caps a sūtra at working. Invoked/moved still come only from `sig/firing_coverage.json`. | `tools/sutra_class.py`, `tests/regression/test_lk_cases.py`, `make coverage` (LK=1) |
| Q4: schema | Yes, through the builder only (each value must occur in a sūtra's samagra) | `tools/build_vivaksha_schema.py` → `data/inputs/vivaksha_schema.json` |

## 2. Gate numbers

Run `python3 -m tools.lk_cases summary` or `make lk`. Never quote these from prose.

| | at `3c03d3ab` | now |
|---|---|---|
| confident | 11 | 13 (+4.1.63, +8.4.62) |
| working | 30 | 33 (+8.4.14, +8.4.15, +8.4.63) |
| FAIL | 131 | 122 |
| NO_POSITIVE | 0 | 4 (2.4.62, 4.1.172, 4.3.82, 7.2.98: their positives were mis-assigned and recast as negatives) |
| UNRUNNABLE | 76 | 76 |

FAIL sub-kinds: engine_error 0 (was 6), not_fired 22 (was 29), mismatch 106.

## 3. Files changed

**Brain (outside the repo):** `rulings/R-012.json`, `R-013.json`, `R-014.json`.

**Rulings and documentation**
- `docs/SOURCE_CONFLICTS.md`: SC-008 (7.1.74), SC-009 (7.3.69), SC-010 (8.4.62).
- `audit/LK_GATE_RULINGS_2026-11-14.md`: the full record.
- `audit/RUN_LOG.md`: the §C entry for 2026-11-14 20:40.
- `handover.md`: the session block.
- This file.

**Schema**
- `tools/build_vivaksha_schema.py`:
  - `taddhitArtha`: `BAva` ["BAvaH"] and `karman` ["karmaRi"].
  - `arthaViSeSa`: `Bakzya` ["Bakzye"].
  - `arthaViSeSa` `applies_to` now also lists `krdanta`.
- `data/inputs/vivaksha_schema.json` is regenerated from the builder. Never hand-edit it.
- `sutras/adhyaya_5/pada_1/sutra_5_1_130.py`: samagra `karmaci` → `karmaRi` (upstream row 51130 has कर्मणि).

**Gate and harness**
- `tools/lk_cases.py`:
  - `sub_kind()` and the `sub` field on each failing case.
  - A `summary` subcommand.
  - `check(..., mutate=False)` for speed.
  - `_mutate` now calls `run.__wrapped__`. Before, it read the lru-cached unmutated run, so every old "redundant" or
    "indeterminate" verdict was wrong.
  - A negative of kind `produced` must now actually be produced.
- `tools/exercise_audit.py`: a kṛdanta case that states a sense the harness never varies (for example `arthaViSeSa`) runs
  with its own vivakṣā (`_HARNESS_KEYS`, `_own_sense`).
- `tests/regression/test_lk_cases.py` (new):
  - Always: the verdicts match the fixtures and `grade()`.
  - With `LK=1`: the grade of every confident or working sūtra may not fall.
- `tools/sutra_class.py`: an `lk_grade` field; LK confident replaces the mention proxy; an LK FAIL demotes; both dates are
  shown in the header of `docs/CONFIDENT_SUTRAS.md`.
- `tools/status.py`: warns when the ledger is older than the LK verdicts.
- `Makefile`:
  - `coverage` runs `LK=1 $(PYTHON) -m tools.firing_coverage -n8 -p no:cacheprovider`.
  - New target `lk`.
- `sig/lk_case_verdicts/a2,a4,a5,a7,a8.json`: rerun.
- `sig/sutra_class.json` and `docs/CONFIDENT_SUTRAS.md`: regenerated, but against the **old** ledger (2026-11-12). Rerun
  `make confident` once the new ledger exists.

**Fixtures** (`tests/fixtures/lk_cases/`)
- a7 7.1.74 (R-012):
  - Positives: grAmaRyA, grAmaRye, Sucaye.
  - Declined: grAmaRinA, Sucine.
  - Produced: daDnA, vAriRA.
  - Recorded but not runnable: dadhīca, pIlune.
- a7 7.3.69 (R-013):
  - Positives: BojyaH, BojyA, Bojyam, all with Bakzya.
  - BogyaH without Bakzya is a `produced` negative; BogyaH with Bakzya is an `excluded` negative.
- a8 8.4.62 (R-014):
  - A hasati pair and a hariH pair, each with its declined reading.
  - Also agnicidDasati, trizwubBasati, and the produced negative prAN hasati.
- Triage recasts (`kind: produced`, each citing the Kāśikā):
  - a4: 4.1.63 kzatriyA, 4.1.172, 4.3.82.
  - a2: 2.4.62.
  - a7: 7.2.98 cases 0–4, plus the unrunnable positives tvadIyaH and matputraH.
- The one-off scripts that made these edits are `scratch/apply_lk_rulings.py` and `scratch/apply_lk_triage.py`. `scratch/`
  is untracked.

**Engine**
- `sutras/adhyaya_8/pada_4/sutra_8_4_62.py`: real VIBHASHA (default False). h after a jhay → the 4th of that varga.
- `sutra_8_4_63.py`: real VIBHASHA. A pada-initial ś after a pada-final jhay, before aṭ → ch.
- `sutra_8_4_60.py`: real. t-varga before l → l; n → l tagged `anunasika`.
- `sutra_8_4_55.py`: `_JHAL_CAR` now includes c-varga (J/j/C → c). ścutva makes a c-varga stop after 8.2.30 has run, so
  अग्निचिद्+शेते now gives अग्निचिच्छेते.
- `sutra_8_4_14.py`, `8_4_15.py`, `8_4_16.py`: real rules (ṇopadeśa dhātu; hinu/mīnā; loṭ āni) that read the upasarga
  nimitta.
- `sutra_8_4_2.py`: stops at the upasarga | dhātu seam when the n is `dhatu_v` or `pratyaya_start_v`.
- `engine/natva.py` (new): shared readers (`flat`, `upasarga_nimitta_before`, `dhatu_upadesha`).
- `engine/phases/pada_merger.py`: an upasarga Term's varṇas get `upasarga_v`.
- `core/phases/tripadi.py` (the spine): 8.4.14/15/16 added after 8.4.2; 8.4.60, 8.4.62, 8.4.63 added after 8.4.58.

## 4. Open items, in priority order

1. **The 2 unknown failures** in the full suite. Find and fix them before committing. Suspects are anything that crosses an
   upasarga seam (the 8.4.2 change) or a c-varga stop before khar (the 8.4.55 change).
2. **Ledger, then counts:** `make coverage` (about 1 h or more at -n8), then `make confident`, then `make status`.
   Report the change in the confident count honestly; demotions are expected.
3. **Coordinator only (hotspot `pipelines/tinanta.py`):**
   - The loṭ route runs a short tripādī list without the 8.4 ṇatva rules, so परियाणि (8.4.16) fails.
   - The san route needs 1.2.8, 6.1.16, 7.2.12, 7.4.62 and 8.2.31/37/41 to give जिघृक्षति.
4. **Owner decision:** the 8.4.60 fixture expects `BavAMllunAti` (anusvāra). The Kāśikā has भवाँल्लुनाति (anunāsika), and
   Art. 4 §2 forbids merging the two. The engine also has no SLP1 surface for an anunāsika consonant.
5. **not_fired, still open**:
   - Bucket A (a rival rule or route makes the form): 2.1.14, 3.2.112, 3.3.103, 3.3.156, 4.1.168, 4.2.38, 4.2.107, 4.4.41,
     7.2.56, 7.3.69 (7.3.52 is built for Gurac only), 8.3.26, 7.1.74.
   - Bucket B (no form change by nature; the rule must still leave its own trace row via `apply_rule`): 1.1.59, 1.3.15,
     1.4.8, 3.4.70, 4.1.58, 4.1.93, 4.1.94, 4.2.7, 8.4.43, 8.4.49.
   - Do **not** widen `OK_STATUS` to make bucket B pass.
6. **Samāsa cluster (2.1/2.2):**
   - No samāsa-vidhāyaka fires for, for example, पञ्चन्+नदी: 2.1.20 is a stub and the spec carries no samāhāra sense.
   - So there is no saṃjñā, 2.4.71 never applies, and the output is `paYcannadIs`.
   - Each vidhāyaka needs a real cond and its vivakṣā.
7. **8.3 cluster:**
   - 8.3.23 is not in the tripādī spine and only sees an upasarga Term or a single pada. Its single-pada branch is really
     8.3.24's case.
   - 8.3.5, 8.3.6, 8.3.10 and 8.3.12 are stubs.
8. **Gate stubs that still need real rules:** 5.1.119 ff. (tva/tal never attach), 7.1.74 (the engine has no
   bhāṣitapuṃska stem fact; this is an Art. 18 gap) and 7.3.69.

## 5. How to verify

```bash
python3 -m tools.lk_cases summary                      # grades + FAIL sub-kinds
python3 -m tools.lk_cases run 8.4.14 8.4.62 7.3.69     # rerun some sūtras (writes only those adhyāyas' verdict files)
python3 -m pytest -q tests/regression/test_lk_cases.py tests/constitutional/test_brain_rulings_mirror.py
.venv/bin/python -m pytest -q -n8 -p no:cacheprovider tests/constitutional      # passed: 17148
.venv/bin/python -m pytest -q -p no:cacheprovider tests/unit/test_pada_samhita.py tests/unit/test_praNidadAti_8_4_17.py \
  tests/unit/test_sutra_8_4_1_raSAnatva_samAnapade.py tests/unit/test_8_2_39_8_4_55.py tests/unit/test_gita_gap_fixes.py \
  tests/constitutional/test_vikalpa_branches.py tests/unit/test_derive_all_readings.py               # passed: 102 (with 5 more)
~/data-master/ashtadhyayi-ai/venv/bin/python ~/data-master/ashtadhyayi-ai/rulings/validate.py           # all ok (local)
```

Practical notes:

- An LK run is slow. `explore()` forks on every vibhāṣā reached, so a taddhita chain can take minutes per case.
- Never run two `lk_cases run` processes on the **same adhyāya** at once: each one rewrites that adhyāya's whole verdict
  file.
- Run long jobs as foreground or tool-backgrounded commands. A process started with `( … &)` from a sandboxed shell was
  killed.

## 6. Commit plan (one commit per concern; the reviewer must be a different agent)

1. Rulings, schema and fixtures: SOURCE_CONFLICTS, the builder, the schema, 5.1.130, the fixtures.
2. Gate and harness: `tools/lk_cases.py`, `tools/exercise_audit.py`, `test_lk_cases.py`, `sutra_class`, `status`, the Makefile.
3. 8.4 sandhi: 8.4.55, 8.4.60, 8.4.62, 8.4.63 and the tripādī spine.
4. Upasarga ṇatva: 8.4.2, 8.4.14–16, `engine/natva.py`, `pada_merger`.
5. Verdicts and generated docs: `sig/lk_case_verdicts`, `sig/sutra_class.json`, `docs/CONFIDENT_SUTRAS.md`, the new
   ledger. Commit these last, after `make coverage`.

Then: `make release ID=<each claim>`, and commit the three brain rulings in `~/data-master/ashtadhyayi-ai`.

## 7. Guardrails that applied, and still apply

- Morphology only through `apply_rule`.
- No new `_arm` keys.
- No word-specific `cond`.
- Gold, baselines and `vivaksha_schema.json` are never hand-edited.
- A fixture changes only with a source: a brain ruling, or a Kāśikā pratyudāharaṇa quoted in its `source` or `note`.
- Hotspots (`pipelines/tinanta.py`, `engine/{scheduler,resolver,core_loop,dispatcher}.py`, `CONSTITUTION.md`) are
  coordinator only.
- Any doubt about meaning or sources → ask the owner and record the answer as a brain ruling (Art. 22, AMENDMENT 26).
