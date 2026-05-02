"""
pipelines/avaDIt_luN_han_P026_demo.py — अवधीत् (*han* → *vadh*, luṅ 3.sg para) glass-box.

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P026.json``

Target SLP1: **avaDIt** (अवधीत्).

Spine (engine order; cf. JSON teaching steps **n3–n14**):
  **1.1.68** → **1.3.1** → **3.2.110**/**3.4.69** → **3.1.91** + ``P06a`` →
  **cli/sic** (**3.1.43**/**3.1.44** + *it*) → **2.4.43** (*han* → *vadh*) →
  **6.4.71** (*aṭ*) → *tiṅ* **tip** → **t** → **3.4.114** (*sic* ārdhadhātuka) →
  **7.2.35** (*iṭ*) → **6.4.48** (audit) → **1.1.56** → *vṛddhi* readiness →
  **7.2.7** (first pass COND-false, then *i* → *ī* on *sic*) → *pada* merge →
  **6.4.114** (*s*-loss + *dh* → *ḍ* before *ī*, **before** **8.2.1** so the
  Tripāḍī *asiddha* gate does not block adhyāya **6.**) → **8.2.1**.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_it_halantyam_lopa_yathasankhyam,
    P00_tip_to_t_aprkta,
    P00_vrddhi_prayoga_readiness,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)


def _build_han_luG_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("han"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "han", "karmakatva": "sakarmaka"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "parasmaipada"
    return s


def derive_avaDIt() -> State:
    s = _build_han_luG_state()

    s = apply_rule("1.1.68", s)
    s = apply_rule("1.3.1", s)

    s.meta["3_2_110_luG_arm"] = True
    s = apply_rule("3.2.110", s)
    s = apply_rule("3.4.69", s)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s.meta["3_1_43_cli_luG_arm"] = True
    s = apply_rule("3.1.43", s)
    s = apply_rule("3.1.44", s)
    s = P00_it_halantyam_lopa_yathasankhyam(s)
    # Before **3.4.78**'s *tiṅ* *it*-pass, drop ``upadesha`` on ``sic`` so ``s`` is
    # not re-analysed as *halantyam-it* (same pattern as ``P00_luN_lakara_cli_sic``).
    for t in s.terms:
        if (t.meta.get("upadesha_slp1") or "").strip() == "sic":
            t.tags.discard("upadesha")

    s.meta["2_4_43_han_vadh_luG_arm"] = True
    s = apply_rule("2.4.43", s)
    # Final ``h`` of *vadh* must survive the *tiṅ* *it*-chain (**1.3.3**/**1.3.9**).
    s.terms[0].tags.discard("upadesha")

    s = apply_rule("6.4.71", s)

    s = P00_tip_to_t_aprkta(s)

    s.meta["3_4_114_luN_sic_samjna_arm"] = True
    s = apply_rule("3.4.114", s)

    s.meta["7_2_35_allow_sic"] = True
    s.meta["luN_sic_ardhadhatuka"] = True
    s = apply_rule("7.2.35", s)

    s.meta["6_4_48_P026_trace_arm"] = True
    s = apply_rule("6.4.48", s)

    s = apply_rule("1.1.56", s)

    s = P00_vrddhi_prayoga_readiness(s)
    s = apply_rule("7.2.7", s)
    s.meta["7_2_7_luN_it_vrddhi_arm"] = True
    s = apply_rule("7.2.7", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s.meta["6_4_114_P026_arm"] = True
    s = apply_rule("6.4.114", s)
    s = apply_rule("8.2.1", s)
    return s


__all__ = ["derive_avaDIt"]
