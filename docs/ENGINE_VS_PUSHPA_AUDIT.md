# panini_engine_v3 against Pushpa Dixit — strengths, weaknesses, plan (2026-10-09)

Method: read `engine/{scheduler,phase,core_loop,resolver,paribhasha,strata,state}.py`, `sutras/adhyaya_1/pada_4/sutra_1_4_13.py`,
`sutras/adhyaya_6/pada_1/sutra_6_1_1.py`, `data/inputs/asiddha_strata.json`, `CONSTITUTION.md`, `docs/STATUS.md`; compared with the 13 concept
cards in the brain (`ashtadhyayi-ai/cards/`, Art. 23 two keys) and the prakaraṇa map (`ashtadhyayi-ai/graph/prakarana_map.json`).
Every finding is something read in the code; **[hyp]** marks what still needs a test. Brain pages: `/cards`, `/prakarana`, `/machine` in `Brain.command`.

## Strengths — keep, do not rebuild
| # | strength | evidence | Pushpa card |
|---|---|---|---|
| S1 | Law that forbids prayoga-first / Kaumudī order, blindness of `cond`, one file per sūtra, SIG routing, honest coverage, gaps as outputs, oracle ≠ homework | CONSTITUTION Art. 2, 3, 7, 11, 16, 18, 19 | C-012 (her critique of SK order) |
| S2 | Every resolver layer names the paribhāṣā it implements (PŚ 38, 50, 57); Rajpopat SOI is a diagnostic that never wins | `engine/resolver.py` header, `engine/paribhasha.py` | C-009 |
| S3 | Asiddha is a visibility **matrix**, not a flag: tripāḍī, ābhīya, ekādeśa-for-ṣatva/tuk, plus Kāśikā-sourced exceptions (8.3.13, 6.3.111, 6.1.113) | `engine/strata.py`, `data/inputs/asiddha_strata.json` | C-010 (1)(3)(5) |
| S4 | Lopa kept as a ghost (adarśana), sthānivat module | `engine/lopa_ghost.py`, `engine/sthanivat.py` | C-008 |
| S5 | Phase chain upadeśa → pratyaya → aṅgakārya → sandhi → tripāḍī; adhyāya 1 eligible in every phase (saṃjñā looked up when named) | `engine/phase.py` | C-003, C-005 |
| S6 | Test mass and gold sweeps: ≈17,000 constitutional tests, rāma 24/24, gaṇa-1 laṭ 1,152/1,165 vs recipe | README, `handover.md` | — |
| S7 | Glass-box decision record (layer, winner, losers, reason) | `resolver.Decision`, `record_decision` | — |
| S8 | AMENDMENT 22's lexicon `vyutpatti` is the same thing as a path through the Pratyayabheda machine | `docs/AMENDMENT_22.md` | C-004 |

