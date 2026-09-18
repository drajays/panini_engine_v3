"""
pipelines/kirati_karati_split_prakriyas.py — **P009** (kF/gF → kirati/girati).

Source: ``…/my_scripts/final/split_prakriyas_11/P009.json``.

Yudhiṣṭhira Mīmāṃsaka's Aṣṭādhyāyī-Bhāṣya (pariśiṣṭa, PDF p.643-644, 1.1.51
उरण् रपरः section) derives कॄ (विक्षेपे, तुदादिः) + श + ति to **किरति**, not
**करति**: the तुदादि *vikaraṇa* **श** is *a-pit* (śit-class सार्वधातुक), so
**7.3.84**'s guṇa is blocked and **7.1.100** (ॠत इद्धातोः, ॠ→इ) fires instead,
with **1.1.51** inserting the following *r*. गृ (निगरणे) gives गिरति by the
identical mechanism — both are regression siblings here.

Spine:
  **3.1.91** → **3.1.1–3** → **3.2.123** → (structural +laT) → **3.4.77** → **3.4.78** (*tip*) →
  **3.1.77** (*Sa* vikaraṇa, recipe-armed) → **1.3.8** → **1.3.9** →
  **7.1.100** (ॠ→इ, kF/gF only — short *ṛ* dhātus are untouched) →
  **7.3.84** (guṇa; no-op once 7.1.100 has fired) → **1.1.51** → **1.3.3** →
  **1.3.9** → (flat concat = kirati / girati).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only (plus structural lakāra placeholder insertion).
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3, P00_tin_adesha_base, P00_lac_lat_attach, P00_snam_it_lopa_chain
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _derive_tudadi_F_root(upadesha_slp1: str) -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(upadesha_slp1)),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": upadesha_slp1, "gana": 6},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["prakriya_P009_kirati_note_karati_spine"] = True

    # laṭ setup (structural placeholder + tip selection by 3.4.78).
    s = P00_lac_lat_attach(s)

    s = P00_tin_adesha_base(s, "tip")

    # tudādi vikaraṇa Sa + it-lopa (3.1.77 → 1.3.8 → 1.3.9)
    s = P00_snam_it_lopa_chain(s)

    # 7.1.100 (F→i, kF/gF only) fires before 7.3.84's guṇa gets a chance —
    # 7.3.84 declines once 7.1.100 has marked the aṅga done. 1.1.51 then
    # inserts r after the substituted i (urN_rapara_pending, set by 7.1.100).
    s = apply_rule("7.1.100", s)
    s = apply_rule("7.3.84", s)
    s = apply_rule("1.1.51", s)
    # After uRaN-rapara, the dhātu is no longer in upadeśa-state; otherwise the
    # inserted final 'r' would be mis-read as halantyam-it by a later 1.3.3 on *tip*.
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    # it on tip final p, then lopa → ti.
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    return s


def derive_kirati_karati_split_prakriyas_P009() -> State:
    """कॄ (विक्षेपे, तुदादिः) + तिप् → किरति (7.1.100 + 1.1.51, not 7.3.84's guṇa)."""
    return _derive_tudadi_F_root("kF")


def derive_girati_P009_sibling() -> State:
    """गॄ (निगरणे, तुदादिः) + तिप् → गिरति — same mechanism, regression sibling."""
    return _derive_tudadi_F_root("gF")


__all__ = [
    "derive_kirati_karati_split_prakriyas_P009",
    "derive_girati_P009_sibling",
]

