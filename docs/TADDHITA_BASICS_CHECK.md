# Taddhita basics: owner's deck vs the engine

Source: `~/taddhati prakriya basics/44144.md` + 23 slides (Neelesh Bodas deck; treated as teaching data). Tests: `tests/regression/test_taddhita_basics.py`
(18 pass, 14 strict xfail). Method: `build_taddhita_state` + `run_autonomously(stop_before_tripadi)` under `explore()` (what `derive_taddhita_stem` does),
reading the loop's own step order. `pipelines/chain.py::taddhita` is a thin wrapper over that same stem derivation. Engine untouched.

What the deck teaches: (1) five mahotsargas 4.1.83-5.1.114, default suffix per domain, sense chosen first; (2) vyapekṣā vs ekārthībhāva (vṛtti is
optional/obligatory); (3) it-letters in taddhitas (1.3.2, .3, .4, .6, .7, lopa 1.3.9) and the 13 purposes of an it-letter: svara, strī-pratyaya,
aṅgakārya; (4) aṅga 1.4.13 / 6.4.1, bha 1.4.18, pada 1.4.17, 1.4.19, 1.4.16; (5) ādivṛddhi 7.2.117-118, ṭi-lopa 6.4.143, num 7.2.70;
(6) order: it-lopa, then any ādeśa, then decide ajādi/halādi (bha vs pada). Not in the deck: 1.2.46 / 1.1.38 (the loop does 1.2.46 anyway).

Verdict: ok = by rule, trace shows it; gap = not reached / not modelled; wrong-order = right surface, sūtra order differs from the deck.

| Principle / example | Engine result (trace evidence) | Verdict |
|---|---|---|
| Domain 1 default aṇ, sense apatya: upagu | Opagava; 4.1.92 frame then 4.1.83 | ok |
| Domain 2 default ṭhak: akṣa + dīvyati | Akzika (5.1.19 frame, ṭhak) | ok |
| Domain 3 yat: go + tasmai hitam | gavya | ok |
| Domain 4 cha: vatsa + tasmai hitam | vatsIya (5.1.1) | ok |
| Domain 5 ṭhañ: godāna + krīta | gOdAnika (5.1.18) | ok |
| Sense picks the suffix (same stem, different artha) | dadhi: tena saṃskṛtam / dīvyati -> dAdhika | ok |
| Prātipadika + taddhita = prātipadika | 1.2.46 fires after 1.3.9 in every trace | ok |
| it-lopa order (1.3.3 -> 1.3.9 -> 1.2.46 -> 1.4.13) | dakza: exactly this order | ok |
| 1.3.3 final hal (aṇ, ṇas, tal) | aSvapati, jana+tal -> janata | ok |
| 1.3.7 cuṭū (ḍ of ḍaṭ, ḍvalac) | triMSat -> 1.3.7 before 1.3.9; naqvala | ok |
| 1.3.2 u~ (matup, vatup, ḍmatup) | never fires in the loop; matup is armed only by a recipe flag (5.2.94 "narrow") | gap |
| garut/kumuda + asti -> garutmat, kumudvat | engine gives gAruta, kOmuda (aṇ) | gap |
| yaśas + vini -> yaśasvin (1.3.3 + 1.4.19) | gives yASasa; vini and 1.4.19 not reached | gap |
| 1.3.4, 1.3.6 (ṣkan, ṣṭarac, dānīm) | no case reaches them (ṣṭarac/ṣkan not in loop) | gap (untested) |
| aṅga 1.4.13 / 6.4.1 | present in every trace | ok |
| bha 1.4.18 before ñit/ṇit vṛddhi | dakza: 1.4.18 < 7.2.117 | ok |
| ṇit/ñit vṛddhi: aśvapati, dakṣa, pṛthivī | ASvapata, dAkzi, pArTiva | ok |
| kit vṛddhi 7.2.118 then ṭi-lopa: dadhi + ṭhak | dAdhika; 7.2.118 < 6.4.148 | ok |
| ṇit/ñit: vṛddhi first, then ṭi-lopa | loop does 6.4.148 before 7.2.117 (same surface; paratva says 7.2.117 first) | wrong-order |
| ḍit ṭi-lopa 6.4.143: triṃśat, ekādaśan + ḍaṭ | triMSa, ekAdaSa (needs lex:saMKyA / saMKyAdi tags, S43) | ok |
| ḍit: naḍa + ḍvalac -> naḍvala | naqvala | ok |
| pada 1.4.17 before consonant-initial taddhita: jana + tal | 1.4.17 fires | ok |
| Decide bha/pada only after the ādeśa (ṭh -> ik 7.3.50) | 1.4.17 runs before 7.3.50, then 1.4.18 after (patched by S41-style retagging) | wrong-order |
| ḍhak -eya (kit): vinatā, bharata, śubhra, mṛkaṇḍu, godhā | gives aṇ-type forms (vEnata, BArata, ...) | gap (5 cases) |
| sit -> pada: parśu + ṇas -> pārśva | gives pArSava | gap |
| kraya + ṭhan -> krayika (nit: no vṛddhi, accent) | loop picks ṭhak: krAyika | gap |
| svara by it-letter: cit/kit/ñit/nit/tit/pit/rit/lit (6.1.164-217, 3.1.4) | no accent sūtra fires on the stem (dadhi 6.1.165, aśvapati 6.1.197 absent) | gap |
| strī-pratyaya by ṭit/ṣit (ṅīp 4.1.15, ṅīṣ 4.1.41) | not exercised in the loop; no strī-vivakṣā route found | gap (untested) |
| ugit num 7.2.70 (garut + matup) | blocked by the matup gap | gap |
| Samartha: vyapekṣā / ekārthībhāva (upagoḥ apatyam ... vs kambalam) | none: the vivakṣā alone licenses the taddhita; no samarthatā check | gap (by design today) |

Counts (rows): ok 17, gap 11, wrong-order 2. Tests: 18 pass, 14 strict xfail (12 gap cases, 2 wrong-order, svara x2 counted in the 14).

Top gaps: (1) matup/vatup/vini (1.3.2, 1.4.19, 7.2.70) not in the loop; (2) ḍhak -eya family 4.1.119-129 not loop-driven; (3) no svara at all;
(4) no strī-pratyaya (4.1.15 / 4.1.41) route; (5) ṇit/ñit vṛddhi after 6.4.148 and pada decided before 7.3.50 (order).
