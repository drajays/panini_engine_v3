"""
pipelines/gomAn_prathamA_go_matup.py — गोमान् (*go* + *jas* + *matup*, prathamā-ekavacana).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/गोमान्.md``

Target SLP1: **gomAn** (अलौकिक *go* + *jas* + *matup* → *gomat* … *gomān*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_matup_it_lopa_chain,
    P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi,
    P00_ugit_pratipadika_prathama_sup_tail,
)
from sutras.adhyaya_1.pada_2.sutra_1_2_46 import META_TADDHITA_AVAYAVA


def _structural_merge_gomat(s: State) -> State:
    """Merge ``[go, mat]`` surface into one *prātipadika* ``Term``."""
    all_varnas = []
    for t in s.terms:
        all_varnas.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"prātipadika", "anga", "pulliṅga"},
        meta={"upadesha_slp1": "gomat"},
    )
    before = s.flat_slp1()
    s.terms = [merged]
    after = s.flat_slp1()
    s.trace.append({
        "sutra_id": "__GOMAN_MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "गोमत्-मेलनम्",
        "form_before": before,
        "form_after": after,
        "why_dev": "अङ्ग+मतुप्-शेषयोः संयोजनम् (संरचनात्मकं, न सूत्रम्)।",
        "status": "APPLIED",
    })
    return s


def derive_gomAn() -> State:
    go = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("go"),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "go"},
    )
    go.tags.add("pulliṅga")
    jas = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("jas"),
        tags={"sup", "pratyaya", "upadesha"},
        meta={"upadesha_slp1": "jas"},
    )
    s = State(terms=[go, jas], meta={"linga": "pulliṅga"}, trace=[])

    s.meta["5_2_94_matup_arm"] = True
    s = apply_rule("5.2.94", s)

    # Prevent **1.2.46** *samāsa* merge of ``[go, jas, matup]`` (same opt-in as *itika*+*phak*).
    s.meta[META_TADDHITA_AVAYAVA] = True
    s.meta["prakriya_matup_asti"] = True
    s = P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi(s)
    s.meta.pop(META_TADDHITA_AVAYAVA, None)

    s = P00_matup_it_lopa_chain(s)

    for t in s.terms:
        if "upadesha" in t.tags:
            t.tags.discard("upadesha")

    s = _structural_merge_gomat(s)

    return P00_ugit_pratipadika_prathama_sup_tail(s)


__all__ = ["derive_gomAn"]
