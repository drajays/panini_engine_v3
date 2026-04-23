"""
1.1.12 अदसो मात् — paribhāṣā gate ( *aś* / *sarvān. adas* *it*; before 1.3.x).

Frozen metadata matches [ashtadhyayi-com/data](https://github.com/ashtadhyayi-com/data)
``sutraani/data.txt`` row **i=11012** (field ``e`` in Velthuis; v3 ``text_slp1`` is spaced SLP1).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_12 as s1112

# github.com/ashtadhyayi-com/data sutraani/data.txt i=11012
ASHTADHYAYI_DATA_TXT_I: str = "11012"
ASHTADHYAYI_E_VELTHUIS: str = "adasomaat"


def _slp1_compact(slp1: str) -> str:
    return slp1.replace(" ", "")


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.12"]
    assert r.sutra_id == "1.1.12"
    assert r.sutra_type is SutraType.PARIBHASHA
    assert "adaso" in r.text_slp1
    assert "mAt" in r.text_slp1


def test_patha_matches_ashtadhyayi_com_row_11012():
    """``text_dev`` / ``anuvritti_from`` / compact SLP1 align with ashtadhyayi-com ``data``."""
    r = SUTRA_REGISTRY["1.1.12"]
    assert r.text_dev == "अदसो मात्"
    assert r.padaccheda_dev == "अदसः मात्"
    assert r.anuvritti_from == ("1.1.11",)
    # v3 spaced morphemes; one-token Velthuis ``e`` in data.txt; same phonemes as compact SLP1.
    assert _slp1_compact(r.text_slp1) == "adasomAt"
    assert ASHTADHYAYI_DATA_TXT_I == "11012"
    assert ASHTADHYAYI_E_VELTHUIS == "adasomaat"
    # Long ā: Velthuis ``aa`` (2 chars) vs SLP1 ``A`` (1) — same segment count, different string length.


def test_gate_set_and_idempotent():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    assert s1112.GATE_KEY not in s0.paribhasha_gates
    s1 = apply_rule("1.1.12", s0)
    assert s1112.adaso_mAt_gate_is_set(s1)
    assert s1.paribhasha_gates[s1112.GATE_KEY].get("active") is True
    s2 = apply_rule("1.1.12", s1)
    assert s2.paribhasha_gates == s1.paribhasha_gates


def test_adaso_mAt_gate_is_set_false_initially():
    s = State(terms=[Term(kind="prakriti", varnas=[mk("k")])])
    assert not s1112.adaso_mAt_gate_is_set(s)
