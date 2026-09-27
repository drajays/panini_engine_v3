# Final plan — 2026-09-28

Supersedes the *ordering* of `final_plan.md` (its architecture rules, ratchet
rule and Art. 2 decision rules still apply unchanged). Adds one new input:
**LSK study guides (Parts 1–12) for the rules, Gītā grammatical analysis for
real examples.** Sources live outside the repo in `~/read_panini/`; the repo
holds only sūtra ids, page numbers and forms this engine derives — no book
prose (copyright: Arsha Avinash Foundation, all rights reserved).

## Where the old phases stand

| Phase | Status |
|---|---|
| 0 Compliance hotfix | done (ARM_GATE_BASELINE = 0) |
| 1 Tripāḍī phase | done (`core/phases/tripadi.py`, `engine/phases/pada_merger.py`) |
| 2 Telemetry isolation | done enough; not a blocker |
| 3 Vibhāṣā forks | done (6.4.38 VIBHASHA, `test_vibhasha_forking.py`) |
| 4 Autonomous loop | partial (`engine/core_loop.py`, `test_autonomous_vs_recipe.py`) |
| 5 Pipeline thinning | open — `pipelines/tinanta.py` 4,145 LOC (target < 300) |
| 6–12 Completeness | in progress via `docs/PRAKRIYOTSAVA_FIXES.md` (15/19 fixed) |

## Inputs kept / dropped

- **Kept:** LSK Parts 1–12 (1,900 distinct sūtras cited, every one already has
  a file in `sutras/`), Gītā Grammatical Analysis (1,157 tagged words, clean IAST).
- **Dropped:** everything in `~/read_panini/no/` and the NIOS books — no data
  the engine doesn't already carry.

## Track A — show the rule with a real example (display only, Art. 6 safe)

Lives in `core/` + `api/`; `engine/ sutras/ phonology/ pipelines/` never read it.

- **A1 LSK page on every sūtra. ✅ DONE 2026-09-28** — `tools/build_lsk_index.py`,
  1,895 sūtras; `data/reference/lsk/sutra_pages.json`
  (sūtra → [[part, pdf_page], …]) surfaced in `GET /v1/sutras/{id}` and on
  every trace step (`_lsk`).
- **A2 Engine examples per sūtra. ✅ DONE 2026-09-28** — `tools/build_form_index` also writes a
  `firings(sutra_id, cell_key)` table while it derives, so a sūtra answers
  "which of our forms does this fire in" (e.g. 7.1.15 → सर्वस्मिन्, विश्वस्मात्).
  Shown in `GET /v1/sutras/{id}` → `examples` and in practice ("यही सूत्र और कहाँ?"),
  one per paradigm cell first. Only **path-verified** cells are shown (below).
- **A3 Attested examples.** `data/reference/gita/words.jsonl`
  (verse, IAST, SLP1, tag). A sūtra example that is also a Gītā word is shown
  as attested ("BG 2.33").

## Track D — अभ्यास: practice that explains itself (`/practice`) ✅ MVP DONE 2026-09-28

Modelled on sanskritabhyas.in (paradigm + MCQ/recall/T-F, filters by
stem/liṅga/difficulty), plus what it lacks: **every answer is explained sūtra
by sūtra** from the engine's own derivation, with LSK pages.

- `core/practice.py` + `GET /v1/practice`, `/v1/practice/lemmas`, `api/practice.html`
- Types: शुद्ध विकल्प (MCQ) · रूप लिखें (recall) · सत्य/असत्य · **कौन-सा सूत्र?**
  (show one before→after step, pick the sūtra — unique to a glass-box engine)
- Wrong pick is named ("रामेषु = सप्तमी बहुवचन"); syncretic forms list every cell
- **Answer-key safety:** only cells where our form ∈ Vidyut's
  (`bench/practice_key.py` → `bench/oracle/practice_verified.json`, 18,057 of
  45,936) and, for vendored stems, the attested paradigm.
- Score/streak in localStorage (per-viewer convenience only).
- Next: सही मेल (match), असमान पद (odd one out), per-learner weak-cell review,
  sandhi practice once sandhi is exposed via API, Gītā-word mode (A3).

## Track B — verify against LSK

