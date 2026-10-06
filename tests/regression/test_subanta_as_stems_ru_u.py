"""6.1.114 haśi ca (+6.1.87): as-stems before bhyām/bhiḥ — manobhyām, yaśobhiḥ (ashtadhyayi.com gold agrees)."""
import pytest

import sutras  # noqa: F401
from pipelines.subanta import derive


@pytest.mark.parametrize("stem,lg,vi,va,want", [("manas", "napuṃsaka", 3, 2, "मनोभ्याम्"), ("yaSas", "napuṃsaka", 3, 3, "यशोभिः"),
                                                  ("candramas", "pulliṅga", 3, 2, "चन्द्रमोभ्याम्"), ("manas", "napuṃsaka", 7, 3, "मनस्सु")])
def test_as_stem(stem, lg, vi, va, want):
    assert derive(stem, vi, va, linga=lg).flat_dev() == want
