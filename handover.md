# Handover — Sūtra Coverage → 100 %  (ON HOLD as of 2026-10-03; resume from here)

**Plan of record:** `docs/SUTRA_COVERAGE_100_PLAN.md` (v2) · **Law:** `CONSTITUTION.md` · **Program:** `ROADMAP.md`
**See it:** double-click `Panini Engine.command` → `/coverage` (confident sūtras by pāda; live recipe-free derivation
of nouns and laṭ verbs). Menu `c` refreshes the numbers. CLI: `make confident`, `make autonomy`.

## Where things stand
- **S0 done.** `tools/sutra_class.py` → `sig/sutra_class.json`, `docs/CONFIDENT_SUTRAS.md` (**220 of 3,983 confident**:
  103 operational + 117 structural). Exempt ratchet 3,205 (`tests/constitutional/test_exempt_ratchet.py`). Probes on clones
  go through `engine.scheduler.probe` and are not counted as firings.
- **S1 / ROADMAP C2 largely landed.** Loop (scheduler → resolver → apply_rule, no recipe): 11/11 certain subanta cases,
  3/3 bhū cells, laṭ kartari grid (6 roots × 9 cells), gaṇa-1 sweep **1,152 / 1,165** match the recipe
  (`.audit/tin_auto_sweep.py`, results in `.audit/tin_auto_sweep.json`). Suite: 19,948 passed.
  Mechanisms added: tape-fingerprint vacuity filter · Adhyāya 1 eligible in all phases · pada-merge at Tripāḍī boundary ·
  `apply_pratishedhas` before contention · resolver layers *upadeśa* (1.3.2) and *asiddha* (8.2.1) · tripāḍī cursor ·
  operational paribhāṣās (1.1.51) · adhikāra scope from records (`data/inputs/phase_adhikaras.json`).
- **Real rules written/repaired this stage:** 7.1.18, 2.4.75 (gaṇa 3), 6.1.10 (ślu witness), 6.1.78 (hears past lopa),
  8.4.46/47 (now VIBHASHA).

## Known gaps (the 13 gaṇa-1 misses are rule gaps, not loop gaps)
3.1.79 reads `vana~/zaRa~/kanI~` as tanādi by stem prefix · 7.3.75 (ṣṭhivu~ → ṣṭhīv) unmodelled · `SrA`/`jYA` homonym rows.
Recipe still makes राधे by a 6.1.87 shortcut; the loop uses the real 7.1.18 → śī route (C4 will reconcile).
Unmodelled in the loop: lakāras other than laṭ, ātmanepada/passive, juhotyādi ślu removal (placeholder term stays on tape),
kṛt/taddhita starts.

## Subanta lists → resolver (user-requested, 2026-10-03) — what is done, what is gated
Done: resolver antaraṅga layer (PŚ 50) + apavāda-names-only-its-target; subanta *scanner* is resolver-driven over the whole
tripāḍī and reproduces all 312 vendored cells (`tests/regression/test_subanta_scanner_matches_gold.py`); 7.1.9/7.3.105/7.3.108/1.4.7/7.1.18 fixed or declared.
**Flip done** (0fc62690): `derive()` uses the scanner+resolver; `_RECIPE_ONLY` keeps idam*, tad/yad/etad/kim strī, kim napuṃsaka, anvādeśa on the recipe until their rules exist (ṭāp as a rule; Kāśikā-sourced idam relations). Still open: delete 6.1.97's `_para_competitor` after tiṅanta/kṛdanta/taddhita are loop-driven. Gauge: `python3 -m tools.loop_vs_recipe subanta|tinanta`.
B3 (the 87 निषेधs) needs a scholar to confirm block targets (Art. 19) — it cannot be automated.

