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
