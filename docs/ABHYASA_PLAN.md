# अभ्यासशाला — practice from beginner to grammarian (shared plan + log)

Owner request (2026-11-13): "see sanskritabhyas.in and the RKMVU Grammar site's abhyāsa, make these learning tools
available in our engine, backed by our engine plus Vidyut plus the other processes we have, from beginner to most
advanced. Claude agents are building the engine right now — do it carefully; write a log both agents can refer to."

**Who reads this:** every agent (Claude, Cursor) before touching `/practice`, `core/abhyasa.py`,
`tools/build_abhyasa_bank.py`, `data/practice/`, `webui/abhyasa.py`, `webui/static/abhyasa.js`.
**Status / log:** §7 below (newest at top). Claim id: `abhyasa-shala` (cursor).

## 1. What the two reference sites offer (inventory, 2026-11-13)

**sanskritabhyas.in** (Sharath Kotian; roster 18b — surface gold + drill UX only, Art. 19; never rule logic):

| Family | Lists / views | Drill types | Filters |
|---|---|---|---|
| संज्ञा (noun) | शब्द रूप, comparison of stems | शुद्ध विकल्प चुनें (MCQ) · रूप का स्मरण (recall the whole table) · सही मेल (match form ↔ cell) · सही या गलत (true/false) · असमान पद (odd one out) | level आसान / मध्यम / कठिन / वैयाकरण; अन्त (ajanta / halanta / one letter); लिङ्ग; विभक्ति |
| क्रियापद (verb) | धातु रूप (10 lakāras × prayoga × pada) | same five | gaṇa, upasarga, sanādi (ṇic, san, yaṅ, yaṅluk and stacks), prayoga, pada, lakāra |
| कृदन्त | per root, every kṛt | MCQ, recall, match, T/F, recall the kṛdanta | level, gaṇa, upasarga, sanādi, pada, popular roots only |
| तद्धितान्त | per pratyaya (aṇ, añ, ṭhañ, ṭhak, ḍhak, tva, tal, mayaṭ, matup, ini, tasil, tral) | fill-up, MCQ, T/F ("मूढ + तल् = मूढता"), declension | level |
| सर्वनाम, संख्या | sarva, bhavat, tad, yad, kim, idam, asmad, yuṣmad; eka … ṣaṣ | as nouns | as nouns |
| संधि | — | MCQ ("देवी + आगमनम् ?"), recall, T/F | level |
| नामधातु | putrīya, kṛṣṇāya … (kyac/kyaṅ/kāmyac) forms + kṛdantas | — | — |
| लिपि | Devanāgarī, Brāhmī, Grantha, Śāradā, Siddham … | letter drills | — |

**RKMVU Grammar site** (`cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site/`; learner UI only, runs Vidyut wasm):
- **अभ्यासः** — *write Sanskrit, sentence by sentence*: 12 lessons over a closed, typed lexicon (54 nouns, 29 verbs,
  kāraka frames). An English sentence is generated (seeded, so `#p3-07` is a stable exercise id); the learner types
  Sanskrit (word order free, no sandhi); each word is graded against the derived form table and a wrong word is
  explained by the kāraka sūtra + the vibhakti sūtra (1.4.49 → 2.3.2 under 2.3.1 अनभिहिते). Lessons: bare sentence ·
  vacana · karman · gati-karman · adhikaraṇa · sampradāna/karaṇa/apādāna · laṅ/lṛṭ · loṭ/vidhiliṅ · ktvā/lyap/tumun ·
  śatṛ/śānac · kta/ktavatu · everything at once.
- **कारकम्**, **सन्धिः**, **प्रत्याहार** (varṇa machine), **पाठः** (lessons), **प्रक्रिया**, dhātu/śabda-rūpa, kṛdanta.

We copy **no data and no code** from either site. Our lexicon, lessons and sentence frames are our own; every form is
our engine's derivation; the sites are cited as the pedagogical model only.

## 1b. Owner ruling (2026-11-13 09:46): sanskritabhyas.in is the main reference

"sanskritabhyas.in/hi will be our main reference — I want all its features in our app's अभ्यास / practice tab."
So the `/practice` tab mirrors sanskritabhyas menu for menu; RKMVU's sentence writing and our grammarian drills are extras.

**Parity checklist** (✓ built · ◐ partial · ✗ not yet) — keep this table current when you add a feature:

