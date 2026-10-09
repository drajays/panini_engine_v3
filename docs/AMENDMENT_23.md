# AMENDMENT 23 — Ācārya-prāmāṇya: Pushpa Dixit's concepts and conflict resolution; Pāṇinian prakaraṇa as structure

**Status:** accepted 2026-10-09 on the owner's direct instruction ("amend the constitution now … Aṣṭādhyāyī database plus
agreement from Neelesh or Pushpa Dixit is a must; Pushpa Dixit is the topmost authority unless she is wrong due to clear
facts, then we follow the Aṣṭādhyāyī data; for concepts and conflict resolution Pushpa Dixit has priority").
Branch `amendment-23`; merged only after the gates in *Verification* are green.

## Problem
1. Art. 22 ranks texts but has no place for the living teaching tradition: `T8 प्रक्रिया primers — pedagogical; no deciding authority`.
   The owner's decision is that the *concepts* of the prakriyā (what a saṃjñā is, how a block of sūtras is entered, in what order
   kāryas happen, which of two sūtras wins) are to be taken from Pushpa Dixit, checked against the Aṣṭādhyāyī data.
2. The engine's structure departs from that teaching (`ashtadhyayi-ai/audits/engine_vs_pushpa_notes_1-9.md`, W1–W7): it scans the
   whole registry every step, uses numeric sūtra-id ranges as stand-ins for topic blocks (`engine/phase.py`,
   `engine/scheduler.py::_MULTI_TERM_RANGES`), and Art. 2 forbids "'prakaraṇa' labels" without distinguishing Pāṇini's own
   adhikāra-defined blocks from Kaumudī headings.

## Decision — new Article 23 (text in `CONSTITUTION.md`)
1. **Two keys.** A claim about a *concept* or a *conflict resolution* is implemented only when **both** hold:
   **Key A** — the Aṣṭādhyāyī data (Art. 22 T0 pāṭha; T7 ashtadhyayi.com sūtra data: anuvṛtti, adhikāra, `sutra_prayogas`) does not
   contradict it; **Key B** — Pushpa Dixit or Neelesh Bodas agrees, cited in a *concept card* by video id and timestamp.
2. **Order.** Authentic granthas (T1–T4) decide where their ruling is objective and workable; in doubt Pushpa Dixit decides.
   Where Neelesh Bodas differs from her, her reading is implemented and his is recorded as a declared conflict (Art. 15).
   *(Owner's clarification, 2026-10-09: "authentic granthas decide if they are objective and working; in case we have doubt then
   Pushpa Dixit will win".)*
3. **Override by fact only.** Her reading yields only to a *clear fact*: (a) the pāṭha / anuvṛtti / adhikāra text itself, or
   (b) an attested form (Art. 19). The Aṣṭādhyāyī data is then followed; the card is marked `overruled` with the evidence and shown to
   the owner. A commentator's opinion alone is not a clear fact — it is recorded as a conflict item and her reading stands.
4. **Scope.** Concepts and conflict resolution only. Not surface forms (Art. 19 still decides those from attested usage), not the
   words of a sūtra (T0–T2 still say what a sūtra says), and never an input to `cond()` (Art. 2): the card is a design-time
   source, like Art. 22. The runtime meta-rule book stays the Paribhāṣenduśekhara (Art. 21).
5. **Citation grade.** Raw auto-transcripts are not citation grade. A card may rest on a transcript passage only if every sūtra it
   names resolves in the brain's sūtra tables; otherwise the card is `gist-only` and cannot be Key B.
6. **Pāṇinian prakaraṇa is allowed as scope, Kaumudī prakaraṇa is not.** A block delimited by Pāṇini's own adhikāra heads
   (`adhikara_scope` in the sūtra's record) may decide which sūtras are *eligible*; it never reorders sūtras inside the block
   (Art. 3, Art. 21). Numeric id ranges standing in for blocks are to be replaced by adhikāra-scope records (a ratchet, not a
   deadline). The forbidden identifiers of `test_no_kaumudi_leakage.py` are unchanged.
7. **Art. 22 edit.** New top row *T-A* (the ācāryas of Art. 23, concept/conflict questions only); T8 now reads "primers other than
   the ācāryas named in Art. 23".
8. **Art. 10** counts twenty-four Articles (0 through 23).

## Interpretation (settled by the owner, 2026-10-09)
- **Bhāṣya / vārttika vs Pushpa Dixit.** Granthas win when objective and workable; in doubt she wins and the disagreement is a
  recorded conflict (Art. 15). This restores, with a doubt clause, the 2026-10-06 rule "authentic granthas decide".
- **"Clear fact"** (§3) is limited to pāṭha text and attested forms, so a teacher is never overruled by another teacher or
  commentator alone.

## Verification (Art. 10 §2)
`pytest tests/constitutional` on the branch; grep that nothing else cites "twenty-three Articles"; `git diff` limited to
`CONSTITUTION.md` and this file. No engine code changes in this amendment.

## Follow-on (not part of this amendment)
Concept cards (`ashtadhyayi-ai/cards/`), the sūtra-interaction graph, and replacement of range heuristics by adhikāra scope.

## Acceptance
Owner, 2026-10-09 (session instruction quoted above).
