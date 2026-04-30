"""
pipelines/puras_avyaya_prakriya_19_demo.py — ``prakriya_19`` **Part A** (*puras*).

From the JSON ``panini_engine_pipeline`` (corrected narrative): ``pUrva`` + ``Ni``
+ ``asi`` → **5.3.39** (*pūrvādhara-varāṇām asi …*) ``pur`` + ``asi`` → **1.2.46**
(``META_TADDHITA_AVAYAVA``) → **2.4.71** internal ``Ni`` *luk* → ``asi`` → ``as``
(structural *uccāraṇārtha-ikāra* stand-in; full *taddhita-it* grid for ``asi``
is not yet in the Varṇa *it* scanner) → **1.1.38** + ``su`` + **2.4.82** →
``_pada_merge`` + Tripāḍī tail (**8.2.1**, **8.2.66**, **8.3.15**) → ``puraH``
(SLP1; *puraḥ* / pausal visarga, same class as ``tataH``).

**3.1.1–3.1.3** (*ādyudātta* *adhikāra*) is applied for alignment with the
scholarly step list; **3.1.3** does not alter surface in this slice.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import P00_taddhita_it_lopa_chain
from sutras.adhyaya_1.pada_1.sutra_1_1_38 import META_ASARVA_VIBHAKTI_TADDHITA
from sutras.adhyaya_1.pada_2.sutra_1_2_46 import META_TADDHITA_AVAYAVA

from pipelines.subanta import _pada_merge


def _mk_pUrva() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pUrva")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "pUrva"},
    )


def _mk_Ni_sup() -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Ni")),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "Ni"},
    )


def _mk_asi_taddhita() -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("asi")),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={
            "upadesha_slp1": "asi",
            META_ASARVA_VIBHAKTI_TADDHITA: True,
        },
    )


def _mk_su() -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("s~")),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "s~"},
    )


def _structural_asi_to_as(s: State) -> State:
    """
    *asi* → *as* after **1.3.3–1.3.9** on this frame leaves ``asi`` unchanged
    (no *it* on final *i* in the current scanner).  The śāstrīya outcome for this
    *prayoga* is *pur* + *as* → *puras*; we record a structural step (not a sūtra).
    """
    fb = s.flat_slp1()
    for t in s.terms:
        if (t.meta.get("upadesha_slp1") or "").strip() != "asi":
            continue
        if "taddhita" not in t.tags:
            continue
        t.varnas = list(parse_slp1_upadesha_sequence("as"))
        t.meta["upadesha_slp1"] = "as"
        break
    s.trace.append({
        "sutra_id"    : "__PRAKRIYA_19_ASI_TO_AS__",
        "sutra_type"  : "STRUCTURAL",
        "type_label"  : "उच्चारणार्थ-इकार-लोपः",
        "form_before" : fb,
        "form_after"  : s.flat_slp1(),
        "why_dev"     : "असि-प्रत्ययस्यान्त्य-इकारस्य लोपः → अस् (संरचनात्मकं)।",
        "status"      : "APPLIED",
    })
    return s


def derive_puras_avyaya_prakriya_19() -> State:
    s = State(terms=[_mk_pUrva(), _mk_Ni_sup(), _mk_asi_taddhita()])
    s.meta["prakriya_19_puras"] = True

    s = apply_rule("3.1.1", s)
    s = apply_rule("3.1.2", s)
    s = apply_rule("3.1.3", s)

    s.meta["prakriya_19_puras_5_3_39_arm"] = True
    s = apply_rule("5.3.39", s)

    s.meta[META_TADDHITA_AVAYAVA] = True
    s = apply_rule("1.2.46", s)
    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    s = P00_taddhita_it_lopa_chain(s)
    s = _structural_asi_to_as(s)

    s = apply_rule("1.1.38", s)
    s.terms.append(_mk_su())
    s = apply_rule("2.4.82", s)

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


__all__ = ["derive_puras_avyaya_prakriya_19"]
