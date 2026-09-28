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

## Track E — Pāṇini Lab (`/lab`) ✅ 2026-09-28

Local test panel: pick any dhātu (all 2,049 dhātupāṭha roots) × lakāra ×
prayoga × pada, or any indexed noun stem × liṅga; see the whole paradigm with
Vidyut's forms under each cell (green agree / red differ / error), and click a
cell for its full prakriyā (sūtra text, LSK pages, optional saṃjñā/skipped
rows). `core/lab.py` + `bench/oracle_batch.py` (Vidyut via `.venv`),
`GET /v1/lab/grid`, `/v1/lab/lemmas`, `api/lab.html`. Start: double-click
`Panini Engine.command` (opens /lab) or `make lab`.

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
| 7,639 | 172 | ✅ **FIXED 2026-09-28** 7.1.58 इदितो नुम् धातोः not applied — 1.3.9 now tags *idit* structurally; 7.1.58 runs after dhātu it-lopa | skudi~ → स्कुन्दते |
| 2,818 | 312 | ◐ **PARTLY FIXED 2026-09-28** ātmanepada endings — laṭ 9/9 and lṛṭ 9/9 now correct (एधते…एधामहे, एधिष्यते); loṭ (3.4.90/91/93), liṭ ātmane, laṅ āṭ-vṛddhi still open. *Oracle fixed too: it now gets svara-marked upadeśas.* | eDa~ → एधे |
| 2,577 | 74 | ✅ **FIXED 2026-09-28** guṇa on non-laghu upadhā — 7.3.84 target limited to final ik or laghu upadhā ik | SIkf~ → शीकावहे |
| 1,726 | 40 | ✅ **FIXED 2026-09-28** 6.1.64 धात्वादेः षः सः / 6.1.65 णो नः — scheduled with the dhātu (after it-lopa); vārttika pratiṣedha for ष्ठिव्/ष्वष्क्; ṭ-varga reverts after ṣ→s (स्तोचते) | zvada~ → स्वदते |
| 313 | 35 | ✅ **FIXED 2026-09-28** ām-liṭ — 3.1.36 / 2.4.81 generalised (were ईक्ष्-only); `_derive_lit_am` derives the कृ anuprayoga with the engine's own liṭ in the main root's pada (1.3.63): एधाञ्चक्रे…, उक्षाञ्चकार…. 3,054 of the 3,440 remaining ām cells are **gaṇa 10 (ṇic not implemented)** | eDa~ → एधाञ्चक्रे |
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

The index showed **7.1.58 fired in 0 of 77k derivations**; after the fix it fires in 11,578.

**C0 session log 2026-09-28** (branch `lsk-practice`): verified forms
25,187 → **35,280** (+10,093); path-verified 15,480 → **24,465**. Changes:
1.3.9 `idit` tag · 7.1.58 in `P00_bhuvadi_dhatu_it_anunasik_hal` · 7.3.84
target (final / laghu upadhā only) · 8.4.58 full varga table (k→ङ्, was घ्;
ṭ, p added) · dhātupāṭha: **डुपचँष् पाके (01.1151) was missing** — 'pac' had
resolved to पचिँ; resolver now prefers the root whose mūla-dhātu *is* the name
· 3.1.134 narrow gate: दिवुँ, not दिविँ (idit). Tests that pinned buggy output
corrected with comments (सङ्गसीष्ट ङ्, पचति, devam).

