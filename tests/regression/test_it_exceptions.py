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


def test_at_keeps_no_t_in_kva():
    """1.3.4 is anitya for `at` (Kāśikā: kimo 'at, iṭo 'at): the t is it although at is a vibhakti — kim + at → kva (7.2.105), not kvat."""
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("kim", 1, 1, N, taddhitArtha="saptamIvib"))}
    assert "kva" in got and "kvat" not in got and "kvad" not in got, sorted(got)
