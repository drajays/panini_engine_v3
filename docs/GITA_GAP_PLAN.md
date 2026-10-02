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

## Open clusters (561 differing, 131 unresolved; 421 distinct pairs — a long tail)
1. **vid / brū / vac suppletions (~35 words):** विदुः, वेद, वेत्थ (3.4.83 वा, ṇal-ādi in laṭ); आहुः, आह, प्राहुः (3.4.84 brū → āh);
   उवाच (6.1.17 samprasāraṇa in liṭ), उच्यते (vac, not brū + yak). Needs the liṭ tiṅ list (3.4.82) reused for laṭ.
2. **शृणु (12):** śru + śnu with śṛ (3.1.74) in the svādi/bhvādi homonym pair; the reader picks the bhvādi row.
3. **कश्चित् / कश्चन / केचित् (~17):** the annotation's stem is किञ्चित् (neuter), not kim + cit; not derivable from that stem.
4. **Sandhi-boundary / annotation model:** मधुसूदन (8.3.110 list), कथम् → किम्+थम् (taddhita), आपः (ap-stem, nitya bahuvacana),
   भ्रुवोः (6.4.77/83), सखा (7.1.92–93 arms), स्त्रियः (6.4.79), आशीः / भीः (8.2.36–38), जहि (6.4.36).
5. **Verb tail:** कल्पते (kLp), द्रक्ष्यसि (dṛś), लिप्यते (lip), निबध्नन्ति (nasal drop 6.4.24 before śnā), सिद्ध्यति.
6. **131 unresolved tags:** "no vibhakti/vacana" (111) — the annotation itself is incomplete; taddhita / kṛdanta stems.
7. **8.1.25 (yukta with a paśyārtha verb)** is an input, not derived (needs kāraka analysis); accent / 8.1.19 are not modelled.
8. **adas** feminine and the remaining feminine i/u ṅit forms (मतये/मत्यै, मतेः/मत्याः via 1.4.6) are not done.

## Inputs the engine cannot read from a string (tags the *caller* proposes, the engine verifies)
`anvadesha` (2.4.32: a second mention), `ugit` (matup / vatup / śatṛ origin), `yukta` + `paSyArTa` (8.1.24–25), pāda boundaries.
The reader proposes each from the text and keeps it only if the derivation reproduces the attested form (Art. 17).
