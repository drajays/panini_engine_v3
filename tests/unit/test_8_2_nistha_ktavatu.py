"""8.2.42-57 act on the ta of ktavatu as of kta (Kāśikā 8.2.51 शुष्कवान्, 8.2.52 पक्ववान्, 8.2.44 लूनवान्, 8.2.43 म्लानवान्)."""
import pytest

import sutras  # noqa: F401
from pipelines.krdanta import derive_krdanta

KV = dict(kala="BUta", artha="kartf")


@pytest.mark.parametrize("dh,want", [("04.0080", "SuzkavAn"), ("01.1151", "pakvavAn"), ("09.0016", "lUnavAn"), ("01.1052", "mlAnavAn")])
def test_ktavatu_ta_is_changed(dh, want):
    assert derive_krdanta(dh, 1, 1, "pulliṅga", **KV).flat_slp1().replace(" ", "") == want
