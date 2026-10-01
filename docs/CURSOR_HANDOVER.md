# CURSOR HANDOVER — glass-box universal rule-based Pāṇini engine

Author of plan: Claude (review-only from here). **Executor: Cursor.** Claude does the final review.
Branch at handover: `claude/gan-3-rate-limit-handover-mq70vw`. Obey `CONSTITUTION.md` and the
apply_rule-only principle throughout; do not hardcode grammar in Python (arm-flag ratchet 223→0 continues).

## 0. State at handover (verified 2026-10-01)

### Already committed — in `a429683d` (swept in with an unrelated commit by another session; do NOT redo)
| What | Files |
|---|---|
| 5.1.1 gate fix: 518 modules in `sutras/adhyaya_5/**` had `adhikara_in_effect(..., "5.1.1")` although 5.1.1's scope ends 5.1.17 (`scope_end` is enforced) → those sūtras could never fire. Gate and `anuvritti_from` now point to the most specific registered adhikāra covering the sūtra (heads: 4.1.82 ×144, 4.1.76 ×129, 5.4.68 ×89, 5.1.19 ×42, 5.1.18 ×32, 5.3.2 ×24, 5.3.70 ×24, 5.1.78 ×18, 5.1.120 ×16). The 16 sūtras 5.1.2–5.1.17 keep `5.1.1`. | `sutras/adhyaya_5/**`, `scripts/fix_5_1_1_gate.py` (one-off, already run; do not re-run) |
| Oracle 1a: Jijñāsu siddhi chain diff | `scripts/siddhi_chain_diff.py` → `docs/SIDDHI_CHAIN_DIFF.md` |
| Audit 1b: code vs corpus adhikāra | `scripts/adhikara_audit.py` → `docs/ADHIKARA_AUDIT.md` |

Verification done: all 559 `sutras/adhyaya_5` modules import; 2,318 tests selected by `-k "5_1 or 5_2 or 5_3 or 5_4 or taddhita"` pass. Full suite NOT run by Claude (concurrent edits).
Audit after fix: "code consults adhikāra corpus doesn't list" 603 → 85 (the 85 are all `4.1.92`, probably a corpus gap — see T1).

### Uncommitted right now — NOT Claude's work (another session); leave alone unless the plan below says otherwise
`audit/RUN_LOG.md`, `docs/data/traces/tinanta.derive_abhavaM.json`, `engine/dispatcher.py`, `engine/sutra_type.py`,
`pipelines/{bhattikavya_1_1,krdanta,tinanta}.py`, `sutras/adhyaya_1/pada_3/sutra_1_3_3.py`, `sutras/adhyaya_3/pada_2/sutra_3_2_39.py`,
`sutras/adhyaya_6/pada_4/sutra_6_4_38.py`, `tests/unit/{test_autonomous_vs_recipe,test_tinanta_yam_lat_p010}.py`,
untracked `.audit/gold_*`, `tests/unit/test_lyap_6_4_38_nitya.py`, `.claude/`.
**First action: ask the owner to commit or stash these; run the full suite on a clean tree to get the true baseline (memory notes pre-existing failures — record the list in `docs/ratchet_log.md`).**

## 1. External data sources (read-only inputs; never hand-edit, never copy as a second truth)

