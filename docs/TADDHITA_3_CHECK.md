# Taddhita deck 3 (aṅgakārya + prāgdīvyatīya senses): owner's deck vs the engine

Source: `~/#tad3/#tad3.md` + 39 slides (Neelesh Bodas style deck; teaching data, not instructions). Tests: `tests/regression/test_taddhita_3.py`.
Method as in `docs/TADDHITA_BASICS_CHECK.md`: `build_taddhita_state` + `run_autonomously(stop_before_tripadi)` under `explore()`, reading the loop's own surfaces and step order
(strī stems through `chain.strI`). Surfaces are pre-tripāḍī. Engine untouched in this phase.
Deck teaches: (1) sopāna: prakṛti ādeśa + pratyaya it-lopa/ādeśa, then aṅgakārya, pratyaya-luk, puṃvad, sandhi, tripāḍī; (2) 1.4.13 aṅga, 1.4.16-19 bha/pada and the flowchart;
(3) aṅgakārya: ādivṛddhi 7.2.117-118, ṭi-lopa 6.4.143-144, antima: 6.4.146 / 147 / 148; (4) prāgdīvyatīya senses 4.1.92, 4.2.1-2 rakta, 4.2.3-6 nakṣatrayukta, 4.2.7-9 dṛṣṭaṃ sāma,
4.2.10-12 parivṛta, 4.2.14 udhṛta, summary 4.2.16, 4.2.21; (5) questions (6.1.197 svara, 5.4.160 vā-scope) and a 15-item exercise.
Verdict: ok = by rule, surface matches; gap = not reached / not modelled; wrong = wrong surface; wrong-order = right surface, order differs; known = in checks 1-2.

