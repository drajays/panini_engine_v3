from __future__ import annotations

import sutras  # noqa: F401

from pipelines.praNiyacCati_ner_ghu_8_4_17 import (
    build_pra_ni_yacCati_ghu_state,
    praNiyacCati_ner_ghu,
)


def test_praRiyacCati_flat_yacC_adesa_ghu_upadesa() -> None:
    s = praNiyacCati_ner_ghu()
    assert s.flat_slp1() == "praRiyacCati"
    assert s.terms[2].meta.get("upadesha_slp1") == "da~da"
    assert s.paribhasha_gates.get("sthanivadbhava") is True
    assert s.terms[1].varnas[0].slp1 == "R"


def test_build_includes_1_1_56_and_yacC_surface() -> None:
    s0 = build_pra_ni_yacCati_ghu_state()
    assert s0.terms[2].varnas[0].slp1 == "y"
    assert s0.paribhasha_gates.get("sthanivadbhava") is True
