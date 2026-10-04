"""8.4.41 ष्टुना ष्टुः — flat cross-Term scan, 8.4.43 / 8.4.42 exemptions, trace."""
import sutras  # noqa: F401
from engine import apply_rule
from engine.state import State, Term
from phonology import mk


def _run(*words, pada=True):
    terms = []
    for w in words:
        t = Term(kind="prakriti", varnas=[mk(c) for c in w], tags={"pada"} if pada else set())
        terms.append(t)
    s = State(terms=terms)
    s.tripadi_zone = True
    return apply_rule("8.4.41", s)


def test_cross_word_s_to_z():
    assert _run("rAmas", "wIkate").flat_slp1() == "rAmaz" + "wIkate"


def test_s_before_z_and_pizwa():
    assert _run("rAmas", "zazWaH").flat_slp1() == "rAmazzazWaH"
    assert _run("pizta").flat_slp1() == "pizwa"


def test_8_4_43_tu_before_z_stays():
    assert _run("sanzazWaH").flat_slp1() == "sanzazWaH"


def test_8_4_42_padanta_ttavarga_blocks():
    assert _run("Iq", "te").flat_slp1() == "Iqte"          # separate padas: blocked
    assert _run("Iqte", pada=False).flat_slp1() == "Iqwe"   # apadānta: applies


def test_trace_set():
    assert any(x.get("why_now_dev") for x in _run("rAmas", "wIkate").trace)
