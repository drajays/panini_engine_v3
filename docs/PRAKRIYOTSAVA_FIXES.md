# Prakriyotsava cross-check — fix tracking

Source: `docs/PRAKRIYOTSAVA_CROSSCHECK.md` (19 confirmed bugs, 3 missing
dhātu entries, 7 unimplemented mechanism families). This file tracks status
as fixes land. Update it as you go; it is the source of truth for resuming
this sweep across sessions — do not restate full findings in chat.

## Session status (as of 2026-09-20) — resume here

**15/19 numbered bugs FIXED, 2 PARTIALLY FIXED, 2 still OPEN.** Full suite
clean: 19255 passed, 4 skipped, zero regressions across the whole sweep.
All 3 missing dhātu entries done. यङ्लुक् backlog started (3/9).

Still open, next-highest-leverage first:
- **#12** (denominative क्यच् — राजीयति/राजायते/चर्मयति) — fully
  source-grounded, exact 5-piece plan written out at its own line below.
  Not attempted yet because it needs a new branch on shared `8.2.7`
  (judged too high a regression-risk without dedicated budget). This is
  the best-specified open item — start here.
- **#16 second half** (कृ विधिलिङ् — कुर्यात्) — गुण-block landed; needs a
  उ↔ऋ साम्प्रसारण-shaped transposition with zero existing implementation
  anywhere in the repo. Needs the real sūtra identified from source first.
- **#15 second half** (दिव् — दीव्यति) — गुण-block landed; needs a दीर्घ
  (इ→ई) mechanism, sūtra not yet identified.
- **#9** (उन्नयते) — two gaps, both diagnosed: 8.4.45 (यरोऽनुनासिके...) is
  a pure stub needing real general implementation (careful — other
  उपसर्ग+nasal-root combos likely depend on it too), plus a separate
  आत्मनेपद-licensing rule not yet identified from source.
- **7 unimplemented mechanism families** (यङ्लुक् 3/9 done, 6 to go;
  शतृ/शानच्, माङ्-लुङ्, गण-2/5 vikaraṇa dispatch, वैदिक लेट्, periphrastic
  लिट् परस्मैपद, अञ्च् nasal declension — all untouched, see below).
- दृश्/स्था root suppletion (7.3.78, not wired) — flagged, not fixed.

