"""
pipelines/prakftya_lyap_split_prakriyas_P017_demo.py — **P017** (**प्रकृत्य**).

Source: ``…/my_scripts/final/split_prakriyas_11/P017.json``.

Spine (rule-based ``apply_rule`` only):
  - upasarga ``pra`` + dhātu ``kf``
  - **3.4.21** attach ktvā (recipe-armed)
  - **7.1.37** ktvā → lyap (recipe-armed)
  - *it* chain on ``lyap``: **1.3.8** → **1.3.3** → **1.3.9** ⇒ surface ``ya``
  - **6.1.71** insert *tuk* ⇒ ``tya``
  - **1.1.40** marks lyap/ktvā chain as avyaya (uses ancestry ``upadesha_slp1_original``)
  - subanta nom.sg + avyaya sup-luk: **4.1.2** then **2.4.82**

The prefix+dhātu fusion ``pra`` + ``kf`` is represented structurally by a *pada* merge
near the end so ``flat_slp1`` becomes **prakftya**.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _upasarga(s: str) -> Term:
    return Term(
        kind="upasarga",
        varnas=list(parse_slp1_upadesha_sequence(s)),
        tags={"upasarga"},
        meta={"upadesha_slp1": s},
    )


def _dhatu_kf() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kf")),
        tags={"dhatu", "anga", "prātipadika"},
        meta={"upadesha_slp1": "kf"},
    )


def derive_prakftya_lyap_split_prakriyas_P017() -> State:
    s = State(terms=[_upasarga("pra"), _dhatu_kf()], meta={}, trace=[])
    s.meta["prakriya_P017_prakftya_split_prakriyas_11"] = True

    s.meta["3_4_21_ktvA_arm"] = True
    s = apply_rule("3.4.21", s)

    s.meta["7_1_37_lyap_arm"] = True
    s = apply_rule("7.1.37", s)

    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    s = apply_rule("6.1.71", s)

    # Mark the block as avyaya (1.1.40 sees anga+pratyaya ancestry for ktvā/lyap).
    s = apply_rule("1.1.40", s)

    # Merge prefix+dhātu+pratyaya into one pada then attach su and immediately luk it.
    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    # Structural merge does not preserve `avyaya`; carry it forward so 2.4.82 can see it.
    if s.terms:
        s.terms[0].tags.add("avyaya")
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("2.4.82", s)
    return s


__all__ = ["derive_prakftya_lyap_split_prakriyas_P017"]

