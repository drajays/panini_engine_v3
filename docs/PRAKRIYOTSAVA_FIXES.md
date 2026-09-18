# Prakriyotsava cross-check — fix tracking

Source: `docs/PRAKRIYOTSAVA_CROSSCHECK.md` (19 confirmed bugs, 3 missing
dhātu entries, 7 unimplemented mechanism families). This file tracks status
as fixes land. Update it as you go; it is the source of truth for resuming
this sweep across sessions — do not restate full findings in chat.

Since the crosscheck sweep finished, 4 commits landed that overlap with some
numbered bugs (नदी paradigm, 8.2.7 नलोपः, 8.4.40, 7.2.115 निनाय). **Always
re-verify a bug against current HEAD before fixing it** — it may already be
resolved.

## Numbered bugs (19)

Status legend: OPEN (not yet checked/fixed this pass) · VERIFIED-OPEN (re-ran
repro, still broken) · ALREADY-FIXED (re-ran repro, now correct — prior
commit covered it) · FIXED (fixed this pass, commit `<hash>`) · WONTFIX (with
reason).

1. पथिन्/पन्थाः SLP1 typo (`pipelines/sthanivat_al_ashrita_exceptions_lesson.py`) — **FIXED** (commit 7bf5f91)
2. किरति/करति wrong branch (`pipelines/kirati_karati_split_prakriyas.py`) — **FIXED** (commit 5d58f70). Read PDF p.643-644 directly: the distinguishing signal is NOT root-name or gaṇa, it's purely phonological — 7.1.100's own sūtra text says **ॠत** (long ṝ), not ऋत (short). तॄ/डुकृञ्/भृ/हृ are all **short** ऋ (confirmed in this repo's dhātupāṭha JSON: `BvAdi_DukfY` → `raw_dhatu_after_it_lopa_slp1: "kf"`), so they're phonologically excluded from 7.1.100 regardless of gaṇa/vikaraṇa — करोति/तरति/भरति/हरति all verified unaffected. Implemented 7.1.100 as a real VIDHI (fires on dhātu ending in SLP1 "F" + sārvadhātuka/ārdhadhātuka trigger; substitutes इ, sets `urN_rapara_pending="r"` for 1.1.51, marks `anga_guna_7_3_84` so 7.3.84 declines on the same locus — apavāda marks its own done-state rather than narrowing 7.3.84's cond, per the utsarga/apavāda principle). Pipeline now calls 7.1.100 before 7.3.84; added गिरति (गृ निगरणे) as a regression sibling, same mechanism.
3. व्यूढोरस्केन sandhi never run (`pipelines/sthanivat_al_ashrita_exceptions_lesson.py::derive_vyUDhoraska`) — **FIXED** (commit cea84a8). Read PDF p.655 directly: it's a सिद्धि sibling of महोरस्केन ("इसी प्रकार...जानें"), not a 4th अल्-आश्रित exception; the old विसर्ग/8.3.38 premise had no textual basis (व्यूढ ends in अ, not विसर्ग). Generalized 5.4.151 off its मह्-only hardcode (उरःप्रभृतिभ्यः conditions on the उत्तरपद, not the पूर्वपद), ran the real बहुव्रीहि+कप्+तृतीया spine, extracted the shared 1.1.68→2.2.24→5.4.151 opening into `core/canonical_pipelines.py::P00_kap_bahuvrihi_head` (both पूर्वपद used it, was flagged by the no-duplicate-scheduling-blocks constitutional test). Output verified: `vyUDhoraskena`.
4. sutra_2_4_43.py हन्→वध् SLP1 typo — **FIXED** (commit d628dfd)
5. sutra_6_1_2.py text_dev citation bug — **FIXED** (commit 98711b7)
6. अस् general tiṅanta gives अस्ते not अस्ति, pada= override ignored — **FIXED** (bundled into commit cea84a8 alongside #3 by a git-add mistake — unrelated fixes, same commit; verified separately: `derive('Adadi_02_0060','laT','kartari',3,1)` → `asti`). Fix touched `pipelines/tinanta.py` (dispatch generalized off a stem=="ad"-only special case to any gaṇa-2 root resolved parasmaipada), `sutras/adhyaya_3/pada_4/sutra_3_4_79.py` (3.4.79 ṭeḥ-e now excludes genuinely-parasmaipada tiṅ-ādeśas via the 1.4.99 "parasmaipada" tag), `sutras/adhyaya_6/pada_4/sutra_6_4_111.py` (अस्-root detection now reads post-it-lopa phonetic varṇas instead of stale raw upadeśa meta).
7. ऋ-stem kinship/agent nouns (मातृ/पितृ/भ्रातृ/कर्तृ) general subanta wrong — OPEN
8. sutra_3_3_89.py अथुच् SLP1 typo — **FIXED** (commit 868c48c, plus a ripple fix in `sutra_3_4_114.py` which independently hardcoded the same typo'd string as its ārdhadhātuka-krt allowlist — fixing 3.3.89 alone would have silently broken 7.3.84/6.1.78 downstream for वेपथुः/श्वयथुः)
9. उन्नयते wrong pada + missing gemination — OPEN
10. नदी-saṃjñā (1.4.3) missing from subanta schedule — **ALREADY-FIXED** (commit 6ea98f1, verified 2026-09-18: `1.4.3/1.4.4/1.4.5` now called in `P01_subanta_bootstrap`, `core/canonical_pipelines.py:1270-1272`)
11. `_derive_lRT` missing `apply_rule("1.1.51")` after 7.3.84 guṇa — **FIXED** (commit 72e5456 — कृ लृट् 3sg now `karizyati` = करिष्यति, was `kaizyati`)
12. `derive_denominative_laT()` silent no-op for न्-stem nominals — OPEN
13. General subanta missing 8.2.7/8.2.30/8.2.39 — **FIXED** (commit baef3fc — राजभिः/वाग्भिः/वाक् all verified correct; 8.2.7 gained a pre-merge branch, 8.2.30 gained पदान्ते branch, 8.2.39/8.4.53 generalized from single-letter demo maps to full jhal-vargas)
14. पच् general tiṅanta gives `pacata` not पचति/पचते — OPEN
15. दिव् (दिवादि) gives देव्यति not दीव्यति (श्यन् ङित् guṇa-block missing) — OPEN
16. कृ विधिलिङ् gives करुयात् not कुर्यात् — OPEN
17. दुह् गण-2 कर्तरि लट् gives दुह्ते not दुग्धे (8.2.31 not wired) — OPEN
18. ब्रू गण-2 कर्तरि लट् gives ब्रूते not ब्रवीति, pada override ignored — OPEN
19. कृ लोट् उत्तमपुरुष gives करोणि not करवाणि (3.4.92 आडुत्तम missing) — OPEN

## Missing dhātu entries (3)

- दृश् (दृशिर् प्रेक्षणे) — **FIXED** (commit c16044a, id `BvAdi_dfSir`, upadeśa `dfSir`, gaṇa 1)
- वच् (वचि परिभाषणे) — **ALREADY-FIXED**, stale finding. Present as `Adadi_02_0058`
  (upadeśa `va~ca`, gaṇa 2) since the gaṇas-2–10 bulk import (commit cd03795),
  which landed *after* the cross-check sweep. Also a चुरादि सन्न entry
  `curAdi_10_0380` with the same spelling. No action taken.
- स्था (गतिनिवृत्तौ) — **FIXED** (commit c16044a, id `BvAdi_zWA`, upadeśa `zWA`
  i.e. ष्ठा — this corpus keeps upadeśa-initial ष् (SLP1 `z`) in
  `raw_dhatu_after_it_lopa_slp1` even after the दन्त्य-conversion shows in the
  Devanāgarī fields, matching the existing `zvada~`/स्वद् convention; 6.1.64
  is expected to do the स्/ष् conversion at derivation time, not the data)

**New finding, not yet fixed (logged here per my batch's scope, out of scope
to fix):** general dispatch for both नए roots falls through to plain
शप्-conjugation instead of their real suppletion — `derive('BvAdi_dfSir',
'laT','kartari',3,1)` gives `dfSayati` (should reach पश्यति via the
3.1.137-family root-substitution, likely सुत्र `7.3.78` पाघ्राध्मास्थाम्ना-वर्ग,
which the crosscheck doc's page-notes around p.785–786 already mention as an
existing mechanism used for पश्य/उत्पिब); `derive('BvAdi_zWA','laT',
'kartari',3,1)` gives `zWAati` (should reach तिष्ठति via the same सुत्र's
श्नु-विकरण branch). Both dhātu rows carry a `notes` field pointing at this.
Whoever picks up mechanism family work should check whether 7.3.78 is
implemented at all (`sutras/adhyaya_7/pada_3/sutra_7_3_78.py`) and if so why
it isn't wired into `pipelines/tinanta.py`'s dispatch — same "correct sūtra,
never wired in" shape as the numbered-bug class above, but for दृश्/स्था/वच्
specifically (वच्'s लट्/लोट्/लङ्/विधिलिङ् need the sibling सुत्र 3.1.82 ब्रुवो
वचिः → ब्रू आदेश, likewise unverified/unwired).

## Unimplemented mechanism families (7) — build backlog

1. यङ्लुक् frequentatives (9 attested, 2 already work via `P00_yang_luk_2_4_74_and_1_1_4`) — OPEN
2. शतृ/शानच् present participles (11 attested; `derive_krt()` rejects Satf/SAnac) — OPEN
3. माङ्-लुङ् prohibitive aorist (sūtras 2.4.80/81/82 exist, zero pipeline) — OPEN
4. गण-2/गण-5 vikaraṇa general dispatch (`NotImplementedError`) — OPEN
5. वैदिक लेट् lakāra — OPEN (low priority, Vedic-register)
6. Periphrastic लिट् परस्मैपद (चकार) branch — OPEN
7. अञ्च्-root nasal declension (प्राङ्/प्रत्यङ्/उदङ्/युङ्/कुङ्) — OPEN

## Build-priority word-level candidates (not niche, zero coverage)

राजपुरुष (राजन्+पुरुष तत्पुरुष), क्रिया (कृ+भाव-यक्+टाप्), देवदत्त/दत्त (दा+क्त)

## Working notes

- Constitution: `apply_rule(sutra_id, state)` only. No `_arm` meta flags.
  Structural Term tags/cond() only. See auto-memory `project_engine_constitution.md`.
- "Wired into dispatcher" class (#7,#10,#11,#12,#13,#17, likely #16/#19) is
  highest leverage: rule logic already correct, just needs scheduling into
  `pipelines/subanta.py` `SUBANTA_RULE_IDS_POST_4_1_2` or `pipelines/tinanta.py`
  gaṇa/lakāra dispatch tables.
- "SLP1 typo" class (#1,#4,#8): lowercase digraph (`th`,`dh`) should be
  capital (`T`,`D`).
- "Wrong pada, override ignored" class (#6,#9,#18): check where `pada=`
  kwarg is read vs overwritten downstream in tinanta pipeline.
- Run full suite before/after each fix; do not regress the 18,543-test
  passing baseline (per constitution memory, as of 2026-05-28 snapshot —
  re-check current count, it has grown since).
- Clean-baseline full-suite run before this batch of fixes: 19250 passed,
  4 skipped. If you see ~35 failures in `test_sig_baseline.py[8-*]`,
  `test_sarva_unified_subanta.py`, `test_sarvasmai_smat_smin_prakriya.py` —
  that's another fork's uncommitted WIP on `pipelines/subanta.py`/8.2.x
  sutras sharing this working tree, not a regression from this batch
  (verified: reverting only this batch's files still shows the same
  failures). Multiple forks are working the *same* git checkout
  concurrently in this sweep, not isolated worktrees — always isolate a
  suspected regression to your own changed files before assuming you broke
  something, and only `git add`/commit your own files explicitly (never
  `git add -A`/`git commit -a`, never `git stash` with no pathspec).
