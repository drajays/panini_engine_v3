"""
Locks the spine from `/Users/dr.ajayshukla/Documents/my panini notes/अतिनु.md`.
"""
import sutras  # noqa: F401

from pipelines.atinu_neuter_demo import derive_atinu


def _sutra_ids_chronological(state):
    """All traced sūtra ids in recipe order (any status)."""
    out = []
    for e in state.trace:
        sid = e.get("sutra_id")
        if sid and isinstance(sid, str):
            out.append(sid)
    return out


def test_atinu_surface_from_note() -> None:
    s = derive_atinu()
    assert s.flat_slp1() == "atinu"


def test_atinu_note_spine_order() -> None:
    s = derive_atinu()
    ids = _sutra_ids_chronological(s)
    # अतिनु.md: 1.2.47 (now performs O→u via ec_ig bundle), sup, 7.1.23.
    assert "1.2.47" in ids
    assert "4.1.2" in ids
    assert "7.1.23" in ids
    assert ids.index("1.2.47") < ids.index("4.1.2") < ids.index("7.1.23")


def test_one_two_four_seven_applied_when_ec_final() -> None:
    """EC-final neuter bases take the *एच्→इक्* branch inside 1.2.47."""
    s = derive_atinu()
    row = next(e for e in s.trace if e.get("sutra_id") == "1.2.47")
    assert (row.get("status") or "").upper() == "APPLIED"
