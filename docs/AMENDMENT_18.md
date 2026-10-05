# AMENDMENT 18 — ashtadhyayi.com sūtra data (incl. examples) is gold, equal to Kāśikā

Proposed and accepted by the owner (Dr. Ajay Shukla), 2026-10-05, in session.

## Change
Art. 22 (Prāmāṇya): the ashtadhyayi.com sūtra data — `sutraani__data` (pāṭha, padaccheda, anuvṛtti, adhikāra)
**and** `sutraani__sutra_prayogas` (example words with the sūtra each cites) — is **gold-standard evidence at tier T7,
equal to Kāśikā / Prathamāvṛtti**. Where Vidyut, an older recipe, or an engine modelling choice disagrees with a
sūtra-data example, the example wins and the engine is changed. T2 (Mahābhāṣya) still outranks T7 on a true conflict.

## Unchanged
- Art. 6 firewall: `data/reference/` is read by `tests/` and `tools/` only; the engine never imports it.
  The examples drive *which rule is written and how it is pinned*, not runtime behaviour.
- Art. 19: oracles (Vidyut) can prove wrong, never right.
- Art. 21: runtime conflict resolution is still Ladder 1.

## Consequence
Conflicts recorded in `docs/CONFLICTS.md` are resolved by the sūtra data where it speaks (section G), pinned by a
regression test, and the entry marked closed. Entries on which the data is silent stay open.

## Acceptance
Accepted by the owner in chat ("modify constitution; they are equal evidence to Prathama-vṛtti and Kāśikā").
