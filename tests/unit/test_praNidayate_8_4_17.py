from __future__ import annotations

import sutras  # noqa: F401

from pipelines.praNidayate_ner_ghu_8_4_17 import (
    build_pra_ni_dayate_ghu_state,
    praNidayate_ner_ghu,
)


def test_praRidayate_deN_ghu_flat() -> None:
    s = praNidayate_ner_ghu()
    # ण् = R in v3; not N (ङ्).
    assert s.flat_slp1() == "praRidayate"
    assert s.terms[2].meta.get("upadesha_slp1") == "de~N"
    assert s.terms[1].varnas[0].slp1 == "R"


def test_build_includes_1_1_56() -> None:
    s0 = build_pra_ni_dayate_ghu_state()
    assert s0.terms[2].varnas[0].slp1 == "d"
    assert s0.paribhasha_gates.get("sthanivadbhava") is True
