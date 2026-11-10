# AMENDMENT 19 — named override 6.1.17 over 7.4.60 (Art. 21 L10)

Accepted by the owner in chat 2026-10-05 ("resolve all conflicts following ashtadhyayi.com data; modify constitution").

**Override:** `frozenset({"6.1.17", "7.4.60"}) → "6.1.17"`.

**Why.** In liṭ the abhyāsa of vac/svap/yajādi and of the 6.1.16 class (vyadh, vyac, jyā, vraśc, …) takes samprasāraṇa on the
full abhyāsa (`vya` → `vi`). If 7.4.60 halādiḥ śeṣaḥ (which drops the `y`) ran first, the sūtra could never apply: para would give
`vavyāca`/`jajyau`. Evidence (ashtadhyayi.com `sutra_prayogas`, 6.1.17): `संविव्ययुः`; forms `विव्याध`, `जिज्यौ`.
The tradition reads the abhyāsa kārya in sūtra order here; this is the named exception to para, not a heuristic.

**Pinned by:** `tests/regression/test_liT_abhyasa_samprasarana_6_1_17.py`.

## Addition (2026-10-05): named override 7.3.96 over 7.4.50

`frozenset({"7.3.96", "7.4.50"}) → "7.3.96"`. For laṅ 2sg of as, both rules are open on `Aas+s`; para would delete the root's s
(7.4.50) and leave 7.3.96 no site. The Kāśikā example is `आसीः` (and `आसीत्`): īṭ goes in first. Evidence: ashtadhyayi.com 7.3.96 (examples
`आसीत्`, `आसीः`); 7.4.50 anuvṛtti `सः सि`. Pinned by `tests/regression/test_as_laG_loT.py`.

## Addition (2026-10-05): named override 6.4.101 over 6.4.119

`frozenset({"6.4.101", "6.4.119"}) → "6.4.101"`. loṭ 2sg of `as`: hi → dhi (jhal-final as) precedes the e-ādeśa: `एधि`. Evidence:
ashtadhyayi.com 6.4.119 example `एधि` ("एत्वमभ्यासलोपश्च"), `देहि`, `धेहि`. Pinned by `tests/regression/test_as_laG_loT.py`.

## Addition (2026-10-05): named overrides 6.1.50 over 7.3.84 and 7.2.1

mī/mi/dī before a non-liṭ ārdhadhātuka: `ātva` precedes guṇa/vṛddhi (`दास्यते`, `दाता`, `अदास्त`, `अमासीत्`). Evidence: ashtadhyayi.com dhātu table
(Vidyut agrees); 6.1.50 anuvṛtti `आत् एचः उपदेशे`. Pinned by `tests/regression/test_tinanta_data_resolved_batch2.py`.

## Addition (2026-10-06): named override 6.1.45 over 6.1.8

ec-final roots in liṭ (glai, ṣṭyai, ovai): ātva (6.1.45) is done on the bare root *before* dvitva, so both copies are ā (`जग्लौ`, `तस्थ्यौ`, `ववौ`), not `*जिग्लाय`.
Evidence: brain (ashtadhyayi.com prakriyā, glai liṭ): `glE → glA` (6.1.45) precedes `glA + liw` and `glA glA`; Vidyut agrees. The same fix removes the no-op
vṛddhi E→E of 7.2.115 that stripped the root's own-ec mark (`mula_dhatu_v`) and made 6.1.45 miss. Pinned by `tests/regression/test_tinanta_ec_liT.py`.

## Addition (2026-10-06): named override 7.2.73 over 7.2.3

yam/ram/nam and ā-final aṅgas in parasmaipada luṅ: sak + iṭ (7.2.73) enter at once after the tiṅ is lopa'd (brain prakriyā of `mA luṅ`: `mAs + iw + s + t` precedes every
aṅga rule); with iṭ on the sic, 7.2.4 neṭi forbids the hal-anta vṛddhi of 7.2.3 → `anaMsIt`, `aramsIt`, not `*anAmsIt`. Pinned by `tests/regression/test_tinanta_7_2_73.py`.

## Addition (2026-10-06): named override 6.1.11 over 6.4.51; 6.1.11 handles ajādi roots (6.1.2)

