# Handover — Sūtra Coverage → 100 %  (ON HOLD as of 2026-10-03; resume from here)

## SESSION 2026-10-20 (evening) — cursor: sentence practice without AI
Subhastini **Practice** (`#/abhyasa`) drills Saṃsādhanī's 1000 Sentences from `/v1/practice/sentences` (`tools/practice_sentences.py`);
answers are exact-matched, every blank is an engine-derived form. AI tutor retired. Next: S2 book extraction, S3 proofreading screen
(`docs/INTEGRATION_CLIENTS.md` "Sentence practice without AI").

## SESSION 2026-10-20 (afternoon) — cursor: all Sanskrit literature in one place
Subhastini is the reading front door for everything; this engine serves what it holds at `/v1/library` (`tools/library_providers.py`,
providers as / scl / ac — add a provider class for a new source). Plan + contract: `docs/INTEGRATION_CLIENTS.md` "One place".
`Start Subhastini.command` starts this API, the web UI and `~/sanskrit_learning`'s tutor. Details: RUN_LOG §C 2026-10-20 14:30.

## SESSION 2026-10-20 — cursor: integration clients P0 + P1 (Subhastini front door, sanskrit_learning tutor)
Plan of record: `docs/INTEGRATION_CLIENTS.md`. Done: Subhastini launcher starts this API; word → vidyut readings → engine derivation
(exact match only). Next: P2 `POST /v1/analyze`. Open work item: homograph dhātus share an upadeśa (`SAsu~`), see RUN_LOG §C 2026-10-20 10:05.

## SESSION 2026-10-20 — cursor: ग्रन्थ-पाठकः gains the Prasthānatrayī with Śāṅkara-bhāṣya
`/reader` now lists 13 Prasthānatrayī bhāṣyas (optgroup "प्रस्थानत्रयी") beside the Saṃsādhanī e-readers. Text, structure and aligned ṭīkās
come from Advaita Sharada (Sringeri) — **"All rights reserved": local cache only, never commit `data/reference/advaita_sharada/raw/`**.
Word analyses come from Tamal Maharaj's CC BY Zenodo deposit; every mūla/bhāṣya word is re-derived by the engine before it is ✓.
Rebuild a clone: `python3 -m tools.fetch_advaita_sharada && python3 -m tools.fetch_prasthanatrayi_words` (~5 min, 111 MB local).
10:30 — all 29 Advaita Sharada works now in `/reader` (prakaraṇas, stotras, Siddhāntaleśa + Kṛṣṇālaṅkāra; prose works read by paragraph).
Not yet: 6.4.74 māṅ context; samāsa members judged separately. Details: RUN_LOG §C 2026-10-20.

