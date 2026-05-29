import sutras  # noqa: F401

from pipelines.kurutaH_lat_tanadi_u_demo import derive_kurutaH


def test_kurutaH_surface() -> None:
    s = derive_kurutaH()
    assert s.flat_slp1() == "kurutaH"


def test_kurutaH_key_spine_fires() -> None:
    s = derive_kurutaH()
    fired = {e.get("sutra_id") for e in s.trace if (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}}
    for sid in ("3.1.79", "7.3.84", "1.1.51", "1.2.4", "6.4.110", "8.2.66", "8.3.15"):
        assert sid in fired

