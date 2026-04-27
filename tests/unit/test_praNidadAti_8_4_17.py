from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from pipelines.praNidadAti_ner_ghu_8_4_17 import build_pra_ni_ghu_state, praNidadAti_ner_ghu
from sutras.adhyaya_1.pada_1.sutra_1_1_20 import dhatu_upadesha_slp1_is_ghu


def test_8_4_17_ner_ghu_praNi_dadAti_flat() -> None:
    s = praNidadAti_ner_ghu()
    # ण् is ``R`` in this engine; ``N`` = ङ् (contrast ``phonology`` HAL_DEV).
    assert s.flat_slp1() == "praRidadAti"
    assert s.terms[1].varnas[0].slp1 == "R"


def test_8_4_17_does_not_apply_without_tripadi_or_meta_arm() -> None:
    s0 = build_pra_ni_ghu_state()
    assert s0.tripadi_zone is False
    s1 = apply_rule("8.4.17", s0)
    # No arm, no *Tripāḍī* — rule does not run
    assert s1.terms[1].varnas[0].slp1 == "n"
    s1.meta["8_4_17_pre_tripadi_arm"] = True
    s2 = apply_rule("8.4.17", s1)
    assert s2.terms[1].varnas[0].slp1 == "R"


def test_8_4_17_ghu_is_required() -> None:
    pra = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("pra"),
        tags={"upasarga", "anga"},
    )
    ni = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ni"),
        tags={"upasarga", "anga"},
    )
    other = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("pacati"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "qupa~caY"},  # not ghu
    )
    s = State(terms=[pra, ni, other], meta={})
    s = apply_rule("1.1.20", s)
    u = s.terms[2].meta.get("upadesha_slp1", "")
    assert not dhatu_upadesha_slp1_is_ghu(s, u)
    s.tripadi_zone = True
    s = apply_rule("8.4.17", s)
    assert s.terms[1].varnas[0].slp1 == "n"
