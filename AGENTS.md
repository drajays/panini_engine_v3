# AGENTS.md — entry point for every agent (Claude, Cursor, Codex, …)

Law: `CONSTITUTION.md` (wins over everything). Plan: `docs/SUTRA_COVERAGE_100_PLAN.md`.
Status: run `make status` (generated, dated) — never quote numbers from prose. Handoff: `handover.md`.
Enforcement is by tests/CI, not by this file. If a gate blocks you, fix your change, never the gate.

## Loop (vibe-coding friendly: 5 commands)
1. `make preflight S=6.1.97`  — shows existing file/tests/pipelines/claims. Exists → fix/extend, don't re-add.
2. `make brain S=6.1.97` — **read the brain first** (see "Brain" below). New file: `make scaffold S=6.1.97`.
3. `AGENT=<you> make claim ID=<task> SCOPE="6.1.97 6.1.98"` — exact IDs/paths; overlaps are refused.
4. Work. Run focused tests, then `make full-check`.
5. `make release ID=<task>` and update `handover.md` (status text only).

## Hard rules (each is a failing test)
- One sūtra = one file = one id (`test_sutra_identity`). New file: copy `sutras/_template.py`.
- Morphology only via `engine.dispatcher.apply_rule`. No pipeline logic, `_corrected_` routes, word/surface
  special cases, or new `_arm` keys. A pipeline step with no sūtra is a *gap* (Art. 18), not code.
- Ceilings only go down (`make ratchets`). Never edit gold/baselines to get green.
- Hotspots — coordinator only (`COORDINATOR=1`): engine/{scheduler,resolver,core_loop,dispatcher}.py,
  pipelines/tinanta.py, CONSTITUTION.md.
- Meaning/source ambiguity → stop and ask (Art. 22). Cite per Art. 14.
- Reviewers are read-only and a different agent from the author.

Hook setup once per clone: `make hooks`.

## Brain — the reference every agent reads (owner's instruction, 2026-10-06)
`~/data-master/ashtadhyayi-ai` (guide: its `AI_AGENT_GUIDE.md`; humans: `make brain-wiki`). Read-only; never a
`cond()` input (Art. 6). Built from ashtadhyayi.com (`~/data-master`, synced to upstream), every text tagged by
Art. 22 tier. SLP1 throughout; anunāsika `~` ≠ anusvāra `M` (Art. 4 §2).
- `make brain S=<id>` — samagra + case roles, vārttika/Bhāṣya/Kāśikā/SK gloss, udāharaṇa ＋ (≥2 sources) and
  pratyudāharaṇa －, authentic prakriyā steps, typed graph (anuvṛtti, adhikāra, saṃjñā, pratyāhāra, bādhaka …), conflicts.
- `make resolve S=<id>` — when sources disagree: T1 → T2 → T3 → T4 → T6 → T7 evidence. Decide, cite the tier.
- `make scaffold S=<id>` — metadata, samagra, Art. 14 citations; `cond`/`act` are yours, from the śāstra.
- Anunāsika doubt → apply 1.3.2: the upadeśa whose it-lopa yields the attested form wins
  (`$(BRAIN_PY) itcheck <upadeśa>` / `anunasika`).
- Vidyut in the brain is a T10 minimum-rule floor for a form, never a template or an authority.
