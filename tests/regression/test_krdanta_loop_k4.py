"""K4 — the agent-sense kṛts beside ṇvul-tṛc (3.1.133): ka 3.1.135, ṇa 3.1.142 / 3.1.143. Kāśikā: budhaḥ, kṛśaḥ, jñaḥ, priyaḥ; dāvaḥ, nāyaḥ; grāhaḥ."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

AGENT = dict(krt="Rvultfc")
CASES = [   # (dhātu id, form that must be one of the readings)
    ("04.0068", "buDaH"),        # budh 3.1.135 (iguṇa-upadha: no guṇa, ka is kit)
    ("04.0140", "kfSaH"),        # kṛś
    ("06.0092", "liKaH"),        # likh (vilikhaḥ)
    ("09.0043", "jYaH"),         # jñā
    ("09.0002", "priyaH"),       # prī (6.4.? ī → iy before a vowel-initial affix)
    ("01.1094", "dAvaH"),        # du 3.1.142
    ("01.1049", "nAyaH"),        # nī 3.1.142 (ṇa — the tape still has RI)
    ("09.0071", "grAhaH"),       # grah 3.1.143
    ("01.1049", "nAyakaH"),      # ṇvul-tṛc stay beside ṇa / ka
    ("01.1049", "netA"),
    ("04.0068", "boDakaH"),
]


@pytest.mark.parametrize("ref,want", CASES, ids=lambda c: None)
def test_agent_kft_beside_nvul(ref, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, 1, 1, "pulliṅga", **AGENT))}
    assert want in got, sorted(got)
