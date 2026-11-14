"""7.2.44 ūdit: the bhū that 2.4.52 puts in place of as (upadesha stamp 'BU~') is not ūdit — no iṭ-less reading *BUsyaJi (Bodas, प्रक्रियापद्धति: 5, as + lṛṭ)."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.tinanta import derive


def test_as_lrt_jhi_has_no_it_less_branch():
    got = {b.surface_slp1 for b in explore(lambda: derive("02.0060", "lRT", "kartari", 3, 3))}
    assert "Bavizyanti" in got
    assert "BUsyaJi" not in got and not any(g.startswith("BUs") for g in got), got
