import sutras  # noqa: F401
from engine import apply_rule
from engine.state import State, Term
from engine.vikalpa import choose
from phonology.varna import parse_slp1_upadesha_sequence as P


def _run(*ws, tripadi=True, tags=("pada",), opt=True):
    st = State(terms=[Term(kind="prakriti", varnas=P(w), tags=set(tags), meta={}) for w in ws])
    st.tripadi_zone = tripadi
    with choose({"8.4.45": opt}):
        st = apply_rule("8.4.45", st)
    return "".join(v.slp1 for t in st.terms for v in t.varnas), st


def test_nasal_pakza_all_vargas():
    for ws, out in [(("vAg", "muKam"), "vANmuKam"), (("maruj", "Yakar"), "maruYYakar"),
                    (("zaq", "muKa"), "zaRmuKa"), (("suhfd", "mama"), "suhfnmama"),
                    (("triztub", "namati"), "triztumnamati")]:
        flat, st = _run(*ws)
        assert flat == out, (ws, flat)
        assert any("८.४.४५" in x.get("why_now_dev", "") for x in st.trace)


def test_lakara_gets_anunasika_tag():
    _, st = _run("cal", "namati")
    assert "anunasika" in st.terms[0].varnas[-1].tags


def test_default_and_blocks():
    assert _run("vAg", "muKam", opt=False)[0] == "vAgmuKam"       # other pakṣa
    assert _run("vAg", "muKam", tripadi=False)[0] == "vAgmuKam"   # Tripāḍī only
    assert _run("marut", "mat", tags=("pada", "bha"))[0] == "marutmat"   # bha, not pada
    assert _run("vid", "mi", tags=())[0] == "vidmi"               # apadānta
    assert _run("vAg", "gacCati")[0] == "vAggacCati"              # no nasal follows