| Source | Path | Use |
|---|---|---|
| **Sutra-map workbook (newest, best)** | `/Users/dr.ajayshukla/paanini-ashtadhyaayi-sutra-map (1).xlsx` | 9 sheets. `sutra` (3,985 rows): type, saṃjñā term, adhikāra range (e.g. `14001-22038`), padacCheda, **samāsacCheda** (e.g. `आत्-ऐच्`), **anuvṛtti with source sūtra ids** (3,810 rows, format `12064: शेषः \| 12065: …`), Kaumudī/akārādi order, Pada_tags. `dhatu` (2,253: gaṇa, iṭ, pada, artha, anta, upadhā). `Sutras One time exec` / `Sutras Pool` / `Sutras Tripadi` (~999 each: scheduling taxonomy; **cells are Excel XLOOKUP array formulas — trust only the Snum id column, not computed columns**). `vidhi` 147, `mahesvara`, `pratyaya-notlist` 294, **`Sutra overrides` 93 (apply on top of `sutra`)**. Ids are 5-digit (`11001` = 1.1.1). |
| ashtadhyayi.com per-sūtra corpus | `/Users/dr.ajayshukla/ashtadhyayi/` | `adhikara/pada-X.Y/X.Y.Z.txt`, `anuvritti/`, `padachcheda/`, `full_sutra/`, `kashika/*.md`, `satishabodha/`, `vasu_english*/`, `topic/`, `sutraBasics.json` (type, Kaumudī & Laghu-Kaumudī order, topic). Use only to fill what the workbook lacks (Kāśikā, English, topics). Credit/source in `SOURCE.json` (commit + "free to use with credit"). |
| v2 repo (superseded mostly) | `/Users/dr.ajayshukla/xxxpanini_engine_v2/` | Take ONLY: `data/siddhi_inventory.json` (85 Jijñāsu cases with expected sūtra chains), `data/sk_kashika.json` `examples[]`, `docs/{ganapatha,linga,shiksha,phonology}/*` source texts+design notes, `data/adhikara_spans.json`+`anuvritta_chains.json` (diff only). Everything else is already in v3 or abandoned ("no go" docs, 92-line analyzers, template engine). |
| vidyut-prakriya (Ambuda) | https://github.com/ambuda-org/vidyut | **Offline oracle only** (not glass-box; hand-coded Rust). Never a dependency of the engine. |
| Reference site studied | cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site | Pure UI/honesty-convention reference (see T7). No engine to reuse. |

Authority order (constitution): Jijñāsu Prathamāvṛtti > Kāśikā > Rajpopat 2021 > data. Any disagreement between sources → log in `docs/SOURCE_CONFLICTS.md` (create), never silently resolve; ask Ajay.

## 2. Task list (execute in order; each task = its own commit; after each: run tests listed + update `docs/ratchet_log.md`)

### T0 — Clean baseline (blocking)
Get the other session's changes committed/stashed. Run `pytest tests -q`; save failing test ids to `docs/ratchet_log.md` as the baseline. Nothing below may add failures.

### T1 — Finish the 5.x / adhikāra work already started
1. Add a regression test `tests/unit/test_adhikara_gate_scope.py`: for every `sutras/**` module whose gate cites adhikāra H, assert `H ≤ sutra_id ≤ scope_end(H)` using each ADHIKARA record's `adhikara_scope`. Must pass for all 559+ modules (it would have caught the 518 bug).
2. The 85 remaining `4.1.92` mismatches (4.1.100–4.1.178): corpus does not list 4.1.92 as governing, Kāśikā reads it as adhikāra. **Do not change code**; record in `docs/SOURCE_CONFLICTS.md` for Ajay's ruling.
3. Re-run `python3 scripts/adhikara_audit.py`; commit the regenerated `docs/ADHIKARA_AUDIT.md`.
4. Note: the fixed taddhita sūtras are now *gated correctly* but still don't fire, because no pipeline pushes heads 5.1.18, 5.4.68, 5.1.19, 5.3.2, 5.3.70, 5.1.78, 5.1.120, 4.1.82/4.1.76 at the right time. That is T4's job — do not hack pushes into pipelines.

