from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def _putra_saha_state(*, with_iti: bool = False) -> State:
    t_putra = Term(
        kind="prakriti",
        varnas=[mk("p"), mk("u"), mk("t"), mk("r"), mk("a")],
        tags={"prātipadika", "2_2_28_companion"},
        meta={"upadesha_slp1": "putra"},
    )
    terms: list = [t_putra]
    if with_iti:
        terms.append(
            Term(
                kind="nipata",
                varnas=[mk("i"), mk("t"), mk("i")],
                tags={"nipata"},
                meta={"upadesha_slp1": "iti"},
            )
        )
    terms.append(
        Term(
            kind="nipata",
            varnas=[mk("s"), mk("a"), mk("h"), mk("a")],
            tags={"avyaya", "nipata"},
            meta={"upadesha_slp1": "saha"},
        )
    )
    return State(terms=terms)


def test_metadata():
    r = SUTRA_REGISTRY["2.2.28"]
    assert r.sutra_id == "2.2.28"
    assert r.sutra_type is SutraType.VIDHI


def test_merges_putra_saha_to_saputra_when_armed_tulyayoga():
    s0 = _putra_saha_state()
    s0 = apply_rule("2.1.3", s0)
    s0.meta["2_2_28_arm"] = True
    s0.meta["2_2_28_tulyayoga"] = True
    s1 = apply_rule("2.2.28", s0)
    assert len(s1.terms) == 1
    assert s1.flat_slp1() == "saputra"
    assert {"bahuvrihi", "sahasamasa"}.issubset(s1.terms[0].tags)
    assert s1.meta.get("2_2_28_arm") is False


def test_no_merge_without_tulyayoga_meta():
    s0 = _putra_saha_state()
    s0 = apply_rule("2.1.3", s0)
    s0.meta["2_2_28_arm"] = True
    s0.meta["2_2_28_tulyayoga"] = False
    s1 = apply_rule("2.2.28", s0)
    assert len(s1.terms) == 2
    assert s1.flat_slp1() == "putrasaha"


def test_no_merge_without_samasa_adhikara():
    s0 = _putra_saha_state()
    s0.meta["2_2_28_arm"] = True
    s0.meta["2_2_28_tulyayoga"] = True
    s1 = apply_rule("2.2.28", s0)
    assert len(s1.terms) == 2


def test_optional_iti_between_companion_and_saha():
    s0 = _putra_saha_state(with_iti=True)
    s0 = apply_rule("2.1.3", s0)
    s0.meta["2_2_28_arm"] = True
    s0.meta["2_2_28_tulyayoga"] = True
    s1 = apply_rule("2.2.28", s0)
    assert s1.flat_slp1() == "saputra"
    assert len(s1.terms) == 1


def test_palatal_sha_companion_uses_sac_prefix():
    t0 = Term(
        kind="prakriti",
        varnas=[mk("S"), mk("A"), mk("t"), mk("r"), mk("a")],
        tags={"prātipadika", "2_2_28_companion"},
        meta={"upadesha_slp1": "SAtra"},
    )
    t1 = Term(
        kind="nipata",
        varnas=[mk("s"), mk("a"), mk("h"), mk("a")],
        tags={"avyaya", "nipata"},
        meta={"upadesha_slp1": "saha"},
    )
    s0 = State(terms=[t0, t1])
    s0 = apply_rule("2.1.3", s0)
    s0.meta["2_2_28_arm"] = True
    s0.meta["2_2_28_tulyayoga"] = True
    s1 = apply_rule("2.2.28", s0)
    assert s1.flat_slp1() == "sacAtra"
