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


def test_109_and_94():
    from sutras.adhyaya_6.pada_1 import sutra_6_1_109 as s109, sutra_6_1_94 as s94
    st = State(terms=[Term(kind="prakriti", varnas=P("te"), tags={"pada"}, meta={}),
                      Term(kind="prakriti", varnas=P("atra"), tags=set(), meta={})])
    assert not SUTRA.cond(st) and s109.SUTRA.cond(st)
    s109.SUTRA.act(st)
    assert "".join(v.slp1 for t in st.terms for v in t.varnas) == "tetra"
    st = State(terms=[Term(kind="upasarga", varnas=P("pra"), tags={"upasarga"}, meta={}),
                      Term(kind="prakriti", varnas=P("ejate"), tags={"dhatu"}, meta={})])
    s94.SUTRA.act(st)
    assert "".join(v.slp1 for t in st.terms for v in t.varnas) == "prejate"


def test_127_vibhasha_both_readings():
    import sutras  # noqa: F401
    from engine import apply_rule
    from engine.vikalpa import choose

    def run(opt):
        st = State(terms=[Term(kind="prakriti", varnas=P("maDu"), tags={"pada"}, meta={}),
                          Term(kind="prakriti", varnas=P("atra"), tags=set(), meta={})])
        with choose({"6.1.127": opt}):
            for r in ("6.1.127", "6.1.77"):
                st = apply_rule(r, st)
        return "".join(v.slp1 for t in st.terms for v in t.varnas)
    assert run(True) == "maDuatra" and run(False) == "maDvatra"


def test_89_vs_94():
    from sutras.adhyaya_6.pada_1 import sutra_6_1_89 as s89, sutra_6_1_94 as s94

    def tape(root, w):
        return State(terms=[Term(kind="upasarga", varnas=P("upa"), tags={"upasarga"}, meta={}),
                            Term(kind="prakriti", varnas=P(w), tags={"dhatu"}, meta={"upadesha_slp1": root})])
    st = tape("iR", "eti")
    assert s89.SUTRA.cond(st) and not s94.SUTRA.cond(st)
    s89.SUTRA.act(st)
    assert "".join(v.slp1 for t in st.terms for v in t.varnas) == "upEti"
    assert s94.SUTRA.cond(tape("ejf~", "ejate")) and not s89.SUTRA.cond(tape("ejf~", "ejate"))


def test_97_generic_and_sup_guard():
    from sutras.adhyaya_6.pada_1.sutra_6_1_97 import SUTRA as s97
    def tape(w, sup=False):
        return State(terms=[Term(kind="prakriti", varnas=P("Bava"), tags={"anga"}, meta={}),
                            Term(kind="pratyaya", varnas=P(w), tags={"sup"} if sup else set(), meta={})])
    st = tape("anti"); assert s97.cond(st); s97.act(st)
    assert "".join(v.slp1 for t in st.terms for v in t.varnas) == "Bavanti"
    assert not s97.cond(tape("as", sup=True))  # para sup-ādeśa / 6.1.102 rule the sup junction
    pn = State(terms=[Term(kind="prakriti", varnas=P("te"), tags={"pada"}, meta={}),
                      Term(kind="prakriti", varnas=P("a"), tags=set(), meta={})])
    assert not s97.cond(pn)
