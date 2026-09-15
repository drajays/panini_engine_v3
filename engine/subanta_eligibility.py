"""
engine/subanta_eligibility.py — Shared subanta / kāraka / accent gate eligibility.

Replaces adhyāya 1.2 / 1.4 / 2.3 / 2.4 paribhāṣā-stub ``cond()`` patterns that
fire whenever a gate flag is unset, regardless of derivation class.

CONSTITUTION Art. 2 / 13: reads structural tags and ``derivation_class`` meta
(set at tape init by pipelines — not vibhakti / lakāra coordinates).
"""
from __future__ import annotations

from engine.state import State


def _derivation_class(state: State) -> str:
    return (state.meta.get("derivation_class") or "").strip()


def _has_pratipadika(state: State) -> bool:
    return any("prātipadika" in t.tags for t in state.terms)


def _has_dhatu(state: State) -> bool:
    return any("dhatu" in t.tags for t in state.terms)


def _subanta_scope_active(state: State) -> bool:
    dc = _derivation_class(state)
    if dc in {"subanta", "sarvanama", "samasa", "taddhita", "krdanta"}:
        return True
    if _has_pratipadika(state):
        return True
    if any("sup" in t.tags for t in state.terms):
        return True
    if any("samasa_member" in t.tags for t in state.terms):
        return True
    if any("sarvanama" in t.tags or "pronoun" in t.tags for t in state.terms):
        return True
    return False


def _samasa_scope_active(state: State) -> bool:
    if any("samasa_member" in t.tags for t in state.terms):
        return True
    if _derivation_class(state) == "samasa":
        return True
    if state.meta.get("samasa_frame"):
        return True
    return False


_LAKARA_VALUES = frozenset({
    "laT", "liT", "luT", "lRT", "loT", "liG", "luG", "lRG", "laG", "lRN", "AsIrliG",
})


def _tinanta_spine_active(state: State) -> bool:
    if _derivation_class(state) == "tinanta":
        return True
    # Recipe pipelines that set meta["lakara"] without derivation_class (split_prakriyas, etc.)
    if state.meta.get("lakara") in _LAKARA_VALUES:
        return True
    return any(
        tag.endswith("_derivation") for t in state.terms for tag in t.tags
    )


def _gate_open(state: State, gate_key: str) -> bool:
    return state.paribhasha_gates.get(gate_key) is not True


def karaka_gate_eligible(state: State, gate_key: str) -> bool:
    """2.3.x kāraka-vibhakti paribhāṣā gates — nominal context only."""
    if not _gate_open(state, gate_key):
        return False
    dc = _derivation_class(state)
    if dc == "tinanta":
        return False
    if _has_dhatu(state) and not _has_pratipadika(state):
        return False
    return _subanta_scope_active(state)


def samasa_lakara_gate_eligible(state: State, gate_key: str) -> bool:
    """2.4.1–2.4.9 samāsa / lakāra paribhāṣā gates."""
    if not _gate_open(state, gate_key):
        return False
    if _samasa_scope_active(state):
        return True
    return _subanta_scope_active(state) and len(state.terms) >= 2


def accent_paribhasha_gate_eligible(state: State, gate_key: str) -> bool:
    """1.2.x accent / ekasheṣa paribhāṣā gates."""
    if not _gate_open(state, gate_key):
        return False
    if state.meta.get("chandas"):
        return True
    return _subanta_scope_active(state)


def yajna_accent_gate_eligible(state: State, gate_key: str) -> bool:
    """1.2.34 yajña-karma accent — Vedic / yajña context only."""
    if not _gate_open(state, gate_key):
        return False
    return bool(state.meta.get("yajna_karma") or state.meta.get("chandas"))


def chandasi_gate_eligible(state: State, gate_key: str) -> bool:
    """1.4.x chandas / Vedic provision gates."""
    if not _gate_open(state, gate_key):
        return False
    if state.meta.get("chandas"):
        return True
    return _subanta_scope_active(state) and state.meta.get("vedic_provision")


def nominal_paribhasha_gate_eligible(state: State, gate_key: str) -> bool:
    """1.4.x general nominal paribhāṣā gates (karmaprayoga, etc.)."""
    if not _gate_open(state, gate_key):
        return False
    return _subanta_scope_active(state)


def sarvanama_paribhasha_gate_eligible(state: State, gate_key: str) -> bool:
    """1.4.105–107 sarvanāma / puruṣa paribhāṣā gates."""
    if not _gate_open(state, gate_key):
        return False
    if any(
        "sarvanama" in t.tags
        or "pronoun" in t.tags
        or (t.meta.get("upadesha_slp1") or "").strip() in {"asmad", "yuzmad", "tad"}
        for t in state.terms
    ):
        return True
    return _subanta_scope_active(state)


def tinanta_lakara_placeholder_eligible(
    state: State,
    upadesha_slp1: str,
) -> bool:
    """
    3.2.x lakāra-placeholder insertion — active tinanta spine only.

    ``upadesha_slp1`` is the lakāra upadeśa (e.g. ``laG``, ``laT``).
    """
    if not _tinanta_spine_active(state):
        return False
    if not _has_dhatu(state):
        return False
    _LAKARA_UPADESHA = {
        "laT": "lat_derivation",
        "liT": "lit_derivation",
        "luT": "lut_derivation",
        "lRT": "lrt_derivation",
        "loT": "lot_derivation",
        "liG": "lig_derivation",
        "luG": "lug_derivation",
        "lRG": "lrg_derivation",
        "laG": "lag_derivation",
        "lRN": "lrn_derivation",
    }
    want = _LAKARA_UPADESHA.get(upadesha_slp1.strip())
    if want and any(want in t.tags for t in state.terms):
        return True
    meta_lak = (state.meta.get("lakara") or "").strip()
    if meta_lak and meta_lak == upadesha_slp1.strip():
        return True
    return False
