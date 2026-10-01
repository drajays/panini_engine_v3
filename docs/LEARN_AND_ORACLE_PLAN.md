# Learner UI + oracle-driven engine plan (2026-10-01)

Source review: openpathshala.com's "verb formation" page (three stations, one
equation bar) and the rkmvu.ac.in Grammar site (a static front-end over
`vidyut_prakriya.wasm` plus the ashtadhyayi.com corpus, with strict provenance
tags). Neither has a derivation engine of its own, so what we take from them is
presentation and data, not rule logic. Rule logic stays with
CONSTITUTION Art. 0/11/13.

## What already existed (not to be rebuilt)

- `bench/run.py` + `bench/oracle_vidyut.py`: Vidyut differential on 417 cells.
- `bench/ashtadhyayi_gold.py`: 455,346 tiṅanta cells and 215,155 subanta cells
  against ashtadhyayi.com's tables (93.6% and 90.4% agreement as of 2026-09-30).
- `data/reference/ashtadhyayi_com/` already vendored at a pinned commit.

## Done this session

| Item | Result |
|---|---|
| Oracle input fix | Vidyut was asked with unaccented aupadeśika (`pA` and not `pA\`), so it treated anudātta roots as seṭ and missed 7.3.78 / 6.4.110. Fixed spellings in `bench/oracle_vidyut.py`, then refreshed the CSV. Agreement went from 83.0% to **100% (417/417)**. |
| 7.2.58 गमेरिट् परस्मैपदेषु | Was a gate-flag placeholder, so 7.2.10 blocked iṭ and the engine gave *gamsyati*. It is now a real vidhi scheduled after 7.2.35: गमिष्यति, अगमिष्यत्; ātmanepada संगंस्यते keeps the niṣedha. |
| 8.3.24 नश्चापदान्तस्य झलि | Now covers the dhātu's म् (anuvṛtti मः, Kāśikā आक्रंस्यते): गम्+ता gives गन्ता (previously *gamtA*). A pūrvapada-final म् (परंतपः) is left to 8.3.23. |
| Trace `parts` | `engine/trace.py:term_parts` records `[letters, role, upadeśa]` per Term on form-changing APPLIED steps. This is display metadata only and is not read by any `cond()`. |
| `docs/data/sutras.json` | pāṭha, padaccheda, Kāśikā udāharaṇa and a `ph` (placeholder) flag for all 3,983 sūtras. |
| `docs/learn.html` | Stepper with an equation bar (भव् + अ + ति, with the upadeśa shown under each part), a phase ribbon taken from the sūtra's adhyāya/pāda, a highlighted diff, rule and why-here lines, Kāśikā examples, and a "rules checked before this one" list. Also a predict-the-next-sūtra quiz (decoys are the rules the engine actually rejected at that point), an expert toggle, deep links (`#slug/stepN`), and provenance tags. |

## Engine findings (work queue, by leverage)

Both counts below are now ratcheted by `tests/constitutional/test_glassbox_ratchet.py`
(`python3 -m tools.glassbox_gaps --list` shows every case). Lower the ceilings
when a fix lands.

1. **Placeholder sūtras: 917 → 915.** These files only set
   `state.meta["anga_kind"]` and change nothing. 6.3.111 and 6.3.112 are now
   real rules, as is 8.3.13 (which used a different placeholder key). Next:
   convert the placeholders that the gold-bench clusters point at.
2. **Unrecorded form changes in traces: 93 → 48.** 3.2.123 वर्तमाने लट् now
   attaches laṭ itself (`P00_lat_vartamane`), and 3.3.13 लृट् शेषे च attaches
   lṛṭ (it had been a kṛt-template file that always skipped). Upasarga
   attachment is recorded as a `__UPASARGA__` structural row. What's left is
   per-lesson: taddhita/yaṅ affix insertion after 3.1.3 (~13), सु added to
   avyayas before 1.1.38 (~8), and one-offs.
3. **Gold-bench clusters fixed (2026-10-01).** 93.8% (426,906 / 455,346)
   → **96.0% (437,070)**, 0 errors, 0 cells that agreed before now differ
   (`.audit/gold_diff_baseline.jsonl` vs `.audit/gold_diff.jsonl`).
   - laṅ 2sg of ṛ-final roots: 6.1.68 now runs after guṇa + raparatva, and
     8.3.15 takes any pada-final repha (anuvṛtti रः), not only ru
     (अजागः, अपिपः, अजहः, अससः).
   - Data: 01.0208 पेबृँ is ṛdit (`pebf~`, like पेवृँ); 06.0174 फुल is not kuṭādi.
   - 1.2.1 गाङ्कुटादिभ्योऽञ्णिन्ङित्: the kuṭādi antargaṇa now makes the next
     affix ṅit (कुटिता, चुकुटिथ, अकुटीत्; चुकोट / अकोटि keep guṇa because ṇal and
     ciṇ are ṇit). It runs in `P00_guna_7_3_84` / `P00_guna_7_3_86`.
   - 1.1.51 उरण् रपरः after every 7.3.84 (स्मरतु, अवर्कत).
   - 6.4.24 अनिदिताम्: it no longer deletes 7.1.58's num on idit roots after
     the ṇic merge (स्फुण्ड्यते, तुञ्ज्यते, पंस्यते).
   - 8.4.54 अभ्यासे चर्च on the merged caṅ pada (अबभक्षत्, अजघट्टत्).
   - 6.1.73 छे च after aṭ and on the liṭ abhyāsa (अच्छषत्, चच्छाद).
   - 6.4.64 now runs before 6.1.88 in liṭ (ददे, तस्थे, जज्ञे; previously ददै).
   - 8.2.31 हो ढः yields to 8.2.32/8.2.34, and the tripāḍī tape treats a guṇa
     ādeśa inside the root as sthānivat (दोग्धा, दोग्धि, नद्धा).
   - 8.3.13 ढो ढे लोपः + 6.3.112 / 6.3.111 (लेढा, लीढ, वोढा). 6.3.111/112 see
     the tripāḍī lopa through a cited exception in
     `data/inputs/asiddha_strata.json` (`tripadi_nimitta_exceptions`).
   - Data: 01.0925 was stored as छदिः (the इक्-citation form). It is now छदँ.
4. **Open question, अचच्छन्दत्.** Strict order (aṭ, then 6.1.73 tuk, with
   8.4.54 asiddha) gives अच्चच्छन्दत्. The tables read अचच्छन्दत्. The aṭ
   helper currently skips 6.1.73 when a caṅ abhyāsa follows; this needs a
   Kāśikā / Bhāṣya source before it is treated as settled.
5. **Next clusters** (from `.audit/gold_diff.jsonl`): curādi adanta liṭ ām
   (काथयाञ्चक्रे instead of कथयाञ्चक्रे, ~640), luṅ seṭ vṛddhi 7.2.7
   (असलीत् vs असालीत्, ~400), nitya-san roots 3.1.5–6 (गुप्→जुगुप्सते,
   मान्→मीमांसते, ~1,400), ārdhadhātuka ādeśas 2.4.52/53 (अस्→भू, ब्रू→वच्),
   āśīrliṅ 6.4.24 on anidit nasal roots (तुप्यात्), 7.1.100 ॠत इद्धातोः
   (दीर्यात्), and 7.1.61 रधिजभोरचि (जम्भते).
6. `why_dev` prose quality: some rows (for example 6.1.78) carry essay text.
   The learner page displays it verbatim, so it needs a cleanup pass.
7. संगंस्यते surfaces as *saNgamsyate*: on the upasarga + ātmanepada path the
   gam म् reaches the tripādī without 8.3.24 (multi-term tape).

## Next phases

- **Bench widening.** Add more roots to `bench/grids.py`, each with an
  explicit Vidyut accented spelling, and run `bench.ashtadhyayi_gold`
  nightly with per-cluster diff reports in `bench/report/`.
- **Learner pages from the rkmvu map.** Sūtra page = text + Kāśikā + every
  trace where the sūtra fired or was rejected (a reverse index from
  `docs/data/traces`). Also dhātu-rūpa and śabda-rūpa grids where each cell
  links to its learn.html trace and failures are shown openly.
- **Utsarga/apavāda card.** When a BLOCKED row precedes an APPLIED row, show
  "X beat Y because …" from the resolver event.
