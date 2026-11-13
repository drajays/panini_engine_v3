# krt_meanings_reference_llm.json — outside reference, validator only (checked 2026-11-13)

Source: an LLM-compiled table (78 kṛt pratyayas: sūtras, it-markers, meanings, examples). **The engine never reads it** (guard: tests/constitutional/test_no_external_corpus_in_engine.py); a vivakṣā value needs the sūtra's samagra or the Kāśikā as its citation (Amendments 25/27), not this file.

Checked against ashtadhyayi.db:
- all 135 numeric sūtra ids exist; 11 sūtra texts differ from the DB: orthography only, except real errors: `ksnu` 3.2.139 (ग्स्नुः for क्स्नुः), `ru` 3.2.174 (long list; the sūtra is भियः क्रुक्लुकनौ), `ghinun` 3.2.142 (garbled), `tosun` 3.4.16 (जनो for जनि).
- 133 of 160 example forms occur in the DB (Kāśikā, prayogas, derivations); 27 do not (mostly ordinary forms the DB does not quote, e.g. पठनीयम्, पठितुम्, चक्राणः). Not proof of error, not proof of correctness.
- meaning claims (karaka / kāla) mostly come from the general kṛt sūtras 3.4.67-76, not from each pratyaya's own sūtra; do not copy them into the schema without that citation.

Use: example corpus for the kṛdanta audit / derive_all (the 133 verified forms first); every disagreement is judged against the Kāśikā, never against this file.
