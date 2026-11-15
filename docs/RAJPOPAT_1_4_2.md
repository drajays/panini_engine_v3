# 1.4.2 vipratiṣedhe paraṃ kāryam — Rajpopat's reading vs the tradition (2026-11-16)

Source read: Rajpopat, *In Pāṇini We Trust* (Cambridge PhD, 2022), `~/rajpopat_phd.pdf`: abstract pp. 6–7, §1.5 pp. 22–26, §2.7 pp. 49–51 (deva + bhis), ch. 6 pp. 199–204. Tradition read in the brain DB: Mahābhāṣya on 1.4.2 and 7.1.9, Kāśikā 1.4.2 and 7.1.9. This is a design-time comparison (Art. 22); the engine never reads it.

## The two readings
| | Tradition (Kāśikā, Mahābhāṣya, Paribhāṣenduśekhara) | Rajpopat |
|---|---|---|
| meaning of *para* | the rule that comes LATER in the Aṣṭādhyāyī | the RIGHT-hand-side operation (the affix side) |
| meaning of *vipratiṣedha* | tulyabalavirodha: conflict of two EQUALLY strong rules (Kāśikā; Mbh vārttika 1: *dvau prasaṅgāv anyārthāv ekasmin yugapat prāpnutaḥ*) | conflict between a rule on the LEFT operand and a rule on the RIGHT operand (DOI) |
| unequal rules | nitya / antaraṅga / apavāda / anavakāśa are stronger and defeat the other; 1.4.2 is not used (PŚ 38: *pūrvaparanityāntaraṅgāpavādānām uttarottaraṃ balīyaḥ*) | no such tools (Pāṇini taught none); SOI (same operand): the more specific rule wins; DOI: right wins by 1.4.2 |
| where it comes from | later commentators' paribhāṣās, justified by jñāpakas | Pāṇini's own text only |
| deva + bhis (7.1.9 ato bhisa ais vs 7.3.102 / 7.3.103) | Mbh/Kāśikā 7.1.9: para would give *devebhis*; 7.1.9 still applies after etva by *bhautapūrvya*, so it is nitya: *etvaṃ bhisi paratvāc cet … aistu nityas tathā sati* | 7.1.9 acts on the affix (right) so it wins; mutual blocking, so 'nitya' cannot apply |

Points of agreement: the winner for deva + bhis (devaiḥ); the Mahābhāṣya itself says *iṣṭavācī paraśabdaḥ* (para = "the desired rule"), which both sides admit makes plain 'later in order' a floor and not the whole story.
Points of disagreement: Rajpopat reads para as a position in the WORD, the tradition as a position in the TEXT; he drops nitya/antaraṅga/apavāda, the tradition keeps them. Status: contested in the literature (Kiparsky, Scharf — reported second-hand in docs/RESEARCH_PAPERS_PLAN.md item 8, [UNVERIFIED]); not adopted (Art. 23).

## What the engine does
Ladder (`engine/resolver.py`, AMENDMENT 17): named override → declared apavāda (PŚ 57) → vibhāṣā → antaraṅga → para. Rajpopat's SOI is a diagnostic only (`soi_proposal`); it can never win (Art. 21).

## Experiment: does "the right-hand operand wins" ever disagree with our resolver?
`tools/rajpopat_1_4_2_experiment.py` (offline, monkeypatches the resolver in its own process). For every contested decision the engine takes (layers para / antaraṅga / apavāda) it asks which Terms each rule would change (`probe`). If the changed Term sets are disjoint (Rajpopat's DOI) it computes the rule on the rightmost Term; overlapping sets (ekādeśa across a junction) are SOI and left to the engine. Mode `rp` re-runs the derivation with that rule forced to win; gold = the hand-checked paradigms in `data/reference/ashtadhyayi_com/shabda__data2.txt`.

Result (40 stems sampled evenly from the 9,007 paradigms × 24 cells = 960 cells):
* contested DOI decisions: 39; cases where the right-hand rule differs from the engine's winner: **0**; cells whose form changes: **0**; correct vs gold: 896 both modes (the same 64 mismatches in both: alternatives/vocatives, not rule conflicts).
* Pairs seen (14-stem run): 7.3.113 over 6.4.148 / 1.4.110; 6.1.101 over 6.1.77; 7.1.73 over 7.1.19 / 7.1.20; 6.1.107 over 6.1.77; 7.1.23, 7.3.120. In each, the later-in-order rule is also the right-hand one.
* Tiṅanta: 8 dhātus × 6 lakāras × 9 = 432 cells: 0 contested DOI decisions — the verb pipeline is mostly order-driven (`pipelines/tinanta.py`), so this probe says nothing about verbs.

## Verdict — can the engine show Rajpopat is wrong?
**Not on this data.** On nominal paradigms the two readings pick the same winner every time, so the engine cannot separate them; an honest result is "extensionally equivalent here". To show him wrong one needs a conflict where the DOI-right rule gives a wrong attested form while the tradition's ladder gives the right one (Kiparsky's counterexamples would be the place to look; not verified here — bring the examples and the script can run them). The engine also cannot show the tradition wrong: its ladder is the tradition's, with the ordering data (CONFLICT_OVERRIDES / ORDER_BEFORE, AMENDMENT 19) that exists exactly because plain para failed in some cases — Rajpopat's point that the tradition needs many extra tools is therefore visible in our own code (11 named overrides + 7 ORDER_BEFORE pairs).

## Defect found on the way (S187)
In rāma + bhis the trace says "para: 7.1.9 beat 7.3.102", but 7.1.9 is EARLIER than 7.3.102; the real basis is the declared apavāda (`apavada_of = (7.3.102, 7.3.103)` in sutra_7_1_9.py). The row is mislabelled `para` because the displaced losers are carried into the final para decision.
