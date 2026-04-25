"""2.3.36 + *śālīya* meta (registry only)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology import mk

from sutras.adhyaya_1.pada_4.sutra_1_4_45 import META_LOCUS_INDICES, SAMJNA_KEY
from sutras.adhyaya_2.pada_3.sutra_2_3_36 import META_LOCATIVE, REGISTRY_KEY


def test_registry() -> None:
    r = SUTRA_REGISTRY["2.3.36"]
    assert r.sutra_type is SutraType.SAMJNA
    assert "2.3.1" in r.anuvritti_from


def test_applies_after_1_4_45() -> None:
    t0 = Term(
        kind="prakriti",
        varnas=[mk("S"), mk("A"), mk("l"), mk("A")],
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "SAlA"},
    )
    s0 = State(terms=[t0], meta={
        "prakriya_sAlIya": True,
        META_LOCATIVE: "SAlAyAm",
    })
    s0 = apply_rule("1.4.23", s0)
    s0.meta[META_LOCUS_INDICES] = (0,)
    s1 = apply_rule("1.4.45", s0)
    s2 = apply_rule("2.3.36", s1)
    assert s2.samjna_registry[REGISTRY_KEY] == "SAlAyAm"
