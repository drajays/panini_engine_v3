import sutras  # noqa: F401
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence as P
from sutras.adhyaya_8.pada_2.sutra_8_2_39 import SUTRA as JASH
from sutras.adhyaya_8.pada_4.sutra_8_4_55 import SUTRA as CAR


def _flat(st):
    return "".join(v.slp1 for t in st.terms for v in t.varnas)


def _pada(w):
    return State(terms=[Term(kind="prakriti", varnas=P(w), tags={"pada"}, meta={})])


def test_jashtva_all_targets():
    for w, out in [("vAk", "vAg"), ("liw", "liq"), ("tat", "tad"), ("triwup", "triwub"),
                   ("zaz", "zaq"), ("Gas", None)]:
        st = _pada(w)
        if out is None:
            assert not JASH.cond(st)      # s → ru is 8.2.66's
            continue
        assert JASH.cond(st)
        JASH.act(st)
        assert _flat(st) == out
        assert "८.२.३९" in st.meta["__why_now_dev__"]
    st = _pada("vAk"); JASH.act(st)
    assert st.samjna_registry.get("8_2_39_k_to_g")
    for w in ("vAc", "ruh", "viS"):       # 8.2.30 / 8.2.31 / 8.2.36 take these
        assert not JASH.cond(_pada(w))


def test_khari_ca_across_terms_and_inside():
    def tape(*ws):
        st = State(terms=[Term(kind="prakriti", varnas=P(w), tags=set(), meta={}) for w in ws])
        st.tripadi_zone = True
        return st
    for ws, out in [(("Bag", "ta"), "Bakta"), (("daT", "ta"), "datta"),
                    (("jaGzatus",), "jakzatus"), (("laB", "sya"), "lapsya"), (("Bid", "ta"), "Bitta")]:
        st = tape(*ws); assert CAR.cond(st); CAR.act(st)
        assert _flat(st) == out
        assert "८.४.५५" in st.meta["__why_now_dev__"]
    assert not CAR.cond(tape("gda"))          # no khar follows
    assert not CAR.cond(tape("vac", "ta"))    # c is 8.2.30's
