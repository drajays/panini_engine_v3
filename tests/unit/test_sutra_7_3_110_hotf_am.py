"""Narrow **7.3.110** on ``hotf`` + ``am`` (``prakriya_21``)."""
import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_43 import TAG as SARV


def test_7_3_110_replaces_final_f_before_sarvanamasthana_am() -> None:
    ang = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("hotf")),
        tags={"anga", "prātipadika", "krt_tfc"},
        meta={"upadesha_slp1": "hotf"},
    )
    am = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("am")),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "am"},
    )
    am.tags.add(SARV)
    s = State(terms=[ang, am], meta={}, trace=[])
    s.meta["prakriya_21_7_3_110_arm"] = True
    s = apply_rule("7.3.110", s)
    assert "".join(v.slp1 for v in s.terms[0].varnas) == "hota"
    assert s.terms[0].meta.get("urN_rapara_pending") == "r"
