"""
pipelines/yuvatiH_stri_split_prakriyas_P006_demo.py — **P006** (**युवतिः**).

Source: ``…/my_scripts/final/split_prakriyas_11/P006.json``.

Spine (rule-based ``apply_rule`` only):
  **4.1.1** → **4.1.3** → **4.1.77** (attach *tip*) → **1.3.3** → **1.3.9** →
  **6.4.134** (narrow armed n-lopa for *yuvan*→*yuva*) → **1.2.46** →
  **4.1.2** (su) → structural *pada* merge → **8.2.1** → **8.2.66** → **8.3.15**.

Note: JSON cites **6.4.134** for *yuvan*→*yuva*; the engine's default 6.4.134
implements the *bha* upadhā-a-lopa slice (rājan-type).  For this demo we arm a
strictly-narrow alternate branch via ``state.meta['6_4_134_an_final_n_lopa_arm']``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_subanta_prathama_su_tripadi_visarga
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_yuvan_P006() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("yuvan")),
        tags={"anga", "prātipadika", "prakriya_P006_yuvatiH_demo"},
        meta={"upadesha_slp1": "yuvan"},
    )


def derive_yuvatiH_stri_split_prakriyas_P006() -> State:
    stem = _witness_yuvan_P006()
    stem.tags.add("strīliṅga")

    s = State(terms=[stem], meta={}, trace=[])
    s.meta["prakriya_P006_yuvatiH_split_prakriyas_11"] = True

    s = apply_rule("4.1.1", s)
    s = apply_rule("4.1.3", s)
    s = apply_rule("4.1.77", s)

    # it on tip (p) → lopa
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    # yuvan + ti → yuva + ti (n-lopa) — narrow arm
    s.meta["6_4_134_an_final_n_lopa_arm"] = True
    s = apply_rule("6.4.134", s)
    s.meta.pop("6_4_134_an_final_n_lopa_arm", None)

    s = apply_rule("1.2.46", s)

    s.meta["vibhakti_vacana"] = "1-1"
    s = P00_subanta_prathama_su_tripadi_visarga(s)
    return s


__all__ = ["derive_yuvatiH_stri_split_prakriyas_P006"]

