import sutras  # noqa: F401

from pipelines.dadhiccChatram_samasa_demo import derive_dadhiccChatram


def _fired(trace: list[dict], sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_dadhiccChatram_surface_and_dev() -> None:
    s = derive_dadhiccChatram()
    assert s.flat_slp1() == "daDicCatram"
    assert s.flat_dev() == "\u0926\u0927\u093f\u091a\u094d\u091b\u0924\u094d\u0930\u092e\u094d"


def test_dadhiccChatram_spine_rules() -> None:
    s = derive_dadhiccChatram()
    for need in ("6.1.73", "8.2.1", "8.4.40"):
        assert _fired(s.trace, need)


def test_order_merge_before_tripadi() -> None:
    s = derive_dadhiccChatram()
    ids = [
        e.get("sutra_id")
        for e in s.trace
        if (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
    ]
    assert "__MERGE__" in ids
    assert ids.index("__MERGE__") < ids.index("8.2.1") < ids.index("8.4.40")