**Working method that worked well this sweep, keep using it:** fork per
batch, each fork re-verifies its repro against current HEAD before fixing
(commits land continuously, findings go stale fast), fixes constitutionally
(structural Term tags, no `_arm` flags), runs the full suite (not just the
target repro) before every commit, commits small and often (infra hiccups —
rate limits, network drops — have cut off several forks mid-session; small
frequent commits meant almost nothing was ever lost), and updates this file
in the same commit as the code fix. When two forks share the working tree
concurrently (no worktree isolation used in this sweep), give each a
disjoint file list up front and tell them to isolate any suspected
regression to their own changed files before assuming they broke something.

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
9. उन्नयते wrong pada + missing gemination — **VERIFIED-OPEN, root of the sandhi gap identified, not implemented (regression risk / needs source grounding).** `derive('nI','laT','kartari',3,1,upasargas=['ud'])` gives `unayati`. Two independent gaps:
   - **Consonant sandhi**: `_attach_upasargas()` in `pipelines/tinanta.py` prepends the उपसर्ग Term and applies only 1.4.59 (उपसर्ग saṃjñā) — no उपसर्ग+धातु consonant-boundary sandhi runs at all anywhere downstream for this pair, which is why द् vanishes without trace rather than surviving to become न्. The rule needed is **8.4.45 यरोऽनुनासिकेऽनुनासिको वा** (a यर्-consonant optionally becomes its वर्गीय nasal before a following nasal: द्→न् before न्, giving उद्+नी → उन्नी). Checked `sutras/adhyaya_8/pada_4/sutra_8_4_45.py`: it is a pure paribhāṣā-gate stub (`cond`/`act` just flip a gate flag, no phoneme substitution at all, `tripadi_gate_eligible` generic scaffold) — this is a missing mechanism, not a wiring gap. Not implemented this pass: 8.4.45 is a general "वा" (optional) rule likely needed by other उपसर्ग+nasal-initial roots too (सम्+नम्, निर्+नी, etc., none currently tested in this repo) — a narrow one-word patch would under-serve it and a fully general one needs verification against more than this single attested form, which this pass didn't have budget to gather safely.
   - **आत्मनेपद licensing**: separate from the sandhi gap; general `derive()` resolves परस्मैपद for this उद्+नी combination and no upasarga-conditioned आत्मनेपद rule fires. Needs the specific licensing sūtra identified from source before implementing (same category as #12/#17/#18 — not guessed at).
   Recommend bundling with #17/#18 for a future source-grounded pass; do not attempt piecemeal.
10. नदी-saṃjñā (1.4.3) missing from subanta schedule — **ALREADY-FIXED** (commit 6ea98f1, verified 2026-09-18: `1.4.3/1.4.4/1.4.5` now called in `P01_subanta_bootstrap`, `core/canonical_pipelines.py:1270-1272`)
11. `_derive_lRT` missing `apply_rule("1.1.51")` after 7.3.84 guṇa — **FIXED** (commit 72e5456 — कृ लृट् 3sg now `karizyati` = करिष्यति, was `kaizyati`)
12. `derive_denominative_laT()` silent no-op for न्-stem nominals — **VERIFIED-OPEN, fully source-grounded now, deeper than a wiring fix.** Read PDF p.733–734 directly (crosscheck doc line ~2641). Confirmed the exact chain for all three target words — no more guessing needed, but four separate pieces are missing/inert:
    - **राजीयति** (इच्छार्थे, "wants himself to be king") — **3.1.8 सुप आत्मनः क्यच्** (NOT 3.1.13 — that citation, inherited from the original sweep, was itself wrong). Chain: राजन् + 3.1.8 (क्यच् insertion) → **1.4.15 नः क्ये** (gives राजन् पद-संज्ञा before क्य-affixes) → **8.2.7** (न्-लोप: राजन्+य → राज्+य) → **7.4.33 क्यचि च** (इत्व: राज+य → राजि+य) → 7.4.25 सार्वधातुके दीर्घः (राजि→राजी, already called by `derive_denominative_laT`) → शप्+तिप् → राजीयति.
    - **राजायते** (आचारार्थे, "behaves like a king") — **3.1.11 कर्तुः क्यङ् सलोपश्च** (क्यङ् प्रत्यय, न्-लोप same as above, आत्मनेपद via 1.3.12 since क्यङ् is ङित्).
    - **चर्मयति/चर्मायते** (भावे, "becomes actual leather") — confirmed **3.1.13 लोहितादि॰ is correct here** (चर्मन् genuinely belongs to the लोहितादि गण per this page) — `sutra_3_1_13.py`'s hardcoded stem set `{"pawapawA", "lohita"}` just needs `"carman"` added; same न्-लोप chain as राजीयति then applies. (Also: the crosscheck sweep's target spelling "चर्मण्यति" appears to be a misreading — the source derivation shows no retroflex ण् anywhere, output is चर्मयति.)
    
    **Why not implemented this pass:** three of the four pieces are currently inert stubs whose `act()` only sets a paribhāṣā gate with zero downstream consumer — `sutra_3_1_8.py` (क्यच् insertion), `sutras/adhyaya_1/pada_4/sutra_1_4_15.py` (पद-संज्ञा — grepped repo-wide, `1_4_15_naH_kye`/`naH_kye_gate` have no reader anywhere), `sutras/adhyaya_7/pada_4/sutra_7_4_33.py` (इत्व). Implementing न्-लोप here also means **giving `sutras/adhyaya_8/pada_2/sutra_8_2_7.py` a new branch**: the existing three branches (tripāḍī-zone single-term, `purvapada_n_lopa_recipe` samāsa, pre-merge HAL-initial-sup) don't cover "न्-ending stem tagged पद by 1.4.15, followed by a vowel-initial क्य-affix residue, 2 terms, no tripāḍī zone yet" — a genuinely new site shape. 8.2.7 is shared, security-sensitive infrastructure that #13's fix and a sibling fork's #7 work both already depend on; touching it again under this pass's time budget was judged too high a regression-risk to attempt blind (mirrors the #15/#16 caution already logged in this file — same "touching shared infra broke unrelated roots" lesson). Comparable in total scope to #19 (which took reordering across 5 rules). Next attempt should: (1) implement 3.1.8/1.4.15/7.4.33's `act()`s for real phonemic work, (2) add 8.2.7's 4th branch, (3) add "carman" to 3.1.13, (4) build `derive_icchartha_kyac_laT()` alongside the existing `derive_denominative_laT()`, (5) run full suite after each of the 4 steps individually, not just at the end.
13. General subanta missing 8.2.7/8.2.30/8.2.39 — **FIXED** (commit baef3fc — राजभिः/वाग्भिः/वाक् all verified correct; 8.2.7 gained a pre-merge branch, 8.2.30 gained पदान्ते branch, 8.2.39/8.4.53 generalized from single-letter demo maps to full jhal-vargas)
14. पच् general tiṅanta gives `pacata` not पचति/पचते — **FIXED** (commit 5f22a6e — `_run_lat_kartari_bhuvadi_spine`, the fallback every plain gaṇa-1 root without its own dedicated spine uses, never called 3.4.79; wired in, now gives पचते by this row's own आत्मनेपदी label, and पचति with `pada='parasmai'` override — the "missing vowel" bug was purely rule-scheduling, unrelated to whether this specific dhātupātha row's आत्मनेपदी label is itself correct data for the canonical "पच् भर्जने" root, which is a separate, unexamined data question)
15. दिव् (दिवादि) gives देव्यति not दीव्यति — **PARTIALLY FIXED** (commit c2e51f3). Generalized 1.2.4's पित्-detection from a hardcoded 3-name set to the real phonological test (upadeśa's own trailing letter ends in प्/फ् — this is why शप्/"Sap" doesn't block गुण while श्यन्/"Syan" does), and added a second 1.2.4 call in गण-4's `_apply_vikarana` branch after श्यन् is inserted (pop-then-recall, an idiom this repo already uses elsewhere). गुण is now correctly blocked: `derive('divAdi_04_0001','laT','kartari',3,1)` gives `divyati` (was `devyati`) — matches the source text's own citation ("इयन् के ङित् होने से... नहीं हुआ है"). This re-exposed that मिद् needs its own अपवाद — `sutras/adhyaya_7/pada_3/sutra_7_3_82.py` (मिदेर्गुणः) already existed, glass-box-correct, but was never wired in (मेद्यति was only "correct" before by the same accident that made दिव् wrong — गुण fired unconditionally for every गण-4 root); wired it in right after 1.2.4, verified मेद्यति/भवति unaffected. Still open: दिव् itself needs a separate दीर्घ (इ→ई) — currently `divyati` (short इ), not दीव्यति. Mechanism not yet identified (the original sweep's own page reading only confirmed the गुण-block, calling the दीर्घ "a separate [thing]" without naming a सूत्र) — needs source-grounded identification, not guessed at.
16. कृ विधिलिङ् gives करुयात् not कुर्यात् — **PARTIALLY FIXED** (commit d3d7d21). Same shape as #15's guṇa-block, different firing site: `sutras/adhyaya_7/pada_3/sutra_7_3_84.py`'s root-vowel guṇa branch (कृ's own ऋ) had no check for `liG_yasut_expected` (the existing flag that already correctly pre-blocks the vikaraṇa-IK branch, e.g. उ→ओ in करोति) — extended the same guard to this branch. `derive('BvAdi_DukfY','liG','kartari',3,1)` no longer guṇas ऋ→अर्; करोति/कुरुतः/करवाणि (लट्/लोट्, where the flag is never set) verified unaffected. Still open: output is now `kauyAt`, not कुर्यात् — गुण-blocking alone isn't the whole mechanism. कुर्यात् needs a उ↔ऋ transposition (गण-8's उ ending up before ऋ's consonantal र्-remnant, a साम्प्रसारण-like step) this codebase has no existing implementation of anywhere (grepped, zero hits, confirmed again this pass) — needs the real सूत्र identified from source before implementing, not guessed at.
17. दुह् गण-2 कर्तरि लट् gives दुह्ते not दुग्धे (8.2.31 not wired) — **FIXED** (commit 9dfb0cd). Cleaner PDF re-read (p.784) found the earlier-elusive step: 8.2.32 दादेर्धातोर्घः was a pure gate stub, zero phoneme logic — implemented as the द्-initial-ह्-final (दुह्/दिह्…) apavāda to 8.2.31 हो ढः, ह्→घ् before झल्-initial affix, firing pre-merge (same shape as 8.2.7's pre-merge branch). Also generalized 8.2.40 झषस्तथोर्धोऽधः off a literal-"D"-only trigger to the full झष् class (needed for घ्+त्→घ्+ध्) — this collided with a legacy one-word demo (अग्द, P033) that hardcoded the same phonetic shape for a different root; re-scoped that demo to its own persistent recipe key rather than let it ride the newly-general trigger. 8.4.53 scoped to दुह्'s own spines in tinanta.py rather than the universal tripadi phase — adding it there regressed अपच्ध्वे (false-positive च्+ध् match), reverted that part. Verified: दोग्धि/दुग्धः/दुहन्ति (कर्तरि), दुग्धे (आत्मनेपद).
18. ब्रू गण-2 कर्तरि लट् gives ब्रूते not ब्रवीति, pada override ignored — **FIXED** (commit 2a369a9). Read PDF p.809-810 directly: 7.3.93 ब्रुव ईट् (ब्रू-specific दीर्घ ई augment before हल्-आदि पित् तिप्/सिप्/मिप्), combined with 7.3.84 guṇa (ऊ→ओ) and 6.1.78 एचोऽयवायावः (ओ+ई→अव्+ई), give ब्रवीति/ब्रवीषि/ब्रवीमि; 3pl needed 6.4.77 उवङ्-आदेश (already implemented, general, just unwired) for ब्रुवन्ति. Along the way found and fixed a second, wider bug: `sutra_1_2_4.py` (सार्वधातुकमपित्) checked a `meta["pit"]` key no pipeline ever sets, so it was treating every सार्वधातुक affix (including genuinely-पित् तिप्/सिप्/मिप्) as अपित् and wrongly blocking guṇa via 1.1.5 — fixed using the पित्-anubandha list phonology/pratyaya_pratyahara.py's TIN pratyāhāra already documents. All verified: ब्रवीति/ब्रवीषि/ब्रवीमि/ब्रूतः/ब्रुवन्ति, full suite clean (19251/4 skipped), अद्/अस्/दुह् unaffected.
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

1. यङ्लुक् frequentatives (9 attested) — **IN PROGRESS, 3/9.** लोलुवः/मरीमृजः already worked; added पोपुवः (commit ca2ae49, पू — same ऊ-अंत class as लू, reused लोलुवः's recipe verbatim once the shared middle span was extracted into `core/canonical_pipelines.py::P00_yang_luk_simple_dvitva_to_guna`). Remaining 6: सरीसृप् (सृप् root is **entirely absent from the dhātupāṭha** — needs a data entry first, same shape as the दृश्/स्था gaps above), पापठीति/लालपीति (पठ्/लप्, full derivation cited in crosscheck doc pp.759 — 1.3.1/3.1.22/6.1.9/6.1.4/1.1.59/7.4.83), बिभर्ति/नेनेक्ति (भृ/निज्, p.760), दाति/धाति (दा/धा, Vedic बहुलम् variant — यङ् itself takes लुक् without श्लु, no द्वित्व — a distinct sub-mechanism, not just a new root on the same recipe).
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
