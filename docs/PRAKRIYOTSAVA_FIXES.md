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
7. ऋ-stem kinship/agent nouns (मातृ/पितृ/भ्रातृ/कर्तृ) general subanta wrong — **FIXED** (this pass, on top of commit d6b6a1f). Root cause was NOT the scanner (default `derive()` uses the plain linear one-pass walker `run_subanta_sup_attach_and_finish`/`P13_subanta_iti_anga_sandhi_to_pada`, not the scan-to-fixpoint one — that function is only used when `autonomous_scanner=True`). Two real gaps, both fixed:
   - **6.1.68 reached too early**: its position in `SUBANTA_RULE_IDS_POST_4_1_2` comes before 7.1.94 (which turns ऋ→अन्), so on मातृ it sees अ-ending-in-ऋ, declines, and — since this is a single linear pass, not a retry loop — never gets a second chance once 7.1.94 fires. Fixed the same way this list already handles the identical shape for 6.4.8 (which has TWO occurrences, one early for अनङ्-सौ, one late as a general retry): added a second, idempotent "6.1.68" entry right after the list's second "6.4.8". Already-resolved stems (राजन्, कुमारी...) re-check harmlessly since their सुप् term is already gone.
   - **8.2.7 न्-लोप never saw मातान् as eligible**: its "genuine प्रातिपदिक-अंत न्" signal (`an_pratipadika` tag) is only set at subanta tape-init for stems whose ORIGINAL `stem_slp1` ends in "n" — मातृ's stem is "mAtf", so 7.1.94's mid-derivation ऋ→अन् substitution never got the tag. Fixed by having 7.1.94's own `act()` add the tag when it does the substitution (it just created a genuine अन्-अंत अंग, not a न्-आगम — same category as राजन्).
   - **Bonus, same session**: 7.3.110 (ऋतो ङिसर्वनामस्थानयोः, the गुण rule for ऋत्-stems before ङि/सर्वनामस्थान) had the exact same `krt_tfc`-only restriction 7.1.94 had, and was never scheduled in `SUBANTA_RULE_IDS_POST_4_1_2` at all. Generalized (dropped the restriction, added an explicit ङि branch via `upadesha_slp1=="Ni"` since ङि itself isn't tagged सर्वनामस्थान — ङे/ङसि/ङस् correctly stay excluded, they take 6.1.111 उत्व instead), then wired `"7.3.110"` + `"1.1.51"` (uraṇ rapara, consumes the pending र्) into the schedule right after 7.1.94.
   - Verified full paradigm for मातृ (स्त्रीलिङ्ग): सु माता, औ मातरौ, जस् मातरः, अम् मातरम्, ङि मातरि, भिस् मातृभिः, भ्यस् मातृभ्यः — all correct. Also कर्ता/हर्ता (तृच्, unaffected) and पिता/भ्राता/स्वसा (sibling ऋत्-stems) all correct. द्वितीया बहुवचन (शस्) not independently cross-checked against a gold source (none exists in this repo for any ऋत्-stem) — output `mAtrAn` unverified, flagged rather than guessed at.
8. sutra_3_3_89.py अथुच् SLP1 typo — **FIXED** (commit 868c48c, plus a ripple fix in `sutra_3_4_114.py` which independently hardcoded the same typo'd string as its ārdhadhātuka-krt allowlist — fixing 3.3.89 alone would have silently broken 7.3.84/6.1.78 downstream for वेपथुः/श्वयथुः)
9. उन्नयते wrong pada + missing gemination — **VERIFIED-OPEN, re-confirmed, deeper than filed.** `derive('nI','laT','kartari',3,1,upasargas=['ud'])` gives `unayati` — wrong pada (परस्मैपद, confirmed) AND the उद् उपसर्ग's द् doesn't even survive the उपसर्ग+धातु sandhi boundary (vanishes without trace, not just missing gemination — the general upasarga-attachment path apparently doesn't run the द्→न्/द्वित्व consonant sandhi this boundary needs at all). Two separate, non-trivial gaps (upasarga-conditioned आत्मनेपद-licensing rule, and upasarga+dhātu consonant sandhi), not attempted this pass.
10. नदी-saṃjñā (1.4.3) missing from subanta schedule — **ALREADY-FIXED** (commit 6ea98f1, verified 2026-09-18: `1.4.3/1.4.4/1.4.5` now called in `P01_subanta_bootstrap`, `core/canonical_pipelines.py:1270-1272`)
11. `_derive_lRT` missing `apply_rule("1.1.51")` after 7.3.84 guṇa — **FIXED** (commit 72e5456 — कृ लृट् 3sg now `karizyati` = करिष्यति, was `kaizyati`)
12. `derive_denominative_laT()` silent no-op for न्-stem nominals — **VERIFIED-OPEN, fully source-grounded now, deeper than a wiring fix.** Read PDF p.733–734 directly (crosscheck doc line ~2641). Confirmed the exact chain for all three target words — no more guessing needed, but four separate pieces are missing/inert:
    - **राजीयति** (इच्छार्थे, "wants himself to be king") — **3.1.8 सुप आत्मनः क्यच्** (NOT 3.1.13 — that citation, inherited from the original sweep, was itself wrong). Chain: राजन् + 3.1.8 (क्यच् insertion) → **1.4.15 नः क्ये** (gives राजन् पद-संज्ञा before क्य-affixes) → **8.2.7** (न्-लोप: राजन्+य → राज्+य) → **7.4.33 क्यचि च** (इत्व: राज+य → राजि+य) → 7.4.25 सार्वधातुके दीर्घः (राजि→राजी, already called by `derive_denominative_laT`) → शप्+तिप् → राजीयति.
    - **राजायते** (आचारार्थे, "behaves like a king") — **3.1.11 कर्तुः क्यङ् सलोपश्च** (क्यङ् प्रत्यय, न्-लोप same as above, आत्मनेपद via 1.3.12 since क्यङ् is ङित्).
    - **चर्मयति/चर्मायते** (भावे, "becomes actual leather") — confirmed **3.1.13 लोहितादि॰ is correct here** (चर्मन् genuinely belongs to the लोहितादि गण per this page) — `sutra_3_1_13.py`'s hardcoded stem set `{"pawapawA", "lohita"}` just needs `"carman"` added; same न्-लोप chain as राजीयति then applies. (Also: the crosscheck sweep's target spelling "चर्मण्यति" appears to be a misreading — the source derivation shows no retroflex ण् anywhere, output is चर्मयति.)
    
    **Why not implemented this pass:** three of the four pieces are currently inert stubs whose `act()` only sets a paribhāṣā gate with zero downstream consumer — `sutra_3_1_8.py` (क्यच् insertion), `sutras/adhyaya_1/pada_4/sutra_1_4_15.py` (पद-संज्ञा — grepped repo-wide, `1_4_15_naH_kye`/`naH_kye_gate` have no reader anywhere), `sutras/adhyaya_7/pada_4/sutra_7_4_33.py` (इत्व). Implementing न्-लोप here also means **giving `sutras/adhyaya_8/pada_2/sutra_8_2_7.py` a new branch**: the existing three branches (tripāḍī-zone single-term, `purvapada_n_lopa_recipe` samāsa, pre-merge HAL-initial-sup) don't cover "न्-ending stem tagged पद by 1.4.15, followed by a vowel-initial क्य-affix residue, 2 terms, no tripāḍī zone yet" — a genuinely new site shape. 8.2.7 is shared, security-sensitive infrastructure that #13's fix and a sibling fork's #7 work both already depend on; touching it again under this pass's time budget was judged too high a regression-risk to attempt blind (mirrors the #15/#16 caution already logged in this file — same "touching shared infra broke unrelated roots" lesson). Comparable in total scope to #19 (which took reordering across 5 rules). Next attempt should: (1) implement 3.1.8/1.4.15/7.4.33's `act()`s for real phonemic work, (2) add 8.2.7's 4th branch, (3) add "carman" to 3.1.13, (4) build `derive_icchartha_kyac_laT()` alongside the existing `derive_denominative_laT()`, (5) run full suite after each of the 4 steps individually, not just at the end.
13. General subanta missing 8.2.7/8.2.30/8.2.39 — **FIXED** (commit baef3fc — राजभिः/वाग्भिः/वाक् all verified correct; 8.2.7 gained a pre-merge branch, 8.2.30 gained पदान्ते branch, 8.2.39/8.4.53 generalized from single-letter demo maps to full jhal-vargas)
14. पच् general tiṅanta gives `pacata` not पचति/पचते — **FIXED** (commit 5f22a6e — `_run_lat_kartari_bhuvadi_spine`, the fallback every plain gaṇa-1 root without its own dedicated spine uses, never called 3.4.79; wired in, now gives पचते by this row's own आत्मनेपदी label, and पचति with `pada='parasmai'` override — the "missing vowel" bug was purely rule-scheduling, unrelated to whether this specific dhātupātha row's आत्मनेपदी label is itself correct data for the canonical "पच् भर्जने" root, which is a separate, unexamined data question)
15. दिव् (दिवादि) gives देव्यति not दीव्यति (श्यन् ङित् guṇa-block missing) — **VERIFIED-OPEN, root cause pinned, fix attempted and reverted.** Confirmed: `sutras/adhyaya_1/pada_2/sutra_1_2_4.py` (सार्वधातुकमपित्, tags a qualifying term "kngiti" so 1.1.5 blocks 7.3.84) runs *before* `_apply_vikarana` inserts श्यन् in `_run_lat_kartari_bhuvadi_spine` — by the time it fires there's no विकरण on the tape yet to tag, so श्यन् never gets marked and 7.3.84 wrongly guṇas दिव्'s इ. Tried two fixes, both regressed elsewhere: (a) moving the 1.2.4 call after `_apply_vikarana` — 1.2.4's own `_find()` is a "narrow demo" (its own docstring) that isn't scoped to exclude शप्, so it then *also* wrongly tagged गण-1's शप् "kngiti", blocking गुण for भू (`Bavati`→`Bvati`, broke 26 tests). (b) tagging श्यन् "kngiti" directly in `sutra_3_1_69.py`'s `act()` (its own upadeśa spelling "SyaN" already phonetically carries the ङ्-it) — the "kngiti" tag turned out to have other, unrelated consumers elsewhere that mishandled it (मेद्यति broke: `medyati`→`medti`, विकरण itself disappeared). Both reverted, suite back to clean 19251. Needs either narrowing 1.2.4's own scope (excluding vikaraṇa-tagged terms, or at least शप् specifically) before it's safe to call post-vikaraṇa, or a new, narrowly-scoped tag distinct from "kngiti" for this one purpose — not attempted blind.
16. कृ विधिलिङ् gives करुयात् not कुर्यात् — **VERIFIED-OPEN, re-confirmed.** `derive('BvAdi_DukfY','liG','kartari',3,1)` gives `karuyAt` (क-अ-र-उ-य-आ-त्, guṇa firing on ऋ→अर् same as लट्/लोट्, then उ-विकरण surviving unconverted before यासुट्-यात्). Expected कुर्यात् needs ऋ to NOT take guṇa here (विधिलिङ्'s यासुट्-augment context blocks it — same kṅit-vs-not shape as #15) and a उ↔ऋ vowel-order/saṃprasāraṇa-like resolution this codebase has no existing mechanism for anywhere (grepped, zero hits). Deeper than a scheduling fix; not attempted given #15's regression risk with the same rule family this session.
17. दुह् गण-2 कर्तरि लट् gives दुह्ते not दुग्धे (8.2.31 not wired) — **VERIFIED-OPEN, source-checked, root mechanism identified, exact rule-ids still uncertain.** Current repro: `derive('Adadi_02_0004','laT','kartari',3,1)` gives `dukti` (आत्मनेपद तिङ् now resolves correctly per #6's fix, but the general dispatcher currently picks परस्मैपद तिप्-shape "ति" here for a row this dhātupāṭha marks — check pada resolution for this specific row before assuming आत्मनेपद "ते" is even the right target purusha-ending to chase). Read the actual PDF (pp.784-785, परि॰ न दुहस्नुनमां॰ 3.1.89 section — NOTE: this specific page's दुग्धे example is under a **कर्मवत्-कर्तरि भाव** construction (कर्मवत् कर्मणा 3.1.87 + 1.3.13 भावकर्मणोः आत्मनेपद), not necessarily plain कर्तरि लट् — the two might share the same सन्धि tail but verify the opening is the same before reusing this exact derivation for a plain "सः दुग्धे" repro). Confirmed direct from the scan: **8.2.40 झषस्तथोर्धोऽधः is genuinely in the chain** (upgrades the prior "likely 8.2.40-family, not located" guess to source-confirmed). Also visible but NOT reliably legible at 300dpi even after multiple targeted crops: an earlier step converting ह्→घ् (a root-class-specific rule for द्-initial ह्-final roots — दुह्/दिह्/लिह्/गुह्/ऊह् — likely distinct from the general 8.2.31 हो ढः, which gives ढ् not घ् and wouldn't explain दुग्धे's ग् — 8.2.31 is a red herring for this specific word, keep it scoped to its existing जिघृक्षति caller), and a final deaspiration step घ्+ध्→ग्+ध् whose id I could not pin down with confidence. **Not implemented — needs a cleaner high-res re-read of PDF p.784-785's left-margin term-progression column (small glyphs, this pass's crops were still ambiguous on 2 of the ~4 rule citations) before coding, to avoid implementing a wrong rule-id under the right-shaped fix.**
18. ब्रू गण-2 कर्तरि लट् gives ब्रूते not ब्रवीति, pada override ignored — **PARTIALLY FIXED / re-diagnosed.** The pada half is already fixed (bundled into #6's commit cea84a8 — `derive('Adadi_02_0039','laT','kartari',3,1)` now correctly resolves parasmaipada, giving `brUti` not `brUte`). What's left is NOT "sūtra exists but not wired" as the sweep guessed — grepped the whole repo for ब्रवीति/bravIti/the ईट्-आगम mechanism ब्रू needs before sārvadhātuka apṛkta affixes, zero hits anywhere (no sūtra file, no pipeline). This is a missing mechanism, not a scheduling gap — needs the actual augment rule identified and implemented from the source text before it can be wired in; not attempted blind. VERIFIED-OPEN on the guṇa/augment half only.
19. कृ लोट् उत्तमपुरुष gives करोणि not करवाणि (3.4.92 आडुत्तम missing) — **FIXED** (commit 7ba00f6). Deeper than a one-line scheduling fix — required reordering guṇa/6.1.97/6.1.101/6.1.78 relative to the new āgama, tagging gaṇa-8's u-vikaraṇa "anga" so 6.1.78 can see the o+A boundary, and gating 8.4.1/8.4.2 on 3.4.92 having fired (8.4.2's existing vyavāya scan doesn't treat yaṇ as a blocker — calling it unconditionally regressed 3pl karvantu→karvaṇtu; flagged as a real pre-existing gap in `sutras/adhyaya_8/pada_4/sutra_8_4_2.py` itself, not fixed here). Verified karavāṇi/karvāva/karvāma (kṛ) and bhavāni/bhavāva/bhavāma (bhū), all other cells unchanged.

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
