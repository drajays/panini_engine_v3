"""
engine/phase.py — Derivation phase model (extended for cond discipline).
────────────────────────────────────────────────────────────────────────────

Forward-only phase chain for autonomous enumeration:

    upadesha  →  pratyaya  →  angakarya  →  sandhi  →  tripadi

Legacy default on ``State`` remains ``angakarya`` so recipe pipelines that
never call ``set_phase`` still restrict scheduler scans to aṅgakārya + later
phases only — not adhyāya 3 kṛt stubs on a bare dhātu tape.
"""
from __future__ import annotations

from engine.state import State


class PhaseError(RuntimeError):
    """Attempt to transition backwards, to an unknown phase, or during
    a derivation step that has already begun."""


_VALID_FORWARD: dict[str, str] = {
    "upadesha"  : "pratyaya",
    "pratyaya"  : "angakarya",
    "angakarya" : "sandhi",
    "sandhi"    : "tripadi",
}

_ALL_PHASES = frozenset(_VALID_FORWARD.keys()) | frozenset({"tripadi"})

# Sūtra id ranges eligible per phase (inclusive lo/hi tuples).
_PHASE_RANGES: dict[str, tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]] = {
    "upadesha": (
        ((1, 1, 1), (1, 1, 100)),
        ((1, 2, 1), (1, 2, 72)),
        ((1, 3, 1), (1, 3, 9)),
        ((1, 4, 1), (1, 4, 17)),
    ),
    "pratyaya": (
        ((2, 4, 1), (2, 4, 85)),
        ((3, 1, 1), (3, 4, 117)),
    ),
    "angakarya": (
        # 6.1.1–6.1.71 (dvitva, samprasāraṇa, ṣatva…) come *before* saṃhitā (6.1.72 संहितायाम्) and, by
        # sūtra kram, before the aṅga rules of 6.4 and 7.x that work on their output (abhyāsa-kārya 7.4.59–7.4.97
        # after the dvitva 6.1.8 of liṭ).
        ((6, 1, 1), (6, 1, 71)),
        ((6, 4, 1), (6, 4, 168)),
        ((7, 1, 1), (7, 4, 97)),
    ),
    "sandhi": (
        ((6, 1, 72), (6, 1, 229)),
        ((6, 2, 1), (6, 2, 199)),
        ((6, 3, 1), (6, 3, 999)),
        ((8, 1, 1), (8, 1, 73)),
    ),
}


# Adhyāya 1 (saṃjñā · paribhāṣā · it · pada) is triggered by *what is on the tape*,
# not by a stage of the derivation: 4.1.2 puts an upadeśa there after the
# "upadesha" phase has closed, and सुप्तिङन्तं पदम् (1.4.14) is needed after the
# affix is lopa'd (ROADMAP C1 finding). Eligible in every phase; cond decides.
_ADHYAYA_ONE: tuple[tuple[int, ...], tuple[int, ...]] = ((1, 1, 1), (1, 4, 110))


def _id_tuple(sid: str) -> tuple[int, ...]:
    return tuple(int(p) for p in sid.split("."))


def sutra_in_phase(sutra_id: str, phase: str) -> bool:
    """Return True iff ``sutra_id`` lies in the ID window for ``phase``."""
    if phase == "tripadi":
        return is_tripadi_sutra(sutra_id)
    t = _id_tuple(sutra_id)
    if _ADHYAYA_ONE[0] <= t <= _ADHYAYA_ONE[1]:
        return True
    for lo, hi in _PHASE_RANGES.get(phase, ()):
        if lo <= t <= hi:
            return True
    return False


def set_phase(state: State, new_phase: str) -> State:
    """
    Transition ``state.phase`` to ``new_phase``, in place.  Returns the
    state for convenience.  Raises PhaseError on invalid transitions.

    Self-transitions (same → same) are no-ops (idempotent).
    """
    if new_phase not in _ALL_PHASES:
        raise PhaseError(
            f"unknown phase {new_phase!r}; must be one of {sorted(_ALL_PHASES)}"
        )

    current = state.phase
    if current == new_phase:
        return state

    expected = _VALID_FORWARD.get(current)
    if expected != new_phase:
        raise PhaseError(
            f"invalid phase transition: {current!r} → {new_phase!r}. "
            f"Only valid forward transition from {current!r} is {expected!r}."
        )

    state.phase = new_phase
    state.tripadi_zone = (new_phase == "tripadi")

    form = state.flat_slp1()
    state.emit_structural(
        "__PHASE__",
        form_before=form,
        form_after=form,
        why_dev=f"अवस्था-परिवर्तनम्: {current} → {new_phase}",
        type_label="पदच्छेद-अवस्था",
        phase_from=current,
        phase_to=new_phase,
    )
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
