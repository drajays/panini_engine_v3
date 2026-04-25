"""
1.4.108 *śeṣe prathamaḥ* — *ŚEṢA* *paribhāṣā* for *1.4.101* row *A* (*prathamapuruṣa* *tiṅ*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk

from sutras.adhyaya_1.pada_4.seza_prathama_1_4_108 import (
    GATE_KEY,
    MADHYAMOTTAMA_105_107_BLOCK_META_KEY,
    seza_108_licences_prathama_tin,
)


def _dhatu(**meta) -> Term:
    return Term(
        kind="prakriti",
        varnas=[mk("p"), mk("a"), mk("T")],
        tags={"dhatu"},
        meta={"karmakatva": "sakarmaka", **meta},
    )


def test_sutra_metadata() -> None:
    r = SUTRA_REGISTRY["1.4.108"]
    assert r.sutra_id == "1.4.108"
    assert r.sutra_type is SutraType.PARIBHASHA
    assert "1.4.101" in r.anuvritti_from
    assert "1.4.105" in r.anuvritti_from
    assert "1.4.1" in r.anuvritti_from


def test_prathama_tin_default_śeṣa() -> None:
    s0 = State(terms=[_dhatu()], meta={})
    s1 = apply_rule("1.4.108", s0)
    assert s1.paribhasha_gates[GATE_KEY]["active"] is True
    assert seza_108_licences_prathama_tin(s1) is True


def test_out_when_105_107_block() -> None:
    s0 = State(terms=[_dhatu(**{MADHYAMOTTAMA_105_107_BLOCK_META_KEY: True})], meta={})
    s1 = apply_rule("1.4.108", s0)
    assert s1.paribhasha_gates[GATE_KEY]["active"] is False
    assert seza_108_licences_prathama_tin(s1) is False


def test_second_apply_r3() -> None:
    s0 = State(terms=[_dhatu()], meta={})
    s1 = apply_rule("1.4.108", s0)
    s2 = apply_rule("1.4.108", s1)
    assert s1.paribhasha_gates == s2.paribhasha_gates


def test_no_dhatu_skips() -> None:
    t = Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.4.108", s0)
    assert GATE_KEY not in s1.paribhasha_gates
