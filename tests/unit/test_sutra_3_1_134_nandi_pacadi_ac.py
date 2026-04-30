"""Narrow **3.1.134** (*ac* after *nandī-grahi-pacādi*) for ``prakriya_20``."""
import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def test_3_1_134_appends_ac_after_divi() -> None:
    d = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("divi~")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "divi~"},
    )
    s = State(terms=[d], meta={}, trace=[])
    s.meta["prakriya_20_nandi_pacadi"] = True
    s.meta["prakriya_20_3_1_134_arm"] = True
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.1.134", s)
    assert len(s.terms) == 2
    assert (s.terms[1].meta.get("upadesha_slp1") or "").strip() == "ac"
    assert s.terms[1].meta.get("dit_pratyaya") is True
    assert s.terms[1].meta.get("citi_krt_ac") is True
