# Plan — teaching grammar and showing steps in Subhastini

Written 2026-10-29. Read-only study; nothing here is built yet. Companion plans: `docs/LEARN_AND_ORACLE_PLAN.md` (learn.html), `docs/PLAN_RETIRE_SHORTCUTS_AND_API_TESTS.md` (contract tests).

## What exists today

| Piece | Where | State |
|---|---|---|
| Engine derivation response | `api/main.py:_derivation` | per step: `n, sutra_id, sutra_type, type_dev, text_dev, status (APPLIED/BLOCKED/SKIPPED/AUDIT), before/after {slp1,dev}, changed, why_dev, hint_hi (unreviewed), anuvritti_from, lsk` + `stats` + `applied_path` |
| Analyze with steps | `POST /v1/analyze {text, steps:true}` | readings per word, `status derived/differs/gap`, up to 8 derivations |
| Word analysis of a verse | `GET /v1/library/words/{work}/{section}/{item}` | Saṃsādhanī tags + engine verdict `derived/differs/error/unresolved/not_attempted` |
| Sūtra page data | `GET /v1/sutras/{id}`, `docs/data/sutras.json` | pāṭha, padaccheda, `why_dev`, `examples`, `lsk`, `attested` |
| Grids, practice | `/v1/subanta/paradigm`, `/v1/tinanta/paradigm`, `/v1/practice*` | exist, unused by Subhastini |
| Stepper + quiz (standalone) | `docs/learn.html` over `docs/data/traces/*.json` | equation bar, diff, "rules checked before", predict-next-sūtra quiz, expert toggle |
| Subhastini today | `tools/grammar.py:derive`, `web/app.js:derivHTML` (l.474) | shows only `changed` steps as a flat `<ol>`: id, text, before → after; "Report wrong derivation" → `/v1/reviews` |

So the player UI exists in two halves: the engine side has the data, `learn.html` has the design, Subhastini has the word entry point. P1 joins them without engine changes.

## Gaps (engine fields)

| Need | Field | Status |
|---|---|---|
| Tape parts per step (equation bar भव् + अ + ति) | `parts` = `[letters, role, upadesha]` from `engine/trace.py:term_parts` | **missing in API** (in trace rows only) → add to `_derivation` |
| Why it fired | `why_dev`, `anuvritti_from` | exists (some `why_dev` are essays, plan item 6) |
| Why competitors lost | BLOCKED rows + resolver event (utsarga/apavāda) | **missing**: BLOCKED steps are returned with `status` but no `blocked_by` / `beaten_by` / reason → add `resolver: {winner, losers[], reason}` |
| Honest fidelity per step | `fidelity`: `rule` (real cond/act via apply_rule) / `legacy` (a `_legacy_*` half or recipe, S24) / `shortcut:Sn` (SHORTCUT marker) / `placeholder` (917 sūtras that only set a flag) | **missing** → derive from `SUTRA_REGISTRY` class (`sig/sutra_class.json`) + ledger markers; one lookup, no new rule logic |
| Hindi/English gloss | `hint_hi` (UNREVIEWED), sūtra English | exists for Hindi, English missing; keep the "unreviewed" label |
| Saṃjñā / it-lopa highlight | step `sutra_type` SAMJNA, `parts` role `it` | partial; derive highlight from `parts` diff client-side |
| Next-sūtra quiz | decoys = BLOCKED/SKIPPED rows at that point | in learn.html data; **not in API** → serve from `steps` once `resolver` exists |
| Whole-derivation verdict | `status derived/differs/gap` | exists |

Rule for all of it: display metadata only, never read by a `cond()` (same line as `term_parts`).

## Experience (what the learner sees)

