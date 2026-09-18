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

1. पथिन्/पन्थाः SLP1 typo (`pipelines/sthanivat_al_ashrita_exceptions_lesson.py`) — OPEN
2. किरति/करति wrong branch (`pipelines/kirati_karati_split_prakriyas.py`) — OPEN
3. व्यूढोरस्केन sandhi never run (same file as #1) — OPEN
4. sutra_2_4_43.py हन्→वध् SLP1 typo — OPEN
5. sutra_6_1_2.py text_dev citation bug — OPEN
6. अस् general tiṅanta gives अस्ते not अस्ति, pada= override ignored — OPEN
7. ऋ-stem kinship/agent nouns (मातृ/पितृ/भ्रातृ/कर्तृ) general subanta wrong — OPEN
8. sutra_3_3_89.py अथुच् SLP1 typo — OPEN
9. उन्नयते wrong pada + missing gemination — OPEN
10. नदी-saṃjñā (1.4.3) missing from subanta schedule — **ALREADY-FIXED** (commit 6ea98f1, verified 2026-09-18: `1.4.3/1.4.4/1.4.5` now called in `P01_subanta_bootstrap`, `core/canonical_pipelines.py:1270-1272`)
11. `_derive_lRT` missing `apply_rule("1.1.51")` after 7.3.84 guṇa — OPEN
12. `derive_denominative_laT()` silent no-op for न्-stem nominals — OPEN
13. General subanta missing 8.2.7/8.2.30/8.2.39 — **PARTIALLY FIXED** (8.2.7 landed commit cb16261 — verify 8.2.30/8.2.39 still missing)
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
