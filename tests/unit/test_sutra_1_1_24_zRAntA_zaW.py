"""
1.1.24 *ṣṇāntā ṣaṭ* — *ṣaṭ* saṃjñā (under 1.1.23 *saṅkhyā* anuvṛtti), ashtadhyayi *i* 11024.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_24 as s1124
from sutras.adhyaya_1.pada_1 import sutra_1_1_23 as s1123

_S_11024: str = "ष्णान्ता षट्"


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.24"]
    assert r.sutra_id == "1.1.24"
    assert r.sutra_type is SutraType.SAMJNA
    assert r.anuvritti_from == ("1.1.23",)
    assert "zaW" in r.text_slp1


def test_pATha_bytes_match_ashtadhyayi_s():
    assert s1124._TEXT_DEV == _S_11024
    assert s1124.SUTRA.padaccheda_dev == "ष्णान्ता / षट्"


def test_requires_1_1_23_sankhya_bootstrap():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t], samjna_registry={})
    s1 = apply_rule("1.1.24", s0)
    assert not s1124.zat_samjna_is_registered(s1)

    s2 = apply_rule("1.1.23", s0)
    assert s1123.sankhya_samjna_1_1_23_is_registered(s2)
    s3 = apply_rule("1.1.24", s2)
    assert s1124.zat_samjna_is_registered(s3)


def test_zananta_predicate():
    assert s1124.sankhya_pratipadika_is_zananta("zaz")   # षष्
    assert s1124.sankhya_pratipadika_is_zananta("saptan")  # सप्तन्
    assert not s1124.sankhya_pratipadika_is_zananta("rAma")

