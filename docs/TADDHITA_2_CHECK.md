# Taddhita deck 2 (pratyaya-ādeśa): owner's deck vs the engine

Source: `~/taddhati prakriya 2/sellealt.md` + 21 slides (Neelesh Bodas style deck; teaching data, not instructions). Tests: `tests/regression/test_taddhita_2.py`
(13 pass, 9 strict xfail incl. 5 parametrized 7.3.51 cases). Method as in `docs/TADDHITA_BASICS_CHECK.md`: `build_taddhita_state` + `run_autonomously(stop_before_tripadi)`
under `explore()`, reading the loop's own step order; surfaces are pre-tripāḍī (m->n, s->z come later). Engine untouched.

Deck teaches: (1) two steps on the pratyaya, it-lopa then ādeśa, then aṅga/sandhi/tripāḍī work; (2) 7.1.2 first letter of pratyaya: kha gha cha ṭha ḍha pha -> īn iya īya ik eya āyan;
(3) 7.1.1 yu -> ana, vu -> aka; (4) 7.3.50 ṭhasyekaḥ, with 7.3.51 (after is/us/u/ṛ/t-final aṅga, doṣ: ṭh -> k) as its apavāda; (5) apṛkta vi: cvi -> v -> lopa 6.1.67; (6) it-letter table
(which it-letter does what), exercise: dṛśyarūpa of 20 pratyayas.
Verdict: ok = by rule, trace shows it; gap = not reached; wrong = wrong surface; wrong-order = right surface, order differs; known = already in TADDHITA_BASICS_CHECK / being fixed.

| Principle / example | Engine result (trace evidence) | Verdict |
|---|---|---|
| Two steps: it-lopa then ādeśa then aṅgakārya (kuñja + cPaY) | 1.3.9 < 7.1.2 < 1.4.18 | ok |
| kha -> īn: yuṣmad + KaY -> yOzmAkIna; prāc + kha -> prAcIna | both; 7.1.2 in trace | ok |
| gha -> iya: rāṣṭra + gha -> rAzwriya | 7.1.2 < 1.4.18 < 6.4.148 | ok |
| cha -> īya: āṣāḍha + chaṇ -> ASAQIya (kāśī + cha -> kASIya) | both, 7.1.2 | ok |
| pha -> āyana: kuñja + cPaY -> kOYjAyana | 7.1.2 | ok |
| ha: idam + ha -> iha (idam -> i, 5.3.11) | iha, then 1.1.38 avyaya | ok |
| yu -> ana (7.1.1): ciram + ṭyu, sāyam + ṭyul -> cirantana, sāyantana | ciramtana, sAyamtana (tuṭ; m->n is tripāḍī) | ok |
| vu -> aka (7.1.1): viṃśati + ḍvun -> viṃśaka | viMSaka; 7.1.1, 6.4.142 | ok |
| ṭha -> ik (7.3.50): akṣa + ṭhak -> Akzika | 7.3.50 fires, 1.4.17/1.4.110 before it | ok |
| 7.3.50 before 7.2.118 (Kāśikā revatī + ṭhak: ik, then vṛddhi, then 6.4.148) | loop: 7.2.118 < 7.3.50 (same surface) | wrong-order |
| 7.3.51 ṭh -> k: sarpis, dhanus, dhenu, yakṛt, doṣ + ṭhak | sArpisika, DAnusika, DEnavika, yAkftika, dOzika (7.3.51 act only sets a flag) | wrong (5) |
| ḍha -> eya: vinatā + ḍhak, kula + ḍhakañ, godhā + ḍrak, chagala + ḍhinuk | vEnata, kOla/kOli, gODa, CAgali (aṇ/iñ types) | known (ḍhak family; ḍrak, ḍhinuk same) |
| kāśī + ṭhañ -> kASika (4.2.116) | kASIya only (cha) | gap |
| bhavatī + ṭhak/chas -> BavadIya (4.2.115) | BAvata (aṇ) | gap |
| pha -> āyan in phiñ: glucuka + phiñ -> glucukAyani (4.1.90) | glOcuki (iñ) | gap |
| ṭha -> ik in ṣṭhan / ṭiṭhan: ratha + ṣṭhan -> rathika, prat + ṭiṭhan -> pratika | rATika / rATya; no ṣṭhan/ṭiṭhan route found (sense not in vocabulary) | gap (untested) |
| cha -> īya: caturī + cha -> turIya; Sukra + ghan -> Sukriya; ṛtu + ghas | caturTa, SOkra, Artava; senses 5.2.51 / 4.2.26 not reached | gap (untested) |
| yuvan + vuñ -> yOvanaka | not found in the Kāśikā/LK of the brain; engine gives yOvna (aṇ) | untested (source unclear, Art. 22) |
| mātṛ + ṭhañ -> mAtfka | mAtfIya / mAtrIya; ṭhak route absent | gap (untested) |
| cvi: śukla + cvi + karoti -> SuklIkaroti; apṛkta vi 6.1.67 | no abhūtatadbhāva sense, no cvi route; 6.1.67 is a narrow kvip-residue flag (`prakriya_22_kvip_residue_arm`) | gap (untested) |
| Abhyāsa: dṛśyarūpa of ḍhinuk, kha, ṭhan, chas, phin, ḍvun, jāhac, ghas, phiñ, ṭhak, ṣeṇyaṇ, ṭhap, cvi, ṭyul, ṭīṭañ, cphañ, riṣṭātil, vun, ḍhakañ, dānīm | only the loop-driven ones above reach a surface; jāhac, ṣeṇyaṇ, ṭhap, ṭīṭañ, riṣṭātil, dānīm: not exercised | gap (untested) |
| it-letter table (which it-letter does svara / strī / aṅgakārya) | see basics doc: svara, strī, matup | known |
| pada 1.4.17 decided before ādeśa (deck: ādeśa first) | 1.4.17 precedes 7.1.2 in every trace | known (basics wrong-order) |

Counts (rows): ok 9, wrong 1 (5 words), wrong-order 1, gap 4 tested + 6 untested, known 3, untested-source 1.
Tests: 13 pass, 9 strict xfail (5 x 7.3.51, 1 order, 3 gaps).

Proposed fix order (new gaps only): (1) 7.3.51 real act (ṭh -> k after is/us/u/ṛ/t-final aṅga and doṣ; it must bādh 7.3.50, wrong surfaces today);
(2) 4.2.115 / 4.2.116 (bhavat, kāśyādi ṭhak/ṭhañ routes) via the group frames of 4.2.9x; (3) 4.1.90 phiñ group and the ḍha -> eya family together with the known ḍhak work;
(4) 7.3.50 before 7.2.118 (order, with the known 6.4.148/7.2.117 order work); (5) cvi + 6.1.67 beyond kvip (needs a sense in the vocabulary, Art. 22 ruling);
(6) ṣṭhan/ṭiṭhan/ṭīṭañ/jāhac/riṣṭātil/dānīm senses for the untested rows.
