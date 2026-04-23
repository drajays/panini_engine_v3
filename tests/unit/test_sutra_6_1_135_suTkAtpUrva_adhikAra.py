"""
6.1.135 *suṭ kāt pūrvaḥ* — *sūṭkātpūrva ityadhikāraḥ*
(ashtadhyayi i=61135; scope to 6.1.154).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["6.1.135"]
    assert r.sutra_id == "6.1.135"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("6.1.135", "6.1.154")
    assert r.text_slp1 == "suT kAt pUrvaH"
    assert r.text_dev == "सुट् कात् पूर्वः"


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("6.1.135", s0)
    assert any(e.get("id") == "6.1.135" for e in s1.adhikara_stack)
    s2 = apply_rule("6.1.135", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("6.1.135") == 1

