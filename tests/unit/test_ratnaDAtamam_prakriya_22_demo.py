"""Unit tests for ``prakriya_22`` — *ratnadhātamam* (``pipelines/ratnaDAtamam_prakriya_22_demo``)."""
import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term

from phonology.varna import parse_slp1_upadesha_sequence

from pipelines.ratnaDAtamam_prakriya_22_demo import derive_ratnaDAtamam_prakriya_22


def _fired_ids(state: State) -> list[str]:
    out: list[str] = []
    for e in state.trace:
        sid = e.get("sutra_id")
        if not sid or not isinstance(sid, str):
            continue
        st = (e.get("status") or "").upper()
        if st in {"APPLIED", "AUDIT"}:
            out.append(sid)
    return out


def test_ratnaDAtamam_surface() -> None:
    s = derive_ratnaDAtamam_prakriya_22()
    assert s.flat_slp1() == "ratnaDAtamam"


def test_ratnaDAtamam_spine_order() -> None:
    s = derive_ratnaDAtamam_prakriya_22()
    ids = _fired_ids(s)
    spine = [
        "3.2.76",
        "1.2.46",
        "2.4.71",
        "2.2.19",
        "6.1.67",
        "5.3.55",
        "6.1.107",
    ]
    for sid in spine:
        assert sid in ids, f"missing fired {sid}"
    assert ids.index("3.2.76") < ids.index("1.2.46") < ids.index("2.4.71")
    assert ids.index("2.4.71") < ids.index("2.2.19")
    assert ids.index("2.2.19") < ids.index("6.1.67")
    assert ids.index("6.1.67") < ids.index("5.3.55")
    assert ids.index("5.3.55") < ids.index("6.1.107")


def test_6_1_67_kvip_vi_residue_narrow() -> None:
    ratna = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("ratna")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "ratna"},
    )
    kvip = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("vi")),
        tags={"pratyaya", "upadesha", "krt"},
        meta={"upadesha_slp1": "kvip"},
    )
    s = State(terms=[ratna, kvip], meta={"prakriya_22_kvip_residue_arm": True}, trace=[])
    assert s.flat_slp1() == "ratnavi"
    s1 = apply_rule("6.1.67", s)
    assert s1.flat_slp1() == "ratna"


def test_3_2_76_appends_kvip_after_dhatu() -> None:
    dha = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("DA")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "DA"},
    )
    s = State(terms=[dha], meta={"3_2_76_kvip_arm": True}, trace=[])
    s1 = apply_rule("3.2.76", s)
    assert len(s1.terms) == 2
    assert s1.terms[1].meta.get("upadesha_slp1") == "kvip"
    assert "3_2_76_kvip_arm" not in s1.meta
