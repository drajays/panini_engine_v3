import sutras  # noqa: F401

from pipelines.adhyagIzwa_luN_demo import derive_aDhyagIzwa


def test_adhyagIzwa_surface() -> None:
    s = derive_aDhyagIzwa()
    assert s.flat_slp1() == "aDhyagIzwa"