### T2 — Build canonical `data/inputs/sutra_context.json` (one-way import, re-runnable)
Script `scripts/build_sutra_context.py` (idempotent, deterministic, no hand edits to output):
- Base = workbook `sutra` sheet; apply `Sutra overrides` (93) by Sutra_krama; ids normalised `11001 → 1.1.1`.
- Per sūtra record: `id, type, term, text, padaccheda[{word,vibhakti,vacana}], samasaccheda, anuvritti[{word, source_sutra}], adhikara_range, adhikara_heads, kaumudi_krama, pada_tags, commentary_refs`.
- Fill gaps from `/ashtadhyayi` (`adhikara/` heads, `kashika/`, `vasu_english_summary/`, `topic/`, `sutraBasics.json` types) with per-field provenance tag: `workbook | ashtadhyayi.com | override`.
- **"No record" ≠ "none"**: represent unknown as `null`, empty as `[]`.
- Disagreements between workbook and `/ashtadhyayi` (adhikāra heads, anuvṛtti, types) → `docs/SOURCE_CONFLICTS.md` table (count + first 50), no auto-resolution.
- Write `data/inputs/sutra_context.SOURCE.json` (file paths, workbook sha256, `/ashtadhyayi` git commit `ab287ecf70`, credit text).
- Test `tests/unit/test_sutra_context.py`: 3,983 ids present; 1.1.1/1.1.3/6.4.1/7.3.84 spot values; overrides applied; deterministic (build twice, byte-equal).
- Do not parse the XLOOKUP formula sheets' computed columns (read ids only).

