import sutras  # noqa: F401
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence as P
from sutras.adhyaya_6.pada_1.sutra_6_1_78 import SUTRA


def _run(*parts):
    st = State(terms=[Term(kind="prakriti", varnas=P(p), tags=set(), meta={}) for p in parts])
    assert SUTRA.cond(st)
    SUTRA.act(st)
    return "".join(v.slp1 for t in st.terms for v in t.varnas), st


def test_intra_term():
    assert _run("nea")[0] == "naya"


def test_cross_term_without_anga_tag():  # external sandhi: no aṅga/vikaraṇa gate
    f, st = _run("hare", "eti")
    assert f == "harayeti" and "६.१.७८" in st.meta["__why_now_dev__"]
