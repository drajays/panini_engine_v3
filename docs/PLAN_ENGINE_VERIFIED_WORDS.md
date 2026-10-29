# Plan — every pada shown in Subhastini engine-verified

Aim (owner): each Sanskrit pada Subhastini shows is derived by the engine from Pāṇini's rules. This plan: where we are, what blocks the rest (by cause), when and how each cause is resolved, what Subhastini lacks, and a measurable "done".
Companions: `docs/PLAN_RETIRE_SHORTCUTS_AND_API_TESTS.md` (S24, S-ledger), `docs/PLAN_TEACHING_IN_SUBHASTINI.md` (UI), `docs/GITA_GAP_PLAN.md`.

## 0. Measured today (nothing re-run for this plan; **all files below are 8–26 days old** — the engine has moved on, V0 re-measures)

| Corpus | Source file (date) | Tokens | Verified | Not derived | Not attempted |
|---|---|---|---|---|---|
| DCS, 15 works incl. Mahābhārata, Rāmāyaṇa | `.audit/dcs_gaps*.json` (10-20) | 538,285 | **283,660 = 52.7%** | 24,804 (differs 20,733, unresolved 3,071) | **230,821 = 43%** |
| 11 library works, top-2000 unique forms | `.audit/corpus_gaps.json` (10-21) | 77,792 of 206,345 (37.7%) | 64,019 = 82.3% of analysed | unknown 4,159 · oracle-only 3,206 · split 714 | avyaya 5,694 (listed separately) |
| Gītā via Saṃsādhanī reader | `docs/GITA_GAP_PLAN.md` | 7,472 | 6,279 = 84.0% | differs 1,062 · unresolved 131 | – |

DCS split by kind: subanta 265,477 → 95.1% derived (differs 11,104; unresolved 2,022); tiṅanta 41,987 → 74.6% derived (differs 9,629; unresolved 1,049); **not attempted at all: avyaya 91,813 · samāsa members 87,046 · kṛdanta 50,673 · other 1,289**.
Subhastini library: **221,259 records** (Mahābhārata 72,897; Yogavasiṣṭha 28,216; Rāmāyaṇa 22,518; Kathāsaritsāgara 21,546; Bhāgavatam 12,327; Ṛgveda 10,089 …); only **214 verses** are in its engine cache; one verse costs ~4 s live, so a live sweep ≈ 250 h — it must be a batch job on the forms index, not on-demand.

## 1. How Subhastini analyses a word today (and the four verdict vocabularies)

- **Gītā and Saṃsādhanī e-readers:** `GET /v1/library/words` (`tools/library_providers.py::words`, only providers with `has_words`) → per word `status` ∈ derived ✓ / differs ✗ / error ! / unresolved ? / not_attempted · (`web/app.js` `SCL_MARK`). The annotation is a hypothesis, the engine the judge.
- **Any other text:** `POST /v1/analyze` (`tools/grammar.py`): form index + vidyut proposes readings, the engine re-derives each: `verified / differs / gap / skipped` (`DV_STATUS`); text colouring `source` ∈ curated / engine / kosha / cheda (experimental splits) / none. Sandhi-joined words "stay plain".
- **Corpus tool** (`tools/corpus_gaps`): verified / avyaya / unknown / split / oracle_only. **DCS tool:** derived, derived_8_x, differs, unresolved, not_attempted.
- **Gap:** four vocabularies, no shared cause code, no per-pada badge in the verse view (only hover and the analysis table), no coverage figure inside Subhastini, and `has_words` is false for every library work except the Saṃsādhanī ones.

## 2. Unverified words by cause (share of DCS tokens unless said; E = estimate)