1. **प्रक्रिया-क्रीडक (step player)** — opened from any word in a verse. One card per *applied* step: sūtra Devanāgarī + id, padaccheda, `why_dev`, equation bar before/after with the changed part highlighted, an "also considered" fold (blocked/skipped rivals with the utsarga–apavāda reason), previous/next, deep link `#word/step`.
2. **Modes** — *आरम्भ* (applied steps only, plain gloss, no ids), *मध्यम* (adds why-here, rivals, saṃjñā steps), *वैयाकरण* (every row incl. SKIPPED count, anuvṛtti, lsk page, raw SLP1). One toggle, stored in `localStorage`.
3. **Word explorer** — in a verse, each Saṃsādhanī word is clickable → its engine readings → player. ✓/✗ marks already exist (`SCL_MARK`); ✗ shows engine's other form and opens both derivations side by side.
4. **Quiz "अग्रिम-सूत्रम्?"** — at step *n* show tape + 4 options (the real next sūtra + 3 rivals the engine rejected there); answer reveals why. Score kept per learner in `progress.json`-style local store.
5. **Sūtra page** — text, padaccheda, Kāśikā, examples *from the engine* (`/v1/sutras/{id}.examples`, verified forms only), "where it fired" links into the player.
6. **Confidence labels** — each step shows a small mark: `✓ नियम` (real rule), `◐ पुरातन-मार्ग` (legacy recipe), `△ S36` (shortcut, ledger id), `○ स्थानधारक` (placeholder). A derivation containing any non-✓ step carries a banner "इस प्रक्रिया में N चरण पूर्ण-नियम नहीं"; the reviewer link stays. Learners never see a faked step presented as a rule.
7. **Sanskrit-first** — Devanāgarī leads (verse never carded, per `design.md`); Hindi gloss below, English on hover/toggle. Labels from the existing `web/index.html` vocabulary (पाणिनीय प्रक्रिया, पद-विश्लेषणम्).

## Phases

| Phase | Content | Engine change | Subhastini files | Effort |
|---|---|---|---|---|
| **P1** (≤1 session, existing API) | Replace the flat `<ol>` by the player: applied steps as cards, before→after with diff highlight, `why_dev`, `hint_hi` marked unreviewed, status of each reading, mode toggle (beginner / expert), sūtra link to `/v1/sutras/{id}` text. Pass through the whole `steps` list (not only `changed`). | none | `tools/grammar.py` (`derive`: return full step fields), `web/app.js` (`derivHTML` → `playerHTML`), `web/style.css` (card, diff) | S |
| **P2** (1 session) | Engine adds `parts`, `fidelity` to `_derivation`; Subhastini shows equation bar and confidence marks + banner | `api/main.py:_derivation`, `engine/trace.py` (read-only helpers), `core/trace_view.py`; contract test pin in `/v1/health` (see API-tests plan) | `web/app.js`, `web/style.css`, `tools/grammar.py` | M |
| **P3** (1–2 sessions) | Rivals / "why X beat Y": `resolver` in steps; "also considered" fold; utsarga–apavāda card | resolver event exposure in `engine/trace.py` + `_derivation`; needs ordering of BLOCKED rows (some traces lack them, see S24 trace gaps) | same + `web/app.js` fold | M–L |
| **P4** (1 session) | Next-sūtra quiz, local score store | none beyond P3 | `web/app.js` (quiz view), `tools/server.py` (`/api/quiz` thin proxy if needed) | M |
| **P5** (1 session) | Sūtra pages with engine examples and reverse index "fired here"; grids (`/v1/tinanta/paradigm`, `/v1/subanta/paradigm`) with each cell → player | reverse index from `docs/data/traces` (build script, not in request path) | new `web/` view, `tools/server.py` routes | M |
| **P6** (opt.) | English glosses, reviewed Hindi (`core/i18n_hi` review pass), cleanup of essay-like `why_dev` | content work | data only | ongoing |

## Constraints

- **Stdlib Python, plain JS, no build step** (Subhastini `AGENTS.md`); player is DOM strings like `derivHTML`, no framework.
- **Engine down**: keep the existing offline message; cache derivations in `.cache/color/` style (engine takes seconds per verse) so the player works for visited words.
- **Provenance**: no invented Sanskrit (`RULES.md`). Hindi/English glosses carry a source tag (`engine`, `unreviewed`, `owner-reviewed`).
- **Load**: derive on click, one word at a time; never call sweep endpoints (`/v1/coverage`, `/v1/autonomy/*`) from the UI.
- **Order against other plans**: P1 now (no dependency). P2/P3 touch `api/main.py`, which holds the owner's unstaged edits — land as separate commits, own lines only. P3 is clearer after S24 step A (legacy halves removed), because `fidelity: legacy` then disappears and trace gaps close; until then the `legacy` mark is the honest label.

## Decisions to confirm

1. P1 first, using today's API, before any engine change — recommended.
2. `fidelity` is shown to learners (not hidden behind expert mode) — recommended, it is the honesty guarantee.
3. Quiz decoys only from rivals the engine really rejected (as in `learn.html`), never invented.
