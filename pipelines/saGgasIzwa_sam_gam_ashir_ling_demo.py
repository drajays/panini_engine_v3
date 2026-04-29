"""
pipelines/saGgasIzwa_sam_gam_ashir_ling_demo.py — संगसीष्ट (*saGgasIzwa*) demo.

Source: ``separated_prakriyas/prakriya_13_2026-04-29_14_08_40.json``

Target SLP1: **saGgasIzwa**

OCR in the JSON lists **1|3|26**; that number conflates neighbouring sūtras. The
deterministic spine for this *prayoga* follows ``samo gamyṛcchibhyām`` → **1.3.29**
(ātmanepada with ``sam`` + ``gam``), **1.2.13** (optional *kit* on ``sīyuṭ`` after
``gam``), **6.4.37** (anusvāra-elision on ``gam`` before *jhal* + *kṅiti* **3.4.102**
block), plus **8.3.23**/**8.4.58** interacting with **suṭ**/tripāḍī.

Narrow spine:
  ``sam`` (upasarga) + ``gam`` dhātu → **1.3.29**
  āśīr-liṅ: **3.3.173** → **3.4.77**/**3.4.78**(``ta``) → **3.4.102** → **1.2.13** →
  **6.4.37** → **3.4.107** → *pada* merge → **8.2.1**
  **8.3.23** → **8.3.59** (twice) → **8.4.58** → **8.4.41**
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_saGgasIzwa() -> State:
    sam = Term(
        kind="upasarga",
        varnas=parse_slp1_upadesha_sequence("sam"),
        tags={"upasarga"},
        meta={},
    )
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("gam"),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "gam"},
    )
    s = State(terms=[sam, dhatu], meta={}, trace=[])

    s.meta["1_3_29_samo_gamyricchiblAm_arm"] = True
    s = apply_rule("1.3.29", s)

    s.meta["3_3_173_ashishi_ling_arm"] = True
    s = apply_rule("3.3.173", s)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)

    s.meta["3_4_102_sIyuw_arm"] = True
    s = apply_rule("3.4.102", s)
    s.meta["1_2_13_va_gam_kit_arm"] = True
    s = apply_rule("1.2.13", s)
    s.meta["6_4_37_gam_anunasika_arm"] = True
    s = apply_rule("6.4.37", s)
    s.meta["3_4_107_suw_arm"] = True
    s = apply_rule("3.4.107", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s.meta["8_3_23_m_o_anuswara_arm"] = True
    s = apply_rule("8.3.23", s)
    s = apply_rule("8.3.59", s)
    s = apply_rule("8.3.59", s)
    s = apply_rule("8.4.58", s)
    s = apply_rule("8.4.41", s)
    return s


__all__ = ["derive_saGgasIzwa"]
