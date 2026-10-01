"""
4.1.92 *tasya apatyam* — artha-nirdeśa whose svarita forward force is the
apatya adhikāra, 4.1.92–4.1.178 (SOURCE_CONFLICTS SC-001 ruling).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["4.1.92"]
    assert r.sutra_id == "4.1.92"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("4.1.92", "4.1.178")
    assert r.text_slp1 == 'tasyApatyam'
    assert r.text_dev == 'तस्यापत्यम्'


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("4.1.92", s0)
    assert any(e.get("id") == "4.1.92" for e in s1.adhikara_stack)
    s2 = apply_rule("4.1.92", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("4.1.92") == 1


def test_frame_closes_after_apatya_section():
    from engine.gates import adhikara_in_effect
    s = apply_rule("4.1.92", State(terms=[Term(kind="prakriti", varnas=[mk("a")])]))
    assert adhikara_in_effect("4.1.178", s, "4.1.92")
    assert not adhikara_in_effect("4.2.1", s, "4.1.92")


def test_artha_nirdesha_reaches_purva_affixes():
    from engine.gates import adhikara_in_effect
    r = SUTRA_REGISTRY["4.1.92"]
    assert (r.artha_nirdesha.artha, r.artha_nirdesha.purva_from) == ("apatya", "4.1.83")
    s = apply_rule("4.1.92", State(terms=[Term(kind="prakriti", varnas=[mk("a")])]))
    assert adhikara_in_effect("4.1.83", s, "4.1.92")      # पूर्वैः — aṇ
    assert adhikara_in_effect("4.1.95", s, "4.1.92")      # उत्तरैः — iñ
    assert not adhikara_in_effect("4.1.82", s, "4.1.92")
    assert next(e for e in s.adhikara_stack if e["id"] == "4.1.92")["artha"] == "apatya"
