"""6.1.16 ग्रहिज्यावयिव्यधि…ङिति च (and 6.1.17 on the abhyāsa in liṭ), through the shipped path — Kāśikā: विध्यति, विविधतुः, गृह्णाति, जगृहतुः, जिनाति, विचति."""
import pytest

from pipelines.tinanta import derive

CASES = [
    ("04.0078", "laT", 3, 1, "viDyati"),      # vyadh
    ("04.0078", "liT", 3, 2, "viviDatuH"),
    ("06.0013", "laT", 3, 1, "vicati"),       # vyac
    ("06.0013", "liT", 3, 2, "vivicatuH"),
    ("09.0071", "laT", 3, 1, "gfhRAti"),      # grah
    ("09.0071", "liT", 3, 1, "jagrAha"),
    ("09.0071", "liT", 3, 2, "jagfhatuH"),
    ("09.0034", "laT", 3, 1, "jinAti"),       # jyā: 6.4.2 lengthens, 7.3.80 shortens again
    ("09.0034", "laT", 3, 3, "jinanti"),
]


@pytest.mark.parametrize("ref,lakara,pu,vc,form", CASES)
def test_samprasarana_before_kit_ngit(ref, lakara, pu, vc, form):
    assert derive(ref, lakara, "kartari", pu, vc).render() == form