| # | Cause | Size | Examples | Resolved by | When | Parallel? |
|---|---|---|---|---|---|---|
| C1 | **Avyaya not attempted** | 91,813 = 17% | ca, tu, iti, na, atha, tatas | Listed by Pāṇini: svarādi (1.1.37), cādi/nipāta (1.4.57), upasargas; sup-luk 2.4.82; verdict class `listed` (cites the gaṇa), not "derived". Taddhita/kṛt avyayas (tasil, ktvā) go with C3/C6 | V1 | yes (read-only + one small sūtra set) |
| C2 | **Samāsa members** | 87,046 = 16% | the parts of every compound | Samāsa machine (compound = pair of Terms; S27, S30, S35). Interim: verify the final member as a subanta (2.4.71 sup-luk) and label `compound-part` | V6 | no (shared engine/origin, 2.1–2.2) |
| C3 | **Kṛdanta not an analysis target** | 50,673 = 9.4% | dṛṣṭvā, śrutvā, niśamya, śreyān, dattvā | `pipelines/krdanta` exists; wire it into `/v1/analyze` and the readers, then L4 kṛt coverage (ktvā/lyap, kta/ktavatu, śatṛ/śānac, tumun first: top corpus cluster, 1,501 tokens) | V2 | yes, per kṛt family (Adh.3 files, disjoint from 5.x) |
| C4 | **Tiṅanta differs/unresolved** | 10,678 = 25% of tiṅanta | kārayet (engine gives kirēt: ṇic/homonym), dadyāt, ददर्श, bhuṅkte, māṅ-injunctive 6.4.74 (~51 per sample), desiderative/denominative roots, preverbs not split (alam, tiras, śrad), "no dhātupāṭha row" (vip, svaj, sīv, dūṣay) | L3/L4 lakāra sweep; 3.1.5 san, 3.1.7 denominatives, 3.1.26 ṇic; homonym-by-pada; dhātu lexicon intake | V3 | yes, per lakāra |
| C5 | **Subanta irregular tail** | 13,126 = 4.9% of subanta | striyaḥ, puṃsām, nṛṇām, sakhā, catur, āpaḥ, bhruvoḥ, adas fem., ṅit fem. i/u | 7.1.x/6.4.x arms; S1/S4/S5/S7 (strī/4.1.1 merge) | V4 | partly; 4.1 files after S24 step B |
| C6 | **Taddhita-derived stems** | small in the Gītā (5 tagged "taddhita stem"); 111 of 131 Gītā unresolved are annotations with no vibhakti/vacana (incomplete tags, mostly taddhita/kṛdanta stems) | kathām → kim+thamu, derived adjectives | Taddhita 5.2–5.4 (3 worktree agents on 5.2 now), then the analyser proposes stem+pratyaya+artha and calls `derive_taddhita` | V5 (running) | yes (done by range) |
| C7 | **Sandhi-joined / split** | unknown 4,159 + split 714 = 6.3% of analysed (E; much larger raw in the verse view) | ततो, नमो, इत्य्, श्रीभगवानुवाच, पुमान् | Verify a split by running sandhi forward (6.1.x, 8.2–8.4; `derived_8_x` already proves the path) plus pada context for enclitics (8.1.17–26, S16 samartha-vibhakti) | V7 | partly (rule groups) |
| C8 | **Vedic / chandas** | Ṛgveda 10,089 + Atharvaveda in the library (E: 3–5% of the library) | Vedic subjunctive, injunctive, accent | Phase G / L6 Track G; until then label `vedic-pending` | V8 | later |
| C9 | **Lexicon facts** | unique words only | proper names, uṇādi, loan words, unknown dhātu/prātipadika | Lexicon intake (S14, S33): owner-reviewed stem list; names verified only as declension | continuous | data agents, owner review |
| C10 | **Oracle-only** | 3,206 = 4.1% of analysed | vidyut reading the engine does not reproduce (overlaps C4/C5) | Judged case by case under "Vidyut = validator only": fix engine or record a reasoned verdict | with C4/C5 | – |

Ranking by size: C1 (17%) → C2 (16%) → C3 (9%) → C4+C5 (7%) → C7 → C6/C8/C9.

## 3. Order and timing (sessions of the S24 plan; ≈ 25–35 sessions to M3)

