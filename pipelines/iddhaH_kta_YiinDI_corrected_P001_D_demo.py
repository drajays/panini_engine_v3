"""
pipelines/iddhaH_kta_YiinDI_corrected_P001_D_demo.py — **P001-D** इद्धः (*iddhaḥ*).

Source row **P001-D** in ``corrected_prakriyas_v2``: *ñi*+*indh* (*YiinDI~*, Rudhādi)
+ *kta* → *iddhaḥ*.

Spine: ñi-*it* … → *inD* + *kta* → *ta*; **6.4.24** (*n*-lopa); *pada* merge ``iDta``;
**pre–Tripāḍī** **8.2.40** / **8.4.53** (``corrected_v2_P001_D_pre_tripadi_cluster_arm``, same
firewall pattern as **P001-B** / **8.4.41**) so **4.1.2** is not *asiddha*-blocked; **1.2.46**
Case J; prathamā *su* → ``P00_tripadi_rutva_visarga`` (**8.2.1** opens Tripāḍī here).

Keeping ``ta`` as ``t``+``a`` through merge preserves stem-final ``a`` (*cf.* *citaḥ*),
avoiding a wrong visarga-only tail.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + ``_pada_merge`` only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_ciY_kartari_krt_nistha_adhikara_prefix,
    P00_krt_ardhadhatuka_ekac_it_and_guna_audit,
    P00_lashakvataddhite_it_lopa_chain,
    P00_pratipadika_prathama_sup_after_stem_merge,
    P00_tripadi_rutva_visarga,
)
from pipelines.subanta import _pada_merge

_UPADESHA = "YiinDI~"


def derive_iddhaH_kta_YiinDI_corrected_P001_D() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(_UPADESHA)),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": _UPADESHA},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    s.meta["ekac_dhatu"] = True

    for sid in ("1.3.1", "1.3.5", "1.3.2", "1.3.9"):
        s = apply_rule(sid, s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
    s = apply_rule("1.3.1", s)

    s = P00_ciY_kartari_krt_nistha_adhikara_prefix(s)
    s.meta["3_2_102_target_upadesha_slp1"] = _UPADESHA
    s.meta["3_2_102_kta_arm"] = True
    s = apply_rule("3.2.102", s)
    s = P00_lashakvataddhite_it_lopa_chain(s)
    s = P00_krt_ardhadhatuka_ekac_it_and_guna_audit(s)

    s.terms[0].meta["upadesha_slp1"] = "inD"
    s = apply_rule("6.4.24", s)

    _pada_merge(s)
    s.meta["corrected_v2_P001_D_pre_tripadi_cluster_arm"] = True
    s = apply_rule("8.2.40", s)
    s = apply_rule("8.4.53", s)

    stem = s.terms[0]
    stem.kind = "prakriti"
    stem.tags.discard("pada")
    stem.meta["corrected_v2_P001_D_nistha_stem"] = True
    s.meta["corrected_v2_P001_D_1_2_46_arm"] = True
    s = apply_rule("1.2.46", s)

    s.meta["linga"] = "pulliṅga"
    s = P00_pratipadika_prathama_sup_after_stem_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


__all__ = ["derive_iddhaH_kta_YiinDI_corrected_P001_D", "_UPADESHA"]