| sanskritabhyas feature | Ours (`/practice`) | Answer source |
|---|---|---|
| संज्ञा / सर्वनाम / संख्या drills | ✓ families noun · pronoun · number | engine ∩ (Vidyut ∪ printed ashtadhyayi.com paradigm) |
| क्रियापद drills, all 10 lakāras | ✓ family verb | engine ∩ Vidyut |
| filters: गण, उपसर्ग (22), सनादि, प्रयोग, पद, लकार | ✓ (upasarga/ṇic/san through the engine; yaṅ, yaṅluk, stacks → Vidyut, badged) | as left |
| कृदन्त drills (ल्युट् … क्तिन्), popular roots only | ✓ bank roots = engine ∩ Vidyut; other roots / upasarga / sanādi → Vidyut, badged | |
| तद्धितान्त (अण् … त्रल्) fill-up, MCQ, T/F | ✓ bank items engine ∩ Vidyut; the pratyaya lists → Vidyut, badged | |
| नामधातु (क्यच्, क्यङ्, काम्यच्) | ✓ Vidyut only (engine has no nāmadhātu yet) — badged | |
| संधि MCQ / recall / T-F | ✓ engine join, kept only if Vidyut's sandhi rules split it back | |
| स्वर-युक्त व्यञ्जन, संयुक्त व्यञ्जन drills | ✓ family varna | our transliterator (phonology) |
| लिपि: ब्राह्मी, ग्रन्थ, मिथिलाक्षर, शारदा, सिद्धम — drills + तुलना table | ✓ (varna → सूचियाँ shows the comparison table) | Vidyut lipi |
| drill types: शुद्ध विकल्प, रूप का स्मरण, सही मेल, सही/गलत, असमान पद | ✓ mcq · recall · match · tf · odd (+ table = whole paradigm) | |
| difficulty आसान / मध्यम / कठिन / वैयाकरण (multi-select) | ✓ | |
| अन्त filter (अजन्त / हलन्त / केवल letter), लिङ्ग, विभक्ति | ✓ | |
| पूर्ण शब्द रूप दिखाएं | ✓ button on every paradigm question | |
| सूचियाँ (search, filters) → view | ✓ सूचियाँ view (9,007 stems, every dhātu) | |
| तुलना (compare words / lakāras) | ✓ तुलना view (up to 6 words side by side) | |
| पसंदीदा शब्द | ✓ (localStorage) | |
| सुप् / तिङ् / कृत् / तद्धित प्रत्यय lists | ✓ प्रत्ययाः view (4.1.2, 3.4.78) | |
| शब्दों का आकार (font size) | ✓ अ− / अ+ | |
| भाषा (13 UI languages) | ◐ हिन्दी / English / संस्कृतम् only | |
| खोज (whole-site search) | ◐ list search only; site search is `/sutras` + `/reader` | |
| अनुरोधित शब्द रूप (request a word) | ✗ (any stem can be typed in the शब्दः filter instead) | |
| multiple upasargas (अनु + आङ् …), gati words | ✗ one upasarga at a time | |
| verb "comparison of all lakāras" page | ◐ use the view's lakāra selector; side-by-side lakāras not yet | |
| layout styles (4Col / CSV) | ✗ | |

Extras beyond sanskritabhyas: every answer has source badges (यन्त्रम् / विद्युत् / मुद्रितम्); "प्रक्रिया" opens the engine's
derivation sūtra by sūtra (shared prakriyā view) beside Vidyut's path; कौन सा सूत्र? drills; वाक्याभ्यासः (RKMVU-style
sentence writing graded with kāraka + vibhakti sūtras); प्रत्याहार and इत्संज्ञा drills.

## 2. What we build (and what already existed)

Existing before this work: Flask `/practice` (fill the cell, name the sūtra; live `/api/derive` + `/api/tinanta`),
`core/practice.py` (MCQ / recall / T-F / sūtra over `data/index/forms.db`, keys cross-checked with Vidyut in
`bench/oracle/practice_verified.json`), `/learn` stepper, `/v1/practice/sentences` (Saṃsādhanī 1000 sentences).

New — one page `/practice` (अभ्यासशाला), sanskritabhyas's menus (§1b) with four levels; what each level draws on:

