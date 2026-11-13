"""3.1.37 (दयायासश्च: आम् mandatory), 3.1.38 (उषविदजागृभ्योऽन्यतरस्याम्: optional), and 3.1.40's kṛ / bhū / as anuprayoga
(KV 3.1.37-40; forms checked against the Vidyut rows 6843-6845, 7003-7005 in the DB)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.tinanta import derive


def _all(dhatu):
    return {b.surface_slp1 for b in explore(lambda: derive(dhatu, "liT", "kartari", 3, 1))}


@pytest.mark.parametrize("dhatu,want", [
    ("02.0011", {"AsAYcakre", "AsAmbaBUva", "AsAmAsa"}),          # Asa~: ām is not optional (no Ase)
    ("01.0553", {"dayAYcakre", "dayAmbaBUva", "dayAmAsa"}),
    ("01.0546", {"ayAYcakre", "ayAmbaBUva", "ayAmAsa"}),
    ("02.0067", {"jajAgAra", "jAgarAYcakAra", "jAgarAmbaBUva", "jAgarAmAsa"}),   # 3.1.38 vā: the plain liṭ stays
    ("02.0059", {"viveda", "vidAYcakAra", "vidAmbaBUva", "vidAmAsa"}),           # vid: no guṇa before ām
    ("01.0792", {"uvoza", "ozAYcakAra", "ozAmbaBUva", "ozAmAsa"}),
])
def test_am_readings(dhatu, want):
    assert _all(dhatu) == want
