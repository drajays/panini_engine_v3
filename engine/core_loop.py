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