ajādi ṇijanta before caṅ (aṭ→āṭ, `awi`): the second ekāc `wi` is doubled while the ṇi is still there, then 6.4.51 drops it from the root only → `Awiwat`. Evidence: brain prakriyā of
`aṭ` luṅ (deriv 142, step 10: 6.1.11 / 6.4.51 / 1.1.59 / 6.1.2). Pinned by `tests/regression/test_tinanta_nijanta_ajadi_caN.py`.

## Addition (2026-10-23): named override 6.1.58 over 7.3.84 / 7.3.86

sṛj / dṛś before a non-kit jhal-initial affix: am (a after the last vowel) goes in first — `sṛj + tā → sra-j + tā → स्रष्टा`, `द्रष्टा`, `द्रष्टव्य`, `दद्रष्ट` — not guṇa first (`*सर्क्ता`, `*दर्ष्टा`).
The two are not a mutual विप्रतिषेध: 6.1.58 stays applicable after the guṇa (so it is nitya, PŚ 38) while the am removes the guṇa's site. The resolver's `purva`
layer reads one-sided kills as conflict and would hand it to para. Evidence: brain 6.1.58 (Kāśikā; SK `drazwA`, `srazwA`; Vidyut floor lists 6.1.58 before 1.4.13). Pinned by `tests/regression/test_6_1_58_am.py`.

## Addition (2026-10-31): taddhita order (docs/PLAN_TADDHITA_FIX.md step 1)
`ORDER_BEFORE` (engine/resolver.py), data (first, second): while `first` is a candidate `second` is withheld and the ladder decides among the rest (a CONFLICT_OVERRIDES pair would also outrank a third rule that kram puts earlier: 7.3.16 in dvivārṣika). Pairs: (7.2.117, 6.4.148) ñit/ṇit ādivṛddhi is para (1.4.2), then yasyeti ca (dakṣa + iñ: dākṣi); (7.3.50, 7.2.118) and (7.3.51, 7.2.118): the pratyaya's own ādeśa (ṭh -> ik / k) precedes the aṅga's kiti ca vṛddhi (Kāśikā 7.3.50, revatī + ṭhak).
1.4.17 (pada) waits while an ādeśa of the taddhita pratyaya (7.1.2, 7.3.50) is still to act, so pada / bha is decided on the pratyaya as it finally stands (ṭhak -> ika is yac-initial: bha). No override pair: a pair would also outrank 7.3.16 (dvivārṣika).

## Addition (2026-11-10): ORDER_BEFORE 6.1.33 over 6.1.45 (hve liṭ / san / yaṅ)

ह्वे that is about to be doubled takes samprasāraṇa before dvitva (Kāśikā 6.1.33: "अभ्यस्तकारणस्य ह्वयतेः प्रागेव द्विर्वचनात् संप्रसारणं भवति। जुहाव। जोहूयते। जुहूषति"), so 6.1.45 ātva
finds no ec left (हु). The two meet on the bare root and 6.1.45 is para; the Paribhāṣā "संप्रसारणं तदाश्रयं च कार्यं बलवत्" (Paribhāṣāśekhara; Kaumudī 6.1.31) is why samprasāraṇa wins.
The pair is ORDER_BEFORE (not a CONFLICT_OVERRIDES pair) so 6.1.8 / 6.1.45 for glai etc. stay as above. Pinned by `tests/unit/test_6_1_33_hve_samprasarana.py`.

## Addition (2026-11-10): the same cluster, other touch points

- `engine/phase.py`: 6.1.108 sampprasāraṇāc ca is also eligible in the aṅga phase (gated by the samprasāraṇa on the tape), so hu+e -> hu precedes 7.2.115 / dvitva of the aṅga (juhāva).
- 6.1.46 न व्यो लिटि is a real PRATISHEDHA (tag `na_vyo_liTi_6_1_46` on the root, read by 6.1.45 and 7.2.115); 7.2.115 gives e -> ai for such a root (विव्याय).
- `engine/resolver._reach`: a ṭit āgama (Aṭ, iṭ) is the first part of the pratyaya it stands before (1.1.46), so a nimitta met by the āgama reaches the whole pratyaya. Without it the guṇa of 7.3.84
  (nimitta: the sārvadhātuka Ani) looked bahiraṅga to 6.4.82's aci (the A of Aṭ) and bibhI + Ani gave *bibhyāni; now it is a plain vipratiṣedha, para = 7.3.84 (बिभयानि; Kāśikā 3.4.92: the Aṭ-ed uttama is pit).
