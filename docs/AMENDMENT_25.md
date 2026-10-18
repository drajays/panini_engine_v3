# AMENDMENT 25 — vivakṣā inputs for kṛt, taddhita, kāraka and pada (accepted)

**Status:** accepted by the owner 2026-10-18: *"do the amendment but all must be based on authentic reference, never discover
any rule, see Aṣṭādhyāyī data for any confirmation."* Every value below is therefore taken from the Aṣṭādhyāyī data
(samagra texts, ashtadhyayi.com dhātupāṭha) and cited; nothing is inferred by the engine.
Touches Art. 2 §2 (what `cond()` may read). Hotspot files (`engine/state.py`, `engine/dispatcher.py`, `engine/tape_init/`) are
coordinator-only.

## Problem
About 2,000 sūtras condition on things the State does not carry, so today they are gate stubs or read recipe flags:

| input | sūtras that need it (examples) | today |
|---|---|---|
| the meaning the speaker intends (artha) | kṛt 3.1.133 kartari, 3.3.18 bhāve, 3.3.113 kṛtyalyuṭo bahulam, 3.4.67–70; taddhita senses 4.1.92 ff. (Art. 20 frames); pada 1.3.72 kartrabhiprāye kriyāphale, 1.3.74 | absent; taddhita artha frame exists but nothing says which artha is meant |
| the upapada word | 3.2.1 karmaṇy aṇ … 3.2.97, 3.1.92 tatropapadaṃ saptamīstham, 2.2.19 | absent |
| sakarmaka / akarmaka | 3.4.69, 3.4.72, kṛt gates (3.2.x, 3.3.x), 1.3.88 | `Term.meta['karmakatva']` supplied by the recipe for 3.4.69 only |
| seṭ / aniṭ in niṣṭhā | 7.3.52 vārttika, 7.2.14–56 consumers | absent |
| which rule produced a varṇa | 6.1.79 vānto yi pratyaye, 6.1.80 dhātos tannimittasyaiva | absent |

Pāṇini's grammar starts from vivakṣā: what the speaker wants to say (meaning, kāraka relations, the co-occurring word) is the input to
a derivation, never its output. The engine already accepts such inputs: the lakāra's meaning (3.2.110 bhūte is chosen by the request),
the prayoga (3.4.69), the pada of an ubhayapadī root. This amendment makes the rest explicit, closed and auditable instead of letting
them leak in as recipe flags.

## Decision
1. **`State.vivaksha`** — a new frozen mapping set only by the start-state builders (`engine/tape_init/`) from the request, never by a
   sūtra. Keys are a closed schema, `data/inputs/vivaksha_schema.json`:
   * `artha` — one value from a closed list whose members are Pāṇini's own artha words in SLP1 (`kartf`, `karman`, `karaRa`,
     `sampradAna`, `apAdAna`, `aDikaraRa`, `BAva`, `tAcCIlya`, …) plus the Art. 20 artha-nirdeśa ids (`4.1.92` apatya …);
   * `kala` — `BUta` | `vartamAna` | `Bavizyat` (3.2.84 ff., 3.3.x);
   * `kartrabhiprAya` — bool, kriyāphala goes to the agent (1.3.72, 1.3.74);
   * `karaka` — role of each nominal on the tape (Phase M5).
2. **`cond()` reads a vivakṣā key only through `engine.vivaksha.vivaksita(state, key, value)`**, and only for a value that occurs in
   the sūtra's own `samagra_slp1` (lint: the literal passed to `vivaksita` must be a word of that sūtra's samagra). A rule can ask
   "is *bhāva* meant?" only if it says *bhāve* itself (or by anuvṛtti, which samagra already contains — Art. 4).
3. **Upapada is a `Term`** of `kind="upapada"`: the nominal stem (prātipadika upadeśa) placed before the dhātu, with its vivakṣita
   role in `vivaksha['karaka']`. 3.1.92 gives it the saṃjñā tag `upapada`; 2.2.19 compounds it later. `cond()` reads the tag, the
   stem's upadeśa (when the sūtra names stems, e.g. 3.2.16 cara), and the role through rule 2.