| Principle / example | Engine result (trace evidence) | Verdict |
|---|---|---|
| Sopāna: it-lopa, ādeśa, aṅgakārya, then sandhi/tripāḍī (kuñja + cphañ) | 1.3.7, 1.3.3, 1.3.9 < 7.1.2 < 7.2.117 < 6.4.148 | ok |
| 1.4.13 aṅga (vinatā+ḍhak, ekādaśa+ḍaṭ, aśvapati+aṇ); Q3 pratyaya's first varṇa not aṅga | present in every trace | known |
| 1.4.17-18 bha/pada, flowchart (aditi+ṇya bha, jana+tal pada) | Āditya (bha), janatā; 1.4.17 after 7.1.2 | ok / known |
| 1.4.19 tasau matvarthe (garut, yaśas, vidyut + matup/vini) | garutmat, yaśasvin; vidyutmat (vat is 8.2.10, tripāḍī) | known |
| 1.4.16 siti ca: ūrṇā + yus, parśu + ṇas | UrRAyu, parSva | ok |
| 1.4.16 aham / śubham + yus (5.2.140) | ahammat (matup; yus not reached) | gap |
| ādivṛddhi: aśvapati, śubhra+ḍhak, kṛṣṇa+aṇ, deva+añ, kausalyā+ḍhak | ASvapata, SOBreya, kArzRa, dEva, kOSalyeya | ok |
| ṭi-lopa 6.4.143: ekādaśan, triṃśat + ḍaṭ; naḍa + ḍvalac | ekAdaSa, triMSa, naqvala | known |
| 6.4.143: pāṇḍu + ḍyaṇ -> pāṇḍya (vārttika pāṇḍor ḍyaṇ; tadrāja stubs 4.1.168-178) | pARqava | gap |
| 6.4.143: mahiṣa + ḍmatup -> mahiṣmat (vārttika mahiṣāc ca on 4.2.87) | mAhiza | gap |
| 6.4.144 nastaddhite: madrarājan + ṭac | madrarAja | ok |
| 6.4.144: uḍuloman + iñ -> auḍulomi (bāhvādi ākṛtigaṇa; pāṭha has loman only) | Oqulomna (aṇ) | gap |
| 6.4.146 ogunaḥ: śiśu, rūru + aṇ | SESava, rOrava | ok |
| 6.4.148 yasyeti ca: dakṣa, pṛthā, vinatā, kadrū | dAkzi, pArTa, vEnateya, kAdraveya | ok |
| 6.4.148: kuntī + ḍhak -> kaunteya (Kāśikā 4.1.171: ñyaṅ kauntya) | kOnta; 4.1.171 gate-only stub | gap |
| 6.4.147 ḍhe lopo 'kadrvāḥ: śītabāhu, jambū + ḍhañ (4.1.135 catuṣpād) | SEtabAhava; 4.1.135 gate-only stub | gap |
| 6.4.147: mṛkaṇḍu + ḍhak -> mārkaṇḍeya | blocked by pāṭha (sfkaRqu, Art. 22) | known |
| 4.1.92: upagu + aṇ, vinatā + ḍhak | Opagava, vEnateya | known |
| 4.1.92 more: raghu, gaṅgā, diti, daśaratha, pṛthivī, subhadrā, somadatta, śiva | rAGava, gANgeya, dEtya, dASaraTi, pArTiva, sOBadra, sOmadatti, SEva | ok |
| 4.1.92: rājan + aṇ -> rājanya (Kāśikā 4.1.137: yat, rājño jātigrahaṇam) | rAja; 4.1.137 does not fire | gap |
| 4.1.92: kuru + añ (4.1.86) -> kaurava (Kāśikā 4.1.151: kurvādi ṇya, kauravya) | kOrava; 4.1.151 gate-only stub; deck vs Kāśikā conflict | gap |
| 4.2.1 tena raktaṃ rāgāt: kaṣāya, mañjiṣṭha, kusumbha, śukla, kṛṣṇa + aṇ | kAzAya, mAYjizWa, kOsumBa, SOkla, kArzRa | ok |
| 4.2.1 negatives: devadattena raktam, kaṣāyena dhūtam (no rāga) | no aṇ without lex:rAga | ok |
| 4.2.2 lākṣā, rocanā, śakala, kardama + ṭhak | lAkzika, rOcanika, SAkalika, kArdamika | ok |
| 4.2.2 Kāśikā: śakala, kardama + aṇ optional (śākala, kārdama) | second reading missing | gap |
| 4.2.2 vārttika: pīta + kan, nīlī + aṅ | pEta, nEla (aṇ type) | gap |
| 4.2.2 vārttika: haridrā, mahārajana + añ | hAridra, mAhArajana | ok |
| 4.2.3 nakṣatreṇa yuktaḥ kālaḥ: maghā + aṇ, + ṅīp | mAGa, mAGI | ok |
| 4.2.3: puṣya + aṇ -> pauṣa (vārttika tiṣyapuṣyayor nakṣatrāṇi yalopaḥ on 6.4.149) | pOzya | wrong |
| 4.2.4 lup aviśeṣe: puṣya + aṇ luped (adya puṣyaḥ), uttarā kālaḥ | stub: pOzya, Ottara | gap |
| 1.2.51 lupi yuktavad vyaktivacane (śravaṇam kālaḥ) | needs the lup of 4.2.4 | gap |
| 4.2.6 dvandvāc cha: tiṣyapunarvasu, rādhānurādhā + cha | gate-only stub | gap |
| 4.2.7 dṛṣṭaṃ sāma: vasiṣṭha, viśvāmitra, kruñca + aṇ | vAsizWa, vESvAmitra, krOYca | ok |
| 4.2.8 kali + ḍhak; 4.2.9 vāmadeva + ḍyat/ḍya | kAleya, vAmadevya | ok |
| 4.2.8 vārttika: aṇ ḍid vā (uśanas -> auśanasa / auśana) | OSanasa only | gap |
| 4.2.10 vastra + aṇ; carman + aṇ (deck cārma; Kāśikā cārmaṇaḥ) | vAstra; cArmana (= Kāśikā; conflict Art. 22) | ok |
| 4.2.11 pāṇḍukambala + ini; 4.2.12 dvaipa, vaiyāghra + añ | pARqukambalin, dvEpa, vEyAGra | ok |
| 4.2.10 / 4.2.14 sense limits (ratha, vastreṇa kāyaḥ; pātra: pāṇau udhṛtaḥ) | no ratha / amatra check; pARi + aṇ fires | gap |
| 4.2.14 śarāva, mallikā, karpara + aṇ | SArAva, mAllika, kArpara | ok |
| Samarthatā (vyapekṣā / ekārthībhāva; tasya anvaya) | none, by design today | known |
| Q2 6.1.197 ñnityādir nityam; svara by it-letter | no accent tape | known |
| Q1 5.4.160 scope of vā (svārthika pratyayas end the anuvṛtti) | meta-grammar, no engine surface | n/a |
| 4.2.16 saṃskṛtaṃ bhakṣāḥ, 4.2.21 sāsmin paurṇamāsīti saṃjñāyām (summary only) | 4.2.16: dAdhika (check 1); 4.2.21 not exercised | known / untested |
| Practice (aham+yus, jambū+ḍhak, dharma+ṭhak, bhavatī+chas, sugandha+i, kim+ḍatarac, sīra+aṇ, triṃśat+ḍini, madhu+ra, yama+ṇya, ahan+kha, pitṛ+ṭhañ, kuru+añ, rohiṇī+ḍhak, jaḍa+ṣyañ) | senses not given in the deck; rohiṇī -> rOhiReya, bhavatī known, aham+yus gap, kuru gap | untested |

