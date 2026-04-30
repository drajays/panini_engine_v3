"""``prakriya_20`` Part 1 — *devam* (``pipelines/devam_krt_prakriya_20_demo``)."""
import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.devam_krt_prakriya_20_demo import derive_devam_prakriya_20


def _fired_or_audit_ids(state: State) -> list[str]:
    out: list[str] = []
    for e in state.trace:
        sid = e.get("sutra_id")
        if not sid or not isinstance(sid, str):
            continue
        st = (e.get("status") or "").upper()
        if st in {"APPLIED", "AUDIT"}:
            out.append(sid)
    return out


def test_devam_prakriya_20_surface() -> None:
    s = derive_devam_prakriya_20()
    assert s.flat_slp1() == "devam"


def test_devam_prakriya_20_spine_order() -> None:
    s = derive_devam_prakriya_20()
    ids = _fired_or_audit_ids(s)
    spine = [
        "3.1.134",
        "7.3.86",
        "1.2.46",
        "6.1.163",
        "6.1.158",
        "4.1.2",
        "3.1.4",
        "6.1.107",
        "8.2.5",
    ]
    for sid in spine:
        assert sid in ids, f"missing {sid}"
    assert ids.index("3.1.134") < ids.index("7.3.86") < ids.index("1.2.46")
    assert ids.index("1.2.46") < ids.index("6.1.163") < ids.index("6.1.158")
    assert ids.index("4.1.2") < ids.index("3.1.4") < ids.index("6.1.107")
    assert ids.index("6.1.107") < ids.index("8.2.5")
    assert any(
        e.get("sutra_id") == "__KRDANTA_DEVA_MERGE__"
        and (e.get("status") or "").upper() == "APPLIED"
        for e in s.trace
    )


def test_8_2_5_devam_registry() -> None:
    s = derive_devam_prakriya_20()
    assert "ekadesa_udatta_8_2_5" in s.samjna_registry
