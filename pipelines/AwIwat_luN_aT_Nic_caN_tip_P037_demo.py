"""
pipelines/AwIwat_luN_aT_Nic_caN_tip_P037_demo.py — **आटीटत्** (*āṭīṭat*, *luṅ* 3.sg *para*).

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P037.json``

Target SLP1: **AwIwat** — *aṭ* + *ṇic* + *luṅ* + *caṅ* + *tip*, with *ṣaṭ*-augment
(**6.4.71**) and *dvitva* in the *luṅ*(*i*) frame (**6.1.11**), *abhyāsa* shaping
**7.4.59** → **7.4.93** → **7.4.94** → **7.4.60**, then **6.1.101** contact to
**AwIw** + *caṅ* *a* + *t* merged to *pada* (**_pada_merge**).

**1.1.59** *sthānivat* is pedagogical in the JSON (**n11**); engine does not carry
a standalone *paribhāṣā* step for it.

**Dhātu preservation:** after **1.3.1**, the *upadeśa* tag is removed from the root
``aw`` so halantyam **1.3.9** does not drop the final ``w`` (= ṭ).

**6.1.84** *adhikāra* (JSON *n17*) is not required explicitly for this mechanical
slice because the *ṭiṅ*-residue *a* + *t* is linearly concatenated at *pada*-merge.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_tip_to_t_aprkta, P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _merge_Aw_nic_i(state: State) -> None:
    """Structural | ``Aw`` + ``i`` (ṇic residue) → single *dhātu* ``Awi``."""
    if len(state.terms) < 2:
        return
    stem, nic = state.terms[0], state.terms[1]
    merged = Term(
        kind="prakriti",
        varnas=list(stem.varnas) + list(nic.varnas),
        tags={"dhatu", "anga"},
        meta=dict(stem.meta),
    )
    merged.meta["upadesha_slp1"] = "awi"
    state.terms = [merged] + state.terms[2:]
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "धातु-मेलनम्",
            "form_before": state.flat_slp1(),
            "form_after": state.flat_slp1(),
            "why_dev": "आट् + णिच्-अवशेष → आटि (P037 अन्तरा)।",
            "status": "APPLIED",
        }
    )


def derive_AwIwat_luN_aT_Nic_caN_tip_P037() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("aw")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "aw", "karmakatva": "sakarmaka"},
    )
    dhatu.meta["1_4_22_affix_class"] = "eka"

    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "parasmaipada"

    s = apply_rule("1.1.68", s)
    s = apply_rule("1.3.1", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    s.meta["3_1_26_nic_arm"] = True
    s = apply_rule("3.1.26", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    s.meta["P037_7_2_116_arm"] = True
    s = apply_rule("7.2.116", s)
    _merge_Aw_nic_i(s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s.meta["P037_3_1_48_caN_arm"] = True
    s.meta["3_2_110_luG_arm"] = True
    s = apply_rule("3.2.110", s)
    s = apply_rule("3.1.48", s)
    s = apply_rule("3.4.69", s)

    s = P00_tip_to_t_aprkta(s)

    s = apply_rule("6.4.71", s)
    s = apply_rule("6.1.101", s)

    s.meta["P037_6_4_51_arm"] = True
    s = apply_rule("6.4.51", s)

    s = apply_rule("6.1.1", s)
    s.meta["P037_6_1_11_lugi_arm"] = True
    s = apply_rule("6.1.11", s)
    s.meta["6_1_1_dvitva_arm"] = True
    s = apply_rule("6.1.1", s)
    s = apply_rule("6.1.4", s)

    s.meta["P037_7_4_59_abhyasa_Aw_arm"] = True
    s = apply_rule("7.4.59", s)
    s.meta["P037_7_4_93_sanvat_arm"] = True
    s = apply_rule("7.4.93", s)
    s.meta["P037_7_4_94_dirgha_arm"] = True
    s = apply_rule("7.4.94", s)
    s.meta["P037_7_4_60_Iw_trim_arm"] = True
    s = apply_rule("7.4.60", s)

    s.meta["P037_6_1_101_awIw_cluster_arm"] = True
    s = apply_rule("6.1.101", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    return s


__all__ = ["derive_AwIwat_luN_aT_Nic_caN_tip_P037"]
