"""
1.1.20 *dādhā ghv adāp* — *ghu* *saṃjñā* for *dā*, *dhā*, and *ad*+**āp** *dhātu* *upadeśa*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_20 as s1120

# Ashtadhyayi i=11020 *s* (must match ``_TEXT_DEV`` in ``sutra_1_1_20``).
_S_11020: str = "\u0926\u093e\u0927\u093e \u0918\u094d\u0935\u0926\u093e\u092a\u094d"


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.20"]
    assert r.sutra_id == "1.1.20"
    assert r.sutra_type is SutraType.SAMJNA
    assert "ghv" in r.text_slp1
    assert r.anuvritti_from == ()


def test_pATha_bytes_match_ashtadhyayi_s():
    assert s1120._TEXT_DEV == _S_11020
    assert s1120.SUTRA.padaccheda_dev == "दा-धा / घु / अदाप्"


def test_ghu_set_registration():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t], samjna_registry={})
    s1 = apply_rule("1.1.20", s0)
    assert s1120.ghu_samjna_is_registered(s1)
    assert s1120.dhatu_upadesha_slp1_is_ghu(s1, "da~da")
    assert s1120.dhatu_upadesha_slp1_is_ghu(s1, "da~Da")
    assert s1120.dhatu_upadesha_slp1_is_ghu(s1, "adA~p")
    assert not s1120.dhatu_upadesha_slp1_is_ghu(s1, "qupac~z")
    s2 = apply_rule("1.1.20", s1)
    assert s2.samjna_registry.get(s1120.GHU_KEY) is s1.samjna_registry.get(s1120.GHU_KEY)
