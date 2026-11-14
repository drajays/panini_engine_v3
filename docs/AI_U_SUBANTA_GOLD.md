# अ-इ-उकारान्तशब्दा: as engine tests

Source: Neelesh Bodas, *नामप्रकरणे अकारान्त-इकारान्त-उकारान्ताः अजन्तशब्दाः* (26 Nov 2015, 44 pp): rAma, muni, sAdhu, mAlA, mati, nadI, Denu, vaDU, Pala, vAri, maDu, pratyaya by pratyaya. Teaching aid (Art. 23): the *set* of sūtras per cell is asserted, never the order; the Kāśikā (DB) settles disputes.

**Gold** `tests/regression/data/paddhati_subanta_ai_u.json`: the PDF's final सङ्क्षेपः tables (stem group → sūtras that fire; bracketed "prāpta" contenders are *not* counted), with ids resolved from the sūtra **names** through the sūtra table, never from the PDF's footnote numbers. Forms: rAma / Pala / nadI from `data/reference/shabda_gold` (attested), the other eight written out in the file (vibhāṣā cells carry two readings, each with its own sūtra path: mati/Denu ṅe, ṅasi, ṅas, ṅi; vAri/maDu sambuddhi). Cells covered: vibhakti 1–7 + sambuddhi (8-1); 8-2/8-3 are not in the PDF.
**Test** `tests/regression/test_paddhati_subanta_ai_u.py`: for each (stem, cell) the form ∈ `explore(derive)` readings and every listed sūtra is APPLIED in a branch yielding it.

## Result (242 cells)
| | cells |
|---|---|
| pass | 214 |
| strict xfail (engine gap / order-equivalent / PDF lists a vacuous sūtra) | 28 |
| wrong or missing final form | 2 (vAri, maDu 8-1: the `vAri`/`maDu` luk reading) |
| PDF≠Kāśikā | 0 found |

By class of the 28 (details and fixes in `docs/OPEN_FAILURES.md`): 3 gap 6.1.103 fuses 6.1.102 · 12 gap 6.1.90 not seen for the sup's āṭ · 4 gap S2 (ā-stem ṅit sups) · 2 gap neuter vocative · 2 gap 7.1.24 identity · 2 order-equivalent (7.3.102 before 6.4.3) · 3 PDF lists 6.4.3 on already-long stems.

## PDF errors noticed (do not copy)
- footnote [35] gives इको यणचि as 6|1|78 (it is 6.1.77; 6.1.78 is एचोऽयवायावः); [14]/[15] give ह्रस्वस्य गुणः as 7|1|108 (it is 7.3.108, as [30]).
- the rAma ṅasi row lists अक: सवर्णे दीर्घ: for ṅasi only (note [58]); the gold drops it for ṅas.
- 6.4.3 is listed for every stem in the āma row although for ā/ī/ū-final stems it has nothing to lengthen.

## Fixes made
None to the engine. Every miss is an architectural gap (fused sūtra, ṭāp Term, āgama inside an affix, a missing vibhāṣā branch), not a one-line bug; forcing them in this pass would have meant weakening the tests or touching core sūtras other jobs depend on. They are recorded as strict xfails so each fix flips a test.

## Next
1. neuter ik-stem sambuddhi `vAri`/`maDu` (the only wrong-form cells): a vibhāṣā at the luk (1.1.63 anityatva) — smallest real fix.
2. 7.3.112's āṭ as its own Term → 12 cells (and 6.1.90 for the sup).
3. 6.1.102 for masculine śas then 6.1.103 as s→n → 3 cells.
4. S2 ṭāp merge → 4 cells.
