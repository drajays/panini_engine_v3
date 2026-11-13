# Samāsa machine: design note (slice 1)

## What exists (inventory)
- Lexicon `"padas": true` (commit 7c32772f): `engine/lexicon.stem_terms` keeps a stem's parts as separate Terms;
  `pipelines/subanta._padas_tape` tags every part but the last `samasa_purvapada`. Users: viSvarAj, viSvavAh, vftrahan.
- `2.2.18` tags gatis before a krdanta `samasa_member, samasa_purvapada, tatpurusha` (the only real 2.1/2.2 sūtra on a tape).
  2.1.x/2.2.x others are gate-only or recipe pipelines (`pipelines/*_samasa.py`, `*_dvandva.py`, `*_bahuvrihi.py`).
- Readers of `samasa_purvapada`: 6.3.9, 6.3.14, 6.3.34, 6.3.81, 6.2.184, 7.1.37.
- `5.4.68` opens the samāsānta frame (adhikāra); `5.4.91` reads a one-Term compound through `lex:` tags (S62).
- `pada_merge` flattens all Terms into one pada before the tripāḍī (the seam was lost there).

## Input shape
A tape of Terms, pūrvapada(s) first, uttarapada last, then the sup:
`[pUrva: tags samasa_purvapada (+ tatpurusha / bahuvrihi …)] [uttara: samasa_uttarapada] [sup]`.
Built by a Lexicon entry with `padas: true` (kṛdanta compounds) or by the samāsa sūtras 2.1.x / 2.2.x. Sense facts (honour,
`lex:pUjana`) are the speaker's vivakṣā, never derived from the surface.

## Boundary tags
- Term level (before the merge): `samasa_purvapada`, `samasa_uttarapada` (new; set by `_padas_tape` when the stem has a pūrvapada).
- Varṇa level (after `pada_merge`, for the tripāḍī): every varṇa of those Terms gets `samasa_purva_v` / `samasa_uttara_v`
  (same device as `pratyaya_start_v`). The uttarapada stem is the Term before the sup, so "ekāc" counts only its vowels.

## Slice 1 (done)
- **8.4.12** real: pratipadika-final `n` of an ekāc uttarapada after r/ṣ/ṛ in the pūrvapada, non-blockers between
  (aṭkupvāṅnumvyavāye 'pi, `_BLOCKERS` of 8.4.2). In the subanta tripāḍī pool. vftrahaRO / vftrahaRaH / vftrahaRam.
- **8.4.2** refuses to link r and n across the seam (the seam is not samānapada), so 8.4.12 owns it.
- **5.4.69** real PRATISHEDHA: on a tatpuruṣa whose pūrvapada is su / ati with `lex:pUjana`, blocks 5.4.70 – 5.4.112
  (prāg bahuvrīheḥ) via `blocked_sutras`; the dispatcher then never offers 5.4.91 (surājā, atirājā). Replaces the gate-only S126/S133 half.

## Unblocks next
8.4.12 num / vibhakti n (kṣīrapāṇi, kṣīrapeṇa); 8.4.13 – 8.4.14 (same seam, other uttarapadas); 6.3.x readers that need the
boundary after the merge; 7.2.101 follow-ups once a compound stem keeps its parts.

## Out of scope
- Building compounds from members (2.1.x / 2.2.x vidhi, sup-luk 2.4.71, ṭac attaching to the two-Term shape): 5.4.91 still reads the
  one-Term `lex:` shape, so 5.4.69's block is exercised on the two-Term tape only; unifying them is the real machine.
- Deriving su / ati as karmapravacanīya of honour (1.4.93 – 96 are gate-only): `lex:pUjana` is an input.
- Bahuvrīhi / dvandva / avyayībhāva shapes; accent (6.2) over the seam.

## Slice 2 (done): the vākya → compound, end to end
`chain.samasa(members, **vivaksha)` (members: stem, vibhakti, vacana[, lex tags[, liṅga]]) builds the tape of `engine/tape_init/samasa.py`
(stem Term + sup Term per member, the sup carrying `vib:<name>`), runs the loop (phase adhikāra `samasa` = 2.1.3), and stops when the sups are gone
(2.4.71, its new samāsa branch) and the liṅga is given (2.4.17 dvigu, 2.4.18 avyayībhāva, 2.4.26 para). The result is a `Stem` with `.parts`
(pūrvapada(s) | uttarapada): `chain.sup` rebuilds the two-Term tape (`samasa_purvapada` / `samasa_uttarapada`), `chain.strI` follows the last member.
- Vidhi sūtras (all through `engine/samasa_attach.py`: `pair` / `run` / `mark`): 2.1.6 (+ apavāda of 2.2.18), 2.1.24, 2.1.36, 2.1.37, 2.1.40, 2.1.51 (+ saṃjñā 2.1.52),
  2.1.57, 2.2.8, 2.2.18 (prādi / ku on the vākya), 2.2.24 (anyapadārtha vivakṣā), 2.2.29 (cārtha vivakṣā). The old recipe arms stay beside them.
- Seam readers now fed by the machine: 5.4.69 (surājā, atirājā), 6.3.46 (mahat → mahā: maharṣiḥ via 6.1.87 + 1.1.51), 8.2.7 on the pūrvapada n (rājapuruṣaḥ),
  8.4.12 for the pratipadika-final, nuṃ (`num_v`, kṣīrapāṇi) and sup (`sup_v`, kṣīrapeṇa) n.
- Open: S158 – S164 of docs/SHORTCUT_LEDGER.md (vibhāṣā of the samāsa itself, pratiṣedhas 2.2.10 ff., 2.4.82/83, samāhāra dvandva, jātīya, 2.1.1 samarthaḥ).
