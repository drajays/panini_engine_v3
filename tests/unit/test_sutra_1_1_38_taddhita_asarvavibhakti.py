from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_38 import META_ASARVA_VIBHAKTI_TADDHITA


def test_1_1_38_tags_avyaya_on_asarva_vibhakti_taddhita() -> None:
    anga = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("tad")),
        tags={"anga", "prātipadika", "tyadadi"},
        meta={"upadesha_slp1": "tad"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("tas")),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "tas", META_ASARVA_VIBHAKTI_TADDHITA: True},
    )
    s0 = State(terms=[anga, pr], meta={}, trace=[])
    s1 = apply_rule("1.1.38", s0)
    assert "avyaya" in s1.terms[0].tags
    assert "avyaya" in s1.terms[1].tags


def test_2_4_82_luks_su_after_1_1_38() -> None:
    anga = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("tad")),
        tags={"anga", "prātipadika", "tyadadi"},
        meta={"upadesha_slp1": "tad"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("tas")),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "tas", META_ASARVA_VIBHAKTI_TADDHITA: True},
    )
    su = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("s~")),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "s~"},
    )
    s0 = State(terms=[anga, pr, su], meta={}, trace=[])
    s1 = apply_rule("1.1.38", s0)
    s2 = apply_rule("2.4.82", s1)
    assert s2.terms[-1].varnas == []
    assert "luk_lopa" in s2.terms[-1].tags

