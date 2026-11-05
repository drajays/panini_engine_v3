# Week plan: finish the Laghukaumudī scope (written 2026-10-31; budget resets Fri 2026-11-06 00:30; ~43% weekly budget left, 57% used)

## What "finished" means (honest)
1087 LK sūtras: 106 confident · 85 conf_structural · 367 working · 368 unexercised · 76 gate_only · 61 pending_structural · 24 placeholder.
FINISHED = no placeholder, no pending_structural, every unexercised sūtra is either invoked by a test that names it (fresh ledger) or carries a written deferred reason; gate_only classified. NOT "every sūtra confident". Realistic this week: all 24 placeholders + 61 pending + most gate_only + about half of unexercised; the rest listed in DEFERRED_SUTRAS.md with reasons. Do not promise more.

## Order (highest leverage first)
0. Harness doubt: the Kāśikā-prose source made 211/211 candidates FAIL — probably a harness fault (route/fire check), not 211 engine bugs. One sonnet agent diagnoses 10 rows (cheap) BEFORE any fix agent is paid for. If harness fault: fix tools/exercise_audit.py, re-run, then cluster-fix the true FAILs.
1. bhavya from `as` (A1): partial work sits in .claude/worktrees/agent-a8c71afde4f66ecac (krt_attach.py, sutra_2_4_52.py, sutra_3_1_96.py, tests/regression/test_bhavya_as.py; the agent died on an API error). A new agent continues from that worktree, runs focused tests, commits.
2. Ekādeśa span fix (core, fork of main model): record the sthānin span in the trace; ekādeśa replaces both terms (flips 3 strict xfails in tests/unit/test_ekadesa_both_terms.py; then 6.1.85 and 1.1.56 checks). Also the Amba SAdhi routing (6.4.35) and the visarga seam in pada_samhita.join.
3. Adhyāya 6 placeholders (24) + pending_structural (61, by pāda) — agents per pāda, AGENT_RULES.
4. gate_only (76) classify; unexercised (368) via exercise audit rows once the harness is trusted.
5. Samāsa machine + nipātana batch only if days remain.
Deferred by decision: svara tier, Krishnan probe (≤2000 forms, once, niced, at the very end), kośa blind test, gacCat śatṛ row.

## Token rules (quality never traded)
- Start every session: /clear, read only docs/STATE.md. Agents are launched while the main context is small (forks inherit it).
- ≤2 agents at once. Mechanical = fresh sonnet agent with a 5-line prompt (sūtra list, test file name, ledger id range, "read docs/AGENT_RULES.md"); core/judgment = fork.
- Never read agent output files; reports ≤8 lines. Merge with the recipe in COST_PLAN. One status line per batch.
- Focused tests while working; tests/constitutional before each merge; ONE niced full suite at the end of the week's last merge (wall time ≈4.7 h, costs no tokens) and one firing-ledger refresh (it is the same run).
- Strict xfail over fudge; no word-specific recipes; Vidyut/KKH/Scharf data are validators only (guard test tests/constitutional/test_no_external_corpus_in_engine.py).

## Handover triggers (I do this automatically, no reminder needed)
Write docs/STATE.md (≤40 lines: merged, in flight, next 3 actions, ledger id) and ask for /clear when ANY of: a batch has just merged and context is large; weekly usage ≥ 85%; session usage ≥ 80%; an agent failed with API errors; I notice I am re-reading things already known.
Daily target: Sat/Sun 0+1+2, Mon–Tue 3, Wed 4, Thu merge + full suite + STATE.
