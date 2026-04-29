import sutras  # noqa: F401

from pipelines.adita_luN_dAda_ghu_demo import derive_adita


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


def test_adita_surface() -> None:
    s = derive_adita()
    assert s.flat_slp1() == "adita"


def test_adita_luN_ghu_ic_spine() -> None:
    s = derive_adita()
    ids = _fired_ids(s)
    for need in ("3.2.110", "1.1.20", "1.2.17", "6.4.71", "6.4.64", "3.4.78", "8.2.1"):
        assert need in ids
    assert ids.index("1.1.20") < ids.index("1.2.17") < ids.index("6.4.71") < ids.index("6.4.64")
