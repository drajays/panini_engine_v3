"""
engine/nimitta_predicates.py — Structural signal library.

Re-usable linguistic predicates for sūtra cond() and act() functions.
These replace per-sūtra ad-hoc meta reads (arm flags) with structural
conditions derivable from the tape alone.

CONSTITUTION Art. 2: cond() may read tags, saṃjñā registry, term-local
completion flags, and phonemic structure.  It may NOT read coordinate
annotations (lakāra, puruṣa, vacana) or ad-hoc arm flags.
All predicates here comply with Art. 2.
"""
from __future__ import annotations

from typing import Optional

from engine.state import State, Term
from phonology   import AC, HAL


# ─────────────────────────────────────────────────────────────────────────────
# Phonemic predicates
# ─────────────────────────────────────────────────────────────────────────────

def ends_in_hal(t: Term) -> bool:
    """True when the term's last varṇa is a consonant."""
    return bool(t.varnas) and t.varnas[-1].slp1 in HAL


def ends_in_ac(t: Term) -> bool:
    """True when the term's last varṇa is a vowel."""
    return bool(t.varnas) and t.varnas[-1].slp1 in AC


def begins_with_hal(t: Term) -> bool:
    """True when the term's first varṇa is a consonant."""
    return bool(t.varnas) and t.varnas[0].slp1 in HAL


def begins_with_ac(t: Term) -> bool:
    """True when the term's first varṇa is a vowel."""
    return bool(t.varnas) and t.varnas[0].slp1 in AC


def penultimate_is_a(t: Term) -> bool:
    """True when the second-to-last varṇa is short 'a'."""
    return len(t.varnas) >= 2 and t.varnas[-2].slp1 == "a"


# ─────────────────────────────────────────────────────────────────────────────
# Tag / saṃjñā predicates
# ─────────────────────────────────────────────────────────────────────────────

def is_dhatu(t: Term) -> bool:
    return "dhatu" in t.tags


def is_anga(t: Term) -> bool:
    return "anga" in t.tags


def is_pratyaya(t: Term) -> bool:
    return t.kind == "pratyaya"


def is_ardhadhatuka(t: Term) -> bool:
    return "ardhadhatuka" in t.tags


def is_sarvadhatuka(t: Term) -> bool:
    return "sarvadhatuka" in t.tags


def is_tin_adesha(t: Term) -> bool:
    """True when Term carries the tiṅ-ādeśa tag (set by 3.4.78)."""
    return "tin_adesha_3_4_78" in t.tags


def is_nit(t: Term) -> bool:
    """N-git: carries 'nit' in dhatu_it or it tags."""
    return "nit" in (t.meta.get("dhatu_it") or set()) or "nit" in t.tags


def is_kit(t: Term) -> bool:
    return "kit" in (t.meta.get("dhatu_it") or set()) or "kit" in t.tags


def has_it_agama(v) -> bool:
    """True when varṇa v carries the it_agama tag (iṭ āgama)."""
    return "it_agama" in v.tags


# ─────────────────────────────────────────────────────────────────────────────
# Term-lookup predicates (operate on full state)
# ─────────────────────────────────────────────────────────────────────────────

def dhatu_upadesha(state: State, idx: int) -> Optional[str]:
    """Return upadesha_slp1 of the term at `idx`, or None."""
    if idx < 0 or idx >= len(state.terms):
        return None
    return (state.terms[idx].meta.get("upadesha_slp1") or "").strip() or None


def term_at(state: State, idx: int) -> Optional[Term]:
    """Term at `idx`, or None if out of range."""
    if 0 <= idx < len(state.terms):
        return state.terms[idx]
    return None


def find_term(state: State, *, kind: Optional[str] = None, tag: Optional[str] = None,
              upadesha: Optional[str] = None) -> Optional[Term]:
    """
    Return the first term matching ALL specified criteria, or None.

    kind     : 'prakriti' | 'pratyaya' | ...
    tag      : must be present in t.tags
    upadesha : must equal t.meta['upadesha_slp1']
    """
    for t in state.terms:
        if kind is not None and t.kind != kind:
            continue
        if tag is not None and tag not in t.tags:
            continue
        if upadesha is not None:
            u = (t.meta.get("upadesha_slp1") or "").strip()
            if u != upadesha:
                continue
        return t
    return None