**C0 session 2 (2026-09-28):**
- **Oracle fix:** Vidyut reads pada from svara, which our upadeśas omit, so
  every ātmanepadī root was derived parasmaipadī (एधामि). `bench/practice_key`
  now marks the it-vowel anudātta/svarita from our pada label (`eDa~\`).
- **3.4.79** now requires a ṭit sthānī (1.1.56; `source_lakara_upadesha`
  ends in ṭ) — it had turned ta→te in ṅit laṅ/liṅ/lṛṅ.
- **7.2.81 आतो ङितः** generalised from yak-only to any ṅit ā-ādeśa after an
  a-aṅga (एधेते, पचेते).
- laṭ spine: 1.1.51 after guṇa; 3.4.80 + 6.1.97 + 7.2.81/6.1.66/6.1.87 after
  3.4.79. lṛṭ opts into the ātmanepada tail (1.4.100/3.4.79/3.4.80).
- 64 "baseline locked" karmaṇi/bhāve ṅit-lakāra pins relied on the 3.4.79
  bug: 8 now match Vidyut (pins corrected), 56 are wrong both before and after
  (the karmaṇi/bhāve ṅit spine has no yak/sīyuṭ — भवेत for भूयेत) →
  xfail(strict) `_NGIT_PENDING` in the three test files.
- Verified 35,601 → 39,525 → 40,551 (1.1.51) → 43,297 (6.1.64) → **44,109**
  (3.4.113 inventory: ṭi-replaced taṅ ādeśas te/Ate/se/… stay sārvadhātuka by
  1.1.56, so 1.2.4 marks them ṅit and 7.2.81 fires — एधिष्येते).

**New leads found while fixing** (next C0 items, not yet fixed):
- **karmaṇi/bhāve ṅit lakāras** (laṅ, liṅ, lṛṅ): no yak / sīyuṭ path.
- **loṭ ātmanepada**: 3.4.90 आमेतः, 3.4.91, 3.4.93 एत ऐ not wired; 3.4.79 must
  run after śap (it rewrites the ādeśa upadeśa, hiding it from 3.1.68).
- ~~laṅ āṭ vṛddhi~~ — ✅ fixed: 6.4.71 yields to 6.4.72 for ajādi dhātus,
  6.4.72 generalised (was अद्-in-लृङ् only), 6.1.90 does vṛddhi (ऐधत, आवत्, आर्चत्).
  laṅ ātmanepada 9/9: 3.4.100 इतश्च limited to parasmaipada (taṅ upadeśa
  identity), 7.2.81/6.1.66/6.1.87 tail (ऐधेताम्, ऐधे, ऐधावहि, ऐधामहि).
- **6.1.73 छे च**: उछ् → औछत् for औच्छत् (tuk missing).
- ✅ **liṭ ātmanepada** (2026-09-28): the liṭ spine had only parasmaipada
  endings. Now 3.4.81 (e / ire) + 3.4.79/80 + iṭ before se/dhve/vahe/mahe:
  पस्पर्धे … पस्पर्धिमहे, चक्रे … चकृमहे. 7.2.13 made effective (it fired for
  every root and blocked nothing; now structural, and 7.2.35 obeys it; घस्
  removed from its list). thal is pit (1.1.56) → guṇa, no kit: चकर्थ, चिचेतिथ.
  8.3.78 after any iṆ at the aṅga|ending boundary (चकृढ्वे); after iṭ left to
  8.3.79 (optional). 3.4.82 ādeśas keep their sthānī (1.1.56).
- ✅ **C0 session 3 (2026-09-28)** — loṭ ātmanepada 9/9 (3.4.90/91/93
  generalised from yak-only to any loṭ sthānī; śap trigger + 3.4.113 share
  one list of ṭi-replaced ādeśas). **bhāve = karmaṇi**: one route (yak in
  sārvadhātuka lakāras, 3.1.67 भावकर्मणोः); karmaṇi/bhāve lṛṭ = general lṛṭ
  (sya is ārdhadhātuka). **7.4.28** was a stub → real vidhi (क्रियते).
  **3.4.105/106** structural on the liṅ sthānī (एधेरन्, एधेय, क्रियेय).
  **3.4.80** ṭit-only. **aniṭ**: 7.2.10 now decides from the dhātu's own
  anudātta flag before any val-ādi ārdhadhātuka (sya/tās/sic/sīyuṭ), with
  7.2.70 as apavāda (करिष्यति); one `_it_agama` helper at every non-liṭ iṭ
  site → पक्ता, पक्ष्यति, नेष्यति. **8.2.30** added to the universal Tripāḍī
  phase; **8.3.59** after ku (8.3.57 इण्कोः). **2.4.77** sic-luk decided by
  its own root list + parasmaipada (was proxied by "aniṭ" — अभूत् only
  worked because भू was mis-flagged aniṭ).
- **Data fixes** (vs ashtadhyayi-com/data): भू, मू seṭ; पा पाने id 01.1074
  and परस्मैपदी (was लप्'s id and आत्मनेपदी).
- **Oracle fix**: Vidyut also reads seṭ/aniṭ from svara — `accented()` now
  marks the aniṭ root vowel (qupa\ca~^z). The पच् snapshot table was
  recomputed from the corrected oracle: 90/180 agree, 90 pinned + xfail.
- ✅ **aniṭ luṅ with sic** (2026-09-28): 7.2.3 real (was a stub), 7.2.1
  vowel-final only, both blocked by 1.1.57 after 6.4.48 (अवधीत्); 7.3.96 īṭ
  when 7.2.10 blocked iṭ; jus (3.4.109) whenever sic is present; 8.2.26
  general (sic's s tagged at 3.1.44; in the universal Tripāḍī); 1.1.51 after
  sici-vṛddhi; 6.1.78 after vṛddhi+iṭ; ṣatva after r/l (iṆ). अनैषीत्,
  अपाक्षीत्/अपाक्ताम्, अहार्षीत्/अहार्ष्टाम्, अलावीत्.
- ✅ **tudādi** (4.7k cells): second 1.2.4 pass after śa (apit → ṅit →
  1.1.5 blocks guṇa: पुरति, कृषति) + 7.4.28 before śa.
- ✅ **liṭ abhyāsa**: 7.4.60/61 śar = श ष स only and only before a khay
  (शश्रङ्के, जह्राग); 7.4.62 कुहोश्चुः general (ku-varga + ह → cu; जहार) and
  wired into the liṭ spines; 7.4.59 ec → i/u (1.1.48: तितेपे). The चकार test
  now credits 7.4.62, not 8.4.54, for क → च.
- ✅ **8.2.77 हलि च / 8.2.78 उपधायां च** were stubs; now real (dhātu varṇas
  tagged at the pada merge; 8.2.79 कुर्/छुर् excepted): दीव्यति (tracker #15
  closed), मूर्वति, ऊर्दते.
- Verified 51,422 → **55,698**.
- ✅ 6.4.98 गमहनजनखनघसां लोपः generalised (was घस्-only; cond kept
  coordinate-free): जग्मतुः, जघ्नुः. 8.4.40 स्तोः श्चुना श्चुः in the universal
  Tripāḍī: जज्ञे.
- ✅ **curādi / ṇic** (2026-09-28): 3.1.25, 3.1.35, 6.4.55 were stubs →
  real rules. Bootstrap: gaṇa 10 → 3.1.25 ṇic → it-lopa → 6.4.48 (adanta) /
  7.2.115 (ac-final vṛddhi, ṛ → ār) / 7.2.116 (a-upadhā) / guṇa → 3.1.32 new
  dhātu, conjugated with śap; liṭ = ām-liṭ (3.1.35 + 6.4.55 ṇi → ay):
  चोरयति, अचोरयत्, चोरयिष्यति, चोरयतु, चोरयाञ्चकार, पारयति, वेलयति, च्यावयति.
  Index/Lab/practice now derive by pāṭha **id** (an upadeśa can repeat across
  gaṇas: पूरी 4/10). 8.3.59 आदेशप्रत्यययोः: a dhātu's own upadeśa s (tagged
  at tape init) never takes ṣatva (च्योसयति; सिषेवे still ṣ). Duplicate
  block collapsed into `P00_guna_rapara_ayadi`.
  Derivable 77,317 → **83,859**; refused 16,616 → 10,074; verified
  55,713 → **73,303 (87 %)**.
- Data: 4 curādi upadeśas imported with the nasal on the wrong vowel
  (`ya~ta`, `la~ga`, `pa~Sa`, `ma~da`) → R1 refusals.
- ✅ **svādi (gaṇa 5)**: 3.1.73 generalised (was a recipe flag); second 1.2.4
  pass makes śnu ṅit; 7.3.84 gives the vikaraṇa's own ik guṇa only before a
  *pit* ending even when 1.1.5 bars the root (सुनोति / सुनुतः / सुन्वन्ति);
  the spines' u-vikaraṇa steps key on gaṇa 5 and 8, not 8 alone. laṭ 9/9.
  Derivable 84,858, refused 9,075, verified 73,736.

## Remaining work queue (in order)
1. ✅ **loṭ/laṅ/liṅ for u-vikaraṇa gaṇas** (2026-09-29): 6.4.106 real (was a
   stub); 3.4.87 at the tiṅ stage, हि apit → ṅit; 1.2.4 honours 3.4.92's pit
   for loṭ uttama; 6.1.78 sees an ec-final vikaraṇa (1.4.13 aṅga); 6.1.66's
   āśīr branch no longer eats vidhiliṅ's only s; liṅ savarṇa-dīrgha; 6.4.110/108
   in loṭ and laṅ; 8.2.79 by upadeśa. loṭ 9/9 in gaṇas 1/4/5/6/8.
2. **ṇatva** (8.4.1/8.4.2) in the universal Tripāḍī — needs its vyavāya and
   pratiṣedha conditions stated exactly first (स्तृणोति, क्रीणाति).
3. **gaṇa 9 (śnā)**: 3.1.81 general, 6.4.112/113 (क्रीणन्ति, क्रीणीतः).
4. **gaṇa 2 (luk), 3 (ślu + dvitva), 7 (śnam)** — the remaining refusals.
5. 7.3.84 → 7.3.86 attribution (largest wrong-sūtra lead).
6. 7.2.61–63 (जहर्थ), 3.4.110 (अस्थुः), 7.3.78 (पिबति, तिष्ठति).
7. data: 4 curādi upadeśas with the nasal on the wrong vowel.
- **Guard**: `tests/constitutional/test_engine_is_rule_based.py` — the rule
  path may never import Vidyut, bench/, the verified list or practice/lab.
- **curādi / ṇic (3.1.25)** — gaṇa 10 is the largest remaining family
  (ām-liṭ alone: 3,054 cells); laṭ etc. raise NotImplementedError.
- **6.4.78 अभ्यासस्यासवर्णे**: इष् → इषेष for इयेष. **8.2.78**: उर्द् → ऊर्द्.
- **abhyāsa bugs**: स्मृ → मस्मार (7.4.60 keeps the wrong consonant), हृ → हहार
  (7.4.62 kuhoś cuḥ missing: जहार).
- **8.2.77 हलि च**: ष्ठिव् → ष्ठेवति for ष्ठीवति.
- **aniṭ ignored** in luṭ/liṭ/luṅ: डुपचँष् gives पचिता (→ पक्ता), पपचिषे,
  अपच्त (→ अपक्त / अपाचि). `test_tinanta_pac_karmani_bhave.py` is a snapshot
  of old output, not gold — 9 luṅ cells xfail(strict) until fixed.
- ~~1.1.51 उरण् रपरः~~ — fixed: 7.3.84 now records the upadhā ṛ index for
  1.1.51 (वर्तते, कर्षति), and the laṭ spine calls 1.1.51.
- ~~ātmanepada लृट्~~ — fixed (एधिष्यते).
- **टुओँश्वि (01.1165)** imported as `Svi~` (nasal on the wrong vowel); the
  correct `wuo~Svi` needs 1.3.9 to treat a non-final anunāsika vowel after
  ādi ṭu as *it*. 45 cells refused (were wrong `Sv…` forms before).
- Ratchet rule note: sūtra files touched (1.3.9, 7.3.84, 8.4.58, 3.1.134)
  added no arms (tags / upadeśa identity only) but did not remove one either.

Every fix moves cells into the verified set, which grows the practice pool —
the two tracks share one metric.

Then: Gītā misses ranked by count, merged with the open
Prakriyotsava items. Current top: tad/yad/idam/etad pronouns (saḥ, yaḥ, te,
tat, tān, tasya), yuṣmad/asmad (me, aham, tava, mayā, naḥ), liṭ (uvāca),
loṭ (viddhi), karmaṇi (ucyate), n-stems (brahma), vocatives (janārdana,
pārtha). Each fix: cite LSK part/page in the sūtra docstring's Source list.

## Order

1. ✅ A1, ✅ D (MVP), ✅ A2, ✅ B2, ✅ C0: idit, guṇa scope, 8.4.58, 6.1.64/65, 1.1.51, ātmane laṭ/lṛṭ/laṅ, āṭ.
   Next C0: ām-liṭ, loṭ/liṭ ātmane, aniṭ, karmaṇi/bhāve ṅit spine (yak/sīyuṭ), 7.3.84→7.3.86.
   Test policy: every snapshot cell that is known-wrong is pinned to Vidyut's
   form and xfail(strict) — fixing the spine turns it into a pass.
2. A3, then C driven by B2's miss list, B1 per LSK part alongside C
3. Phase 5 thinning continues as the ratchet allows (unchanged rules)

## Success metrics

| Metric | Now | Target |
|---|---|---|
| Sūtras with LSK page | 1,895 | 1,900 |
| forms.db cells verified vs Vidyut (form) | 73,736 / 84,858 (87 %) | 90 % |
| … of those, sūtra path also agrees | 43,661 | all verified |
| Sūtras that change a surface in forms.db | 102 | grows as coverage grows |
| Gītā tagged-word coverage | 9.9 % | 50 % → 80 % |
| LSK prakriyā order agreement | — | measured per part, rising |
| Full suite | 19,145 passed, 118 xfail (each pinned to Vidyut) | zero regressions every commit |