| Step | Work | Size | After |
|---|---|---|---|
| V0 | **Measure and name**: one verdict vocabulary `verified / listed / compound-part / differs / gap / not-attempted / out-of-scope / vedic-pending` with a `cause` code C1–C10; `tools/verified_coverage.py` → `sig/verified_coverage.json` (per corpus, per cause); re-run niced on a ≤200-word sample first, then batch | ½–1 | T12 suite green, nothing else heavy |
| V1 | Avyaya `listed` class (C1) | 1 | V0 |
| V2 | Kṛdanta as analysis target + ktvā/lyap, kta/ktavatu, śatṛ/śānac, tumun (C3) | 2–3 | V0; parallel with 5.2 merge |
| V3 | Tiṅanta residual by lakāra + sanādyanta + dhātu intake (C4, C10) | 3 | V0 |
| V4 | Strī / puṃs / nṛ / sakhā tail (C5), S7 first | 2 | S24 step B for 4.1 |
| V5 | Taddhita 5.2–5.4, analyser proposes secondary stems (C6) | 3–4 | running |
| V6 | Samāsa machine (C2) | 3–5 | V4 |
| V7 | Sandhi-split verification and pada context (C7) | 2 | V3 |
| V8 | Vedic Track G (C8) | later | M3 |

Run V1–V3 beside S24 only where files are disjoint (Adh.3 vs 4/5); engine/* edits stay serial in the main session. Parallel worktree agents: per kṛt family, per lakāra, per 5.x range, per-corpus read-only sweeps, lexicon proposals. Never parallel: samāsa machine, `engine/origin`, resolver, sandhi/pada context, anything touching shared files. Every agent reports xfail(strict) with a cause rather than patching a form.

## 4. What Subhastini needs (files; engine side marked ⚙)

| Need | Where |
|---|---|
| Per-pada badge in the verse view (✓ engine · ≈ listed · ✗ differs · ? gap · · not attempted), tooltip = sūtras + cause | `web/app.js` (word spans), `web/style.css` |
| One verdict field with a cause code on every word ⚙ | `tools/library_providers.py`, `api/main.py` (`/v1/analyze`, `/v1/library/words`) — separate commits, user's unstaged api edits untouched |
| `has_words` true for every library work (analyse by `/v1/analyze`), results stored in a file, not live | `tools/shelf.py`, new `tools/verify_library.py` writing `.cache/verified/<work>.jsonl`; uses the ⚙ forms index; run niced overnight |
| Coverage dashboard (per work: % verified, top causes, unknown stems) | `web/app.js` + `GET` of `sig/verified_coverage.json` through the API |
| Lexicon intake: unknown stems queue → owner review → engine Lexicon ⚙ | `tools/lexicon.py` (exists) + `data/inputs` lexicon file; never invent Sanskrit (`RULES.md`) |
| Sandhi-split view: split proposed → forward-derived → ✓ per join ⚙ | with V7 |
| Regression corpus: ~25 reviewed golden words/verses per cause | the L2 test of `PLAN_RETIRE_SHORTCUTS_AND_API_TESTS.md` §3 |
| Honest marks for shortcut steps (S-items) | teaching plan P2 `fidelity` |

## 5. Definition of done and the gate

- **Gate (measured, monotonic):** `sig/verified_coverage.json` holds, per corpus, tokens by verdict; a test fails if `verified+listed` share drops or if any word has no cause code; the ceiling only moves up, in its own commit (same rule as the arm ratchet).
- **Milestones:** M1 Gītā ≥ 98% verified/listed, no unresolved without a cause (needs V0–V4) · M2 the 11-work corpus ≥ 95% (V0–V7) · M3 DCS + Subhastini library ≥ 90%, remainder fully classified (V8 for Ṛgveda/Atharvaveda) · **Done** = every pada Subhastini shows is `verified`, `listed` or carries a named reason from §6.
- Never counted as verified: a word whose form matches vidyut or the annotation but whose derivation was not run by the engine; a shortcut step shown as a real rule (teaching plan P2).

## 6. What rules alone can never verify (be honest in the UI)

1. **Lexical inputs Pāṇini does not derive:** dhātupāṭha and gaṇapāṭha membership, nipātana, uṇādi and proper names. The engine verifies the form *given* the listed item (verdict `listed`); that the item exists is a lexicon fact, not a derivation.
2. **Which reading is right in context** (sense, case relation, homonym root) is the annotator's hypothesis; the engine verifies the form, not the meaning.
3. **Corpus faults:** scribal/OCR errors, ārṣa usages (e.g. ātmanepada for parasmaipada), metrical licence — the engine may rightly reject them: verdict `differs` with note, never forced.
4. **Not Sanskrit:** Gurbani, Kabir, Dasbodh, Prakrit/Pali in the library: `out-of-scope`.
5. **Vedic** until Track G: `vedic-pending`; **accent** is not modelled anywhere yet.
