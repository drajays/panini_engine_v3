"""
engine/krt_eligibility.py — Shared kṛt/pratyaya insertion eligibility gate.

Replaces hundreds of adhyāya-3 stub ``cond()`` implementations that fire on
``any("dhatu" in t.tags)`` regardless of derivation class.

CONSTITUTION Art. 2 / 13: reads structural tags and ``derivation_class`` meta
(set at tape init by pipelines — not lakāra coordinates).
"""
from __future__ import annotations

from engine.gates import adhikara_in_effect
from engine.nimitta_predicates import tin_adesha_present, vikarana_on_tape
from engine.state import State
from engine.subanta_eligibility import _tinanta_spine_active

_LAKARA_UPADESHA = frozenset({
    "laT", "liT", "luT", "lRT", "loT", "liG", "luG", "lRG", "laG", "lRN",
})


def _has_dhatu(state: State) -> bool:
    return any("dhatu" in t.tags for t in state.terms)


def _krdanta_scope_active(state: State) -> bool:
    """True when this derivation is building a kṛdanta / needs kṛt affix rules."""
    if any("krdanta_pending" in t.tags for t in state.terms):
        return True
    dc = (state.meta.get("derivation_class") or "").strip()
    if dc in {"krdanta", "taddhita"}:
        return True
    if state.phase == "pratyaya" and dc == "krdanta":
        return True
    return False


def _tinanta_blocks_krt(state: State) -> bool:
    """Tiṅanta spine must not enumerate bare kṛt-insertion stubs."""
    dc = (state.meta.get("derivation_class") or "").strip()
    if dc == "tinanta" and not _krdanta_scope_active(state):
        return True
    # Bare dhātu probe (no derivation_class): deny kṛt stubs.
    if not dc and not _krdanta_scope_active(state):
        return True
    return False


def krt_insertion_eligible(
    state: State,
    sutra_id: str,
    *,
    gate_key: str | None = None,
    adhikara_id: str | None = None,
) -> bool:
    if _tinanta_blocks_krt(state):
        return False
    if gate_key and state.paribhasha_gates.get(gate_key) is True:
        return False
    if adhikara_id and not adhikara_in_effect(sutra_id, state, adhikara_id):
        return False
    return _has_dhatu(state)


def _tin_pratyaya_chain_started(state: State) -> bool:
    """
    True when tiṅ pratyaya machinery is on the tape — not bare dhātu + tags only.

    Paribhāṣā-stub sūtras in 3.4.x register background gates; they must not fire
    on tape-init probes that have ``derivation_class=tinanta`` but no lakāra
    placeholder, vikaraṇa, or resolved tiṅ ādeśa yet.
    """
    if tin_adesha_present(state):
        return True
    if state.meta.get("tin_adesha_pending"):
        return True
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _LAKARA_UPADESHA:
            return True
        if "lakAra_pratyaya_placeholder" in t.tags:
            return True
        if "vikarana" in t.tags:
            return True
    if vikarana_on_tape(state, "Sap") or vikarana_on_tape(state, "Syan"):
        return True
    return False


def tin_pratyaya_gate_eligible(
    state: State,
    sutra_id: str,
    *,
    gate_key: str | None = None,
) -> bool:
    """
    Eligibility for 3.4.x tiṅ-vidhāna paribhāṣā-stub sūtras.

    Denies bare-dhātu probes, kṛdanta-only contexts, and tinanta tape-init
    states before lakāra / vikaraṇa / tiṅ ādeśa appear on the tape.
    """
    if not _tinanta_spine_active(state):
        return False
    if gate_key and state.paribhasha_gates.get(gate_key) is True:
        return False
    if not _has_dhatu(state):
        return False
    return _tin_pratyaya_chain_started(state)


def samhita_gate_eligible(
    state: State,
    sutra_id: str,
    *,
    gate_key: str | None = None,
    min_terms: int = 2,
) -> bool:
    """
    Eligibility for 6.x saṃhitā / sandhi paribhāṣā-stub sūtras.

    Requires ≥``min_terms`` on the tape (junction context).
    """
    if len(state.terms) < min_terms:
        return False
    if gate_key and state.paribhasha_gates.get(gate_key) is True:
        return False
    return any("anga" in t.tags or t.varnas for t in state.terms)


def tripadi_gate_eligible(
    state: State,
    sutra_id: str,
    *,
    gate_key: str | None = None,
) -> bool:
    """Eligibility for 8.2+ Tripāḍī VIDHI stubs — only inside Tripāḍī zone."""
    if not state.tripadi_zone and state.phase != "tripadi":
        return False
    if gate_key and state.paribhasha_gates.get(gate_key) is True:
        return False
    return bool(state.terms)


def gate_key_for_sutra(sutra_id: str, suffix: str = "1") -> str:
    """Default paribhāṣā gate key pattern used by adhyāya-3 stub sūtras."""
    parts = sutra_id.split(".")
    body = "_".join(parts)
    return f"{body}_{suffix}"
