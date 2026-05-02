"""
pipelines/dyukAmA_bahuvrihi_paribhasha_P023_demo.py — P023 (द्युकामा)

Goal: derive ``dyukAmA`` (“heaven-desiring”, bahuvrīhi; feminine).

This is a *samāsa + paribhāṣā illustration* driven by the JSON spine.
We do NOT attempt full samāsa generation rules; instead, we:
  - assert samāsa prātipadika readiness via 1.2.46 and 2.2.14 (recipe-armed),
  - perform a structural merge (recorded in trace) to represent compound formation,
  - then follow the cited phonology / strī / sup tail.

Spine (key steps):
  1.1.68, 1.2.46, 2.2.14,
  6.1.127 (div→di+u), 1.1.56, 6.1.66 (attempt; expected skip), 6.1.77 (di+u→dyu),
  1.2.45,
  4.1.1, 4.1.3, 4.1.4 (ṭāp), 6.1.101 (a+A→A),
  4.1.2 (su), 1.3.2, 1.3.9, 1.2.41 (apṛkta), 6.1.68 (su-lopa).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _compound_merge_dyu_kAma(state: State) -> None:
    """Structural: merge first 3 Terms (dy + u + kAma) into one prakṛti stem."""
    if len(state.terms) < 3:
        return
    lefts = state.terms[:3]
    rest = state.terms[3:]
    all_varnas = []
    for t in lefts:
        all_varnas.extend(t.varnas)
    stem = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"anga", "upasarjana"},  # bahuvrīhi output treated as a stem
        meta={"upadesha_slp1": "dyukAma", "vyutpanna": True},
    )
    state.terms = [stem, *rest]
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "समास-मेलनम्",
            "form_before": state.flat_slp1(),
            "form_after": state.flat_slp1(),
            "why_dev": "समास-रचना — dyu + kAma इति संयुक्त-प्रातिपदिक-रूपेण संरचनात्मक-मेलनम्।",
            "status": "APPLIED",
        }
    )


def derive_dyukAmA_bahuvrihi_P023() -> State:
    div = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("div")),
        tags={"anga"},
        meta={"upadesha_slp1": "div", "vyutpanna": True},
    )
    kAma = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kAma")),
        tags={"anga"},
        meta={"upadesha_slp1": "kAma", "vyutpanna": True},
    )
    # Start with two members; sup comes later after strī.
    s = State(terms=[div, kAma], meta={}, trace=[], samjna_registry={})

    s = apply_rule("1.1.68", s)
    s = apply_rule("1.2.46", s)
    s.meta["P023_2_2_14_bahuvrihi_arm"] = True
    s = apply_rule("2.2.14", s)

    # div → di + u (P023-armed 6.1.127), then yaṇ across Terms.
    s.meta["P023_6_1_127_div_v_to_u_arm"] = True
    s = apply_rule("6.1.127", s)

    # Paribhāṣā note: sthānivadbhāva gate (for the demo).
    s = apply_rule("1.1.56", s)
    # JSON cites 6.1.66 as a blocked attempt; in v3 this call is a no-op for this state.
    s = apply_rule("6.1.66", s)

    # di + u → dy + u (iko yaṇ aci) across Terms (armed general path).
    s.meta["6_1_77_ik_yan_aci_general_arm"] = True
    s = apply_rule("6.1.77", s)
    s.meta.pop("6_1_77_ik_yan_aci_general_arm", None)

    # Structural: represent compound stem dyu + kAma.
    _compound_merge_dyu_kAma(s)

    # Prātipadika saṃjñā for avyutpanna is blocked by vyutpanna/pratyaya presence;
    # we call 1.2.45 here to align with JSON note (it may skip).
    s = apply_rule("1.2.45", s)
    # Ensure prātipadika+strī tags for ṭāp.
    s.terms[0].tags.add("prātipadika")
    s.terms[0].tags.add("strīliṅga")

    # Strī adhikāra + ṭāp.
    s = apply_rule("4.1.1", s)
    s = apply_rule("4.1.3", s)
    s = apply_rule("4.1.4", s)
    s = apply_rule("6.1.101", s)

    # Structural: fold the ṭāp residue Term into the stem so sup sits immediately
    # after the aṅga for 1.2.41 / 6.1.68.
    if len(s.terms) >= 2 and "stri_wAp" in s.terms[1].tags:
        # 6.1.101 has already created the long-A in the stem; the residue Term is structural noise now.
        s.terms.pop(1)
        s.trace.append(
            {
                "sutra_id": "__MERGE__",
                "sutra_type": "STRUCTURAL",
                "type_label": "टाप्-अवशेष-लोपः",
                "form_before": s.flat_slp1(),
                "form_after": s.flat_slp1(),
                "why_dev": "टाप्-प्रत्ययस्य अवशेषः संरचनात्मकतया अपसार्यते (आदेश-दीर्घः ६.१.१०१ इत्यनेन सिद्धः)।",
                "status": "APPLIED",
            }
        )

    # Attach prathamā-ekavacana and drop it via 6.1.68 (ṭāp-anta path).
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.2.41", s)
    s.meta["P023_6_1_68_tApanta_arm"] = True
    s = apply_rule("6.1.68", s)

    s = apply_rule("1.1.68", s)
    return s


__all__ = ["derive_dyukAmA_bahuvrihi_P023"]

