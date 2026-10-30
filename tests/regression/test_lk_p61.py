"""P1 — the 6.1 placeholders made real (6.1.76, 91, 95, 105, 122, 123, 128, 132, 138, 140, 141): each on a hand-built tape, 3 positive and 2 negative cases."""
import pytest

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State, Term
from engine.vikalpa import choose
from engine.vivaksha import set_vivaksha
from phonology import mk
from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


def T(slp1, *tags, kind="prakriti", **meta):
    return Term(kind=kind, varnas=[mk(c) for c in slp1], tags=set(tags), meta=dict(meta))


def flat(s):
    return [("".join(v.slp1 for v in t.varnas)) for t in s.terms]


def fires(sid, s):
    return SUTRA_REGISTRY[sid].cond(s)


# --- 6.1.76 padāntād vā ------------------------------------------------------------------------------------
@pytest.mark.parametrize("left,right,want", [("lakzmI", "CAyA", "lakzmIt"), ("kuwI", "CAyA", "kuwIt"), ("kuvalI", "CAyA", "kuvalIt")])
def test_6_1_76_tuk_after_pada_final_dirgha(left, right, want):
    s = State(terms=[T(left, "pada"), T(right)])
    with choose({"6.1.76": True}):
        s1 = apply_rule("6.1.76", s)
    assert flat(s1)[0] == want and flat(s1)[1] == right


def test_6_1_76_is_optional_the_other_reading_leaves_the_tape():
    s = State(terms=[T("lakzmI", "pada"), T("CAyA")])
    s1 = apply_rule("6.1.76", s)           # default: the vā is not taken
    assert flat(s1) == ["lakzmI", "CAyA"]


@pytest.mark.parametrize("left,right,tags", [("daDi", "Catram", {"pada"}), ("lakzmI", "CAyA", set()), ("lakzmI", "rAjA", {"pada"})])
def test_6_1_76_does_not_fire_outside(left, right, tags):
    s = State(terms=[T(left, *tags), T(right)])
    with choose({"6.1.76": True}):
        assert flat(apply_rule("6.1.76", s)) == flat(s)


# --- 6.1.91 upasargād ṛti dhātau ---------------------------------------------------------------------------
@pytest.mark.parametrize("up,dh,want", [("upa", "fcCa", ["up", "ArcCa"]), ("pra", "fcCa", ["pr", "ArcCa"]), ("upa", "fD", ["up", "ArD"])])
def test_6_1_91_vrddhi(up, dh, want):
    s = State(terms=[T(up, "upasarga", kind="upasarga"), T(dh, "dhatu", kind="dhatu")])
    assert flat(apply_rule("6.1.91", s)) == want


@pytest.mark.parametrize("a,b,ta,tb", [("KawvA", "fcCa", set(), {"dhatu"}), ("upa", "FcCa", {"upasarga"}, {"dhatu"}), ("ni", "fcCa", {"upasarga"}, {"dhatu"}), ("upa", "ita", {"upasarga"}, set())])
def test_6_1_91_not_outside(a, b, ta, tb):
    s = State(terms=[T(a, *ta), T(b, *tb)])
    assert flat(apply_rule("6.1.91", s)) == flat(s)


# --- 6.1.95 omāṅoś ca ---------------------------------------------------------------------------------------
@pytest.mark.parametrize("a,want", [("SivAya", "SivAy"), ("kA", "k"), ("yA", "y")])
def test_6_1_95_pararupa_before_om(a, want):
    s = State(terms=[T(a), T("om")])
    s1 = apply_rule("6.1.95", s)
    assert flat(s1) == [want, "om"]


@pytest.mark.parametrize("a,b", [("hari", "om"), ("SivAya", "ehi")])
def test_6_1_95_not_without_avarna_or_om(a, b):
    s = State(terms=[T(a), T(b)])
    assert flat(apply_rule("6.1.95", s)) == flat(s)


# --- 6.1.105 dīrghāj jasi ca ---------------------------------------------------------------------------------
@pytest.mark.parametrize("anga,up,first", [("kumArI", "jas", "j"), ("mAlA", "jas", "j"), ("kumArI", "Ow", "O")])
def test_6_1_105_blocks_purvasavarna(anga, up, first):
    s = State(terms=[T(anga, "anga"), T(first + "s" if first == "j" else first, "sup", kind="pratyaya", upadesha_slp1=up)])
    s1 = apply_rule("6.1.105", s)
    assert "6.1.102" in s1.blocked_sutras


@pytest.mark.parametrize("anga,up,form", [("rAma", "jas", "jas"), ("mAlA", "su~", "s")])
def test_6_1_105_not_for_short_or_other_sup(anga, up, form):
    s = State(terms=[T(anga, "anga"), T(form, "sup", kind="pratyaya", upadesha_slp1=up)])
    s1 = apply_rule("6.1.105", s)
    assert "6.1.102" not in s1.blocked_sutras


# --- 6.1.122 sarvatra vibhāṣā goḥ ----------------------------------------------------------------------------
@pytest.mark.parametrize("right", ["agram", "ajinam", "anIkam"])
def test_6_1_122_prakritibhava_of_go_before_a(right):
    s = State(terms=[T("go", "pada"), T(right)])
    with choose({"6.1.122": True}):
        s1 = apply_rule("6.1.122", s)
    assert PRAGHYA_TERM_TAG in s1.terms[0].tags and flat(s1)[0] == "go"


