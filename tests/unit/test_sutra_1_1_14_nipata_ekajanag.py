"""
1.1.14 (निपात एकाजनाङ् / *ss* एकाच् अनाङ् निपातः प्रगृह्यम्) — *pragṅhya* for *ekāc* *anāṅ* *nipāta*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_14 as s1114


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.14"]
    assert r.sutra_id == "1.1.14"
    assert r.sutra_type is SutraType.SAMJNA
    assert r.anuvritti_from == ("1.1.11",)
    # CONSTITUTION Art. 4: *anuvṛtti*-*sahita* pāṭha (ashtadhyayi ``ss``) is canonical in ``SUTRA`` .
    assert r.text_dev == s1114.ANUVRITTI_SAHITA_DEV
    assert r.text_slp1 == "ekAc anA~G nipAtaH pragfhyam"
    # Index *s* (short) vs *ss* (baked) — both exposed on the sūtra module.
    assert s1114.SANKSIPTA_PATHA_DEV == "निपात एकाजनाङ्"
    assert "निपातः" in r.padaccheda_dev
    assert "एकाच्" in r.padaccheda_dev
    assert "अनाङ्" in r.padaccheda_dev
    assert "१.१.११" in r.padaccheda_dev or "1.1.11" in r.padaccheda_dev
    assert "प्र. ए." in r.padaccheda_dev


def test_samjna_bootstrap_idempotent():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("1.1.14", s0)
    assert s1114.nipata_ekajang_samjna_is_registered(s1)
    s2 = apply_rule("1.1.14", s1)
    assert s2.samjna_registry.get(s1114.SAMJNA_KEY) is True
