"""
1.1.21 *ādyantavad ekasmin* — *paribhāṣā* *gate* for *ādyantavad* *atideśa* (ashtadhyayi *i* 11021).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_21 as s1121

# i=11021 *s*
_S_11021: str = "\u0906\u0926\u094d\u092f\u0928\u094d\u0924\u0935\u0926\u0947\u0915\u0938\u094d\u092e\u093f\u0928\u094d"


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.21"]
    assert r.sutra_id == "1.1.21"
    assert r.sutra_type is SutraType.PARIBHASHA
    assert "Adyantavad" in r.text_slp1
    assert r.anuvritti_from == ()


def test_pATha_bytes_match_ashtadhyayi_s():
    assert s1121._TEXT_DEV == _S_11021
    assert s1121.SUTRA.padaccheda_dev == "आदि-अन्तवत् / एकस्मिन्"


def test_paribhasha_gate():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t], paribhasha_gates={})
    assert not s1121.aadyantavad_ekasmin_paribhasha_set(s0)
    s1 = apply_rule("1.1.21", s0)
    assert s1121.aadyantavad_ekasmin_paribhasha_set(s1)
    assert s1.paribhasha_gates[s1121.GATE_KEY]["pATha"] == "1.1.21"
    s2 = apply_rule("1.1.21", s1)
    assert s1121.aadyantavad_ekasmin_paribhasha_set(s2)