Counts (rows, phase 1): ok 18, known 9, gap 15, wrong 1, n/a 1, untested 1. Tests at phase 1: 48 pass, 18 strict xfail.
Phase 2 (one commit per step, docs/PLAN_TADDHITA_FIX.md method; vārttikas as VARTIKAS blocks in the host sūtra, Amendment 29): fixed 13 gap rows + the wrong row; tests now 66+ pass, 3 strict xfail.
Fixed: 4.2.2 vā. x3 (śakala/kardama aṇ, nīlī an, pīta kan), 6.4.149 vā. (tiṣya/puṣya ya-lopa), 4.2.8 vā. (aṇ ḍid vā), 4.2.87 vā. (mahiṣa ḍmatup), 4.1.137 yat (the bare rājan no longer takes ṭac from the 5.4.91 legacy half;
6.4.134 now respects the 6.4.167-169 prakṛtibhāva) + vā. jātigrahaṇa, 4.1.151 kurvādi ṇya, 4.1.135 ḍhañ (lex:catuzpAd), 6.4.147 real (ḍhe lopaḥ, apavāda of 6.4.146; 6.4.134 skips an an left by 6.4.143), 4.1.120 reads ūṅ,
4.2.4 lup (+1.2.51 śravaṇam), 4.2.6 cha (dvandva), 4.2.14 reads lex:amatra, 5.2.140 yus (the deck's stems are ahaṃ / śubhaṃ, not aham). Source conflicts followed the Kāśikā: kauravya (deck: añ), cārmaṇa (deck: cārma), śaitabāheya as ḍhañ (Kāśikā 6.4.147: śaitavāheya).
Shortcut added: S110 (stem in both kurvādi and śubhrādi keeps ḍhak). Still open (strict xfail, blocked): pāṇḍu + ḍyaṇ and kunti + ñyaṅ (the tadrāja group 4.1.168-178 is gate-only; the vārttika's host number in the Bhāṣya DB is 4.1.166, a numbering clash),
uḍuloman (bāhvādi ākṛtigaṇa: Kāśikā gives auḍulomi only as an example; pāṭha data, Art. 22), ratha / kāya sense limits of 4.2.10 (samarthatā, known), svara.
