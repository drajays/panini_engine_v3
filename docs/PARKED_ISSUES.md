# PARKED_ISSUES — minor / peripheral, narrow-area items to resolve later

Not blockers. Add one line per item: area · what · evidence · what is needed.

## tiṅanta
- caha~ (curādi): CLOSED — engine right (mit row 10.0120, SK 6.4.92 cahayati); see docs/PARKED_ISSUES_RESOLVED.md.
- fRu~ loṭ 2sg: VERIFIED engine bug (arRu); needs guṇa-before-6.4.106 ordering + the vibhāṣā fork (aguṇa fRu / guṇa arRuhi). Waits on vikalpa support.
- gurI~: CLOSED — engine right (kuṭādi 1.2.1, brain dhātu row 6.0131).
- bhvādi sf luṅ (`asArzIt`) and bhvādi Divi~ (`Dinvati`): engine right per SK / 3.1.80; Vidyut differs. Only a note.
- vibhāṣā alternates not generated (one form per cell): ūrṇu liṭ, kṛṣ-type sic fork.
- Intermittent: hrage~ / fDu~ liṭ lost 6.1.8 once in one ledger_recheck run; a full-suite run hung once at bhū laG-2-2. Not reproducible (12 reruns, 12 hash seeds).
- SK §43: 40 gate-only sūtras (docs/SK43_COVERAGE.md): prefix-dependent ṣatva/ṇatva (8.3.117/118, 8.4.14), liṭ samprasāraṇa of vye/hve (6.1.15–19, 37–40) — verified implementable, correct numbers in PARKED_ISSUES_RESOLVED.md.
- Stale recipe pipeline disagrees with the (correct) loop for ajādi ṇijanta caṅ (awwa~) — recipe is being retired, ignore.

## subanta (from the 9,005-stem ashtadhyayi.com gold sweep, 2026-10-06; harness = bench/ashtadhyayi_gold.py --kind subanta)
Remaining differences are almost all *not* missing sūtras but missing stem metadata. Each needs a stem-origin input (like `ugit`, `tfc`, `han_dhatu`) or samāsa/upasarga info:
- Compound / upasarga stems: ṇatva & ṣatva across a member boundary (antarmanas→antarmanāḥ not antarmaṇaḥ, caturānana, citrabhānu, prakampana, kṛmighna, tryahna): ~1,000 cells. Needs samāsa/upasarga metadata (8.4.1 "samānapade").
- kvip/kvin/dhātu-final stems: dṛś/spṛś (8.2.62 kuḥ), rāj/vraśc/yaj finals (8.2.36 → ṭ), yac/añc (tiryaṅ, tiraścaḥ), iyaṅ/uvaṅ of dhī/śrī/bhū/bhrū/strī (6.4.77–83 are stubs), 7.3.54 han→ghn (vīraghnaḥ): ~900 cells.
- śatṛ -at stems (runDat, kaTayat) need `ugit`; kvasu -vas (vidvas: 6.4.131 samprasāraṇa, 8.2.72 vidvatsu) not written: ~250 cells.
- Anusvāra orthography: stems spelled with M (saṃyama, saṃveda, vāchaṃyama): gold keeps ṃ, engine gives the parasavarṇa (8.4.58). ~700 cells.
- Sense-dependent sarvanāma / optional forms: adhara, antara, sama, prathama, viśva (neuter); pāda → pad (6.4.130 only for bahuvrīhi final); pratyeka; 'sapta' numerals (saptan jas/śas luk 7.1.22): ~400 cells.
- ṣatva/s oddities: grāvan/pīvan 7/3; uśanas 1/1 (uśanā); ṭ-cluster 'ratnamuṭtsu' (8.3.29 ḍaḥ si dhuṭ).
- Not engine: gold quirks (kālakriyāmāna n, jagaccakṣuṣ).
