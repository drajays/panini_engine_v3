"""
1.4.56 *prāg rīśvarān nipātāḥ* — adhikāra scope opener (ashtadhyayi i=14056).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.4.56"]
    assert r.sutra_id == "1.4.56"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("1.4.56", "1.4.97")
    assert "rISvar" in r.text_slp1
    assert r.text_dev == "प्राग्रीश्वरान्निपाताः"


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("1.4.56", s0)
    assert any(e.get("id") == "1.4.56" for e in s1.adhikara_stack)
    s2 = apply_rule("1.4.56", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("1.4.56") == 1

