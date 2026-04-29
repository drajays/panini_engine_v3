import sutras  # noqa: F401

from pipelines.atiri_atinu_kulam_demo import derive_atinu, derive_atiri


def test_atiri() -> None:
    s = derive_atiri()
    assert s.flat_slp1() == "atiri"


def test_atinu() -> None:
    s = derive_atinu()
    assert s.flat_slp1() == "atinu"