def find_sic_term(state: State) -> Optional[Term]:
    """Return the sic pratyaya term if present."""
    return find_term(state, kind="pratyaya", upadesha="sic")


# ─────────────────────────────────────────────────────────────────────────────
# Structural sequence predicates
# ─────────────────────────────────────────────────────────────────────────────

def is_ardhadhatuka_following(state: State, anga_idx: int) -> bool:
    """True when the term at anga_idx+1 is an ardha-dhātuka pratyaya."""
    nxt = term_at(state, anga_idx + 1)
    return nxt is not None and is_ardhadhatuka(nxt)


def is_sarvadhatuka_following(state: State, anga_idx: int) -> bool:
    """True when the term at anga_idx+1 carries the sārvadhatuka tag."""
    nxt = term_at(state, anga_idx + 1)
    return nxt is not None and is_sarvadhatuka(nxt)


def sic_has_it_agama_i(state: State) -> bool:
    """
    True when a *sic* pratyaya is present, has not yet had iṭ-vṛddhi applied,
    and its first varṇa is 'i' tagged as it_agama.

    Structural replacement for the ``7_2_7_luN_it_vrddhi_arm`` gate.
    """
    pr = find_sic_term(state)
    if pr is None or not pr.varnas:
        return False
    if pr.meta.get("7_2_7_luN_it_vrddhi_done"):
        return False
    v0 = pr.varnas[0]
    return v0.slp1 == "i" and has_it_agama(v0)


def tin_uttama_karmani_present(state: State) -> bool:
    """
    True when a tiṅ-ādeśa pratyaya ends in 'E' (ātmanepada uttama loṭ).

    Structural replacement for the ``3_4_92_loT_karmani_arm`` gate.
    """
    for t in state.terms:
        if not is_tin_adesha(t):
            continue
        if t.meta.get("3_4_92_done"):
            continue
        if t.varnas and t.varnas[-1].slp1 == "E":
            return True
    return False


def tin_uttama_parasmaipada_present(state: State) -> bool:
    """
    True when a tiṅ-ādeśa pratyaya has upadeśa 'ni', 'vas' (→v), or 'mas' (→m).

    Structural replacement for the ``3_4_92_loT_uttama_arm`` gate.
    """
    for t in state.terms:
        if not is_tin_adesha(t):
            continue
        if t.meta.get("3_4_92_done"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "ni":
            return True
        if up == "vas" and t.varnas and t.varnas[0].slp1 == "v":
            return True
        if up == "mas" and t.varnas and t.varnas[0].slp1 == "m":
            return True
    return False


def prakriti_is_pratipadika_not_sanadi(t: Term) -> bool:
    """
    True when a prakriti term carries 'prātipadika' but not 'sanadi'.

    Structural replacement for ``P025_3_1_32_arm`` / ``kath_3_1_32_arm`` gate:
    the dhātu saṃjñā should land on the stem, not on the sanādi term itself.
    """
    return (
        t.kind == "prakriti"
        and "prātipadika" in t.tags
        and "sanadi" not in t.tags
    )


def tin_adesha_present(state: State) -> bool:
    """True when at least one term carries the tiṅ-ādeśa tag from 3.4.78."""
    return any(is_tin_adesha(t) for t in state.terms)


def vikarana_on_tape(state: State, upadesha_slp1: str) -> bool:
    """True when a pratyaya term matches the given vikaraṇa upadeśa."""
    up = upadesha_slp1.strip()
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() == up:
            return True
    return False


def adhikara_and_nimitta(
    state: State,
    adhikara_id: str,
    sutra_id: str,
    site_fn,
) -> bool:
    """
    Composable cond template: adhikāra open AND ``site_fn(state)`` not None.

    ``site_fn`` should be a module-level ``_find_*_site(state) -> Term | None``.
    """
    from engine.gates import adhikara_in_effect

    if not adhikara_in_effect(sutra_id, state, adhikara_id):
        return False
    return site_fn(state) is not None
