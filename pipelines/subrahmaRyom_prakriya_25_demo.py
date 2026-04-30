"""
pipelines/subrahmaRyom_prakriya_25_demo.py — ``prakriya_25`` (*subrahmaṇyom*).

Glass-box tail (JSON ``ordered_sutra_sequence``):

  * **6.1.152** — *pratīṣkaśaś ca kaśeḥ* (trace-only ANUVADA for this *prayoga*).
  * **6.1.62** — narrow *pararūpa* junction ``subrahmaRyA`` + ``om`` → ``subrahmaRyom``.

Earlier *taddhita* / *ṭāp* / *savṛddhi* legs are out of band for this *corpus* slice;
the recipe supplies the vocative feminine stem + *om* as lexical *upadeśa*.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + one structural merge.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_subrahmaRyA_om() -> State:
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("subrahmaRyA")),
        tags={"anga", "prātipadika", "strīliṅga"},
        meta={"upadesha_slp1": "subrahmaRyA"},
    )
    om = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("om")),
        tags={"nipāta"},
        meta={"upadesha_slp1": "om"},
    )
    return State(terms=[stem, om], meta={}, trace=[])


def _structural_pada_merge(s: State) -> State:
    """Collapse ``[subrahmaRyo, m]``-style tape to one *pada* (not a sūtra)."""
    b = s.flat_slp1()
    acc: list = []
    for t in s.terms:
        acc.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=acc,
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "subrahmaRyom"},
    )
    s.terms = [merged]
    s.trace.append(
        {
            "sutra_id": "__SUBRAHMArYOM_PADA_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "सुब्रह्मण्योम्-पद-मेलनम्",
            "form_before": b,
            "form_after": s.flat_slp1(),
            "why_dev": "ओम्-पूर्वं एकं पदम् (संरचनात्मकं)।",
            "status": "APPLIED",
        }
    )
    return s


def derive_subrahmaRyom_prakriya_25() -> State:
    s = _mk_subrahmaRyA_om()
    s.meta["prakriya_25_6_1_152_arm"] = True
    s = apply_rule("6.1.152", s)
    s.meta["prakriya_25_6_1_62_pararupa_arm"] = True
    s = apply_rule("6.1.62", s)
    s = _structural_pada_merge(s)
    return s


__all__ = ["derive_subrahmaRyom_prakriya_25", "_mk_subrahmaRyA_om"]
