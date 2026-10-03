import sutras  # noqa: F401
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence as P
from sutras.adhyaya_8.pada_4.sutra_8_4_40 import SUTRA


def _run(*ws, tripadi=True):
    st = State(terms=[Term(kind="prakriti", varnas=P(w), tags=set(), meta={}) for w in ws])
    st.tripadi_zone = tripadi
    ok = SUTRA.cond(st)
    if ok:
        SUTRA.act(st)
    return ok, "".join(v.slp1 for t in st.terms for v in t.varnas), st


def test_scutva_cases():
    for ws, out in [(("rAmas", "Sete"), "rAmaSSete"), (("rAmas", "cinowi"), "rAmaScinowi"),
                    (("mas", "j"), "maSj"), (("Bavan", "Sete"), "BavaYSete"),
                    (("ut", "C"), "ucC"), (("rAjan", "jalasi"), "rAjaYjalasi"),
                    (("yaj", "na"), "yajYa"), (("yAc", "na"), "yAcYa"), (("suhfd", "ca"), "suhfjca")]:
        ok, flat, st = _run(*ws)
        assert ok and flat == out, (ws, flat)
        assert "८.४.४०" in st.meta["__why_now_dev__"]


def test_sat_cit_after_jashtva_only_and_blocks():
    assert _run("sad", "cit")[1] == "sajcit"          # d+c → j+c (after 8.2.39 made sad)
    assert not _run("praS", "na")[0]                   # 8.4.44 śāt
    assert not _run("rAmas", "Seta", tripadi=False)[0]  # Tripāḍī only