@pytest.mark.parametrize("left,right,tags", [("citragu", "agram", {"pada"}), ("go", "indra", {"pada"}), ("go", "agram", set())])
def test_6_1_122_not_outside(left, right, tags):
    s = State(terms=[T(left, *tags), T(right)])
    with choose({"6.1.122": True}):
        s1 = apply_rule("6.1.122", s)
    assert PRAGHYA_TERM_TAG not in s1.terms[0].tags


# --- 6.1.123 avaṅ sphoṭāyanasya -------------------------------------------------------------------------------
@pytest.mark.parametrize("right", ["agram", "ajinam", "Odanam"])
def test_6_1_123_avang_before_ac(right):
    s = State(terms=[T("go", "pada"), T(right)])
    with choose({"6.1.123": True}):
        s1 = apply_rule("6.1.123", s)
    assert flat(s1)[0] == "gav"


@pytest.mark.parametrize("left,right,tags", [("citragu", "agram", {"pada"}), ("go", "kzIram", {"pada"}), ("go", "agram", set())])
def test_6_1_123_not_outside(left, right, tags):
    s = State(terms=[T(left, *tags), T(right)])
    with choose({"6.1.123": True}):
        s1 = apply_rule("6.1.123", s)
    assert flat(s1)[0] == left


# --- 6.1.128 ṛty akaḥ ----------------------------------------------------------------------------------------
@pytest.mark.parametrize("left,want", [("brahma", "brahma"), ("KawvA", "Kawva"), ("hotf", "hotf"), ("kumArI", "kumAri")])
def test_6_1_128_prakritibhava_and_hrasva_before_ri(left, want):
    s = State(terms=[T(left, "pada"), T("fSya")])
    with choose({"6.1.128": True}):
        s1 = apply_rule("6.1.128", s)
    assert flat(s1)[0] == want and PRAGHYA_TERM_TAG in s1.terms[0].tags


@pytest.mark.parametrize("left,right,tags", [("KawvA", "indra", {"pada"}), ("brahma", "fSi", set())])
def test_6_1_128_not_outside(left, right, tags):
    s = State(terms=[T(left, *tags), T(right)])
    with choose({"6.1.128": True}):
        s1 = apply_rule("6.1.128", s)
    assert PRAGHYA_TERM_TAG not in s1.terms[0].tags


# --- 6.1.132 etattadoḥ sulopo 'koranañsamāse hali --------------------------------------------------------------
def _su(up="s~"):
    return T("s", "sup", kind="pratyaya", upadesha_slp1=up)


@pytest.mark.parametrize("stem,name,nxt", [("sa", "tad", "dadAti"), ("eza", "etad", "BuNkte"), ("sa", "tad", "SamBuH")])
def test_6_1_132_su_lopa_before_consonant(stem, name, nxt):
    s = State(terms=[T(stem, "anga", upadesha_slp1=name), _su(), T(nxt)])
    s1 = apply_rule("6.1.132", s)
    assert flat(s1) == [stem, "", nxt]


@pytest.mark.parametrize("stem,name,nxt,tags", [("ya", "yad", "dadAti", set()), ("sa", "tad", "atra", set()), ("saka", "saka", "dadAti", set()), ("sa", "tad", "SivaH", {"lex:nanjsamAsa"})])
def test_6_1_132_not_outside(stem, name, nxt, tags):
    s = State(terms=[T(stem, "anga", *tags, upadesha_slp1=name), _su(), T(nxt)])
    assert flat(apply_rule("6.1.132", s)) == flat(s)


# --- 6.1.138 / 140 / 141 suṭ -------------------------------------------------------------------------------------
def _kr(up, dh, sense):
    s = State(terms=[T(up, "upasarga", kind="upasarga", upadesha_slp1=up), T(dh, "dhatu", kind="dhatu", upadesha_slp1=dh)])
    if sense:
        set_vivaksha(s, arthaViSeSa=sense)
    return s


@pytest.mark.parametrize("up", ["sam", "pari", "upa"])
def test_6_1_138_sut_for_samavaya(up):
    s1 = apply_rule("6.1.138", _kr(up, "kf", "samavAya"))
    assert [t.meta.get("upadesha_slp1") for t in s1.terms] == [up, "suT", "kf"]


@pytest.mark.parametrize("up,dh,sense", [("sam", "kf", None), ("pra", "kf", "samavAya"), ("sam", "BU", "samavAya")])
def test_6_1_138_not_outside(up, dh, sense):
    s = _kr(up, dh, sense)
    assert len(apply_rule("6.1.138", s).terms) == 2


@pytest.mark.parametrize("up", ["upa"])
def test_6_1_140_sut_for_lavana(up):
    s1 = apply_rule("6.1.140", _kr(up, "kF", "lavana"))
    assert [t.meta.get("upadesha_slp1") for t in s1.terms][1] == "suT"


@pytest.mark.parametrize("up,dh,sense", [("upa", "kF", None), ("sam", "kF", "lavana"), ("upa", "kf", "lavana")])
def test_6_1_140_not_outside(up, dh, sense):
    s = _kr(up, dh, sense)
    assert len(apply_rule("6.1.140", s).terms) == 2


@pytest.mark.parametrize("up", ["upa", "prati"])
def test_6_1_141_sut_for_himsa(up):
    s1 = apply_rule("6.1.141", _kr(up, "kF", "hiMsA"))
    assert [t.meta.get("upadesha_slp1") for t in s1.terms][1] == "suT"


@pytest.mark.parametrize("up,dh,sense", [("upa", "kF", None), ("sam", "kF", "hiMsA"), ("upa", "kf", "hiMsA")])
def test_6_1_141_not_outside(up, dh, sense):
    s = _kr(up, dh, sense)
    assert len(apply_rule("6.1.141", s).terms) == 2
