"""
pipelines/jiRNu_prathamA_ji.py — जिष्णुः (*ji* + *gsnuC*, prathamā-ekavacana).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/जिष्णु.md``

Target SLP1: **jizRuH** (जिष्णुः).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_krt_ardhadhatuka_ekac_it_and_guna_audit,
    P00_lashakvataddhite_it_lopa_chain,
    P00_pratipadika_prathama_sup_after_stem_merge,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ji"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "ji"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_jizRuH() -> State:
    s = _build_state()

    s = apply_rule("1.3.1", s)
    s = apply_rule("3.2.134", s)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s.meta["3_2_139_gsnu_arm"] = True
    s = apply_rule("3.2.139", s)
    s = P00_lashakvataddhite_it_lopa_chain(s)

    s = P00_krt_ardhadhatuka_ekac_it_and_guna_audit(s)

    # Stem *jisnu* only (no Tripāḍī yet — **4.1.2** is blocked once ``8.2.1`` opens).
    s = P00_pratipadika_prathama_sup_after_stem_merge(s)
    # Tripāḍī on *jisnu*+*su*: **8.3.59** / **8.4.1** on the stem cluster, then *ru*/*visarga*.
    s = apply_rule("8.2.1", s)
    for sid in ("8.3.59", "8.4.1", "8.2.66", "8.3.15"):
        s = apply_rule(sid, s)
    return s


__all__ = ["derive_jizRuH"]
