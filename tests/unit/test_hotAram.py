"""``prakriya_21`` — *hotāram* / ``hotAram`` (``pipelines/hotAram_prakriya_21_demo``)."""
import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.hotAram_prakriya_21_demo import derive_hotAram_prakriya_21
from pipelines.krdanta import derive_tfc_pratipadika


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


def test_hotAram_prakriya_21_surface() -> None:
    s = derive_hotAram_prakriya_21()
    assert s.flat_slp1() == "hotAram"


def test_hotAram_prakriya_21_spine_order() -> None:
    s = derive_hotAram_prakriya_21()
    ids = _fired_or_audit_ids(s)
    spine = [
        "3.1.133",
        "7.3.84",
        "4.1.2",
        "1.1.43",
        "7.3.110",
        "1.1.51",
        "6.4.11",
        "3.1.4",
    ]
    for sid in spine:
        assert sid in ids, f"missing {sid}"
    # **6.1.107** is COND-FALSE here: ``…r`` + ``am`` must keep ``am``-initial ``a``
    # (see ``sutra_6_1_107`` *r*-boundary guard).
    row107 = next((e for e in s.trace if e.get("sutra_id") == "6.1.107"), None)
    assert row107 is not None
    assert (row107.get("status") or "").upper() == "SKIPPED"
    assert ids.index("4.1.2") < ids.index("1.1.43")
    assert ids.index("1.1.43") < ids.index("7.3.110") < ids.index("1.1.51")
    assert ids.index("1.1.51") < ids.index("6.4.11") < ids.index("3.1.4")


def test_hotf_stem_before_subanta() -> None:
    k = derive_tfc_pratipadika("hu")
    assert k.flat_slp1() == "hotf"
