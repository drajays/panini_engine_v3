"""
engine/core_loop.py — Autonomous Sapāda-Saptādhyāyī derivation loop.

Drives adhyāyas 1.1–7.4 + 8.1 (the "Sapāda-Saptādhyāyī") autonomously through
phase-scoped scheduler pools, stopping before Tripāḍī (8.2.1+).

The loop:
  1. For each phase in order (upadesha → pratyaya → angakarya → sandhi):
     a. Advance ``state.phase`` if needed.
     b. Repeat: enumerate → resolve → apply until zero candidates.
  2. Return converged state (Tripāḍī not yet applied).

Vibhāṣā rules produce forks (handled by exec_vibhasha via apply_rule).
This module is CONSTITUTIONAL: it contains NO sūtra IDs.
"""
from __future__ import annotations

from engine.phase import set_phase
from engine.scheduler import enumerate_candidates
from engine.resolver  import record_decision, resolve_with_reason
from engine           import apply_rule
from engine.state     import State

MAX_ITERATIONS = 500

# Phases run by the autonomous Sapāda-Saptādhyāyī loop (pre-Tripāḍī).
_SAPADA_PHASES: tuple[str, ...] = (
    "upadesha",
    "pratyaya",
    "angakarya",
    "sandhi",
)


class ConvergenceError(RuntimeError):
    """Raised when the loop exceeds MAX_ITERATIONS without halting."""


def open_adhikaras(state: State) -> None:
    """Hold open the adhikāras of the current phase, each for the scope its own record
    declares (अङ्गस्य governs to the end of Adhyāya 7).

    The loop does this itself; ``ensure_adhikara_for_phase`` (recipe pipelines) still
    stops at 6.4.148 and is left alone until C4.
    """
    import json
    from pathlib import Path

    from engine.registry import SUTRA_REGISTRY

    path = Path(__file__).resolve().parent.parent / "data" / "inputs" / "phase_adhikaras.json"
    for sid in json.loads(path.read_text(encoding="utf-8")).get(state.phase, ()):
        if not any(e.get("id") == sid for e in state.adhikara_stack):
            state.adhikara_stack.append(
                {"id": sid, "scope_end": SUTRA_REGISTRY[sid].adhikara_scope[1]}
            )


def apply_pratishedhas(state: State) -> State:
    """Art. 21 Ladder 1, step 3: prohibitions are settled *before* rules contend.

    Every PRATISHEDHA whose condition holds and that would add something new to
    ``state.blocked_sutras`` is applied; the scheduler then never offers what they
    forbid (6.1.104 नादिचि removes 6.1.102 for ā+ic, so वृद्धि wins by being alone).
    """
    from engine.dispatcher import apply_rule as dispatch
    from engine.registry import SUTRA_REGISTRY
    from engine.scheduler import probe, tape_fingerprint
    from engine.sutra_type import SutraType

    for sid, rec in sorted(SUTRA_REGISTRY.items(), key=lambda kv: tuple(map(int, kv[0].split(".")))):
        if rec.sutra_type is not SutraType.PRATISHEDHA or rec.cond is None:
            continue
        try:
            if not rec.cond(state):
                continue
            trial = probe(sid, state)
        except Exception:
            continue
        if tape_fingerprint(trial) != tape_fingerprint(state):
            state = dispatch(sid, state)
    return state


def advance_phase(state: State) -> bool:
    """Close the current stratum and open the next (Art. 3). False at the last one.

    Entering Tripāḍī is the one place the tape is re-cut: the terms become a single
    pada (structural book-keeping, traced as ``__MERGE__``, not a sūtra).
    """
    from engine.phase import _VALID_FORWARD

    nxt = _VALID_FORWARD.get(state.phase)
    if nxt is None:
        return False
    if nxt == "tripadi":
        from engine.phases.pada_merger import pada_merge

        pada_merge(state)
    set_phase(state, nxt)
    return True


def _advance_to_phase(state: State, target: str) -> None:
    """Walk forward until ``state.phase == target``."""
    from engine.phase import _VALID_FORWARD

    while state.phase != target:
        nxt = _VALID_FORWARD.get(state.phase)
        if nxt is None:
            break
        set_phase(state, nxt)


def _run_phase_until_converged(state: State, *, iteration_budget: list[int]) -> State:
    """Inner loop: fire all applicable sūtras in the current ``state.phase``."""
    while True:
        open_adhikaras(state)
        state = apply_pratishedhas(state)
        candidates = enumerate_candidates(state)
        if not candidates:
            break
        iteration_budget[0] += 1
        if iteration_budget[0] > MAX_ITERATIONS:
            form = state.flat_slp1()
            raise ConvergenceError(
                f"run_sapadasaptadhyayi: no convergence after {MAX_ITERATIONS} "
                f"iterations on form {form!r} (phase={state.phase!r})"
            )
        decision = resolve_with_reason(candidates, state)
        record_decision(state, decision)
        state = apply_rule(decision.winner, state)
    return state


def run_sapadasaptadhyayi(state: State) -> State:
    """
    Run the autonomous loop until convergence across all pre-Tripāḍī phases.

    Convergence = zero eligible sūtras in each phase pool on the current state.

    Returns the post-convergence state (Tripāḍī not yet applied).
    """
    iteration_budget = [0]
    start_idx = 0
    if state.phase in _SAPADA_PHASES:
        start_idx = _SAPADA_PHASES.index(state.phase)

    for target in _SAPADA_PHASES[start_idx:]:
        _advance_to_phase(state, target)
        state = _run_phase_until_converged(state, iteration_budget=iteration_budget)

    return state


def derive_autonomous_tinanta(
    upadesha_slp1: str,
    lakara: str,
    prayoga: str,
    purusha: int = 3,
    vacana: int = 1,
    *,
    upasargas: list[str] | None = None,
    pada: str | None = None,
    san_recipe: bool = False,
    nic_recipe: bool = False,
) -> State:
    """
    Autonomous tinanta derivation entry.

    Phase 5 M5: standard kartari/karmani/bhave paths use the same bootstrap +
    dispatch spine as ``pipelines.tinanta.derive()`` (shared recipe layer).
    Adādi and upasarga-special laṭ spines are included when ``upasargas`` /
    dhātu-class routing matches ``derive()``.  Unknown prayoga classes still
    fall back to ``run_sapadasaptadhyayi``.
    """
    from pipelines.tinanta import (
        _bootstrap_tinanta_derivation,
        _dhatu_row_by_upadesha,
        _dispatch_tinanta_spine,
    )

    if prayoga not in ("kartari", "karmani", "bhave"):
        from engine.tape_init.tinanta import build_tinanta_initial_state

        state = build_tinanta_initial_state(upadesha_slp1, lakara, prayoga)
        return run_sapadasaptadhyayi(state)

    row = _dhatu_row_by_upadesha(upadesha_slp1)
    state, gana, pada_key, complete = _bootstrap_tinanta_derivation(
        row,
        lakara,
        prayoga,
        upasargas=upasargas,
        pada=pada,
        san_recipe=san_recipe,
        nic_recipe=nic_recipe,
        purusha=purusha,
        vacana=vacana,
    )
    if complete:
        return state
    assert pada_key is not None
    return _dispatch_tinanta_spine(
        state,
        gana=gana,
        lakara=lakara,
        prayoga=prayoga,
        pada_key=pada_key,
        purusha=purusha,
        vacana=vacana,
    )
