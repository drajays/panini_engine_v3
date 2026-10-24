"""K3 — the kṛtya sūtras that name a meaning (3.1.102, 103, 115, 116, 121, 125): the vivakṣā carries the meaning the sūtra itself states
(karaṇe, svāmivaiśyayoḥ, nade, nakṣatre, patre, āvaśyake); forms are Kāśikā udāharaṇas."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

CASES = [   # (dhātu id, artha, form that must be a reading, form that must not be)
    ("01.1159", "karaRa", "vahyaH", "vAhyaH"),          # vah 3.1.102 (vahyaM karaRam)
    ("01.1159", None, "vAhyaH", "vahyaH"),              # without the instrument sense: ṇyat
    ("01.1086", "svAmivESya", "aryaH", None),           # f 3.1.103
    ("01.1086", None, "AryaH", None),
    ("07.0002", "nada", "BidyaH", None),                # Bid 3.1.115
    ("06.0024", "nada", "udDyaH", None),                # ujJ → uddh
    ("04.0079", "nakzatra", "puzyaH", "pOzyaH"),        # puz 3.1.116
    ("04.0089", "nakzatra", "sidDyaH", None),            # siD → siddh
    ("07.0007", "patra", "yugyaH", "yogyaH"),           # yuj 3.1.121
    ("09.0016", "AvaSyaka", "lAvyaH", "lavyaH"),        # lU 3.1.125
    ("09.0014", "AvaSyaka", "pAvyaH", None),
]


@pytest.mark.parametrize("ref,artha,want,never", CASES, ids=lambda c: None)
def test_kftya_meaning(ref, artha, want, never):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, 1, 1, "pulliṅga", krt="kftya", artha=artha))}
    assert want in got, sorted(got)
    if never:
        assert never not in got, sorted(got)
