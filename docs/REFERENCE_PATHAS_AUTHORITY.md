# Reference pāṭhas as authority

Principle (owner): Pāṇini's pāṭhas are part of the rules. A word that the rules derive from a pāṭha entry is **engine-verified**, with the entry cited. Only what no pāṭha holds stays outside.

## Inventory (`python3 -m tools.patha_inventory` → `sig/patha_inventory.json`)
| pāṭha | in repo | status |
|---|---|---|
| dhātupāṭha | `dhatupatha_upadesha.json`, 2240 entries (gaṇa, upadeśa, it-markers, artha, set/anit flags) | rich; 1165 in gaṇa 1 includes curated extensions — mark which entries are Pāṇinian vs added |
| gaṇapāṭha | `ganapatha_full.json`, 262 gaṇas / 5592 members, each linked to a sūtra | good; **`akrti` is 0 for all** (derived from the name only), so no gaṇa is known to be open |
| uṇādi | `unadi_patha.json` | **empty stub** (0 of ~750–800) — biggest hole |
| nipātana | no list; each nipātana sūtra is its own authority | deferred as a batch (L5), e.g. 5.1.65/76/90/113/114 |
| sarvādi / tyadādi / ajādi / svarādi / cādi / prādi | duplicated in small files (`sarvadi_slp1` 36, `ganapatha.json` 31, `ganapatha_full` 26 — three different counts), `ajadi_gana_slp1` 19 vs 23 | one source of truth needed: `ganapatha_full` |
| liṅgānuśāsana | 14 stems | stub; not Pāṇini's, a lexical source |
| taddhita pratyaya list | 4 entries | stub; the sūtras teach the set |

## `authority` record
Carried by any step or verdict that rests on a pāṭha membership:
`{"pATha": "gaRapAWa", "entry": "anupravacanAdiH/anupravacana", "sutra": "5.1.111", "source": "ashtadhyayi-ai ganapath", "edition": "ganapatha_full@<hash>"}`
Same shape for dhātu (`entry` = `dhatupatha_id`, e.g. `01.0001`) and uṇādi (`entry` = sūtra number). `engine/gana.py` gains `authority(name, stem)` returning it (or None); `in_gana` stays the boolean.

## Verdict classes
- `derived-from-pATha`: the rules derived the form and every pāṭha fact used has an authority record. Counts as verified.
- `listed`: the form is licensed by a closed list or a nipātana sūtra and the sūtra itself performs the form (never a recipe that knows the answer); the authority names the sūtra / list.
- `lexicon-intake`: stem in no pāṭha (proper names, ārṣa, corpus faults); entered with `source` in `subanta_lexicon.json` after owner review; not verified.

## Nipātana and uṇādi
The list only licenses; the sūtra does the work. A nipātana sūtra's `act` produces the irregular form through `apply_rule` on the tape (ādeśa/āgama as the sūtra says). An uṇādi sūtra is a vidhi sūtra file like any other (pratyaya + it-markers + kit/ṅit effects), with `authority.pATha="uRAdi"`; a stem is verified only if the uṇādi sūtra attaches to a dhātu of the dhātupāṭha.

## ākṛtigaṇa extension
A gaṇa flagged open (`akrti`: true, set from the commentary list, not the name) accepts a caller-added member only through `data/inputs/gana_extensions.json` rows `{gana, member, reason, reviewer, date}`; the authority then reads `edition: "extension"` and the verdict stays `derived-from-pATha` only if the owner-reviewed row exists. Every use is logged in the trace.

## Surfacing
trace step → `authority` list; API step and word verdict → `authority` + class; Subhastini badge: ✔ derived / ◐ listed / ○ intake (see `PLAN_ENGINE_VERIFIED_WORDS.md`).

## Order
1. One gaṇa source (retire the small duplicates; reconcile sarvādi 26/31/36 against the Kāśikā list). 2. Flag real ākṛtigaṇas. 3. Load the uṇādi pāṭha, then uṇādi sūtras by pāda. 4. Nipātana batch. 5. `authority()` and the verdict classes.