| Level | Topics and drills |
|---|---|
| 1 आसान | वर्णाः/प्रत्याहाराः (expand ac, hal, ik …; is X in Y) · सन्धिः savarṇa-dīrgha, guṇa · सुबन्तम् a/ā stems · तिङन्तम् laṭ/loṭ/laṅ/lṛṭ gaṇa-1 parasmai · वाक्यम् lessons 1–3 |
| 2 मध्यम | i/u/ī/ū/ṛ stems, sarvanāma · all gaṇa-1 lakāras, ātmanepada · kṛdanta ktvā/tumun/kta/ktavatu · sandhi vṛddhi/yaṇ/ayādi · वाक्यम् 4–8 · match + odd-one-out |
| 3 कठिन | consonant stems, numerals · other gaṇas, liṭ/luṅ/āśīrliṅ · participles, kṛtya, lyuṭ, tṛc, ṇvul · taddhita · sandhi pūrvarūpa/pararūpa/prakṛtibhāva · whole-table recall |
| 4 वैयाकरण | name the sūtra (any family) · it-saṃjñā of an upadeśa (1.3.2–1.3.9) · karmaṇi/bhāve · rare roots · hard (near-miss) distractors |

Question types: `mcq`, `recall`, `tf`, `match`, `odd`, `table`, `compose` (vākya), `karaka`, `sutra`, `it`.

## 3. The answer-key rule (Art. 0, 2, 6, 19)

1. **Every answer is our engine's derivation**, made through the ordinary entry points
   (`pipelines.subanta.derive`, `pipelines.tinanta.derive`, `pipelines.krdanta.derive_krdanta(_stem)`,
   `pipelines.taddhita_loop.derive_taddhita`, `pipelines.pada_samhita.join`, `phonology.pratyahara.build_pratyahara`,
   `pipelines.it_prakarana.run_it_prakarana`). The UI never computes a form.
2. **Vidyut is the cross-check**, never the key: an item enters the bank only when the engine's form is among Vidyut's
   (`vidyut: "agree"`). Families Vidyut cannot check (sandhi joins, pratyāhāra, it-saṃjñā) are marked
   `check: "engine"` and their sūtra path is shown.
3. **A disagreement is not hidden** — it goes to `data/practice/abhyasa_gaps.json` (engine form, Vidyut forms,
   request). That file is a work queue for the engine agents, ranked by family.
4. A "which sūtra?" question is asked only when every surface-changing sūtra of the engine is also on Vidyut's path
   (same rule as `core/practice.path_ok_keys`) or, for engine-only families, from the engine trace.
5. Distractors may be produced mechanically (other cells, other kṛts, wrong vowel outcomes); each is checked to be
   *not* among the accepted answers. Distractor code is display code and never reaches the engine.
6. Kāraka → vibhakti in the sentence drills is a **teaching table** (1.4.24–55 → 2.3.2–50, under 2.3.1) that chooses
   the request (vibhakti, vacana) handed to the engine — exactly what a learner choosing a cell does. The engine does
   not yet derive vibhakti from kāraka; when it does, the drill switches to it.

Nothing here is imported by `engine/`, `sutras/`, `phonology/`, `pipelines/` (Art. 6 firewall unchanged).

## 4. Data flow

```
tools/build_abhyasa_bank.py  (run with .venv/bin/python — engine + Vidyut in one process)
   ├── engine derivations (entry points above)          ┐
   ├── Vidyut (bench/oracle_dhaturupa helpers)           ├─→ data/practice/abhyasa_bank.json   (committed, SLP1)
   ├── data/index/forms.db + practice_verified.json      │    data/practice/abhyasa_gaps.json   (engine ≠ Vidyut)
   └── data/practice/vakya_lexicon.json (our lexicon)    ┘
core/abhyasa.py   live: nouns/pronouns/numbers/verbs derived on demand (engine + Vidyut worker + printed corpus, cached);
                  bank: kṛdanta, taddhita, sandhi, vākya, pratyāhāra, it → catalog(), question(), lists(), grade_compose()
webui/abhyasa.py  Flask blueprint: /api/abhyasa/{catalog,question,grade,explain}
webui/templates/practice.html + webui/static/abhyasa.js — the ladder, drills, progress (localStorage), explanations
   (explain = a live engine derivation rendered by prakriya.js, with Vidyut's verdict beside it)
```

Rebuild: `.venv/bin/python -m tools.build_abhyasa_bank` (all families, ~30–60 min) or `--only sandhi,varna,…`.
The bank records the engine commit it was built from; the explain view re-derives live, and says so when the engine
has moved since.

## 5. Contract with the engine agents (please keep these stable, or tell us in §7)

