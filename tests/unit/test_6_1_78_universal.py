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


def test_97_generic_and_para_rivals():
    from sutras.adhyaya_6.pada_1.sutra_6_1_97 import SUTRA as s97

    def tape(stem, w, up=None, tags=()):
        return State(terms=[Term(kind="prakriti", varnas=P(stem), tags={"anga", *tags}, meta={}),
                            Term(kind="pratyaya", varnas=P(w), tags={"sup"} if up else set(),
                                 meta={"upadesha_slp1": up} if up else {})])
    st = tape("Bava", "anti"); assert s97.cond(st); s97.act(st)
    assert "".join(v.slp1 for t in st.terms for v in t.varnas) == "Bavanti"
    assert not s97.cond(tape("rAma", "as", up="jas"))     # 6.1.102 is para (1.4.2)
    assert not s97.cond(tape("anya", "as", up="jas", tags={"sarvanama"}))  # 7.1.17
    assert not s97.cond(State(terms=[Term(kind="prakriti", varnas=P("te"), tags={"pada"}, meta={}),
                                     Term(kind="prakriti", varnas=P("a"), tags=set(), meta={})]))
    assert not s97.cond(tape("yA", "anti"))               # long ā: tapara (1.1.70)


def test_97_examples_from_the_sutra_commentary():
    from sutras.adhyaya_6.pada_1.sutra_6_1_97 import SUTRA as s97

    def run(stem, nxt, stem_tags=("anga",)):
        st = State(terms=[Term(kind="prakriti", varnas=P(stem), tags=set(stem_tags), meta={}),
                          Term(kind="pratyaya", varnas=P(nxt), tags=set(), meta={})])
        if not s97.cond(st):
            return None
        s97.act(st)
        return "".join(v.slp1 for t in st.terms for v in t.varnas)
    assert run("paWa", "anti") == "paWanti"      # a + a
    assert run("laBa", "e") == "laBe"            # a + e
    assert run("yA", "anti") is None             # ā: tapara
    assert run("apaca", "i") is None             # i is not guṇa (6.1.87 instead)
    assert run("daRqa", "agram", stem_tags=("pada",)) is None   # padānta → 6.1.101