## Cross-reference (sūtra → list → file → loader → status)
`python3 -m tools.patha_inventory` writes `sig/patha_inventory.json` key `xref` (332 rows): 260 gaṇa-linked rows (32 wired to a real sūtra, 228 present but **unused** — the sūtra is still a stub), 10 pāṭha/in-sūtra lists, dhātu-gaṇa names, and heuristic "-Adi" words. `missing` = sūtra names a list with no data. Ratchet: `docs/data/patha_missing_baseline.json` (52 today); `tests/unit/test_patha_inventory.py` fails on any new entry. Known missing: uṇādi (0 rows), saṃkhyā words (1.1.23), pāraskarādi (6.1.157) and vargyādi (6.2.131) (gaṇas with no members), dhātu sub-lists puṣādi/dyutādi/kuṭādi, ~47 heuristic candidates to be reviewed against the Kāśikā. Kāśikā-attested extra members have no data file at all.

## Intake (agent D) — `python3 -m tools.intake_patha`, then `python3 -m tools.build_ganapatha_full`
Sources: data-master (`unaadi`, `dhatu`, brain db `ganapath`, `sutraani/kashika.txt` as the cross-check). Decision per item: **A** derived by the engine, **B** stored from a pāṭha, **C** source needed. Decisions with Kāśikā evidence: `docs/data/patha_xref_classified.json` (52 entries; 6 stay missing = `patha_missing_baseline.json`).
| item | decision | data / where |
|---|---|---|
| uṇādi (3.3.1, 3.4.75) | B, 748 sūtras (157/123/160/238/70), numbering contiguous | `data/inputs/unadi_patha.json` |
| dhātu gaṇasūtras (ghaṭādayo mitaḥ …) | B, 30 rows | `data/inputs/dhatupatha_ganasutras.json` |
| puṣādi, dyutādi, kuṭādi, jakṣityādi, radhādi … | B, already in the engine's dhātu entries (`antarganas`, 538 of 539 source marks); one stray source mark (phul 06.0174, beyond the Kāśikā bound of kuṭādi) deliberately not taken; ḷdit is A (it-marker, 1.3.2) | `dhatupatha_upadesha.json` |
| pāraskarādi (6.1.157) | B: members were hidden in the brain's `<<…>>` notes; 5 verified in the Kāśikā (rathaspā repaired from the brain's slip), gaṇasūtras 163/164 kept as rules; ākṛtigaṇa | overlay → `ganapatha_full.json` |
| vargyādi (6.2.131) | A: the yat-forms (4.3.54) of digādi from varga to its end — stored as `derived`, not as words | overlay `extra.derived` |
| sarvādi 26 → 35 | B: the three enumerating gaṇasūtras expanded in place from Kāśikā 1.1.34–36; pūrvādi (9, 7.1.16) and ḍatarādi (5, 7.1.25) are stretches of it | `ganapatha_full.json` |
| haritādi (4.1.100), kaṇvādi (4.2.111) | B: stretches of bidādi / gargādi named by the Kāśikā / Kaumudī | `sub_ganas` → `ganapatha_full.json` |
| ākṛtigaṇa flag | B: 0 → 27 gaṇas, read from the Kāśikā of the gaṇa's sūtra; 7 gaṇas share a sūtra with others and stay unresolved (`sig/patha_intake.json`) | `akrti` |
| 20 heuristic hits, 7 in-sūtra lists, 5 aliases (prādi, lohitādi, yājakādi, sukhādi, gotrādi), kuru-nādi (letter), kaṣādi (sūtra range) | not lists / A | `patha_xref_classified.json`, `sutra_aliases` |
| sense-restricted members in the brain's notes (bhidā vidāraṇe …, 60 gaṇas) | candidates only, `members_restricted` with `verified_in_kashika`; not in `members` | `ganapatha_full.json` |
| saṃkhyā (1.1.23) | bahu, gaṇa, vatu, ḍati stored; -vatup / -ḍati by tag (A); the primitive numerals are laukika: **C** | `samkhya_patha.json` |
| svapādi (6.1.188), indrajananādi (4.3.88, open ākṛtigaṇa) | **C** | baseline |
| nipātana, liṅgānuśāsana | no list in Pāṇini's pāṭhas / not Pāṇini's | unchanged |

Proposed engine wiring (main session): `engine/gana.py` — `authority(name, stem)` reading `sutra_aliases` (a sūtra reads another's gaṇa), `members_restricted` (only with the sense) and `derived`; load `unadi_patha.json` for the uṇādi sūtras; retire `sarvadi_slp1.json` (36 words incl. invented 'priya-viśva', 'māsa-pūrva'), `ajadi_gana_slp1.json`, `tyadadi_slp1.json`, `ganapatha.json` in favour of `ganapatha_full.json`.
