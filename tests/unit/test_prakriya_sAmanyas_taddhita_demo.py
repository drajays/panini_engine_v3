"""Unit tests for ``prakriya_18`` — *sāmanyaḥ* (``pipelines/sAmanyas_taddhita_demo``)."""
import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.sAmanyas_taddhita_demo import (
    _mk_Ni_sup,
    _mk_sAman,
    derive_sAmanyas,
)


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


def _trace_row(state: State, sutra_id: str) -> dict | None:
    for e in state.trace:
        if e.get("sutra_id") == sutra_id:
            return e
    return None


def test_sAmanyas_surface_prathamA_eka() -> None:
    s = derive_sAmanyas()
    assert s.flat_slp1() == "sAmanyaH"


def test_sAmanyas_6_4_168_blocks_6_4_144() -> None:
    s = State(terms=[_mk_sAman(), _mk_Ni_sup()])
    s.meta["prakriya_18_sAmanyas"] = True
    s.meta["prakriya_18_4_4_98_arm"] = True
    s = apply_rule("4.4.98", s)
    s = apply_rule("6.4.168", s)
    assert "6_4_168_yat_prakritibhava_sAman" in s.samjna_registry
    s.meta["prakriya_18_6_4_144_attempt_arm"] = True
    s = apply_rule("6.4.144", s)
    row = _trace_row(s, "6.4.144")
    assert row is not None
    assert (row.get("status") or "").upper() == "SKIPPED"


def test_sAmanyas_full_demo_spine_order() -> None:
    s = derive_sAmanyas()
    ids = _fired_ids(s)
    spine = ["4.4.98", "6.4.168", "1.2.46", "2.4.71", "6.1.213", "6.1.158", "8.2.66"]
    for sid in spine:
        assert sid in ids, f"missing fired {sid}"
    assert ids.index("4.4.98") < ids.index("6.4.168")
    assert ids.index("6.4.168") < ids.index("1.2.46") < ids.index("2.4.71")
    assert ids.index("6.1.213") < ids.index("6.1.158") < ids.index("8.2.66")
    merge = _trace_row(s, "__TADDHITA_SAMANYA_MERGE__")
    assert merge is not None
    assert (merge.get("status") or "").upper() == "APPLIED"
    r144 = _trace_row(s, "6.4.144")
    assert r144 is not None
    assert (r144.get("status") or "").upper() == "SKIPPED"
