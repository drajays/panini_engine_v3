# AGENTS.md — entry point for every agent (Claude, Cursor, Codex, …)

Law: `CONSTITUTION.md` (wins over everything). Plan: `docs/SUTRA_COVERAGE_100_PLAN.md`.
Status: run `make status` (generated, dated) — never quote numbers from prose. Handoff: `handover.md`.
Enforcement is by tests/CI, not by this file. If a gate blocks you, fix your change, never the gate.

## Loop (vibe-coding friendly: 4 commands)
1. `make preflight S=6.1.97`  — shows existing file/tests/pipelines/claims. Exists → fix/extend, don't re-add.
2. `AGENT=<you> make claim ID=<task> SCOPE="6.1.97 6.1.98"` — exact IDs/paths; overlaps are refused.
3. Work. Run focused tests, then `make full-check`.
4. `make release ID=<task>` and update `handover.md` (status text only).

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
