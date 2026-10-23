# All-sūtra plan — Laghukaumudī first, then the rest (2026-10-23)

Sits under `SUTRA_COVERAGE_100_PLAN.md` (v3 phases) and `PRAKARANA_MACHINE_PLAN.md`; changes only the **order of work**.
Source of the list: brain `texts` source=`laghukaumudi` = **1,087 sūtras** (`tools/lk_plan.py` → `docs/data/lk_worklist.json`,
regenerated with the engine status). Remaining 2,896 = non-LK (Vedic/svara/rare taddhita/uṇādi-adjacent), done last.

| Phase | Scope (Aṣṭādhyāyī order inside) | LK sūtras not yet done* | Gate |
|---|---|---|---|
| L0 | worklist + status ledger (done) | – | file committed |
| L1 | Adh.1 saṃjñā/paribhāṣā/pada/kāraka-saṃjñā + Adh.2 (samāsa/vibhakti data) | 1: 77 · 2: 64 | each sūtra: failing test from Kāśikā → cond/act → conflicts |
| L2 | Adh.6 placeholders (84 in LK; 573 total): 6.1 dvitva/abhyasta → ac-sandhi → 6.2/6.3 → 6.4 aṅga | 6: 164 | placeholder count ↓, sweeps = baselines |
| L3 | Adh.7 aṅga (iṭ, guṇa/vṛddhi, ādeśa) + Adh.8 tripāḍī | 7: 188 · 8: 110 | Gate C tiṅanta through the loop |
| L4 | Adh.3 sanādi/kṛt/tiṅ (lakāra sweep: other adādi lakāras, 6.4.114) | 3: 122 | Vidyut floor ⊆ fired |
| L5 | Adh.4–5 strī/taddhita (AMENDMENT 25 vivakṣā inputs first) | 4: 111 · 5: 78 | pilot per mechanism, zero engine edits |
| L6 | non-LK 2,896: Vedic/svara (Track G), uṇādi, gaṇa-driven rest | – | completeness invariant |
\*counts = LK sūtras whose status is not confident/confident_structural, from the worklist.

## Order rule
Pāṇini order between prakaraṇas; inside a prakaraṇa finish the **whole group across lakāras/pratyayas** before moving on
(6.1.6 batch showed one sūtra touches 4 spines). Owner rulings are asked in batches at the end of a phase, never mid-sūtra.

## Least-token routine (per batch of ~8–10 sūtras)
1. `make preflight` + `make brain S=` only for sūtras in the batch; read once, no re-reading.
2. State lives in files (`lk_worklist.json`, `handover.md`), not chat. Replies: result + failures only.
3. Focused tests while working; `make full-check` (15 min) once per phase-step, in background.
4. Doubts → `docs/SOURCE_CONFLICTS.md` pending list; asked in one batch.
5. Forks only for independent sūtra groups (no hotspot edits); prompts one paragraph.