| Entry point the drills call | Used for |
|---|---|
| `pipelines.subanta.derive(stem, vibhakti, vacana, linga=)` | nouns, pronouns, numerals, vākya |
| `pipelines.tinanta.derive(ref, lakara, prayoga, purusha, vacana, pada=)` | verbs, vākya |
| `pipelines.krdanta.derive_krdanta(ref, vib, vac, linga, **vivaksha)` / `derive_krdanta_stem` | kṛdanta (vivakṣā per kṛt as in `tools/exercise_audit._KRT_VIV`) |
| `pipelines.taddhita_loop.derive_taddhita(stem, vib, vac, linga, taddhitArtha=…)` | taddhita |
| `pipelines.pada_samhita.join(left, right)` | sandhi (ac seams only, today) |
| `pipelines.it_prakarana.run_it_prakarana` + `engine.it_samjna.it_records` | it-saṃjñā drill |
| `phonology.pratyahara.build_pratyahara(start, end_it)` | pratyāhāra drill |
| term tag `origin_pratyaya:<upadeśa>` | naming the kṛt / taddhita an item used |

If you rename one of these, run `python3 -m pytest tests/unit/test_abhyasa.py -q` — it fails loudly.

## 6. Known engine gaps surfaced while building (for the engine agents)

Found 2026-11-13 by probing `derive_krdanta` (details and the full list: `data/practice/abhyasa_gaps.json`):
- avyaya kṛts declined as nominals: ktvā → *gatvAH*, *paWitvAH* (1.1.40 avyaya + 2.4.82 sup-luk for kṛt avyayas; same
  root cause as the known *gantum* gap). The drill asks the avyaya stem (gatvA) meanwhile.
- `derive_krdanta(…, kala="vartamAna", artha="kartf")` (Śatṛ) and `artha="kartf"` (tṛc) on gamx~ / paWa~ return the
  bare root (*gam*, *paw*) — the participle needs `samAnADikaraRa=apraTamA` (K6); tṛc needs `krt=Rvultfc`.
- `krt="kftya"` alone yields yat (*gamyaH*) for gam — tavya / anīyar only appear as vikalpa branches (explore).
- `phonology.pratyahara.IN` is built as `build_pratyahara("i","R")`, which stops at the first ṇ (aiuṇ) and gives {i,u};
  the comment says "with the second ṇ (laṇ)" for 8.3.57 iṇkoḥ. Worth a look (not changed here).

More found by the bank build (2026-11-13, engine 3e07292d; full list in `data/practice/abhyasa_gaps.json`):
- **asmad / yuṣmad**: only prathamā eka is right; every other cell repeats the stem *aham* (*ahena*, *ahAn* for mayā, asmān)
  — 7.2.86 ff. (yuṣmad-asmad ādeśas) are not reaching the loop. Highest-value fix for learners.
- **ṛ-guṇa across padas**: mahA + fzi → *mahazi* (should be maharṣi: 1.1.51 uraṇ raparaḥ after 6.1.87) — also devazi, rAjazi.
- hase~ lṛṭ *hatizyati* (hasiṣyati: 7.4.49 saḥ syārdhadhātuke must not fire across iṭ); qudAY vidhiliṅ *dadAyAt* (dadyāt).
- pragṛhya (1.1.11) cannot be drilled from a bare pada join: the join needs to know the left pada is a dual.
- **Speed:** `pipelines.tinanta.derive` takes ~5 s a cell for some adādi roots (ada~ laṭ: 47 s for 9 cells; all ten
  lakāras 11 min; hana~ 5½ min) against < 0.1 s for bhvādi. The tab therefore reads verified tables first
  (`core/abhyasa.verified_tin`: bank + forms.db cells Vidyut agrees with) and gives live derivation a 10 s budget.
- Homograph upadeśas resolve to the first row (asa~ → 01.1029, jYA → 01.0923, zu → 01.1091): the builder uses pāṭha ids.

## 8. शब्द खोजें + व्युत्पत्तिः (owner, 2026-11-13 15:22–15:27)

"Make a search like sanskritabhyas, so we can make the shabdarūpa of words beyond the list (गार्गी) and check how it is
made from its likely dhātu … use the kośa base text in ~/subhastini to find the origin dhātu, pratyaya etc. and make an
organic rule-based mechanism."

- **Search bar** on `/practice` (`core/abhyasa.search`, POST `/api/abhyasa/search`): list matches (9,007 stems, dhātus);
  an inflected form is placed in its paradigm (रामस्य → राम, षष्ठी एकवचनम्) from the printed ashtadhyayi.com tables; any
  other input is taken as a prātipadika, its liṅga from the printed table, else the kośa entry (स्त्री/पुं/नपुं), else
  its ending; the full table is derived (engine, Vidyut-checked; Vidyut-only cells badged).
