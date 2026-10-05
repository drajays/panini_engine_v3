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
