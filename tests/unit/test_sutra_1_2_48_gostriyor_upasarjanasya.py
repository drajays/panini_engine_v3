from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from phonology.gostriyor_upasarjana import (
    apply_go_hrasva,
    apply_strI_pratyaya_final_hrasva,
    flat_slp1,
)


def _term(varnas_slp1: str, **kwargs) -> Term:
    tags = kwargs.pop("tags", set())
    meta = kwargs.pop("meta", {})
    varnas = [mk(c) for c in varnas_slp1]
    return Term(kind="prakriti", varnas=varnas, tags=tags, meta=meta)


def test_metadata():
    r = SUTRA_REGISTRY["1.2.48"]
    assert r.sutra_id == "1.2.48"
    assert r.sutra_type is SutraType.VIDHI
    assert "1.2.47" in r.anuvritti_from


def test_phonology_go_branch():
    v = apply_go_hrasva([mk("c"), mk("i"), mk("t"), mk("r"), mk("a"), mk("g"), mk("o")])
    assert v is not None
    assert flat_slp1(v) == "citragu"


def test_phonology_strI_branch():
    v = apply_strI_pratyaya_final_hrasva(
        [mk("a"), mk("t"), mk("i"), mk("K"), mk("a"), mk("w"), mk("v"), mk("A")]
    )
    assert v is not None
    assert flat_slp1(v) == "atiKawva"


def test_citragu_when_armed_and_tagged():
    t = _term(
        "citrago",
        tags={"prātipadika", "upasarjana", "gostriyor_go"},
    )
    s0 = State(terms=[t], meta={"1_2_48_arm": True})
    s1 = apply_rule("1.2.48", s0)
    assert s1.flat_slp1() == "citragu"
    assert s1.terms[0].meta.get("hrasva_1_2_48") is True
    assert s1.meta.get("1_2_48_arm") is False


def test_atikhATvA_style_strI_pratyaya():
    t = _term(
        "atiKawvA",
        tags={"prātipadika", "upasarjana", "TAp_anta"},
    )
    s0 = State(terms=[t], meta={"1_2_48_arm": True})
    s1 = apply_rule("1.2.48", s0)
    assert s1.flat_slp1() == "atiKawva"


def test_nirvArANasI_style_final_I():
    t = _term(
        "nirvArARasI",
        tags={"prātipadika", "upasarjana", "TAp_anta"},
    )
    s0 = State(terms=[t], meta={"1_2_48_arm": True})
    s1 = apply_rule("1.2.48", s0)
    assert s1.flat_slp1() == "nirvArARasi"


def test_Iiyas_bahuvrIhi_pratishedha_blocks():
    t = _term(
        "bahuSreyasI",
        tags={
            "prātipadika",
            "upasarjana",
            "TAp_anta",
            "Iyas_bahuvrIhi_pratishedha",
        },
    )
    s0 = State(terms=[t], meta={"1_2_48_arm": True})
    s1 = apply_rule("1.2.48", s0)
    assert s1.flat_slp1() == "bahuSreyasI"
    assert s1.meta.get("1_2_48_arm") is True


def test_unarmed_does_not_apply():
    t = _term("citrago", tags={"prātipadika", "upasarjana", "gostriyor_go"})
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.2.48", s0)
    assert s1.flat_slp1() == "citrago"


def test_without_upasarjana_tag():
    t = _term("citrago", tags={"prātipadika", "gostriyor_go"})
    s0 = State(terms=[t], meta={"1_2_48_arm": True})
    s1 = apply_rule("1.2.48", s0)
    assert s1.flat_slp1() == "citrago"