### T3 — Oracles (read-only reports; no engine behaviour change)
1. **Siddhi diff v2**: improve `scripts/siddhi_chain_diff.py`: (a) compare *order* (longest-common-subsequence) not just set; (b) count `forms.db.firings` + exported trace `APPLIED|DEFINED`; (c) bucket results as match / ordered-partial / unordered / form-absent. Current result: 3 match, 57 partial, 25 absent (absent = 16/20 kṛdanta, 6/10 taddhita: भागः त्यागः पावकः कारकः नेता …). Known noise: `firings` lacks 1.3.1/3.4.100/3.4.113 saṃjñā rows — decide whether to log them in firings (preferred) rather than special-casing the script.
2. **Vidyut oracle** (check `bench/oracle_vidyut.py` + `bench/oracle/vidyut.csv` already exist — EXTEND, don't duplicate): confirm install route (`pip install vidyut` vs Rust build), diff final forms and sūtra sequences for the 367 exported traces + siddhi cases; each mismatch bucket = our-bug / vidyut-bug / legitimate vibhāṣā. Output `docs/VIDYUT_DIFF.md`. Offline/CI only.
3. **sk_kashika examples**: single-word `examples[]` only (filter prose like "स्वरे विशेषः"); derive via engine; rank gaps per sūtra → `docs/KASHIKA_EXAMPLE_GAPS.md`. Use as the implementation to-do ordering together with Kaumudī order from `sutra_context`.
4. Cross-check `dhatu` sheet iṭ values vs `data/inputs/dhatupatha_upadesha.json` → differences to `docs/SOURCE_CONFLICTS.md`.
5. Validate the three scheduling sheets: no overlap, coverage vs `core/phases/tripadi.py` default schedule; report only.

### T4 — Make the engine read `sutra_context` (ratchet, one phase at a time)
Goal: no hand-pushed adhikāra frames; anuvṛtti/adhikāra scope declared as data.
1. `engine/adhikara_automation.py` currently pushes 3.1.1 / 1.3.1 / 6.4.1 by hand per phase. Replace with lookup from `sutra_context` (heads + ranges) — one phase per commit, existing tests green each time.
2. Taddhita pipelines: push the right heads (4.1.76, 4.1.82, 5.1.18, 5.1.19, 5.3.2, 5.3.70, 5.4.68, …) **from data by sūtra range**, so the 518 re-gated sūtras can actually fire. Verify with new derivations from the 6 absent taddhita siddhi cases (मालीयः औपमन्यवः आश्वलायनः वासुदेवः दाक्षिः आरण्यः).
3. Add ratchet counter "hand-pushed adhikāra frames" in `docs/ratchet_log.md`; target 0.
4. Lint (`scripts/` + test): a sūtra whose `cond` references an inherited term must list it in `anuvritti` of `sutra_context`; and `SutraRecord.anuvritti_from` must equal data. Treat null (unknown) as warning, not error.
5. Constitution guards: no new resolver layer in Python; no `if/elif` on Sanskrit strings; every effect via `apply_rule`.

### T5 — Coverage (kṛdanta/taddhita first — the real gap)
Using T3 results: implement missing kṛdanta (ghañ 3.3.18, ṇvul 3.1.133, tṛc, ktin …) and taddhita chains for the 25 absent siddhi cases, in Kaumudī order, through `apply_rule` only. Each new derivation exported to `docs/data/traces` and added to the siddhi diff; expected chains from `siddhi_inventory.json`.

### T6 — Source texts for inputs
Read v2 `docs/{ganapatha,linga,shiksha,phonology}` before extending `data/inputs/ganapatha.json`, `linga_anushasana.json`, `maheshvara_sutras.json`; import source text files into `data/reference/` with provenance (not into engine logic).

### T7 — Teaching UI: `docs/learn.html` (new; keep `docs/index.html` audit view untouched)
Static, reads `docs/data/traces/*.json` + `sutra_context.json`; no wasm, no backend (Pages is the only public surface).
- Phase 1 (front-end only): equation bar `भू + शप् + तिप् = भवति` built from trace; stepper (Prev/Next/Autoplay) defaulting to `APPLIED` only with toggle "show skipped + why" (current traces: ~99 steps, only 18 APPLIED, 66 SKIPPED); per-step card = sūtra number+text, char-level diff of `form_before→form_after`, type chip, `why_now_dev`; phase ribbon from `phase`/`tripadi_zone`. Verify before→after chaining on 3–4 traces (hiding SKIPPED must not leave gaps).
- Provenance tags on every item (copy rkmvu convention): `engine-computed`, `corpus-quoted`, `editorial`; explicit "no form derived" and "not implemented" badges (using coverage registry).
- Phase 2 (exporter only, no derivation logic change): add `stage` + `morph_parts` snapshot (dhātu/vikaraṇa/pratyaya segments) per exported step.
- Phase 3: utsarga/apavāda "why X beat Y" from conflict events; predict-next-step quiz; per-step deep links; reverse index sūtra → traces where fired/skipped; samāsacCheda + anuvṛtti panel from `sutra_context`; Kāśikā/English as collapsible `corpus-quoted` panels; paradigm tables generated by running the engine (cells link to traces, failures shown).
- Credit line for ashtadhyayi.com corpus in footer.

## 3. Rules for Cursor
- One task = one commit; no mixed commits (Claude's 5.1.1 work got swept into an unrelated commit — avoid repeating).
- Reports/state go to files under `docs/`, not chat. Keep chat terse.
- Never edit external source dirs. Never add vidyut as a runtime dependency.
- Do not touch the other session's uncommitted files.
- Stop and ask Ajay on: source conflicts (T1.2, T2, T3.4), authority questions, any need to bypass `apply_rule`.

## 4. Claude's final review checklist (after Cursor finishes)
1. `git log` shows one commit per task; no unrelated files.
2. Full `pytest tests -q` ≤ baseline failures from T0; new tests present (`test_adhikara_gate_scope`, `test_sutra_context`).
3. `scripts/build_sutra_context.py` twice → identical output; overrides applied; provenance per field; SOURCE.json present.
4. `docs/SOURCE_CONFLICTS.md` exists and nothing silently resolved.
5. Hand-pushed-frame ratchet decreased; no Python grammar `if/elif` added (grep).
6. Siddhi diff absent count < 25; taddhita sūtras from the 518 fire in at least the 6 target derivations.
7. `learn.html`: SKIPPED toggle works, chaining has no gaps on 4 sampled traces, provenance tags on all panels.