## Resume here (S1 remainder, in order)
1. **B2/B3** — declare conflicts (`apavada_of` / `blocks_sutra_ids`); the 87 निषेधs typed VIDHI (`docs/NISEDHA_REVIEW.md`; scholar confirms targets).
2. **The 393 invoked-but-unfinished sūtras** (see `sig/sutra_class.json`: status `gate_only`/`placeholder`/`working` with invoked=true), in Aṣṭādhyāyī order; delete pipeline code each real rule replaces, same commit.
3. **Gate C**: all 364 shipped derivations (`docs/data/traces/`) through the loop; other lakāras; then C3 (`derive()` → thin router) and C4 (pipelines → fixtures).
4. **S2** mechanisms (M1–M10 in the plan) before the S3 sweep. After every stage: `python3 -m tools.firing_coverage && make confident`, then report the confident list.

## Rules that bite
One file per sūtra (Art. 7) · no `_arm` keys / no utsarga narrowing (Art. 13/15) · no bare sūtra ids or `data/reference` mentions in `engine/` or sūtra files
(`test_prakriya_integrity`, `test_no_reference_import_from_engine`) · test expectations from Kāśikā/attested/oracle, never model-written (Art. 19).

## Caution
A second session commits to this repo (it swept uncommitted edits into `f6a213ce`). Check `git status`/`git log` before editing; prefer a worktree.
An old stash `trace noise` (branch claude/gan-3-rate-limit-handover) is still in `git stash list` — not mine, left alone.

## Tiṅanta lakāra stage — status (2026-10-03, end of session)
**Committed (6adf4caf):** bhū, all ten lakāras, parasmaipada, 9/9 through the loop (`tests/regression/test_tinanta_loop_bhu_paradigms.py`).
**Gaṇa-1 parasmaipada sweep** (`python3 -m tools.loop_vs_recipe tinanta --lakara X --pada parasmai`; ~7 min per lakāra): laṭ, laṅ, lṛṭ 540/540; lṛṅ 540/540; loṭ 534 (only ātmanepada-ish `klidi~`); luṭ 537 (`klidi~`); luṅ fixed after (re-sweep); liṭ and liṅ/āśīrliṅ re-sweep pending (liṅ/āśīrliṅ diffs were manTa~/SunDa~ = 6.4.24 fixed, klidi~ ātmanepada).
**Uncommitted fixes after 6adf4caf (need commit once suite green + ledger regenerated):**
6.4.24 (kṅit must be the immediately following affix) · 7.2.116 (dropped lakāra-meta liṭ branch; ṇit-based) · 1.2.5 (liṭ read from tiṅ provenance `source_lakara_upadesha=="liT"`; Ral/Tal excluded as pit by sthānivat) · 3.4.114 (sic ārdhadhātuka without recipe flag) · 7.2.4 (real pratiṣedha, blocks 7.2.1/7.2.3 when sic has iṭ) · engine/it_samjna.py (`it_lopa_already_done` ignores grown-in iṭ).
**Apavāda declarations (resolved against Kāśikā text + audit):** 3.1.33→3.1.68 etc. confirmed (true apavāda). 7.2.35/7.3.96 withdrawn (para, not apavāda). 2.4.77→3.4.108 kept but is NOT an apavāda (different sthānī): it stands in for the jñāpaka of 3.4.110 (luk'd sic is no trigger for jus); removing it gives *aBUvuH (verified). Open: replace with a CONFLICT_OVERRIDES amendment (Art. 21 L10, needs signature); also the engine's 3.4.108 carries 3.4.109's luṅ-sic jus (id mislabel).
**Next:** ātmanepada for all lakāras (3.4.79–3.4.93, 3.4.102 sīyuṭ, 3.4.106); liṭ for gam/nī/pā/kṛ vs Vidyut (6.4.98 etc.); kṛ lṛṭ (7.2.10 should read upadeśa form); then other gaṇas, tiṅanta default flip, kṛdanta, taddhita. After each stage: `python3 -m tools.firing_coverage && python3 -m tools.sutra_class && python3 -m tools.sig_benchmark --freeze`, commit, `tools.sutra_changes --since <prev> --write`.
Gotchas: `.audit/pathdiff.py` needs `PYTHONPATH=.` and separate args (zsh doesn't split strings); full suite ≈10–15 min — run in background, flaky 7.1.35 failure seen once under concurrent edits.
