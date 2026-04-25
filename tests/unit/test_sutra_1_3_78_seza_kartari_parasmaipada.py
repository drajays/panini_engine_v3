"""
1.3.78 *śeṣāt kartari parasmaipadam* — default *parasmaipada* in *kartari* for the *śeṣa* *dhātu* set.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk

from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import (
    ATMANE_LICENSE_META_KEY,
    GATE_KEY,
    kartari_parasmaipada_seza_active,
)


def _dhatu_paT(**meta) -> Term:
    return Term(
        kind="prakriti",
        varnas=[mk("p"), mk("a"), mk("T")],
        tags={"dhatu"},
        meta={"karmakatva": "sakarmaka", **meta},
    )


def test_sutra_metadata() -> None:
    r = SUTRA_REGISTRY["1.3.78"]
    assert r.sutra_id == "1.3.78"
    assert r.sutra_type is SutraType.PARIBHASHA
    assert "1.3.14" in r.anuvritti_from


def test_default_parasmaipada_when_no_atmane_license() -> None:
    s0 = State(terms=[_dhatu_paT()], meta={})
    s1 = apply_rule("1.3.78", s0)
    assert s1.paribhasha_gates[GATE_KEY]["active"] is True
    assert kartari_parasmaipada_seza_active(s1) is True


def test_no_parasmaipada_default_when_atmane_licensed() -> None:
    s0 = State(terms=[_dhatu_paT(**{ATMANE_LICENSE_META_KEY: True})], meta={})
    s1 = apply_rule("1.3.78", s0)
    assert s1.paribhasha_gates[GATE_KEY]["active"] is False
    assert kartari_parasmaipada_seza_active(s1) is False


def test_second_apply_skipped_r3_safe() -> None:
    s0 = State(terms=[_dhatu_paT()], meta={})
    s1 = apply_rule("1.3.78", s0)
    s2 = apply_rule("1.3.78", s1)
    assert s2.paribhasha_gates[GATE_KEY]["active"] is True


def test_no_dhatu_skips() -> None:
    t = Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.3.78", s0)
    assert GATE_KEY not in s1.paribhasha_gates
