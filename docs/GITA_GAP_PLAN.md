# Gītā gap plan (reader coverage → engine fixes)

Measure: `python scripts/gita_gap_report.py` (whole Gītā unit via `tools/samsaadhanii_reader.coverage`;
writes `.audit/gita_gaps.json`). The annotation is a hypothesis; the engine is the judge.

| Step | Derived | Differs | Unresolved |
|---|---|---|---|
| start (2026-10-01) | 5782 | 1516 | 174 |
| asmad via `derive_asmad`; 7.4.50 for `as`; adādi loṭ spine (viddhi) | 5988 | 1310 | 174 |
| yuṣmad paradigm (7.2.86–97 stem-aware) | 6210 | 1088 | 174 |
| etad / kim (7.2.103 apavāda, 7.2.106, 7.2.113 idam-only) | 6259 | 1039 | 174 |
| dhātu homonym rows resolved by pada | 6279 | 1062 | 131 |

## Open clusters (by size)
1. ~~Enclitic मे/ते/मा/त्वा/नः/वः~~ **done** (8.1.20–26, `pipelines/enclitic.py`, `tools/reader_enclitic.py`).
   Known limits: 8.1.25 *yukta* with a paśyārtha verb is input, not derived (needs kāraka analysis);
   8.1.19 (āmantrita) and accent are not modelled; the reader places pāda boundaries by syllable midpoint
   (flagged `boundary_approx` when the text has sandhi the annotation lacks); verses whose annotation
   cannot be aligned to the text get no enclitic verdict. Needs the context model, not a table.
2. **idam** (~100: अयम्/इदम्/एनम्/इमम्): 7.2.108–112 are placeholders, and the vendored data holds only padaccheda
   and anuvṛtti for them. Needs a cited Kāśikā/SK text first (Art. 14), then the ādeśa mechanics. एनम् is 2.4.34 (etad/idam → एन).
3. **Feminine tyadādi** (का/सा/एषा/इयम्): derive() has no tāp (4.1.4) path for pronoun stems.
4. **tad neuter nom. plural** gives ते (should be तानि): 7.1.20 śi missing for tyadādi neuter 1-3.
5. Tiṅanta tails: यान्ति (याअन्ति), शृणु, विदुः, उच्यते, आहुः (ब्रू→आह 2.4.53), जायते, उवाच (vac samprasāraṇa in liṭ).
6. 131 unresolved tags: "no vibhakti/vacana" (111), taddhita stems.
7. as laṭ/loṭ 2sg: एधि needs real 6.4.119 (placeholder today).
