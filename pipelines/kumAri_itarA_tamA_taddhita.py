"""
pipelines/kumAri_itarA_tamA_taddhita.py — *kumArI* + *tarap* / *tamap* (atiśayane),
ending in merged taddhita-anta *prātipadika* *kumAritara* / *kumAritama* (full *strī* *subanta* is a separate *corpus* slice).

*Cross-check:* user `kumari.md` (Kāśikā: **6.3.43** *ṅy* + *anekāca* before *taddhita it*-lopa).

**5.3.55** / **5.3.57** append the *taddhita*; **1.1.22** is *gha*; **1.2.46** *prātipadika*;
**6.3.43** *hrasva* on the *I*; ``P00_taddhita_it_lopa_chain``; structural merge; ``subanta``.
CONSTITUTION Art. 7 / 11: *apply_rule* + structural merge only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term

from core.canonical_pipelines import (
    P00_taddhita_it_lopa_chain,
    P00_taddhita_samartha_pragdivyata_adhikaras,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from phonology.varna import parse_slp1_upadesha_sequence


def _build_kumArI_state() -> State:
    t = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("kumArI"),
        tags={"prātipadika", "anga", "strīliṅga"},
        meta={"upadesha_slp1": "kumArI"},
    )
    s = State(terms=[t], meta={"linga": "strīliṅga"}, trace=[])
    return s


def _structural_merge_pratipadika(s: State, *, label: str) -> State:
    from engine.state import Term

    all_v = [v.clone() for t in s.terms for v in t.varnas]
    stem = s.flat_slp1().strip()
    merged = Term(
        kind="prakriti",
        varnas=all_v,
        tags={"prātipadika", "anga", "strīliṅga"},
        meta={"upadesha_slp1": stem},
    )
    b = s.flat_slp1()
    s.terms = [merged]
    a = s.flat_slp1()
    s.trace.append(
        {
            "sutra_id": f"__KUMArI_TADDHITA_MERGE__{label}__",
            "sutra_type": "STRUCTURAL",
            "type_label": "कुमारी-तद्धित-मेलनम्",
            "form_before": b,
            "form_after": a,
            "why_dev": "तद्धित-प्रक्रियायां अङ्ग+प्रत्यय-संयोजनम् (संरचनात्मकं)।",
            "status": "APPLIED",
        }
    )
    return s


def derive_kumAri_taddhita_core(*, arm: str) -> State:
    """
    Taddhita leg only. ``arm`` is ``\"5_3_57_tarab_arm\"`` or ``\"5_3_55_tamap_arm\"``;
    sets **5.3.57** or **5.3.55** and returns after *it* chain + merge.
    """
    if arm not in ("5_3_57_tarab_arm", "5_3_55_tamap_arm"):
        raise ValueError(arm)
    s = _build_kumArI_state()
    s = apply_rule("2.1.1", s)
    s = P00_taddhita_samartha_pragdivyata_adhikaras(s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s.meta[arm] = True
    sid = "5.3.57" if arm == "5_3_57_tarab_arm" else "5.3.55"
    s = apply_rule(sid, s)
    s = apply_rule("1.1.22", s)
    s = apply_rule("1.2.46", s)
    s.meta["6_3_43_NGy_hrasva_arm"] = True
    s = apply_rule("6.3.43", s)
    s = P00_taddhita_it_lopa_chain(s)
    return _structural_merge_pratipadika(s, label=arm)


def derive_kumAritara() -> State:
    """*kumArI* + *tarap* → single merged *prātipadika* surface ``kumAritara`` (taddhita-anta)."""
    return derive_kumAri_taddhita_core(arm="5_3_57_tarab_arm")


def derive_kumAritama() -> State:
    """*kumArI* + *tamap* → ``kumAritama`` (taddhita-anta)."""
    return derive_kumAri_taddhita_core(arm="5_3_55_tamap_arm")


__all__ = [
    "derive_kumAri_taddhita_core",
    "derive_kumAritara",
    "derive_kumAritama",
]
