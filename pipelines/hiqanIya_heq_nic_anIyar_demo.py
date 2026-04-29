"""
pipelines/hiqanIya_heq_nic_anIyar_demo.py — हिडनीय (hiqanIya) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/हिडनीय.md`

Target SLP1: **hiqanIya** (हिडनीय)
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _merge_heq_nic_to_hiqi(s: State) -> State:
    """Structural: ``heq`` + ṇic ``i`` → ``hiqi`` (single dhātu tape)."""
    if len(s.terms) < 2:
        return s
    dh, nic = s.terms[0], s.terms[1]
    if "nic" not in nic.tags:
        return s
    before = s.flat_slp1()
    dh.varnas = [v.clone() for v in dh.varnas] + [v.clone() for v in nic.varnas]
    dh.meta["upadesha_slp1"] = "hiqi"
    dh.meta["6_4_51_nic_tail_i"] = True
    dh.tags.add("sanadi")
    s.terms.pop(1)
    s.trace.append(
        {
            "sutra_id": "__HEQ_NIC_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "णिच्-धातु-मेलनम्",
            "form_before": before,
            "form_after": s.flat_slp1(),
            "why_dev": "हेड्+णिच् → हिडि (संरचनात्मकं, न सूत्रम्)।",
            "status": "APPLIED",
        }
    )
    return s


def derive_hiqanIya() -> State:
    # Post–it-lopa धातु हेड् → ``heq`` (मित्-गण; note).
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("heq")),
        tags={"dhatu", "anga", "upadesha", "mit"},
        meta={"upadesha_slp1": "heq"},
    )
    s = State(terms=[stem], meta={}, trace=[])

    s.meta["3_1_26_nic_arm"] = True
    s = apply_rule("3.1.26", s)
    s.meta.pop("3_1_26_nic_arm", None)

    s = apply_rule("6.4.92", s)

    s = _merge_heq_nic_to_hiqi(s)

    s = apply_rule("6.4.1", s)
    s = apply_rule("3.1.32", s)

    s.meta["3_1_96_anIyar_arm"] = True
    s = apply_rule("3.1.96", s)

    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    if s.terms:
        s.terms[-1].meta["krtya_anIya_pratyaya"] = True

    s = apply_rule("6.4.51", s)
    s = apply_rule("7.3.86", s)
    return s


__all__ = ["derive_hiqanIya"]