## Weaknesses
| # | weakness (evidence) | Pushpa card | fix |
|---|---|---|---|
| W1 | Global scan: `enumerate_candidates` walks all ~3,985 records every step, then dry-runs survivors (`effective_candidates`) | C-001 | P1–P2 |
| W2 | Numeric ranges stand in for blocks: `_MULTI_TERM_RANGES` calls 6.1.1–229 "saṃhitā" (data: saṃhitā = 6.1.72–6.1.157; 6.1.1–12 is dvitva); `_PHASE_RANGES`; `_skip_krt_window` | C-001 | P2 |
| W3 | 6.1.1 fires on a hard-coded form (`pawat`), on `san` only, or on a `dvitva_recipe` flag — not one block with five nimittas (liṭ, san, yaṅ, caṅ, ślu) | C-007 | P5 |
| W4 | 1.4.13: one boolean `anga` tag, once (`("1.4.13_anga",0)`), taddhita cases by pipeline flags; aṅga must be per pratyaya | C-006 | P5 |
| W5 | adhyāya 4–5 and 3.4.118+ outside the loop (`_PHASE_RANGES`); taddhita only by hand pipelines | C-004 | P3 |
| W6 | Two engines: 193 hand-ordered pipelines + the loop; C4 turns recipes into fixtures, i.e. away from prakaraṇa order | C-001 | P3–P4 |
| W8 | `CONFLICT_OVERRIDES` = 10 named pair verdicts (AMENDMENT 19): āṭ/aṭ before caṅ-dvitva (6.4.72/71 over 6.1.11), ātva before dvitva (6.1.45 over 6.1.8), īṭ before s-lopa (7.3.96 over 7.4.50)… They look like **stage order** (āgama → dvitva → aṅga-kārya); a stage model would derive them instead of patching pairs **[hyp]** | C-013 (open) | P4 |
| W9 | `asiddha_strata.json` ābhīya range is **6.4.22–6.4.129** ("up to भस्य"). Kāśikā ("आ भात्" = to the end of the adhyāya), Bālamanoramā ("आ पादपरिसमाप्तेः"), sūtrārtha and Neelesh Class 29 all give **6.4.22–6.4.175**; the 6.4.129 reading is Böhtlingk (Art. 22 T9, zero prāmāṇya). Also `not_modelled`: the **samānāśraya** condition (asiddhavat only when the two rules have the same āśraya, Kāśikā) — modelled as "full mutual invisibility" | C-010 (accepted) | **P2b — first behaviour fix** |
| W10 | Antaraṅga decided by **dry-run probing** (`_zones`, `_reach`); PŚ 38 antaraṅga is still `not_modelled` as a procedure | needs a card | P5 |
| W11 | Sūtra ids typed in engine code: `it_rules = 1.3.2…1.3.9` in the resolver and ids inside `CONFLICT_OVERRIDES`, against `paribhasha.py`'s own "no sūtra id typed by hand" | C-002 | P2 |
| W12 | Breadth: 287 / 3,983 implemented (7.2 %), 222 confident (`docs/STATUS.md`, 2026-10-05) | C-001 | P7 (by prakaraṇa) |
| W13 | No prakriyā label per sūtra (only `derivation_class` strings); shared saṃjñā/sandhi sūtras vs per-prakriyā sūtras (7.3.101 vs 7.3.102) not representable | C-003 | P1 |
| W14 | No stage (sopāna) structure; Pushpa: 13 sopānas, five upāṅgas before aṅga-kārya — lists not yet found | C-013 (open) | P4 |
| W15 | Pada identity is merged at tripāḍī entry (`advance_phase`); rules that need pada/apada earlier rely on 1.4.14 firing in time **[hyp]** | C-005 | P5 test |
| W16 | Constitution Art. 2 banned prakaraṇa labels; Art. 23 §6 now allows adhikāra blocks, but topical prakaraṇas (saṃprasāraṇa, nalopa, numāgama) are defined by **anuvṛtti descent**, which §6 did not name | C-002 | AMENDMENT 24 |

## What the brain now gives the engine (no code needed)
`make prakarana S=<sūtra | P04 | C-007>` prints the prakaraṇas (Pāṇini's data, Pushpa's names), her stated extent, and the cards.
Differences between her extent and the data are flagged: nalopa (hers 6.4.23–33, data 6.4.23–55), saṃprasāraṇa (hers 6.1.15–44, data 6.1.13–44).

## Plan (ordered by risk; each phase gated as in `PRAKARANA_MACHINE_PLAN.md`)
1. **P0** baselines + counters (no change).
2. **P1** scope index from brain data: adhikāra blocks (73) + anuvṛtti-descent blocks + per-sūtra prakriyā label (W13); shadow run `fired ⊆ eligible`.
3. **P2** replace range heuristics (W2, W11); **P2b** fix W9 (6.4.22–175 and samānāśraya) — card C-010 is accepted, Key A is Kāśikā + data; sweeps must not regress.
4. **P3** Pratyayabheda machine drives derivation; bring taddhita into the loop (W5, W6).
5. **P4** stages as blocks once C-013 is accepted; try to **delete** the ten overrides (W8) and measure.
6. **P5** per-card fixes: W3, W4, W10, W15 — test first, from Kāśikā/attested forms.
7. **P6** completeness invariant + Vidyut floor; **P7** breadth by prakaraṇa.