## SESSION 2026-10-18 (afternoon) — AMENDMENT 25 accepted and implemented; `Test Engine.command`
Owner: "all must be based on authentic reference, never discover any rule, see Aṣṭādhyāyī data for any confirmation".
Done: `State.vivaksha` + `engine/vivaksha.py` (vocabulary generated from the sūtras' samagra, each value cited); tiṅanta
tape records artha from prayoga (3.4.69); `data/inputs/dhatu_karmakatva.json` from ashtadhyayi.com `karma` (2,229 rows,
10 gaps) copied onto the dhātu Term; dispatcher stamps `origin:<sūtra>` on created varṇas (ignored by vacuity/marks);
Art. 2 §2 amended; `tests/constitutional/test_amendment_25_vivaksha.py`. Not yet: upapada Term (with kṛt), niṣṭhā-seṭ probe.
**Fixed (2026-10-18 night):** the loop depended on set-hash order (pre-existing at 45e6f9a3; `PYTHONHASHSEED=2` diverged pac
laṭ). Cause: `scheduler.tape_fingerprint` and `resolver._term_sig` compared `repr()` of Term.meta, and a set's repr depends on the
hash seed and insertion history — an unchanged tape could look changed (vacuity filter, antaraṅga zones). Now `scheduler._canonical`
(sets sorted, recursively); memo keys too. `tests/regression/test_hash_seed_independence.py` derives in subprocesses under seeds
0/2/7 and requires identical sūtra sequences. Launchers no longer pin the seed.
`Test Engine.command` (double-click): derive any verb with every sūtra step (`tools/derive_trace.py`), the Kāśikā probe, quick
and full tests, or start the web UI. Brain card agents TR_s01–03 stalled on permission prompts after 4 cards (C-1800 = the 13
sopānas, closes C-013); 10 videos of those slices still to card.

## SESSION 2026-10-18 — cursor: plan v3, Phase 0 + Phase 1 (READ FIRST)
**Plan of record:** v3 phase table at the top of `docs/SUTRA_COVERAGE_100_PLAN.md` (engine pulls, brain supplies). Transcript job closed
(`~/transcript_repo/_skipped/SKIPPED.tsv`; 3 last Pushpa gap slices TR_s01–03 carded in the brain). **AMENDMENT 25** drafted
(`docs/AMENDMENT_25.md`, vivakṣā inputs) — needs owner signature before Phase 4.
**Phase 0:** ledgers regenerated (firing 714 invoked / 428 moved; confident 286; lint implemented 315). Suite 20,343 passed, 14 skipped, 7 xfailed.
`make bench` not rerun (Vidyut oracle; next session).
**Phase 1:** `tools/findings_probe.py` + `tests/regression/test_findings_probe_loop.py` (26/30; 4 strict xfails: hve 6.1.33, vye 6.1.46, bhī loṭ āni,
śās 6.4.34). Real rules: 8.3.60, 7.3.55/56/57 split, 6.4.25 root spelling, 7.3.88 PRATISHEDHA (+ `vikarana_luk` tag from 2.4.72/2.4.77; 6.4.77 uvaṅ
when guṇa forbidden), 6.4.42 (+ `origin:` varṇa tag, `engine/strata.varna_visible` for 6.4.22), 7.4.68, 7.4.69, 6.4.81, 6.4.72 āṭ tag, 6.4.122
(moved out of 6.4.120), 7.2.114, 8.2.36 apavāda of 8.2.30. Details: brain `transcript_work/ENGINE_FINDINGS.md` top section.
**Next:** the 4 xfails; 6.1.70 file holds a 6.1.66 slice (move to 6.1.66, write real 6.1.70; 6.1.66 also carries 6.1.68 work); then Phase 2 (P2 scope
index; loop should record BLOCKED for pratiṣedha-removed candidates). Gotcha: never edit a sūtra file while a run imports it (gave a phantom tFa).

## SESSION 2026-10-10/11 — prakaraṇa track P0/P1 + Vidyut-as-validator (READ FIRST, then the older notes below)
**Rulings (owner):** Aṣṭādhyāyī kram is the law; Patañjali/Kātyāyana/Pushpa Dixit/Neelesh Bodas only clarify within it. Siddhānta-kaumudī order is NOT authority.
Vidyut = validator only: a disagreement is a flag that needs a recorded verdict (`ours`|`engine`, reason, authority) in `data/inputs/vidyut_order_overrides.json`.
**Committed (main):** AMENDMENT 22 lexicon/vyutpatti records (`engine/lexicon.py`, `engine/origin.py`, `data/inputs/subanta_lexicon.json`, `lexicon_compose_rules.json`; real 8.2.9/8.2.10) ·
P0 `SCAN_STATS` in scheduler + `tools/scan_stats.py` (`docs/ratchet_prakarana_p0.json`) · P1 `tools/build_scope_index.py` → `data/inputs/adhikara_scope_index.json` (+ test) ·
`tools/stage_order.py` (empirical prakaraṇa order, 171 tiṅanta derivations) · `tools/vidyut_order.py` (`.venv/bin/python -m tools.vidyut_order --gana 1 --roots 10 --lakara laT liT luG --write`).
**Measured:** scheduler scans all 3,983 records every step (~600 cond calls/step). Adhikāra heads alone cut little (2.5–3.6k); prakaraṇa-module union 0.9–1.9k (2–4×). 10× needs the L2 stage order → concept cards.
**Brain has NO Pāṇinian tiṅanta/kṛt/taddhita derivations** (only 4,863 subanta, 171 words; commentaries are prose). Order evidence for verbs = Aṣṭādhyāyī text + Pushpa/Neelesh cards (to be written). `~/data-master/ashtadhyayi-ai/graph/build_lecture_orders.py` (uncommitted, 76 paragraphs only) is thin.
**Vidyut-order baseline (30 gaṇa-1 cells, laṭ/liṭ/luṅ):** 0 clean. Set gaps: 1.4.13 (all), 8.4.68, 6.1.4/6.1.5 (liṭ), 8.3.111, 7.4.61, 1.3.2, 1.3.7, 3.4.114, 1.1.5, 8.3.24. Order flags: 7.4.60<7.4.59 = ours (verdict written);
7.2.35<6.4.71/72, 7.4.62<7.4.59 agree with kram (verdicts NOT yet written); 3.2.110/3.2.115 vs 1.3.9/1.3.12/1.3.78 pada-selection and 3.2.110<1.3.9 open (check brain Mahābhāṣya); class override `non_operational` (saṃjñā/adhikāra/atideśa/paribhāṣā/anuvāda order not checked) is PROPOSED, needs owner sign-off.
**Real bug found:** 2.4.77 (sic-luk) fires after 3.4.100/3.4.114 in `aBUt` though kram puts it first and its cond is already true → suspect phase/range gating (`engine/phase.py`, `scheduler._skip_*`, W2). Fix via P2.
**Next, in order:** (1) write verdicts for the kram-consistent flags with `make brain S=…` citations; (2) P2: replace `_PHASE_RANGES`/`_MULTI_TERM_RANGES` by prakaraṇa/adhikāra scopes, parity with `docs/ratchet_prakarana_p0.json` + sweeps, start with 2.4.x; (3) shadow assertion "fired module's always-before modules already touched" (extend stage_order to subanta/kṛdanta first); (4) set gaps above; (5) Pushpa Dixit cards per L2 stage (needs transcripts_repo listening). Resolver/scheduler are coordinator-only (`COORDINATOR=1`).
**Gotchas:** full suite ≈6 min, serial only; `test_autonomy_tinanta_grid[1-1-pac]` flaked once under `-x` (passes alone/HEAD). Untracked and left alone: `panini_audit_report.md`, `scratch/`, `.audit/*.out`. Old stash `trace noise` is not ours.


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

## Reference brain + AMENDMENT 20 (2026-10-06) — READ FIRST
From now on every agent reads the brain before touching a sūtra: `make brain S=<id>` (see AGENTS.md "Brain").
AMENDMENT 20 **accepted** and merged: `samagra_*` on all 3,983 records (Art. 4 rewritten; 2,413 composed — check
vipariṇāma before relying on them); row-i citation in every file; anunāsika ≠ anusvāra (joiner + parser fixed,
`han~` = हनँ; engine it-prakaraṇa verified on all 2,240 dhātus); दृशिँर्, चक्षिँङ् restored by 1.3.2; `sutra_context.json`
pāṭha = T0 (ashtadhyayi.com data synced to upstream 5744762: 3.1.73 स्वादिभ्यः, 3.1.31 आर्धधातुके …); legacy
root field RESOLVED: `raw_dhatu_after_it_lopa_*` = engine it-lopa residue, new `citation_dhatu_*` = traditional root,
all readers updated (`scripts/fill_dhatu_it_lopa.py` after any dhātupāṭha edit; test pins it). AMENDMENT 21 (vārttika ids `X.Y.Z.vN`) proposed,
deferred to Track G. Open: `curAdi_10_0470` कर्णँ vs mūla कर्ण (adanta?) needs a scholar; brain `anunasika` lists the rest.

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
**Apavāda declarations (resolved against Kāśikā text + audit):** 3.1.33→3.1.68 etc. confirmed (true apavāda). 7.3.96→6.1.68 likewise a load-bearing stand-in (withdrawal gave *AtiH/*acetiH for seṭ 2sg; pinned by tests/regression/test_luG_set_no_vrddhi.py). 7.2.35→7.2.3 is NOT a true apavāda (nitya) but is a load-bearing stand-in: withdrawing it broke luṅ seṭ roots (*avAnizam), so it stays until nitya/antaraṅga is modelled. 2.4.77→3.4.108 kept but is NOT an apavāda (different sthānī): it stands in for the jñāpaka of 3.4.110 (luk'd sic is no trigger for jus); removing it gives *aBUvuH (verified). Open: replace with a CONFLICT_OVERRIDES amendment (Art. 21 L10, needs signature); also the engine's 3.4.108 carries 3.4.109's luṅ-sic jus (id mislabel).
**Next:** ātmanepada for all lakāras (3.4.79–3.4.93, 3.4.102 sīyuṭ, 3.4.106); liṭ for gam/nī/pā/kṛ vs Vidyut (6.4.98 etc.); kṛ lṛṭ (7.2.10 should read upadeśa form); then other gaṇas, tiṅanta default flip, kṛdanta, taddhita. After each stage: `python3 -m tools.firing_coverage && python3 -m tools.sutra_class && python3 -m tools.sig_benchmark --freeze`, commit, `tools.sutra_changes --since <prev> --write`.
Gotchas: `.audit/pathdiff.py` needs `PYTHONPATH=.` and separate args (zsh doesn't split strings); full suite ≈10–15 min — run in background, flaky 7.1.35 failure seen once under concurrent edits.

## Status 2026-10-05 (loop vs recipe; samples, not the frozen ledger)
`python3 -m tools.loop_vs_recipe tinanta --lakara laT --gana N [--pada atmane] --limit 12` (a sample or another gaṇa never overwrites `sig/loop_vs_recipe.json`).
- **Ātmanepada, gaṇa 1, 20 roots:** laṭ, liṭ, luṭ, lṛṭ, loṭ, laṅ, liṅ, luṅ all 180/180; āśīrliṅ 160/180 (the remaining cell is 2pl `eDizIDvam`: recipe, Vidyut agree, the loop now agrees too once 8.3.78 leaves ṣīdhvam alone — re-sweep to confirm).
- **laṭ, 12 roots, other gaṇas (cells of 108):** 2 → 92 · 3 → 88 · 4 → 99 · 5 → 96 · 6 → 108 · 7 → 108 · 8 → ~84 (re-sweep) · 9 → 107 · 10 → 108.
- Open: gaṇa 2 (cakziN, liha~ ḍhatva, han 3sg), gaṇa 3 (pF 1du, māṅ/hāṅ — the recipe's `mimAe` looks wrong, Vidyut should arbitrate), gaṇa 4 `zWivu~` (7.3.75-ish dīrgha), gaṇa 5/9 3pl `cinvanti` (6.4.87/6.4.? hnuvor), then the other lakāras per gaṇa.
- Vidyut⊆engine gaps: `docs/SUTRA_SUPERSET_GAPS.md` (tools/sutra_superset.py). Remaining: 3.4.107 in the *recipe* path for ātmane liṅ, 8.3.111, lakāra it-letters 1.3.2/1.3.3, 7.2.13 liṭ dual (recipe path), 7.4.61, 8.3.24, 1.1.5, 3.1.40 (recipe path).
- Ledgers (`sig/`, firing_coverage, sutra_class, sig_benchmark --freeze) NOT regenerated this session.
- Known: the full suite is order-/load-sensitive in rare cells (7.1.35 tAtaN, liṭ kṛ); each passes alone and in a quiet serial run. Do not run sweeps while the suite runs.
- Engine spelling trap: some kṛt/taddhita upadeśas spell ñ as `N` (GaN); tiṅ/vikaraṇa `N` is really ṅ (7.2.116 handles both).


## Status 2026-10-05 (late) — loop vs Vidyut (the real oracle), by `tools/tri_compare.py`
`.venv/bin/python -m tools.tri_compare ALL --gana N --lakara X --pada parasmai|atmane|ubhaya --limit K` prints every cell where
the **loop** differs from **Vidyut** (also shows the recipe; the recipe is often the one that is wrong). One root:
`tools.tri_compare ROOT --gana N --lakara X --pada P`. Sweeps and the harness take **row ids** (an upadeśa repeats across gaṇas)
and `start_state(NS(..., pada="atmane"))` picks the pada of an ubhayapadī root.
Cells differing from Vidyut, first 5–8 roots per gaṇa (measured before the last few fixes):
- parasmaipada: gaṇa 1 = 0 in every lakāra; laṭ/loṭ/laṅ/liṅ/lṛṭ/luṭ ≈ 0 for gaṇas 2–9 except pf/pF, Basa~, quDAY, tF (Vidyut empty), Dana~;
  liṭ gaṇa 3/5/6/9 a few roots (hi, rADa~, vyaca~ samprasāraṇa 6.1.17, quBfY); luṅ gaṇa 3 `o~hAk` (Vidyut seṭ, our data aniṭ).
- ātmanepada: laṭ 0 everywhere but gaṇa 10 (ṇic roots: the harness cannot run them — `_bootstrap` returns a finished recipe state);
  open: dIN luṭ `dAtA`, liṭ cakziN (Vidyut gives āṃ forms), loṭ zwiGa~.
- ubhayapadī: laṭ ≈ 0 except `hu`/`quDAY` ātmane (Vidyut returns nothing for some), `liha~`/`duha~` bhaṣ (8.2.37 dhokṣi), ciY (Vidyut empty).
Rules made structural or fixed this round (all Vidyut-checked): 6.4.37, 7.3.54, 6.4.112/113, 7.4.75/76/77/72, 6.4.78, 6.4.100, 6.4.64, 7.2.77/78,
7.2.1 (over 7.3.84), 7.2.3, 7.1.4, 7.1.100/102, 7.3.55, 7.3.83, 6.4.82, 6.4.63, 6.4.87/77 (uvaṅ/yaṇ), 3.4.108/109 jus after abhyasta, 1.2.2 vij iṭ.
Fixed engine-wide: aṭ is its own Term before the abhyāsa; every vikaraṇa rule stands only before a sārvadhātuka lakāra; v/y finals lose the
upadeśa tag (else 1.3.3 strips them); memo key includes gates, registry, adhikāra stack.
Full suite: serial and quiet it is green (≈6 min); run concurrently with sweeps it can fail on liṭ/7.1.35 cells — never run both at once.
Ledgers (`sig/`) still not regenerated.
