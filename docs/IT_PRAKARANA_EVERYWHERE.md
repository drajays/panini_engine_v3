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
   7.2.58 इट्, 8.3.28 कुक्/टुक्, 8.3.29 धुट्, 6.3.67 मुम्, 6.3.74 नुट् … Readers then test private marker tags
   (`nut_agama_inserted` in 7.1.54/55, 6.4.4, 6.4.6, 6.4.7; `it_agama` for iṭ).
2. **Āgama sūtras pre-tag their own it-letters** (the sūtra judges itself): 6.4.88 वुक्, 7.1.52 सुट्.
3. **उच्चारणार्थ vowels treated as it**: 1.3.9's record for वुक् reads "उ → इत् (१.३.३)" — 1.3.3 (हलन्त्यम्) cannot name a
   vowel, and the उ is not an anubandha at all. Sources: Kāśikā 3.4.102 "सीयुडागमो भवति। टकारो देशविध्यर्थः। उकार
   उच्चारणार्थः।"; Bālamanoramā 7.1.54 "नुटि टकार इत्। उकार उच्चारणार्थः। टित्त्वादाद्यवयवः।", 6.4.88 "वुकि ककार इत्, उकार
   उच्चारणार्थः। कित्त्वादन्तावयवः।"; Nyāsa "उकार उच्चारणार्थः — अनुबन्धत्वमस्य निरस्यति". Known dispute: 3.2.141 (शमादि
   घिनुण्) — Kāśikā उच्चारणार्थ vs Bhāṣya अनुबन्ध (SK) → owner ruling needed for that one only.
4. **No lasting register**: per-Term records vanish when the pada is merged (final state has none).

## Design (proposed — needs owner approval, touches 1.1.46 and 1.3.x)
1. **Utter as taught.** One engine helper `engine/agama.py: utter(upadesha_slp1, *, uccarana=…) -> Term` builds the āgama
   / ādeśa as its own Term tagged `agama|adesha` + `upadesha`, `meta.upadesha_slp1` = the taught form (`nuw`), the
   उच्चारणार्थ vowel recorded in `meta.uccaranartha` (from a cited table, never guessed) and not uttered.
2. **1.3.2–1.3.8 judge, 1.3.9 deletes and records** — unchanged machinery; no sūtra pre-tags its own its (remove the
   6.4.88 / 7.1.52 tagging).
3. **1.1.46 / 1.1.47 place it.** After its it-lopa, a ṭit āgama becomes the first avayava of the following Term, a kit the
   last avayava of the preceding one (1.1.46 आद्यन्तौ टकितौ), a mit after the last vowel (1.1.47) — a structural step through
   `apply_rule("1.1.46")`, visible in the trace. Its varṇas carry `agama:<upadeśa>` so readers ask "is this n the nuṭ?" by
   that tag instead of private markers.
4. **Register.** 1.3.9 also appends to `state.samjna_registry["it_ledger"]` (upadeśa, Term role, letter, sūtra, class, step),
   which survives merges; `has_it` keeps reading the live Term.
5. **Migration order** (one cluster per commit, focused tests + sig baseline each): नुट् (7.1.54/55 + readers 6.4.4/6/7,
   6.3.74) → इट् (7.2.35 family; readers via `it_agama`) → तुक् 6.1.71 → वुक् 6.4.88 / सुट् 7.1.52 (drop self-tagging) → the rest
   of the list above. Each sūtra file keeps its Art. 14 block; Kāśikā / Bālamanoramā cited for the anubandha reading.
6. **Gate**: `tests/constitutional/` — no `it_candidate_*` tag written outside 1.3.2–1.3.8; every `agama` Term carries
   `upadesha_slp1`; 1.3.9 records exist for every āgama with an anubandha.

## Coordination
Touches core sūtras every derivation runs (1.1.46, 1.3.3, 1.3.9) and readers in 6.4 / 7.1 / 7.2; run by the coordinator
(or one agent with a claim on the whole cluster), never in parallel with other 6.4 / 7.x work. Owner decision pending: who
runs it, and the 3.2.141 उ ruling.