- **व्युत्पत्तिः** (`core/vyutpatti.py`, POST `/api/abhyasa/vyutpatti`, `/api/abhyasa/vyutpatti/engine`):
  1. *Proposals* — Subhastini's `lexicon/lex.db` (`$PANINI_LEXDB`; Śabdakalpadruma, Vācaspatyam, Bhāratīkośa, Apte …):
     sūtra numbers, quoted sūtra texts (matched to our registry / uṇādi pāṭha by text), formulas (गर्ग+यञ्+ङीप्, गॄ - ग),
     "इति X" pratyayas, dhātu + artha. Each proposal lists the kośas behind it. Read-only, never committed.
  2. *Verification* — Vidyut regenerates the word from base/dhātu + pratyaya (its sūtra path shown; a near miss shown as
     "Vidyut makes …"); each cited sūtra is checked against its Kāśikā udāharaṇas (or the uṇādi examples); each cited
     sūtra's engine status (`sig/sutra_class.json`); our engine re-derives on request (`engine_check`: taddhita via
     taddhitArtha, kṛt via the vivakṣā table `core/abhyasa.KRT_VIVAKSHA_ENGINE`).
  3. *Recursion* — the base gets the same treatment, down to the dhātu (गार्गी → गर्ग → गॄ + ग, उणादि 1.125).
  4. *Fallbacks* — Kāśikā sūtras whose examples are the word; uṇādi sūtras whose examples are it; Vidyut
     generate-and-test over likely bases (undo ādi-vṛddhi; only bases a dictionary lists) and same-initial dhātus.
- Worked example गार्गी: kośas → गर्ग + यञ् + ङीप् with 4.1.105, 4.1.16, 6.4.150; Kāśikā cites गार्गी under 4.1.16 and
  6.4.150 ✓; **Vidyut makes गार्ग्यी** (misses 6.4.150 after 4.1.16); **our engine makes गार्ग्या** (ṭāp: 4.1.16 यञश्च is
  `unexercised`). Engine gap for the engine agents: real 4.1.16 (ṅīp after yañ, apatya) + 6.4.150 y-lopa on that path.
- asmad / yuṣmad drills now use `pipelines.asmad_subanta` (as `core.analyze.rederive` does) — all 21 cells correct; the
  generic `pipelines.subanta.derive("asmad")` is still wrong beyond 1/1 (§6).

## 7. Log (newest at top)

- **2026-11-13 15:45 [cursor]** — §8 built: search bar, व्युत्पत्ति tree (kośa proposals → Vidyut / Kāśikā / uṇādi /
  engine verification, recursive), asmad/yuṣmad via their own pipeline. Tests: `tests/unit/test_vyutpatti.py` (7).
  `tests/unit/test_abhyasa.py::test_engine_entry_points…[tinanta]` fails only while another agent's cherry-pick leaves
  conflict markers in `pipelines/tinanta.py` (not ours).

- **2026-11-13 11:55 [cursor]** — Full bank built (engine 3e07292d, 1 h 55 min): varṇa 37, it 96, sandhi 52, vākya 270,
  subanta 137, tinanta 468, kṛdanta 131 (15 kṛts), taddhita 17; 602 engine≠Vidyut gaps queued. Claim `abhyasa-shala` released.

- **2026-11-13 10:10 [cursor]** — Owner made sanskritabhyas.in the main reference (§1b). Built: `core/abhyasa.py` (live
  question engine, 12 families × 9 drill types, filters as sanskritabhyas), `tools/abhyasa_vidyut.py` (Vidyut worker:
  sub/tin grids with sanādi + upasarga, kṛt, taddhita, nāmadhātu, sandhi split-back, lipi), `tools/build_abhyasa_bank.py`
  (bank: varṇa, it, sandhi, vākya, subanta, tinanta, kṛdanta, taddhita; writes after every family), `webui/abhyasa.py`
  (blueprint `/api/abhyasa/*`, registered in `webui/app.py` right after `/practice`), new `practice.html` + `abhyasa.js`,
  `data/practice/vakya_lexicon.json` (our lexicon: 29 nouns, 18 verbs, 9 lessons). Tests: `tests/unit/test_abhyasa.py`.
  Nouns/verbs are drilled **live** (any of 9,007 stems / every dhātu); kṛdanta, taddhita, sandhi, vākya come from the bank.
- **2026-11-13 09:50 [cursor]** — Claim `abhyasa-shala` registered (`audit/claims.json`, RUN_LOG §B). Sites surveyed (§1).
  Plan written. Building: bank builder → core → blueprint → page → tests. Engine files are **not** touched.
