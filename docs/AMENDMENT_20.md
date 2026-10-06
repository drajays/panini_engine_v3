# AMENDMENT 20 — Art. 4 made true in the files: mūla pāṭha + samagra; anunāsika ≠ anusvāra

**Status:** ACCEPTED 2026-10-06 (Art. 10 §1–3).

## 1. Problem

- Art. 4 said `text_slp1` / `text_dev` are the *anuvṛtti-complete* form, with 1.3.3 as the example. ~3,900 of 3,983
  files store the **mūla pāṭha** there (1.3.3 = `halantyam`), and tests, the trace UI, the practice quiz and the API
  rely on that. The Article and the code disagreed; changing the files to match the old wording would break readers.
- Anunāsika was not handled uniformly. `phonology/joiner.py` moved ँ off its vowel (`sa~Sca` → सशँच; `Ga~wa` and
  `Gawa~` both → घटँ). `parse_slp1_upadesha_sequence` put a `~` written after a consonant on the nearest *earlier*
  vowel (`han~` → h·a~·n), i.e. the wrong vowel for 1.3.2.

## 2. Change

1. **Art. 4 rewritten.** `text_*` = mūla pāṭha (ashtadhyayi.com `data.txt` `s`, T0), unchanged in every file. New
   `SutraRecord` fields `samagra_slp1` / `samagra_dev` = the anuvṛtti-complete sentence (`data.txt` `ss`); where `ss`
   is empty (2,413 sūtras) it is composed from adhikāra + padas + anuvṛtti and the file says so. Metadata only.
   1.3.3 now reads `text_slp1 = "halantyam"`, `samagra_slp1 = "upadeSe antyam hal it"`.
2. **Art. 4 §2 — anunāsika ≠ anusvāra.** ँ = `anunasika` tag on the vowel it is written on (SLP1 `~` right after it);
   `~` after a consonant = that consonant's anunāsika inherent `a` (`han~` = `hana~` = हनँ, `qupac~z` = डुपचँष्);
   ं = varṇa `M`. Never merged. Joiner and parser fixed accordingly; joiner ∘ tokenizer is the identity on all
   1,532 anunāsika-bearing upadeśas/words in ashtadhyayi.com.
3. **Anunāsika conflicts are decided by 1.3.2 itself:** the upadeśa whose it-saṃjñā (1.3.2–1.3.8) + lopa (1.3.9)
   yields the attested form is the right one. Applied here:
   - `BvAdi_dfSir` (curated extension) had lost its ँ: दृशिर् → **दृशिँर्** `dfSi~r` — the canonical row 01.1143's
     upadeśa. The engine now strips `ir` (vārttika इर इत्संज्ञा वाच्या) and records *irit* (3.1.57).
   - Engine it-prakaraṇa on all 2,240 dhātus of `data/inputs/dhatupatha_upadesha.json` now matches what
     1.3.2/1.3.3/1.3.5 + the irit vārttika dictate (was 2,239).
4. **Art. 14 citation** `ashtadhyayi.com data.txt row i=<a p nnn>` in every sūtra file (3,577 added; 37 malformed,
   e.g. `601077`, corrected).
5. **`data/inputs/sutra_context.json` pāṭha** (`scripts/build_sutra_context.py`): workbook text that differs from T0
   is corrected to T0 (201) — except where the only difference is an added ँ marking a pratijñā-anunāsika it-vowel
   (क्विँप्, घिनुँण्: 9 kept). Owner overrides untouched. All 210 logged in `sutra_context.conflicts.json` → `text`.

## 3. Evidence

ashtadhyayi.com `sutraani/data.txt` (`s`, `ss`, `an`, `ad`, `pc`) — T0; `dhatu/data.txt` + `vidyut_dhatupatha.tsv`
(aupadeśika). Kāśikā on 1.3.7 for the pratyaya-initial छ/झ/ठ/ढ that are not it (used by the reference brain's check).

## 4. Pinned by

- `tests/constitutional/test_samagra_baked_in.py` — samagra on every record; 1.3.3 example; row-i citation in every file.
- `tests/constitutional/test_anunasika_anusvara_distinct.py` — ँ/ं distinct; round trips; `Ga~wa` ≠ `Gawa~`;
  `han~` ≡ `hana~`; dhātupāṭha Devanāgarī ↔ SLP1 agree on every anunāsika; engine it-prakaraṇa on all 2,240 dhātus.

## 5. Acceptance (Art. 10 §3)

Accepted in writing by drajayshukla (owner), 2026-10-06: "Accept AMENDMENT 20 — yes — correct it and give handover
to that repo agent; from now onward agent will read this repo as brain." (Requested earlier the same day: "do amendment
but don't break anything … handle anunasik correctly … also apply in our engine.")

## 6. Test record

`python3 -m pytest tests/` on branch: **13 failed, 20,212 passed** (29 skipped, 3 xfailed). Untouched `main` HEAD:
13 failed, 20,189 passed. The 13 failures are identical on both and environmental (missing practice/notes fixture
files; untracked `data/upstream/ashtadhyayi_dhatu_data.json`). No new failure.

## 7. Found, not changed (needs the owner)

`raw_dhatu_after_it_lopa_slp1` in `dhatupatha_upadesha.json` (legacy v2 field, read by 9 modules) is wrong in 274 rows:
it applies 1.3.7 to dhātus (`Rada~` → `ad`), drops idit consonants (`awi~` → `a`), misses 1.3.3 (`trapU~z` → `trapz`),
and folds in 6.1.64/6.1.65 (`zvid` → `svid`). The engine's own it-prakaraṇa is right on all of them.
