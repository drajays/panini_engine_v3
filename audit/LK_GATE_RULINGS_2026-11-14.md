# LK case gate: rulings and what was done (2026-11-14)

Scope: the 248 sūtras the LK case gate (`tools/lk_cases.py`) covers. Starting point: commit `3c03d3ab`
(11 confident, 30 working, 131 FAIL, 76 unrunnable). Re-run any sūtra with `python3 -m tools.lk_cases run <ids>`;
`make lk` prints the summary.

## Result

| grade | before | now |
|---|---|---|
| confident | 11 | 13 |
| working | 30 | 33 |
| FAIL | 131 | 122 |
| NO_POSITIVE | 0 | 4 |
| UNRUNNABLE | 76 | 76 |

FAIL by sub-kind (a sūtra can sit under more than one): 0 engine errors (was 6), 106 with a wrong form, 22 with the
right form but no firing (was 29). Changes: 4.1.63 and 8.4.62 became confident. 8.4.14, 8.4.15 and 8.4.63 became working.
2.4.62, 4.1.172, 4.3.82 and 7.2.98 are now NO_POSITIVE: their positives were mis-assigned and became negatives (see Q1),
so they need real positives.

## Q1: right form, sūtra not fired. The trace is required.

Article 16 counts a sūtra only when a derivation in the suite invokes it and it changes the state, and Article 0 wants
the trace to explain the form. A case where the form is right but the sūtra did not fire is never a pass and is never
marked "redundant". The gate reports it as the sub-kind `not_fired`.

How the 29 cases were triaged (`scratch/triage_not_fired.py` lists the rules that applied in the branch that gave the form):