- **B1 LSK prakriyā gold, Parts 2 → 3 → 4 first.** OCR (tesseract `san`)
  each `[LSK]` block; the sūtra sequence comes from the clean text layer, the
  form from OCR reconciled against our own derivation. Diff our trace's
  sūtra order vs LSK's; each disagreement is a ticket.
- **B2 Gītā coverage metric. ✅ DONE 2026-09-28** — `tools/build_gita_words.py`
  → `data/reference/gita/words.jsonl` (2,309 words, 208 verses, ch. 1–6; verse +
  word + tag only). `bench/gita_coverage.py [--write]`. Baseline: **8.6 % tagged**
  (174/2,034), 8.3 % tagged + Vidyut-verified. Misses mix grammar gaps (pronouns,
  n/s-stems, liṭ, karmaṇi) with lexicon gaps (only 72 noun stems indexed; pārtha,
  bhārata absent; `karma` is indexed as an a-stem, not karman).

## Track C — coverage, ordered by real frequency

**C0 — top of queue: forms.db vs Vidyut disagreements (27,392 tiṅanta cells,
103 subanta)**, `bench/oracle/practice_verified.json["disagree"]`. Families
(heuristic classification, verify each before fixing):

| cells | roots | family | example (ours → Vidyut) |
|---|---|---|---|
| 7,639 | 172 | 7.1.58 इदितो नुम् धातोः not applied | skudi~ skodai → skundAmi |
| 2,818 | 312 | pada: ātmanepada endings wrong (3.4.79 टित आत्मनेपदानां टेरे) — *oracle also lacks svara, so parasmai is not proof* | eDa~ eDai → एधे |
| 2,577 | 74 | guṇa on non-laghu upadhā (7.3.86 scope) | SIkf~ SekAvahi → SIkAvaH |
| 1,726 | 40 | 6.1.64 धात्वादेः षः सः | zvada~ zvadai → svad- |
| 313 | 35 | ām-liṭ (3.1.35–40) | eDa~ eDeDa → eDAYcakre |
| 12,319 | 704 | unclassified — classify next | |

**C0b — right form, wrong sūtra (9,707 verified cells).** `bench/practice_key`
now also checks that every sūtra that changed our surface is in Vidyut's path
(`path_extra`). Vidyut records only its first branch, so treat each as a lead:

| cells | sūtra we credit | likely correct | example |
|---|---|---|---|
| 4,838 | 7.3.84 | 7.3.86 पुगन्तलघूपधस्य (7.3.86 fires in **0** derivations) | मुद् लङ् |
| 1,765 | 3.1.68 | gaṇa-specific vikaraṇa | अक्षू लट् |
| 1,129 | 8.4.54 | vacuous abhyāsa step? | गाधृ लिट् |
| 3 cells/stem | 7.1.12 | 7.3.105 → 6.1.78; 7.3.113 → 6.1.101 (7.3.105 fires in **0**) | लतया, लतायाः |

The index also shows **7.1.58 fires in 0 of 77k derivations** — the idit family above.

Every fix moves cells into the verified set, which grows the practice pool —
the two tracks share one metric.

Then: Gītā misses ranked by count, merged with the open
Prakriyotsava items. Current top: tad/yad/idam/etad pronouns (saḥ, yaḥ, te,
tat, tān, tasya), yuṣmad/asmad (me, aham, tava, mayā, naḥ), liṭ (uvāca),
loṭ (viddhi), karmaṇi (ucyate), n-stems (brahma), vocatives (janārdana,
pārtha). Each fix: cite LSK part/page in the sūtra docstring's Source list.

## Order

1. ✅ A1, ✅ D (MVP), ✅ A2, ✅ B2. Next: C0 families largest-first (7.1.58 first)
2. A3, then C driven by B2's miss list, B1 per LSK part alongside C
3. Phase 5 thinning continues as the ratchet allows (unchanged rules)

## Success metrics

| Metric | Now | Target |
|---|---|---|
| Sūtras with LSK page | 1,895 | 1,900 |
| forms.db cells verified vs Vidyut (form) | 25,187 / 77,317 (33 %) | 90 % |
| … of those, sūtra path also agrees | 15,480 | all verified |
| Sūtras that change a surface in forms.db | 102 | grows as coverage grows |
| Gītā tagged-word coverage | 8.6 % | 50 % → 80 % |
| LSK prakriyā order agreement | — | measured per part, rising |
| Full suite | 19,255 passed | zero regressions every commit |
