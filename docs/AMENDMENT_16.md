# AMENDMENT 16 — अर्थनिर्देश (artha-nirdeśa) on adhikāra records

> Per Constitution Art. 10, this document records the proposed change, its
> rationale, and its acceptance status.

**Date opened:** 2026-10-01
**Author:** drajayshukla (ruling); drafting and implementation by Cursor
**Status:** **ACCEPTED 2026-10-01**. Article 20 is part of CONSTITUTION.md.

---

## 1. Background

The engine typed 4.1.92 तस्यापत्यम् as a plain `ADHIKARA` running to 4.3.120,
following the ashtadhyayi.com `data.txt` type field. The adhikāra corpus doesn't
list it as governing 4.1.93 onward, and Kāśikā doesn't call it an adhikāra:

> अर्थनिर्देशोऽयम्, पूर्वैरुत्तरैश्च प्रत्ययैरभिसंबध्यते। (Kāśikā 4.1.92)

Its own commentaries explain both directions:

- **पूर्वैः** (backward) is shown by the separate yoga. Nyāsa: "पूर्वैस्तावदणादिभिः
  सम्बध्यते; असंयुक्तविधानात्। अस्य यदि पूर्वैरभिसम्बन्धो न भवेत् `तस्यापत्यमत इञ्`
  इत्येकयोगमेव कुर्यात्"
- **उत्तरैः** (forward) comes from svarita, 1.3.11. Nyāsa: "उत्तरैरप्यभिसम्बध्यते;
  तेष्वस्य स्वरितत्वात्।" Padamañjarī: "उतरैरपि सम्बध्यते; स्वरितत्वात्साकांक्षत्वाच्च
  तेषाम्।" Mahābhāṣya: "अवश्यमुत्तरार्थमर्थनिर्देशः कर्तव्यः।"
- Siddhānta-Kaumudī: "…अपत्येऽर्थे उक्ता वक्ष्यमाणाश्च प्रत्यया वा स्युः।"

(All quotes verified in the local ashtadhyayi.com `sutraani/` texts:
`kashika.txt`, `nyaas.txt`, `padamanjari.txt`, `bhashya.txt`, `kaumudi.txt`, key `41092`.)

The `SutraType` enum couldn't express this. It is neither a pure forward scope
nor an eleventh sūtra-lakṣaṇa.

## 2. Ruling (Ajay, 2026-10-01)

4.1.92 is an artha-nirdeśa with a bidirectional connective scope. Through
svarita it acts as the governing heading of the apatya section (उत्तरार्थम्). It
should get a dedicated class if needed, written into the Constitution and based
on the rules.

## 3. Change

1. **No new `SutraType`.** Article 1's ten-fold list comes from the classical śloka
   and stays closed. The forward force is adhikāra by 1.3.11, so the record stays
   `ADHIKARA`.
2. **New class `engine.sutra_type.ArthaNirdesha`** (`artha`, `artha_dev`,
   `purva_from`, `source`), carried as `SutraRecord.artha_nirdesha`. Validated at
   import: it is only allowed on ADHIKARA, `purva_from` must precede the sūtra, and
   `source` must not be empty.
3. **Frame semantics.** The frame covers `purva_from` … `adhikara_scope[1]`
   (`scope_start` in the stack entry; `engine.gates.adhikara_in_effect` honours it)
   and carries the meaning label `artha`.
4. **4.1.92** gets `ArthaNirdesha(artha="apatya", purva_from="4.1.83", …)`, and its
   scope end moves from 4.3.120 to **4.1.178**, the end of the apatya section. No
   gate outside 4.1 cited 4.1.92.
5. **Article 20** is added to CONSTITUTION.md. Article 10's count goes from twenty
   to twenty-one Articles.

## 4. Enforcement

- `tests/constitutional/test_artha_nirdesha.py`: ADHIKARA-only, backward reach,
  and the `source` quoted verbatim in the sūtra docstring.
- `tests/unit/test_adhikara_gate_scope.py`: gate scope includes `purva_from`.
- `tests/unit/test_sutra_4_1_92_prAgdIvyatIyaSezAdhikAra.py`: the frame covers
  4.1.83–4.1.178 and not 4.1.82 or 4.2.1.

## 5. Acceptance

Accepted in writing by drajayshukla, 2026-10-01: "make unique class if needed —
put this in constitution — must be based on rules". This closes
`docs/SOURCE_CONFLICTS.md` SC-001.
