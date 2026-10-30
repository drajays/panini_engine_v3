# Plan — finish the Laghukaumudī sūtras first (written 2026-10-30)

Owner: the Laghukaumudī (LK) scope, 1087 sūtras, is finished before anything else (S24 retirement, teaching UI, corpus coverage follow it).
Status source: `docs/data/lk_worklist.json` × `sig/sutra_class.json`; refresh with `python3 -m tools.sutra_class && python3 -m tools.lk_plan && python3 -m tools.deferred_register`.

## 1. Status (2026-10-30)
| status | LK sūtras | meaning |
|---|---|---|
| confident + confident_structural | 187 | invoked, moves the tape, cited, tested ≥ 5× |
| working | 262 | real cond/act, exercised |
| **unexercised** | **446** | implemented, but the firing data (`sig/…`) predates T9–T14 and the unit tests; most are done, not proven — **step 0 below refreshes it** |
| pending_structural | 61 | definitional, class proof pending |
| gate_only | 57 | cond is a gate, no real act yet |
| **placeholder** | **74** | not implemented: 6.4 (40), 6.3 (18), 6.1 (15), 6.2 (1) |

Read this honestly: the "open 638 of 1087" in `DEFERRED_SUTRAS.md` mixes *not implemented* (placeholder 74 + gate_only 57 + the 187 left-out-on-purpose entries) with *not yet proven by the sweep* (446). The real work is about **190–260 sūtras**, not 638.

Left out on purpose (187 rows) by missing feature: nipātana batch 40 · samāsa machine 37 (compound as a pair of Terms) · chandas/Track G 24 · svārthika design 12 · it-marker audits 11+4+2+2 (1.3.3/1.3.4/1.3.7, 7.4.32) · vikalpa across sūtras 7 · samartha-vibhakti 8 · comparatives 5 · rest ≤ 3 each.

## 2. Order (each step is one session unless noted; agents = worktree forks on disjoint files)
| # | work | closes | agents |
|---|---|---|---|
| 0 | refresh exercise data: one niced `tools.firing_coverage` run + `sutra_class`; commit the new `sig/` baselines | turns "unexercised" into real status; exposes the true gap list | none (one heavy job) |
| 1 | it-marker audit 1.3.3 / 1.3.4 / 1.3.7 / 7.4.32 (agent K, in flight) + `kva` | ~19 deferred 5.x rows, 5.4.17–19, 42–55, 5.2.31–34 | K |
| 2 | adhyāya 6 placeholders: 6.4 (40), 6.3 (18), 6.1 (15), 6.2 (1) — the largest unimplemented block; per-pāda forks (6.1 / 6.3 / 6.4), each with its own test file | 74 placeholders | 3 |
| 3 | gate_only + pending_structural (118): adhyāya 1 (37), 6 (19), 7 (16), 2 (15), 8 (13) — real cond/act or a recorded class proof | 118 | 2 (1+2 / 6+7+8) |
| 4 | samāsa machine: a compound as a pair of Terms (S30, S36, S62, S66); then re-open the 37 deferred rows and remove the one-Term shortcuts | 37 rows + 6 shortcuts | main only (shared engine), then 1 fork for the sūtras |
| 5 | nipātana batch: one generator, 40 sūtras act through `apply_rule` (the list licenses, the sūtra performs) | 40 rows | 2 (4.x / 5.x) |
| 6 | samartha-vibhakti (S16) + vivakṣā for denoted things; svārthika design (owner decision: how a senseless "svārthe" pratyaya is licensed) | ~26 rows | main + 1 |
| 7 | vikalpa exploration across competing sūtras (S32, S45, S52) in the scheduler | 7 rows + 4 shortcuts | main only |
| 8 | Track G (chandas/svara) — only the LK-scope Vedic sūtras (24); the rest of Vedic stays after LK | 24 rows | 1 |
| 9 | end gate: all 1087 in {confident, confident_structural, working} or explicitly `left-out` with a reason, `lk_plan` shows 0 placeholder, 0 gate_only | LK done | — |

Rough size: steps 0–3 ≈ 4–5 sessions, 4–7 ≈ 6–8, 8 ≈ 1–2, total ≈ 12–15 sessions at the current pace (T13 + T14 = 400 sūtras in 2 sessions with 4 parallel agents).

## 3. Rules that keep quality while cutting tokens
- **One batch = one table + one generator + one test file** (T9–T14 pattern). The generator lives in the scratchpad until the batch is accepted; no helper files under `sutras/`.
- **Agents write only sūtra files + their own test file**; shared files (`engine/*`, `tools/build_vivaksha_schema.py`, `data/*`, `docs/*`) are edited by the main session from the agent's ≤ 25-line report. Ledger ids are pre-allocated per agent (S70+ next free: check the ledger tail).
- **Laws agents must be told every time** (cost of forgetting = a rework round): `vivaksita(state, key, value)` literals only and the value's form must be in the sūtra's own samagra; no word-specific recipes; strict xfail with cause rather than a fudge; focused tests only.
- **Full suite once per merged set**, niced, ~2 h (5.7 h when two agents also run tests); never edit source while it runs.
- **Merge order**: branch merges for committed agents; copy for uncommitted; conflicts are always in `tools/build_vivaksha_schema.py` + schema JSON → resolve the builder by hand, then regenerate the schema (`git checkout --theirs` + rebuild).
- **Don't re-read what a file already says**: start a session from `docs/STATE.md` (one page, below), not from `handover.md`'s history.

## 4. Handover design (token-lean)
Create `docs/STATE.md` (≤ 40 lines, overwritten at each session end, never appended): last commit, suite result, LK status table (section 1 numbers), next batch + stop sūtra id, agents in flight (worktree path + task), open owner decisions, next free ledger id. `handover.md` keeps only one Update paragraph per session (already the practice) and is read for its last paragraph only. Session start: `STATE.md` → `git status` → the batch. Session end: tools (`sutra_class`, `lk_plan`, `deferred_register`), `STATE.md`, one handover paragraph, commit.

## 5. Owner decisions waiting
1. svārthika design (5.4.7, 8, 13–15, 23, 27–29, 34, 38, 39; 5.1.58): how a sūtra that names no sense is licensed.
2. `kva` / 1.3.4: does `na vibhaktau tusmāḥ` cover taddhita vibhaktis (audit K will propose)?
3. Whether the LK end gate counts `unexercised` as done once the refreshed sweep shows the sūtra fires.
