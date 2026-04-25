"""
8.4.1 *raṣābhyāṃ no ṇaḥ samānapade saṃhitāyām* (ashtadhyayi i=84411).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def _with_tripadi(s: State) -> State:
    s = apply_rule("8.2.1", s)
    assert s.tripadi_zone
    return s


def test_sutra_metadata():
    r = SUTRA_REGISTRY["8.4.1"]
    assert r.sutra_id == "8.4.1"
    assert r.sutra_type is SutraType.VIDHI
    assert "समानपदे" in r.text_dev
    assert "8.2.1" in r.anuvritti_from
    assert "8.2.108" in r.anuvritti_from


def test_puz_n_a_ti_adjacent_samAnapade():
    # One *Term*: *puṣ* + *n* (after *z*) in *saṃhitā* (e.g. *puṣṇāti* cluster).
    t = Term(
        kind="dhatu",
        varnas=[mk("p"), mk("u"), mk("z"), mk("n"), mk("A"), mk("t"), mk("i")],
    )
    s0 = _with_tripadi(State(terms=[t]))
    s1 = apply_rule("8.4.1", s0)
    # *R* = ण् in SLP1 (see *phonology.mk*).
    assert s1.terms[0].varnas[3].slp1 == "R"
    assert "R" in s1.flat_slp1()
    assert s1.flat_slp1() == s0.flat_slp1().replace("n", "R", 1)


def test_f_n_rikara_varttika_tisR():
    # *f* = ऋ; *ऋवर्णात् Нस्य णत्वं* in *prakriyā* (one *Term*).
    t = Term(kind="subanta", varnas=[mk("t"), mk("i"), mk("f"), mk("n"), mk("A"), mk("m")])
    s0 = _with_tripadi(State(terms=[t]))
    s1 = apply_rule("8.4.1", s0)
    assert s1.terms[0].varnas[3].slp1 == "R"
    assert "R" in s1.flat_slp1()


def test_agnir_nayati_not_samAnapade_two_terms():
    # *r* is pada-final; *n* is first of next *Term* — 8.4.1 / 8.4.2 do not apply.
    t0 = Term(kind="pada1", varnas=[mk("a"), mk("g"), mk("n"), mk("i"), mk("r")])
    t1 = Term(kind="pada2", varnas=[mk("n"), mk("a"), mk("y"), mk("a"), mk("t"), mk("i")])
    s0 = _with_tripadi(State(terms=[t0, t1]))
    s1a = apply_rule("8.4.1", s0)
    assert s1a.flat_slp1() == s0.flat_slp1()
    s1b = apply_rule("8.4.2", s1a)
    assert s1b.flat_slp1() == s0.flat_slp1()
