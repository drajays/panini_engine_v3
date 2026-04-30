"""
pipelines/yUpadAru_vfkaBhaya_prakriya_39_demo.py — ``prakriya_39`` (यूपदारु / वृकभयम्).

Source: ``…/separated_prakriyas/prakriya_39_2026-04-29_14_21_36.json``.

JSON ``ordered_sutra_sequence`` lists **2.4.7** only (step **15** OCR fragment ``2|4|7``).
That conflicts with the scholarly ``panini_engine_pipeline``, which correctly cites **2.4.71**
(*सुपो धातुप्रातिपदिकयोः*) for internal ``sup`` *luk* — **2.4.7** is *विशिष्टलिङ्गो नदी…*, unrelated.
This recipe follows **2.4.71** and documents the JSON ambiguity.

Spine (glass-box):
  • **यूपदारु**: **2.1.3** → **2.1.36** → **1.2.46** → **2.4.71** → **1.2.43** → **2.2.30** → **1.2.46**
    (merge) → **4.1.2** → **7.1.23**.
  • **वृकभयम्**: **2.1.3** → **2.1.37** → **1.2.46** → **2.4.71** → **1.2.43** → **2.2.30** → **1.2.46**
    → **4.1.2** → **7.1.24** → **6.1.107**.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _prakriti_member(stem: str, *, demo_tag: str) -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(stem)),
        tags={"anga", "prātipadika", "samasa_member", demo_tag},
        meta={"upadesha_slp1": stem},
    )


def _sup(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": up},
    )


def derive_yUpadAru_prakriya_39() -> State:
    yUpa = _prakriti_member("yUpa", demo_tag="prakriya_39_yUpadAru_demo")
    ne = _sup("Ne")
    dAru = _prakriti_member("dAru", demo_tag="prakriya_39_yUpadAru_demo")
    su_mem = _sup("s~")
    s = State(terms=[yUpa, ne, dAru, su_mem], meta={}, trace=[])

    s = apply_rule("2.1.3", s)
    s.meta["prakriya_39_catvarTI_compound_vidhi_note"] = True
    s.meta["prakriya_39_2_1_36_arm"] = True
    s = apply_rule("2.1.36", s)

    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    s.meta["prakriya_39_tatpurusa_upasarjana"] = True
    for t in s.terms:
        if t.kind == "prakriti" and (t.meta.get("upadesha_slp1") or "") == "yUpa":
            t.tags.add("prakriya_39_upasarjana_purva")

    s = apply_rule("1.2.43", s)
    s = apply_rule("2.2.30", s)
    s.samjna_registry.pop("1.2.46_generic_pratipadika", None)
    s = apply_rule("1.2.46", s)

    s.terms[0].tags.add("napuṃsaka")
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("7.1.23", s)
    return s


def derive_vfkaBhayam_prakriya_39() -> State:
    vfka = _prakriti_member("vfka", demo_tag="prakriya_39_vfkaBhaya_demo")
    Byas = _sup("Byas")
    bhaya = _prakriti_member("bhaya", demo_tag="prakriya_39_vfkaBhaya_demo")
    su_mem = _sup("s~")
    s = State(terms=[vfka, Byas, bhaya, su_mem], meta={}, trace=[])

    s = apply_rule("2.1.3", s)
    s.meta["prakriya_39_paYcamI_compound_vidhi_note"] = True
    s.meta["prakriya_39_2_1_37_arm"] = True
    s = apply_rule("2.1.37", s)

    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    s.meta["prakriya_39_tatpurusa_upasarjana"] = True
    for t in s.terms:
        if t.kind == "prakriti" and (t.meta.get("upadesha_slp1") or "") == "vfka":
            t.tags.add("prakriya_39_upasarjana_purva")

    s = apply_rule("1.2.43", s)
    s = apply_rule("2.2.30", s)
    s.samjna_registry.pop("1.2.46_generic_pratipadika", None)
    s = apply_rule("1.2.46", s)

    s.terms[0].tags.add("napuṃsaka")
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("7.1.24", s)
    s = apply_rule("6.1.107", s)
    return s


__all__ = ["derive_yUpadAru_prakriya_39", "derive_vfkaBhayam_prakriya_39"]
