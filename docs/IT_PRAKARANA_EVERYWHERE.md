# It-prakaraṇa on every upadeśa (āgama, ādeśa, pratyaya) — engine plan

Owner (2026-11-14): "1.3.2–1.3.9 must generate the it-saṃjñā and do the lopa as applicable — every time it is needed: a
new pratyaya, āgama or ādeśa. Sūtras judge it, and a database of it-saṃjñās exists so later sūtras can refer to it. Both.
And every important change (saṃjñā, insertion, removal, mutation) must be visible; recurring ones (it-lopa) in a summary."

## What already works
- `engine/it_samjna.py` + `pipelines/it_prakarana.py`: the ordered procedure 1.3.2 → 1.3.8 (name) → 1.3.9 (delete). 1.3.9
  writes a **record** on the Term (`it_records`: letter, sūtra, class name kit / ṅit / ṭit / pit / ñīt / ṭvit …) and the tag
  `it:<name>`; later sūtras read `has_it(term, "kit")` etc. 1.3.3 judges **any Term tagged `upadesha`** whose final varṇa is
  hal — so a pratyaya or āgama that enters as its own upadeśa Term is judged automatically (तिप्, लिँट्, णल्).
- Display (done 2026-11-14, `webui/static/prakriya.js`): every इत्संज्ञा-लोपः group shows the upadeśa, each it-letter →
  class (sūtra) and the struck letters; groups appear in the Beginner view; an "इत्संज्ञा-कोशः" table lists every upadeśa's
  it-letters in the derivation (from 1.3.9's own record line).

## What is wrong (audit 2026-11-14, engine f8b26eb2)
1. **Āgamas spliced as bare letters** — no 1.3.x judgment, no record: 7.1.54 नुट् (and 7.1.55), 7.2.35 इट् (+ the 7.2.x iṭ
   family), 6.1.71 तुक्, 7.1.58 नुम्, 7.2.82 मुक्, 3.4.107 सुट्, 7.3.37 युक्, 7.3.93 ईट्, 7.3.92 इम्, 7.4.20 उम्, 7.1.6 रुट्,
   7.2.58 इट्, 8.3.28 कुक्/टुक्, 8.3.29 धुट्, 6.3.67 मुम्, 6.3.74 ~~नुट्~~ **[CORRECTED 2026-11-14: नुड् — ḍit, not ṭit; 1.1.46 names only ṭit/kit, so a ḍit āgama's place needs its own source before it joins a cluster]** … Readers then test private marker tags
   (`nut_agama_inserted` in 7.1.54/55, 6.4.3 **[added]**, 6.4.4, 6.4.6, 6.4.7; `it_agama` — a varṇa tag read by ~20 sūtra files: 1.2.2, 1.2.18, 6.4.51/52/62/64/120, 7.2.4/38/39/40/72–77, 8.2.27/28, 8.3.78/79). Verified: 7.1.54 does `varnas.insert(0, mk("n", "nut_agama_inserted"))`, 7.2.35 `mk("i")` tagged `it_agama` (and 7.2.35 defines `act` twice — a wrapper over `_orig_act` — an Art. 7 smell to clean in the same job); the it-log of rāmāṇām is empty.
2. **Āgama sūtras pre-tag their own it-letters** (the sūtra judges itself): 6.4.88 वुक्, 7.1.52 सुट्, **[added: 3.4.82 (ṇal/thal ādeśa: `it_candidate_cutu`/`halantyam`) and the duplicate table in engine/nal_adi.py]**. **[Verified]** 7.1.52 tags suṭ's ṭ `it_candidate_nit_tu_du`, so the it-log reads ('sAm', 'w', **1.3.5**, name None) — wrong sūtra (ṭ is named by 1.3.3, final hal; 1.3.5 is ñi/ṭu/ḍu *initial of a dhātu*) and no `it:wit`, so nothing can ask "is this ṭit".
3. **उच्चारणार्थ vowels treated as it** **[verified: liṭ log = ('vuk','u','1.3.3', name None), ('vuk','k','1.3.3','kit'); 6.4.88 pre-tags u with `it_candidate_halantyam`]**: 1.3.9's record for वुक् reads "उ → इत् (१.३.३)" — 1.3.3 (हलन्त्यम्) cannot name a
   vowel, and the उ is not an anubandha at all. Sources **[CORRECTED: Kāśikā 3.4.102 is about sīyuṭ — "लिङादेशानां सीयुडागमो भवति। टकारो देशविध्यर्थः। उकार उच्चारणार्थः।" — so it supports vuk only by analogy; Kāśikā 6.4.88 is silent on the u. The direct statements are Bālamanoramā (both quotes below verified verbatim) and Padamañjarī/Nyāsa on 3.2.141]**: Kāśikā 3.4.102 "सीयुडागमो भवति। टकारो देशविध्यर्थः। उकार
   उच्चारणार्थः।"; Bālamanoramā 7.1.54 "नुटि टकार इत्। उकार उच्चारणार्थः। टित्त्वादाद्यवयवः।", 6.4.88 "वुकि ककार इत्, उकार
   उच्चारणार्थः। कित्त्वादन्तावयवः।"; Nyāsa "उकार उच्चारणार्थः — अनुबन्धत्वमस्य निरस्यति". Known dispute: 3.2.141 (शमादि
   घिनुण्) — Kāśikā उच्चारणार्थ vs Bhāṣya अनुबन्ध (SK) → owner ruling needed for that one only.
4. **No lasting register** **[PARTLY FALSE]**: per-Term `it_records` / `it:<name>` tags do vanish at pada merge, but (a) `state.meta["it_lopa_log"]` — 1.3.9 appends every record of the whole derivation in order (sutra_1_3_9.py:183, engine/it_samjna.py META_IT_LOPA_LOG) — survives, it is what the webui table reads; (b) the merger keeps `origin_it:<letter>` tags (engine/phases/pada_merger.py:105, engine/origin.py) and `it_lopa_done` of the dhātu. What is missing is only: āgama/ādeśa it-letters never enter that log, and log rows carry no role/step.

## Design (proposed — needs owner approval, touches 1.1.46 and 1.3.x)
1. **Utter as taught.** One engine helper `engine/agama.py: utter(upadesha_slp1, *, uccarana=…) -> Term` builds the āgama
   / ādeśa as its own Term tagged `agama|adesha` + `upadesha`, `meta.upadesha_slp1` = the taught form (`nuw`), the
   उच्चारणार्थ vowel recorded in `meta.uccaranartha` (from a cited table, never guessed) and not uttered.
2. **1.3.2–1.3.8 judge, 1.3.9 deletes and records** — unchanged machinery; no sūtra pre-tags its own its (remove the
   6.4.88 / 7.1.52 tagging).
3. **1.1.46 / 1.1.47 place it.** **[CORRECTED — see Review §R2: 1.1.46 is today a PARIBHĀṢĀ gate (`GATE_KEY`, no placement act), `phonology/agama_placement_1_1_46.py` is referenced by nothing but its own file; the charts' order is place → remove it-varṇas, not lopa → place; and apply_rule from inside an act is not allowed (Art. 7 / apply_rule law).]** After its it-lopa, a ṭit āgama becomes the first avayava of the following Term, a kit the
   last avayava of the preceding one (1.1.46 आद्यन्तौ टकितौ), a mit after the last vowel (1.1.47) — a structural step through
   `apply_rule("1.1.46")`, visible in the trace. Its varṇas carry `agama:<upadeśa>` so readers ask "is this n the nuṭ?" by
   that tag instead of private markers.
4. **Register.** **[CORRECTED: extend the existing `state.meta["it_lopa_log"]` rows with role (pratyaya/āgama/ādeśa) and step instead of a second store `samjna_registry["it_ledger"]`]** 1.3.9 appends (upadeśa, Term role, letter, sūtra, class, step), which survives merges; `has_it` keeps reading the live Term.
5. **Migration order** (one cluster per commit, focused tests + sig baseline each): नुट् (7.1.54/55 + readers 6.4.4/6/7,
   6.3.74) → इट् (7.2.35 family; readers via `it_agama`) → तुक् 6.1.71 → वुक् 6.4.88 / सुट् 7.1.52 (drop self-tagging) → the rest
   of the list above. Each sūtra file keeps its Art. 14 block; Kāśikā / Bālamanoramā cited for the anubandha reading.
6. **Gate**: `tests/constitutional/` — no `it_candidate_*` tag written outside 1.3.2–1.3.8; every `agama` Term carries
   `upadesha_slp1`; 1.3.9 records exist for every āgama with an anubandha.

## Coordination
Touches core sūtras every derivation runs (1.1.46, 1.3.3, 1.3.9) and readers in 6.4 / 7.1 / 7.2; run by the coordinator
(or one agent with a claim on the whole cluster), never in parallel with other 6.4 / 7.x work. Owner decision pending: who
runs it, and the 3.2.141 उ ruling.

## Review 2026-11-14 (second reader; repo f8b26eb2 + HEAD) — corrections and rulings
Claims verified as stated: nuṭ/iṭ/vuk/suṭ listings and the bare-letter splicing (7.1.54, 7.1.55, 7.2.35, 7.1.52); vuk's u logged under 1.3.3 with no class; Bālamanoramā 6.4.88 "वुकि ककार इत्, उकार उच्चारणार्थः। कित्त्वादन्तावयवः।" and 7.1.54 "नुटि टकार इत्। उकार उच्चारणार्थः। टित्त्वादाद्यवयवः।"; Nyāsa 3.2.141 "उकार उच्चारणार्थः इति। अनुबन्धत्वमस्य निरस्यति". Sūtra ids/names in the list all check (7.1.55 षट्चतुर्भ्यश्च, 7.3.37 शाच्छासाह्वाव्यावेपां युक्, 7.3.93 ब्रुव ईट्, 7.3.92 तृणह इम्, 7.4.20 वच उम्, 7.1.6 शीङो रुट्, 6.3.67 अरुर्द्विषदजन्तस्य मुम्) except 6.3.74 (नुड्, see §1). Not in the report but found: 1.3.3 `_eligible` carries ~8 special exclusions (suT mid-u hack, tAm/ktrim/Rin-in-vin finals, two `corrected_v2_P0xx` demo flags) that any migration must keep.

### R1. 3.2.141 घिनुण् and the u — sourced recommendation
* **Kāśikā 3.2.141**: "घकार उत्तरत्र कुत्वार्थः। उकार उच्चारणार्थः। णकारो वृद्ध्यर्थः।" **Nyāsa** adds "अनुबन्धत्वमस्य निरस्यति। अनुबन्धत्वे सति शमिनौ शमिन इति उगिदचाम् 7.1.70 इति नुम् प्रसज्येत। इह शमिनितराम्… उगितश्च 6.3.45 इत्यन्यतरस्यां ह्रस्वत्वम्" and **Padamañjarī** "नायमनुबन्धः… घरूपकल्पचेलड् [6.3.43] इति नित्यमिष्यते" — i.e. Kāśikā school: u not it → hrasva nitya (शमिनितरा only).
* **Bhāṣya 3.2.141** (vārttika "घिनण्यं वक्तव्यः"): objects that with ghinuṇ (u as it) 7.1.70 would give *śaminau, and answers "झल्ग्रहणं तत्र चोदयिष्यति" (num only for jhal-ending stems); and for 6.3.45 "इष्यत एव ह्रस्वत्वम्" — accepts ugit-ness. **Kaumudī 3.2.141** (verbatim): "उकार उच्चारणार्थ इति काशिका। अनुबन्ध इति भाष्यम्। तेन शमिनितरा शमिनीतरेत्यत्र उगितश्च इति ह्रस्वविकल्पः। न चैवं शमिनावित्यादौ नुम्प्रसङ्गः। झल्ग्रहणमपकृष्य झन्तानामेव तद्विधानात्।"
* So the rulings **differ observably**: Kāśikā → शमिनितरा / शमिनितमा only; Bhāṣya+Kaumudī → शमिनितरा / शमिनीतरा (vibhāṣā). **Recommend**: engine default = Bhāṣya/Kaumudī (u is an anubandha of ghinuṇ → `udit` → 6.3.45 vikalpa; num blocked by the jhal-grahaṇa apakarṣa) because the project's scope is Laghukaumudī/Siddhāntakaumudī and Art. 21 prefers explicit vibhāṣā exploration; record the Kāśikā reading as a declared alternative pakṣa (Art. 23 grade: Kāśikā = primary text, Bhāṣya = higher authority on conflict — owner's call; either way the choice must be one explicit table entry, not a code branch). For **vuk, nuṭ, suṭ, iṭ, tuk, num… no such dispute is found in the DB**: u/ī/ṭ-less vowels in these are uccāraṇārtha by Bālamanoramā; the 3.2.141 ruling does not block the first clusters.

### R2. Order of naming, placement and lopa; 1.1.46's real status
* Sources agree naming comes first (the āgama is ṭit/kit/mit *because* 1.3.3 named its it-letter: Padamañjarī 1.1.46 "इत्संज्ञकत्वेन देशविशेषो लक्ष्यते…"; Bālamanoramā "टित्त्वादाद्यवयवः"). Neither Kāśikā nor Nyāsa on 1.1.46 fixes lopa-before-placement. The **13-box chart** and **Neelesh's 9-step list** both put "do the āgama" *before* "remove the it-varṇas from the āgama" (PRAKARANA_MACHINE_PLAN §10). So the order to implement is **utter → 1.3.2–1.3.8 name → place (1.1.46/1.1.47) → 1.3.9 lopa**, not the draft's lopa → place. The ṭit/kit/mit class must therefore be read from the *named* (still present) letter, or from the kept record; both exist.
* 1.1.46 is a **PARIBHĀṢĀ** in the engine (`GATE_KEY` flag, no tape effect). Making it an acting placement sūtra changes its type and its 40 references. Two options: **(a)** keep it a paribhāṣā; each āgama vidhi's act inserts at the side given by a shared pure reader of the *taught form's* named class (extend `phonology/agama_placement_1_1_46.py` — exists, unused — with mit); **(b)** insert unplaced, let the scheduler pick 1.1.46/47 as acting rules. (a) is smaller and is what the aṭ/ṣuk sūtras already do by hand; (b) is more faithful to "visible step" but must not be done by apply_rule *inside* an act (law). **Recommend (a) for the first clusters**, plus the *naming* done by the scheduler (1.3.3 on the just-entered āgama Term) before the vidhi's placement is final — if that ordering cannot be got without bundling, entering the Term with its named class from `upadesha_slp1` is the fallback and is still strictly better than a bare letter.
* uccāraṇārtha vowel: not an it, not deleted by 1.3.9; it simply is not on the tape (nuṭ → n + ṭ(it)); store it in `meta.uccaranartha` from a cited table.

### R3. Fit with the machine plan, Art. 7, Art. 21
* Boxes 4, 6, 8 (it-lopa of āgama / ādeśa / second āgama) are exactly the missing it-steps — this plan is the implementation of those boxes; keep the box number as the stage label of each logged step.
* Art. 7: `engine/agama.py: utter()` is a Term-builder called from the vidhi's own act; no sūtra may call another sūtra from act. One cluster = sūtra files + readers, never a bundle.
* Art. 21 is untouched (no scheduling change). Constitutional tests at risk: `test_no_varnas_direct_write_outside_act`, `test_glassbox_ratchet`, `test_exempt_ratchet`, `test_astadhyayi_kram_respected`, `test_no_new_arm_gates`; the proposed gate must be added with a ratchet baseline, not a hard zero (3.4.82 and nal_adi also self-tag).

### R4. Cost and smallest safe first cluster
* Files: nuṭ cluster = 7.1.54, 7.1.55 + readers 6.4.3, 6.4.4, 6.4.6, 6.4.7 (7 files, all with `nut_agama_inserted`) + `phonology/agama_placement_1_1_46.py` + a new engine helper; iṭ = 7.2.35 + the ~20 `it_agama` readers; whole list ≈ 25–35 sūtra files (the draft's "~25" is about right; the draft's "roughly 25 + 1.1.46, 1.3.3, 1.3.9" — under option (a) 1.1.46 and 1.3.9 need no change at all; 1.3.3 only for the tag-vs-eligibility rule).
* Tests at risk for the nuṭ cluster: 8 test files mention 7.1.54/55/nut/ nuw or the gen-pl forms (test_pUrvaparANAm_dvandva, test_sarva_unified_subanta, test_SamBu_subanta, test_abhyasa, test_1_4_6_nadi_vibhasha, test_amba_fixtures, test_lk_p64a, test_shabda_paradigms) + `tests/regression/data/paddhati_subanta_ai_u.json`, `brain_declension_cells.json`, `sig_applied_paths_baseline.json`; 30 test files mention "1.3.9" (any exact-trace assertion gains a 1.3.3/1.3.9 row for the āgama); sig/*.json baselines (sig_baseline, sig_transitions, global_sutra_edges) will shift and need a ratchet re-baseline.
* **First cluster: nuṭ only (7.1.54, 7.1.55)**, genitive plural: focused tests = rAma/hari/nadI/vaDU/mAlA/Denu + 6.4.3 cases (rAmARAm, hariRAm, nadInAm, vaDUnAm, mAlAnAm, DenUnAm, catasfRAm, nfRAm/nFRAm, SaRRAm) asserting (i) form unchanged, (ii) log has ('nuw','w','1.3.3','wit'), (iii) no `nut_agama_inserted` tag read by 6.4.3/4/6/7, (iv) ṭit placement before Am; then the five test files above, then re-baseline sig.

### R5. Recommendation: start now vs hand off
Not "start now". The change is mostly mechanical for nuṭ but (1) two design points in this draft are wrong (order; 1.1.46 type/apply_rule), (2) 7.2.35's iṭ is read by ~20 files and 6.4.x/7.x are being edited by other agents, (3) the sig re-baseline touches shared files. **Hand to the coordinator as one claimed job**, nuṭ cluster first with option (a), after the owner rules on R1 (default: Bhāṣya/Kaumudī for 3.2.141) and R2 (a vs b).

## Owner rulings (2026-11-14)
1. **3.2.141 / vuk-type u:** default = Bhāṣya (Kaumudī "अनुबन्ध इति भाष्यम्"): the u is an anubandha (it-marker), so the vibhāṣā readings both hold. The Kāśikā / Nyāsa / Padamañjarī reading (u uccāraṇārtha → only hrasva) is recorded as an explicit alternative, not the default.
2. **1.1.46 ādyantau ṭakitau** stays a **paribhāṣā** read by each āgama sūtra (the sthāna of the āgama), never an acting vidhi sūtra and never called via apply_rule from inside another act.
Consequence: the nuṭ cluster (7.1.54/55 + readers 6.4.3/4/6/7) can be claimed as one coordinated job; order = name it-letters → place by 1.1.46 reading → 1.3.9 lopa, extending `state.meta["it_lopa_log"]`.


## Shipped 2026-11-15 (cursor) — इट् cluster

Owner screenshot on `/dhaturupa` (स्कुन्द् + स + आथाम् → bare इ) is the go-ahead. Implemented option (a) of §R2 as a
**segment inside the host**, not a separate Term:

1. `engine/agama.py` — `utter_into(state, term, at, upadesha)` puts the taught letters at the 1.1.46 position the vidhi
   already chooses; tags them `agama_seg:<upadeśa>#n`. UCCARANARTHA table (cited) drops the उ of नुट्/तुक्/वुक्… before
   utterance. `pending_segments` / `close_judged` / `is_agama_letter`.
2. 7.2.35 — four insert branches call `_utter_it` → `utter_into(..., "iw")`; the leftover इ keeps the grandfathered
   `it_agama` tag so the ~20 readers keep working.
3. 1.3.3 — `_segment_finals` names the final hal of every unjudged āgama segment; why_now names "इट् (आगमः) — ट्".
4. 1.3.9 — deletes segment its, writes them via `record_agama_it_lopa` into `host.meta["agama_it_records"]` and
   `state.meta["it_lopa_log"]` with `agama=<upadeśa>` (the host never becomes `it:wit`); marks the leftover segment
   letters `agama_it_done`. Summary: "इट् (आगमः) — ट् → टित् (१.३.३)".
5. `engine/it_samjna.it_lopa_already_done` / `upadesha_residue` ignore āgama letters in the host's residue.
6. Dispatcher post-hook (`_it_prakarana_on_new_agama`): after any non-1.3.x `apply_rule` that left a pending segment,
   runs `pipelines.it_prakarana.run_it_prakarana` (sequence lives in pipelines/, no bare sūtra-id literals in engine/).
   Covers every recipe call site and the loop in one place.
7. Focused test: `tests/unit/test_it_prakarana_agama.py` (स्कुन्दिषाथाम् / भविष्यति). Hindi hint for 7.2.35 cleaned.

**Not yet:** नुट् (7.1.54/55 + 6.4.3/4/6/7 readers) — next cluster; वुक्/सुट् self-tagging; the rest of the bare-letter list.
Sig / notes-audit / brain-mirror / upadeśa-input failures on this HEAD are the same on bare `main` (pre-existing).


## Shipped 2026-11-15b (cursor) — याट् / स्याट् + 8.4.68

Owner screenshot रमायै: engine jumped 7.3.113 → 6.1.88 with bare या (no ट्, no 1.3.x); Vidyut shows
1.3.3 याट् → 1.3.9 या → 6.1.88 य्+ऐ → 8.4.68.

1. **7.3.113** utters ``yAw`` via ``engine.agama``; dispatcher runs 1.3.3/1.3.9 (ट् → टित्, deleted).
2. **7.3.114** same for ``syAw``.
3. **8.4.68**: act tags short ``a`` as ``samvrta`` (Mahābhāṣya saṃvṛtāpratyāpatti); ``pipelines/subanta`` applies it
   after the tripāḍī VIDHI pool (ANUVADA was excluded from that pool — tinanta already called it via recipe /
   ``execute_tripadi_phase``).

Still bare-letter (next): नुट् 7.1.54/55, तुक्, नुम्, मुक्, सुट्, युक्, ईट्, … (see §What is wrong).


## Shipped 2026-11-15c (cursor) — नुम् family

Owner screenshot: 7.1.58 कुथ् → कुन्त्थ् as bare न्. Now ``utter_num`` (उच्चारणार्थ उ dropped) → 1.3.3 म् → मित् →
1.3.9 deletes; leftover न् keeps ``num_agama``. Same for 7.1.59 / 7.1.60 / 7.1.69. 1.3.9 summary names the taught
āgama (नुम्), not the uttered residue.


## Shipped 2026-11-15d (cursor) — अट् / आट्

Owner: 6.4.71 कुन्थ्अव → अकुन्थ्अव as bare अ. Now ``utter_at`` / ``utter_at(..., dirgha=True)`` for 6.4.71/72;
1.3.3 ट् → टित्, 1.3.9 deletes; leftover अ/आ keeps ``aT_agama_v``.


## Shipped 2026-11-15e (cursor) — lakāra 1.3.2

laṅ/loṭ recipes called only 1.3.3+1.3.9 after attach, so अँ of लँङ् never became इत् and 3.4.78
saw ``la~``. Now 1.3.2 runs too: लँङ् — अँ → अदित्, ङ् → ङित्; only ल् remains before तिङ्.


## Shipped 2026-11-15f (cursor) — लृँङ् keeps ङ् for 1.3.3

``3.3.139`` deleted final ``N`` after ``lakara_varnas("lfN")``, so 1.3.3 never named ङ् and the
ledger showed only ऋँ → ऋदित्. Full लृँङ् stays; 1.3.2 + 1.3.3 + 1.3.9 leave ल्.
