"""
pipelines/citaH_prathamA_ciY.py — चितः (*ciñ* + *kta*, prathamā-ekavacana).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/चितः.md``

Target SLP1: **citaH** (चितः).  Scheduling is ``apply_rule`` only (CONSTITUTION
Art. 7 / 11); *Tripāḍī* opens only after *sup* so **4.1.2** is not *asiddha*-blocked.

**1.4.110** (*avasāna*) cannot be invoked after **8.2.1** in this engine: non–8.x
sūtras are *asiddha*-gated once ``tripadi_zone`` is true (``engine/gates.py``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_ciY_dhatu_hal_it_then_bhuvadi,
    P00_ciY_kartari_krt_nistha_adhikara_prefix,
    P00_krt_ardhadhatuka_ekac_it_and_guna_audit,
    P00_lashakvataddhite_it_lopa_chain,
    P00_pratipadika_prathama_sup_after_stem_merge,
    P00_tripadi_rutva_visarga,
)


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ciY"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "ciY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_citaH() -> State:
    s = _build_state()

    s = P00_ciY_dhatu_hal_it_then_bhuvadi(s)

    s = P00_ciY_kartari_krt_nistha_adhikara_prefix(s)
    s.meta["3_2_102_target_upadesha_slp1"] = "ciY"
    s.meta["3_2_102_kta_arm"] = True
    s = apply_rule("3.2.102", s)
    s = P00_lashakvataddhite_it_lopa_chain(s)

    s = P00_krt_ardhadhatuka_ekac_it_and_guna_audit(s)

    s = P00_pratipadika_prathama_sup_after_stem_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


__all__ = ["derive_citaH"]
