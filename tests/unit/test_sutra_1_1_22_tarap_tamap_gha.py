"""
1.1.22 *tarap-tamapau ghaḥ* — *gha* *saṃjñā* for *tarap* / *tamap* taddhita *pratyaya* (ashtadhyayi *i* 11022).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_22 as s1122

_S_11022: str = "तरप्तमपौ घः"


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.22"]
    assert r.sutra_id == "1.1.22"
    assert r.sutra_type is SutraType.SAMJNA
    assert "tarap" in r.text_slp1
    assert r.anuvritti_from == ()


def test_pATha():
    assert s1122._TEXT_DEV == _S_11022
    assert s1122.SUTRA.padaccheda_dev == "तरप्-तमपौ / घः"


def test_gha_set():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t], samjna_registry={})
    s1 = apply_rule("1.1.22", s0)
    assert s1122.gha_samjna_is_registered(s1)
    assert s1122.taddhita_pratyaya_upadesha_slp1_is_gha(s1, "tarap")
    assert s1122.taddhita_pratyaya_upadesha_slp1_is_gha(s1, "tamap")
    assert not s1122.taddhita_pratyaya_upadesha_slp1_is_gha(s1, "tva")
    s2 = apply_rule("1.1.22", s1)
    assert s2.samjna_registry.get(s1122.GHA_KEY) is s1.samjna_registry.get(s1122.GHA_KEY)
