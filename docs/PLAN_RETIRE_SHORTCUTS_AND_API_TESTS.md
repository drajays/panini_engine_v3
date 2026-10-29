# Plan — retire S24, burn down the ledger, hold the ratchets, test the API from Subhastini

Written 2026-10-29. Research only; nothing measured here ran the suite (a full run was in progress). Companion: `docs/SESSION_PROTOCOL.md`, `docs/ALL_SUTRA_PLAN.md`, `docs/SHORTCUT_LEDGER.md`.

## 0. Numbers that are measured vs. quoted

| Item | Value | Source |
|---|---|---|
| Sūtra files still carrying `_legacy_cond` (S24) | **252** (`grep -l _legacy_cond sutras \| wc -l`) | measured today |
| Open ledger rows | S1, S4–S35 (S2, S3 closed) | `docs/SHORTCUT_LEDGER.md` |
| "40 legacy demo pipelines → 48 trace gaps" | **quoted from the owner; not reproducible with a tool today** (`ls pipelines` shows 195 files, none named `*corrected*`; `sig/gaps.json` is stale, 2026-09-15: 281 gaps) | first task of the S24 work is to define and print this number |
| `sig/loop_vs_recipe.json` | subanta 1728/1728 agree; tiṅanta loṭ 534/540, liṅ 531/540 (klidi~ cluster) | measured by the recipe-vs-loop tool |
| Arm ratchet | `tests/constitutional/test_no_new_arm_gates.py`, `test_no_demo_ids_in_sutra_arm_keys.py`, `audit/ratchet_collapse.py --status` | repo |

**Action 0 (half a session, do first):** make one command (`make s24-status`) that prints: legacy-file count, pipelines that still call a recipe instead of the loop, trace gaps (the 48). Without it "48 → 0" has no gate.

## 1. WHEN — order and dependencies

S24 itself says: *remove at the end of the taddhita track*. That is the right point, for a concrete reason: until 5.2–5.4 are real, every new taddhita session adds more `_legacy_*` halves (T9–T12 kept them). Retiring now would be redone.

| # | Work | Start when | Depends on | Size | Parallel? |
|---|---|---|---|---|---|
| 1 | Finish taddhita 5.2 (3 worktree agents running), then 5.3, 5.4 | now | T12 suite green | 3–4 sessions | yes, by sūtra range (disjoint files) |
| 2 | **S24 step A — inventory + move recipes** (`core/canonical_pipelines`, recipe tests → `derive_taddhita` / loop; list recipes that cannot move yet) | after 5.4 | 1; Action 0 | 2 sessions | agents per pipeline family (disjoint pipeline files); main session owns `core/`, `engine/` |
| 3 | **S24 step B — delete `_legacy_*`** in batches by adhyāya/pāda; each batch: delete, focused tests, `grep` count falls | right after A, same week | A for that family | 3–4 sessions (252 files) | yes, per pāda, mechanical; agent reports counts only |
| 4 | S7 + S4 + S1 + S5 (strī side) — see §1.1 | after 4.1 strī files stop changing, i.e. after step B for 4.1 | B (4.1 files clean) | 2 sessions | no — touches shared `engine/origin` and 4.1.x; main session only |
| 5 | S6 (8.4.47/56 duplicate doubled readings), S21 (6.4.144 an-stems), 6.3.90/91, 7.3.3, 1.3.7 audit | any time after 1; S21 before 5.2 xfails flip | none | 1 session each | one agent each, own sūtra files, main applies engine edits |
| 6 | Samāsa machine (a samāsa as a pair of Terms: S30, S35, S27, 5.1.112 `lex:samAsa`) | after 4 | 2.1–2.2 audit | 3–5 sessions | no |
| 7 | Lexicon tables replacing `lex:` caller tags (S14 and every row that cites it) | after 6 | 6 | 2–3 sessions | partly (data files) |

### 1.1 The four named rows
- **S1** (7.1.78/79 stubs; abhyasta read as `origin_abhyasta` inside 7.1.80/81): make 7.1.78 a real pratiṣedha, 7.1.79 neuter vā; delete the tag read. Small; needs the tiṅanta spine stable → step 4.
- **S4** (4.1.6 vārttikas: `dhātor ugitaḥ pratiṣedhaḥ`, `añcateś copasaṃkhyānam`): data + two guards in 4.1.6. Small; Lexicon fact for ugit dhātus already in dhātupāṭha.
- **S5** (7.1.80 luk dhātus in ā get no optional num): record the aṅga's final through luk (`engine/luk.py` already moves it to `lumat_*` meta; read that). Small.
- **S7** (NIp Term borrows `prātipadika`+`anga` tags): the real fix is one pratyayānta-prātipadika merge (4.1.1) after the strī pratyaya, not per sūtra. This is the only non-trivial one; S1/S4/S5 are 2-hour items once S7's merge exists, so do S7 first inside step 4.

### 1.2 Ratchet hygiene (continuous, not a phase)
- Every commit: the two constitutional tests stay green; `audit/ratchet_collapse.py --status` shows no rise; no ceiling edit in the same commit as feature work (a ceiling may only go **down**, in its own commit, `--ratchet-to-current`).
- Agents may not edit ceilings or add `_arm` keys (already in the agent prompts; add the line to `SESSION_PROTOCOL.md`).
- After step B, delete `test_*_legacy` fixtures and drop the arm ceiling to the new floor in one commit. Target path in `project_v4_architecture.md`: arm count 223 → 0.

