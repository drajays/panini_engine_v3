# Plan: taddhita gaps fixed by rule (from docs/TADDHITA_BASICS_CHECK.md; tests tests/regression/test_taddhita_basics.py)
Method: apply_rule / loop only; one sūtra one file; vivakṣā literals (Amendment 25); shortcut = `# SHORTCUT Sn` + ledger; else strict xfail. Serial, one commit per step.

| # | Step | Sūtras | Test (xfails flipped) | Status |
|---|---|---|---|---|
| 1 | Order: vṛddhi before ṭi-lopa; pada/bha after the pratyaya's ādeśa | 7.2.117 over 6.4.148 in `CONFLICT_OVERRIDES` (AMENDMENT_19 addendum); 1.4.17 waits while 7.1.2 / 7.3.50 is pending | test_vrddhi_before_ti_lopa_for_nit_ait, test_pada_bha_decided_after_adesha | done |
| 2 | matup / vini / ḍmatup in the loop | the deck's `asti` was the cāturarthika sense (4.2.67): matup needs `astyasya` (5.2.94); 1.4.19 real (bha for t/s-final aṅga before a matvarthīya), 4.2.87 real (ḍmatup, apavāda of 4.1.83), 8.2.9 / 8.2.10 accept ḍmatup | garutmat, yaśasvin, kumudvān (+ test_matup_vini_by_rule: 1.3.2, 1.4.19, 7.2.70 garutmantau) | done; naḍa has both 4.2.87 and 4.2.88: strict xfail (S45/S52) |
| 3 | ḍhak -eya family | 4.1.123 real (śubhrādi), 4.1.120 reads the strī-pratyaya origin (was dead: tag typo `strIliNga`); chain.strI records ṭāp as origin | vainateya (chain), śaubhreya, bhārateya, gaudheya | done; mṛkaṇḍu, pārśva: strict xfail (below) |
| 4 | strī in taddhita / chain | 4.1.15 apavāda of 4.1.4 and reads ika as ṭhak (origin_sthanin, 1.1.56); 4.1.41 real (ṣit, gaurādi) via `append_stri`; 1.4.13 / 1.4.18 take a strī-pratyaya; 4.1.4 stops after a strī-pratyaya | aupagavī, ākṣikī, dādhikī, gaurī, ṣit stem | done |
| 5 | samarthatā gate | 2.1.1, 4.1.82 | test_samarthata_is_a_named_gate (strict xfail) | blocked |
| 6 | Svara | 3.1.3, 6.1.164/165/185/197/217 | test_svara_by_itletter (strict xfail) | blocked |

## Blockers / notes
- Step 2: ghost `ika` etc. unaffected. naḍa + `asti`: 4.2.88 (para) wins and 4.2.87 is lost; both readings (naḍvān, naḍvalaḥ) need the loop to explore between competing sūtras (ledger S45/S52). Kāśikā 4.2.87 gives both.
- Step 3, mṛkaṇḍu: Kāśikā 4.1.123 lists मृकण्डु; `data/inputs/ganapatha_full.json` has `sfkaRqu` in SuBrAdiH (built by tools/intake_patha.py). Art. 22 conflict: owner ruling or upstream correction, not a code change.
- Step 3, pārśva: SK 1.4.16 teaches `parśūnāṃ samūhaḥ pārśvam` (ṇas) from a gaṇa-vārttika; no sūtra row carries it (5.3.117 parśvādi gives aṇ/añ svārtha). Needs the vārttika layer (Art. 18 gap). 4.1.129 godhāyā ḍhrak is still a stub (no `Qrak` rule in 7.1.2).
- Step 4, unrelated find: `chain.krt(...)+strI` gives pAWakA; 7.3.44 (ikā) is not reached.
- Step 5: the loop starts from a stem + the vivakṣā `taddhitArtha`; the word the stem is related to is not on the tape, and no samagra names vyapekṣā / ekārthībhāva, so Amendment 25 cannot admit a value. Needs a sentence/vṛtti layer (the related pada) first.
- Step 6: there is no accent tape (no udātta/anudātta/svarita on `Varna` or `Term`; 6.1.164/165/185/197/217 are gate stubs; 3.1.3 only opens the adhikāra). A svara step needs a pitch attribute on each varṇa carried through it-lopa/ādeśa/sandhi (1.1.50 sthānivat, 8.2.4 etc.) before any of these sūtras can be real. Not invented here.
