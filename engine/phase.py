"""
engine/phase.py — Three-phase derivation model.
─────────────────────────────────────────────────

CONSTITUTION v3.1 amendment.  The derivation proceeds through three
phases in strict forward order:

    "angakarya"  → Adhyāya 6.4.x / 7.x base modifications (fixed-point)
    "sandhi"     → Adhyāya 6.1.x + 8.1.x sandhi rules (one pass)
    "tripadi"    → Adhyāya 8.2.1–8.4.68 (linear, asiddha to earlier)

Phase transitions are declared by pipelines / recipes via
`set_phase(state, new_phase)`.  Backward transitions raise PhaseError.
The `tripadi_zone` bool on State mirrors `phase == "tripadi"` for
backward compatibility with v3.0 gates.

Rationale: prior to v3.1, the only phase machinery was the bool
`tripadi_zone`, set by 8.2.1.  This worked for "am I past the
tripāḍī barrier?" but gave no vocabulary for "am I in aṅgakārya?"
vs "am I in sandhi?" — which matters once aṅgakārya becomes a
fixed-point sweep (Article 7.3 amendment).
"""
from __future__ import annotations

from engine.state import State


class PhaseError(RuntimeError):
    """Attempt to transition backwards, to an unknown phase, or during
    a derivation step that has already begun."""


_VALID_FORWARD = {
    "angakarya" : "sandhi",
    "sandhi"    : "tripadi",
}

_ALL_PHASES = frozenset({"angakarya", "sandhi", "tripadi"})


def set_phase(state: State, new_phase: str) -> State:
    """
    Transition `state.phase` to `new_phase`, in place.  Returns the
    state for convenience.  Raises PhaseError on invalid transitions.

    Valid transitions:
        angakarya → sandhi
        sandhi    → tripadi

    Self-transitions (same → same) are no-ops (idempotent).
    """
    if new_phase not in _ALL_PHASES:
        raise PhaseError(
            f"unknown phase {new_phase!r}; must be one of {sorted(_ALL_PHASES)}"
        )

    current = state.phase
    if current == new_phase:
        return state  # idempotent

    expected = _VALID_FORWARD.get(current)
    if expected != new_phase:
        raise PhaseError(
            f"invalid phase transition: {current!r} → {new_phase!r}. "
            f"Only valid forward transition from {current!r} is {expected!r}."
        )

    state.phase = new_phase
    # Mirror into tripadi_zone for backward compat with v3.0 gates.
    state.tripadi_zone = (new_phase == "tripadi")

    state.trace.append({
        "sutra_id"    : "__PHASE__",
        "sutra_type"  : "STRUCTURAL",
        "type_label"  : "पदच्छेद-अवस्था",
        "form_before" : state.flat_slp1(),
        "form_after"  : state.flat_slp1(),
        "why_dev"     : f"अवस्था-परिवर्तनम्: {current} → {new_phase}",
        "status"      : "APPLIED",
        "phase_from"  : current,
        "phase_to"    : new_phase,
    })
    return state


def is_tripadi_sutra(sutra_id: str) -> bool:
    """
    Pure numeric test: is this a tripāḍī sūtra (8.2.1 – 8.4.68)?
    Used by the gate to enforce phase-boundary.
    """
    try:
        a, p, n = (int(x) for x in sutra_id.split("."))
    except Exception:
        return False
    return (a == 8 and (p, n) >= (2, 1)) and (a < 8 or (p, n) <= (4, 68))