| bucket | sūtras | what it needs |
|---|---|---|
| A. A rival rule or route makes the form; the sūtra is a stub or is never scheduled | **fixed:** 8.4.14, 8.4.15. **Open:** 2.1.14 (2.2.18 makes the samāsa), 3.2.112 (3.3.13), 3.3.103, 3.3.156 (3.3.161 takes the liṅ), 4.1.168 (4.1.86), 4.2.38 (4.2.37), 4.2.107 (4.1.83 + 4.3.53), 4.4.41 (4.4.8), 7.2.56, 7.3.69 (7.3.52 kutva never reaches ṇyat, so bhojya is right by accident), 8.3.26 (8.3.23 not at the seam), 7.1.74 Sucaye | A real cond and act, plus an apavāda/bādhaka declaration where a general rule wins today |
| B. The sūtra changes no form by its nature (niyama, pratiṣedha, atideśa, a sense frame) | 1.1.59, 1.3.15, 1.4.8, 3.4.70, 4.1.58, 4.1.93, 4.1.94, 4.2.7, 8.4.43, 8.4.49 | Must still pass through `apply_rule` and leave its own trace row (BLOCKED / APPLIED on the state it governs). `OK_STATUS` was **not** widened |
| C. The sūtra legitimately does not apply: the case was mis-assigned | 4.1.63 क्षत्रिया (Kāśikā: अयोपधादिति किम्? क्षत्रिया), 7.2.98 tvam/tvām/mayā/tvayi/mayi (sup forms are 7.2.97/7.2.94; 7.2.98 is for a pratyaya or uttarapada: त्वदीयः, मत्पुत्रः), 4.1.172 (in the gotra sense kauravya is 4.1.151's), 4.3.82 (aśmamaya is a vikāra, 4.3.143), 2.4.62 (bare stem, no tadrāja) | **Done.** Recast as negatives of kind `produced`, citing the Kāśikā (`scratch/apply_lk_triage.py`). The Kāśikā positives त्वदीयः and मत्पुत्रः were added but cannot run yet |

The ṇatva fix (bucket A) works like this:

- After the pada merge, an upasarga's varṇas carry `upasarga_v` (`engine/phases/pada_merger.py`).
- 8.4.2 now stops at the upasarga | dhātu seam when the n belongs to the dhātu or begins a pratyaya.
- 8.4.14, 8.4.15 and 8.4.16 are real rules, scheduled right after 8.4.2 in `core/phases/tripadi.py`.
- One open gap: 8.4.16 परियाणि (pariyARi). The loṭ route in `pipelines/tinanta.py` runs a short tripādī list without the
  8.4 ṇatva rules. That file is a hotspot, so the change needs the coordinator.

## Q2: the three owner cases (brain R-012, R-013, R-014; mirrored as SC-008, SC-009, SC-010)

- **7.1.74.** dadhīca is rejected. dadhi + ṭā → दध्ना is 7.1.75, so it is a negative of kind `produced`, not a positive.
  - Positives are the Kāśikā's ग्रामण्या, ग्रामण्ये and शुचये.
  - The num branch (ग्रामणिना, शुचिने) is the `declined` reading.
  - वारिणा is `produced`. SK पीलुने is recorded but cannot run yet.
  - Also fixed: `grAmaRiNA` was bad SLP1 (N is ṅ), and that case had been marked positive although it is the declined branch.
  - 7.1.74 itself is still a gate stub: the engine has no bhāṣitapuṃska stem fact (Art. 18 gap).
- **7.3.69.** Both readings agree with the Kāśikā (भोज्यं निपात्यते भक्ष्येऽभिधेये … भोग्यः कम्बलः). They only collided because
  the spec could not state the sense.
  - The sense is now the vivakṣā value `arthaViSeSa=Bakzya`.
  - भोज्यः, भोज्या and भोज्यम् with Bakzya are positives.
  - भोग्यः without Bakzya is `produced`; with Bakzya it is `excluded` (the owner's case).
  - The engine gives भोज्यः in both senses, because 7.3.52 kutva is built for Gurac only. That is why भोग्यः-produced fails.
- **8.4.62.** There is no conflict: the sūtra is optional (अन्यतरस्याम्). The SK gives वाग्घरिः and वाग्हरिः literally.
  - The owner's वाघरिः is the `declined` reading.
  - The broken first case (its text said hariḥ, its expected value said hasati) was split into a hasati pair and a hariḥ pair.
  - `agniciddhasati` (bad SLP1) is now `agnicidDasati`.

## Q3: counts. The gate replaces the proxy, not the ledger.

- `tools/sutra_class.py` changes:
  - For any sūtra the gate grades, LK `confident` replaces the "named in tests at least 5 times" proxy.
  - An LK `FAIL` holds the sūtra at `working` at most.
  - Invoked and moved still come only from the firing ledger.
  - `docs/CONFIDENT_SUTRAS.md` prints the ledger date and the verdict date, and warns when the ledger is older.
- `tests/regression/test_lk_cases.py`:
  - Always on: the committed verdicts must match the fixtures and `grade()`, so no grade can be hand-edited.
  - With `LK=1`: every confident or working sūtra is re-derived, and its grade may not fall.
- `make coverage` now runs the ledger with `LK=1`, so the LK derivations count as invoked and moved (Art. 16(1)).
- `make status` warns when the ledger is older than the verdicts.

## Q4: schema. Added through the builder only.

- `taddhitArtha`: `BAva` (5.1.119–136) and `karman` (5.1.124 ff.).
- `arthaViSeSa`: `Bakzya` (7.3.69). `arthaViSeSa` now also applies to `krdanta`.
- `sutra_5_1_130.py`: the samagra read `karmaci`; it now reads `karmaRi` (upstream row 51130 has कर्मणि).
- The 6 engine errors became real verdicts. They are still FAIL: 5.1.119 ff. are gate stubs that never add tva/tal.

## Fixes to the harness found along the way

- `_mutate` used the lru-cached `run()`, so every "redundant" or "indeterminate" mutation result was the unmutated reading.
  It now calls `run.__wrapped__`.
- A negative of kind `produced` passed even when the form was never produced. It now must be produced, as `declined` must.
- A kṛdanta case that states a sense the harness never varies (such as `arthaViSeSa`) now runs with its own vivakṣā.

## Engine gaps: what was done, what remains

- **Done (8.4):**
  - 8.4.60 तोर्लि.
  - 8.4.62 झयो होऽन्यतरस्याम् (optional).
  - 8.4.63 शश्छोऽटि (optional, pada-final jhay).
  - 8.4.14, 8.4.15 and 8.4.16.
  - 8.4.55 खरि च now also turns a c-varga stop made by 8.4.40 ścutva into car. Before, अग्निचिद् + शेते stopped at अग्निचिज्शेते.
- **Open, 8.4.60.** The fixture expects `BavAMllunAti`, with anusvāra M. The Kāśikā has भवाँल्लुनाति, an anunāsika, and by
  Art. 4 §2 the anunāsika ~ is not the anusvāra M. The engine also has no SLP1 surface for an anunāsika consonant.
  **Owner decision needed.**
- **Open, samāsa cluster (2.1 / 2.2).** This is not one fix. For पञ्चन् + नदी no samāsa-vidhāyaka fires: 2.1.20 is a stub and
  the spec carries no samāhāra sense. So there is no samāsa saṃjñā, and 2.4.71 sup-luk never applies. That is where
  `paYcannadIs` comes from. Each vidhāyaka needs its real cond and its vivakṣā.
- **Open, 8.3 cluster.**
  - 8.3.23 does not make the anusvāra at a two-pada seam (`samskartA`). It is not in the spine in `core/phases/tripadi.py`,
    and its cond only sees an upasarga Term or one merged pada. That cond also mixes in the within-pada m-before-jhal case,
    which belongs to 8.3.24, not 8.3.23.
  - 8.3.5, 8.3.6, 8.3.10 and 8.3.12 (ru) are stubs.
- **Open, sanādi.** grah + san (jiGfkzati) needs 1.2.8, 6.1.16, 7.2.12, 7.4.62 and 8.2.31/37/41 on the san route in
  `pipelines/tinanta.py` (a hotspot).
- **Open, taddhita / kṛt.** These are case by case.
