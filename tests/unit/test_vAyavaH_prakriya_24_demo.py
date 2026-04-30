"""Unit tests for ``prakriya_24`` — *vāyavaḥ* (``pipelines/vAyavaH_prakriya_24_demo``)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from phonology.varna import parse_slp1_upadesha_sequence

from pipelines.vAyavaH_prakriya_24_demo import derive_vAyavaH_prakriya_24, _mk_vA_dhatu


def _trace_ids(state: State) -> list[str]:
    return [e.get("sutra_id") for e in state.trace if isinstance(e.get("sutra_id"), str)]


def test_vAyavaH_surface() -> None:
    s = derive_vAyavaH_prakriya_24()
    assert s.flat_slp1() == "vAyavaH"


def test_vAyavaH_json_spine_and_subanta_hotspots() -> None:
    s = derive_vAyavaH_prakriya_24()
    ids = _trace_ids(s)
    for sid in (
        "1.3.1",
        "3.1.91",
        "3.1.3",
        "3.3.174",
        "7.3.33",
        "7.3.109",
        "6.1.78",
        "8.2.66",
        "8.3.15",
    ):
        assert sid in ids, f"missing trace row {sid}"
    assert ids.index("1.3.1") < ids.index("3.1.91") < ids.index("3.1.3")
    assert ids.index("3.1.3") < ids.index("3.3.174") < ids.index("7.3.33")


def test_3_3_174_appends_uR() -> None:
    s = State(terms=[_mk_vA_dhatu()], meta={"prakriya_24_uR_arm": True}, trace=[])
    s1 = apply_rule("3.3.174", s)
    assert len(s1.terms) == 2
    assert s1.terms[1].meta.get("upadesha_slp1") == "uR"
    assert s1.terms[1].meta.get("prakriya_24_uR_source") is True


def test_7_3_33_inserts_y_after_A() -> None:
    from engine.state import Term

    vA = _mk_vA_dhatu()
    u = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("u")),
        tags={"pratyaya", "upadesha", "krt"},
        meta={"upadesha_slp1": "u", "prakriya_24_uR_source": True},
    )
    s = State(terms=[vA, u], meta={"prakriya_24_7_3_33_arm": True}, trace=[])
    s1 = apply_rule("7.3.33", s)
    assert "".join(v.slp1 for v in s1.terms[0].varnas) == "vAy"
    assert s1.terms[0].meta.get("7_3_33_yuk_inserted") is True