4. **Karmakatva is lexical data**: a `karmakatva` field per dhātupāṭha row (`sakarmaka` | `akarmaka` | `dvikarmaka` | `ubhaya`),
   cited per row to a T-tier source (Dhātupāṭha artha, Kṣīrataraṅgiṇī / Mādhavīya-dhātuvṛtti, Kāśikā udāharaṇa). A row with no
   cited value is an Art. 18 gap, never guessed. `Term.meta['karmakatva']` joins the allowlist in `Term`'s docstring and is copied
   from data by the tape builder, not set by recipes.
5. **Seṭ/aniṭ in niṣṭhā is derived, not stored**: the engine's own 7.2.x iṭ rules decide it on a probe clone
   (`engine.scheduler.probe`, not counted as firings); the result is a derived Term tag `nistha_set` / `nistha_anit`. Until 7.2.14–56
   are real rules, sūtras that need it stay gaps.
6. **Varṇa provenance is a varṇa tag** `origin:<sutra_id>` written by the dispatcher on every varṇa an ādeśa/āgama creates (cloned
   with the varṇa). `cond()` may read it. 6.1.80 then asks "was this e/o made because of the following y-pratyaya?" structurally.
7. **Art. 2 §2 is amended** to add to the permitted reads: `vivaksita(...)` under rule 2; Term kind `upapada` and its tags;
   `Term.meta['karmakatva']`; varṇa tags `origin:*`. Art. 2 §3 is unchanged: no coordinates, no surface spelling, no gold, no
   `data/reference/`.

## Pilots (Art. Gate S2: each lands as record + tests with zero further engine edits)
3.2.1 karmaṇy aṇ (upapada + artha: kumbhakāraḥ) · 3.3.18 bhāve (artha: pākaḥ) · 3.4.69 (karmakatva from data) ·
1.3.74 / 1.3.86 (kartrabhiprāya: corayate; bodhayati) · 6.1.80 (origin tag: lavyam, avaśyalāvyam; pratyudāharaṇa oyate, auyata) · 7.3.52 (probe: pākaḥ).
Expected forms from Kāśikā udāharaṇas (Art. 19).

## Enforcement
`tests/constitutional/test_vivaksha_named_in_samagra.py` (rule 2 lint) · `test_vivaksha_set_only_by_tape_init.py` ·
`test_karmakatva_from_data.py` (no recipe writes) · `test_varna_origin_by_dispatcher.py` · the existing Art. 2 static test extended
to the new reads.

## Implementation status (2026-10-18)
| decision | state |
|---|---|
| 1 `State.vivaksha`, set only by `engine/tape_init` | done; tiṅanta builders record `artha` from the requested prayoga (3.4.69: kartṛ / karman / bhāva) |
| 2 `vivaksita` + samagra lint | done: `engine/vivaksha.py`; vocabulary generated by `tools/build_vivaksha_schema.py` from the sūtras' samagra (artha 7, kāla 3, kartrabhiprāya 1 values, each with its citing sūtras); no sūtra reads it yet — first readers are the pada block (1.3.72/1.3.74) and kṛt |
| 3 upapada Term | permitted (Art. 2); lands with the kṛt mechanism (3.1.92, 3.2.1), which has no tape yet |
| 4 karmakatva data | done: `tools/build_dhatu_karmakatva.py` → `data/inputs/dhatu_karmakatva.json` from ashtadhyayi.com `karma` (2,229 rows; 10 engine-only rows are gaps); tape builder copies it; bhāve of a sakarmaka root marks avivakṣita karman (Padamañjarī 1.3.29: प्रसिद्धेरविवक्षातः कर्मणोऽकर्मिका क्रिया) |
| 5 niṣṭhā seṭ by probe | waits for real 7.2.14–56 |
| 6 varṇa `origin:` tags | done in `engine/dispatcher.py`; excluded from vacuity/marks comparisons; read by `engine/strata.varna_visible` (6.4.22) |
| 7 Art. 2 §2 | amended in CONSTITUTION.md |

Enforcement: `tests/constitutional/test_amendment_25_vivaksha.py` (schema cited, samagra lint, writers only in tape_init,
karmakatva equals ashtadhyayi.com, recipe-write ceiling, origin stamping).
