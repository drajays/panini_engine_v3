import sutras  # noqa: F401

from pipelines.prakriya_02_adhyagIzwa_demo import derive_prakriya_02


def _fired_ids(state) -> list[str]:
    out: list[str] = []
    for e in state.trace:
        sid = e.get("sutra_id")
        if not sid or not isinstance(sid, str):
            continue
        st = (e.get("status") or "").upper()
        if st in {"APPLIED", "AUDIT"}:
            out.append(sid)
    return out


def test_prakriya_02_surface() -> None:
    s = derive_prakriya_02()
    assert s.flat_slp1() == "aDhyagIzwa"


def test_prakriya_02_key_spine_fires_in_order() -> None:
    # This locks the intended spine described in the JSON’s `panini_engine_pipeline`.
    s = derive_prakriya_02()
    ids = _fired_ids(s)
    must = [
        "2.4.45",  # iN -> gAN
        "1.2.1",   # ṅit-atideśa
        "6.4.66",  # A -> I
        "7.2.35",  # iṭ on sic
        "8.2.1",   # tripāḍī gate
        "8.3.59",  # ṣatva
        "8.4.41",  # ṣṭutva
    ]
    for m in must:
        assert m in ids
    assert ids.index("2.4.45") < ids.index("1.2.1") < ids.index("6.4.66") < ids.index("7.2.35")
    assert ids.index("8.2.1") < ids.index("8.3.59") < ids.index("8.4.41")

