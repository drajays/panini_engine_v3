"""1.3.7 is anitya (Kāśikā): the cu / ṭu initial of cuñcup, caṇap, jāhac, caraṭ, jātīyar stays, so the forms the Kāśikā gives come out."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

N = "napuṃsaka"
CASES = [   # (sense, stem, a form that must be among the readings)
    ("mUla", "karRa", "karRajAham"),       # 5.2.24 karṇajāham
    ("vitta", "vidyA", "vidyAcuYcu"),      # 5.2.26 vidyācuñcuḥ
    ("vitta", "vidyA", "vidyAcaRam"),      # caṇaḥ
    ("BUtapUrva", "ADhya", "ADhyacaram"),  # 5.3.53 āḍhyacaraḥ
    ("prakAra", "paTu", "paTujAtIyam"),    # 5.3.69 paṭujātīyaḥ
]


@pytest.mark.parametrize("sense,stem,want", CASES, ids=lambda c: None)
def test_cutu_stays(sense, stem, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, N, taddhitArtha=sense))}
    assert want in got, sorted(got)