## 2. Audit gaps not yet planned

| From | Finding | Planned? | Proposal |
|---|---|---|---|
| `audit_claude.md` §arm keys (P013/P017/P036 in predicates) | demo ids inside rule predicates | ratchet only freezes them | burn-down list inside step B (each arm key dies with its recipe) |
| `audit_claude.md` §P01 saṃjñā blocks stamp every trace | display noise, state-aware blocks (P0–P2 in that report) | not scheduled | one session after step A; cuts trace length for the API too |
| `docs/NOTES_AUDIT.md` | 30 notes unmatched; note-only sūtras (3.1.1, 4.1.1, 5.3.55…) never applied by the engine | no | feed to step 4 (4.1.1 merge is exactly the note-only sūtra) |
| `audit_tinanta_cursor.md` | missing spines ✗ in tiṅanta demos; insert in Aṣṭādhyāyī order | partly (L3/L4) | tie to step B for tiṅanta files |
| `sig/loop_vs_recipe.json` | klidi~ cluster: recipe `klindasva` vs loop `klindAsva` (12 cells) | no | one agent, before step A closes (a recipe that disagrees with the loop must be judged, not copied) |
| `sig/gaps.json` | stale (2026-09-15) | no | regenerate at Action 0 |
| `docs/pre_refactor_audit.md` | clean (0 duplicate ids, 0 literal violations) | n/a | rerun after step B |
| API (`api/main.py`, version "3.3") | no version pin or contract file; only in-process smoke test | no | §3 |

## 3. API tests from `/Users/dr.ajayshukla/subhastini`

**Facts.** Subhastini is stdlib-only (no pip, no build step; `AGENTS.md`). It reaches the engine at `SUBHASTINI_ENGINE` (default `http://127.0.0.1:8000`) in `tools/shelf.py` (`/v1/library*`) and `tools/grammar.py` (`/v1/analyze`, `/v1/reviews`). It has **no tests directory**; `tools/check.py` is its only validator. Engine side has `tests/test_api_smoke.py` (in-process, no HTTP).

**Layers (cheapest first; none runs a derivation sweep):**

| Layer | Where | What | Cost |
|---|---|---|---|
| L0 pin | engine `api/main.py` | `/v1/health` returns `{"api_version":"3.3","contract":"subhastini-1"}`; bump `contract` only when a field Subhastini reads changes | 5 lines |
| L1 contract | **Subhastini** `tests/test_engine_contract.py` (stdlib `unittest`, `urllib`) | for each endpoint Subhastini actually calls, assert status 200 and the **keys it reads** (not values) | < 5 s |
| L2 golden | **Subhastini** `tests/golden_words.json` + test | ~25 words/verses whose engine verdict was reviewed by the owner; assert `✓`/form match. Generated from the engine by `tools/make_golden.py` (engine repo), checked in, regenerated only deliberately | < 60 s (one-word derives, serial) |
| L3 degrade | **Subhastini** `tests/test_engine_down.py` | `SUBHASTINI_ENGINE=http://127.0.0.1:9`: shelf and grammar return the documented fallback, never raise | < 2 s |
| L4 engine side | engine `tests/test_api_http.py` | `fastapi.testclient` over the same L1 list, so a rename fails in the engine's CI before Subhastini sees it | < 10 s |

**Running without load.** L1–L3 skip (not fail) when the engine is not reachable (`unittest.skipUnless(health_ok())`); they never call `/v1/coverage`, `/v1/autonomy/*` or sweeps. Run only while no full suite is running (`pgrep -f "pytest tests"`). Command from Subhastini: `python3 -m unittest discover -s tests -v` (engine started by `./run_web.sh` or `uvicorn api.main:app --port 8000`); a `make test-engine` target in Subhastini wraps both.

**First five tests (file `tests/test_engine_contract.py`):**
1. `test_health_pin` — `/v1/health` has `sutras > 3000` and `contract == "subhastini-1"`.
2. `test_library_catalog_shape` — `/v1/library` lists works with `id`, `title`; the works named in `tools/shelf.py` `WORDS` exist.
3. `test_library_item_roundtrip` — `/v1/library/works/gita/...` first item has the fields `shelf.py` reads (text, id, section).
4. `test_words_gita_2_47` — `/v1/library/words/gita/…` returns word rows with stem/vibhakti and an engine verdict key (`verified` or equivalent as `web/app.js` reads it).
5. `test_analyze_one_word` — `POST /v1/analyze {"text":"रामः"}` returns readings; `{"steps":true}` returns a `steps` list; `POST /v1/reviews` is **not** called in tests (it writes a file on the engine side) — assert only that a bad body gives 4xx, using an invalid `target`.

Then `test_golden_words` (L2) and `test_engine_down` (L3) as 6 and 7.

**Open point for the owner:** whether `POST /v1/reviews` should get a dry-run flag so the happy path can be tested without writing review files.

## 4. Next three actions
1. Action 0 (`make s24-status`) and a regenerated `sig/gaps.json`.
2. L0 pin + Subhastini tests 1–5 (one session, no engine logic touched).
3. Finish 5.2 → 5.4; then step A/B of S24 as in §1.
