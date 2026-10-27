"""K9 — the meanings that put śatṛ / śānac / śānan / cānaś in laṭ's place: 3.2.125 sambodhana, 3.2.126 lakṣaṇa-hetu, 3.2.127 sat-saṃjñā,
3.2.128 pū / yaj śānan, 3.2.129 cānaś, 3.2.131 dviṣaḥ, 3.2.132 suñaḥ yajñasaṃyoge, 3.2.133 arhaḥ praśaṃsāyām (Kāśikā udāharaṇas)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

VT = dict(kala="vartamAna")
CASES = [   # (dhātu id, vibhakti, vivakṣā, form that must be one of the readings)
    ("01.0381", 8, dict(sambodhana="sambodhana"), "paWan"),                  # हे पचन् (3.2.125)
    ("01.0002", 8, dict(sambodhana="sambodhana"), "eDamAna"),                # हे पचमान
    ("01.0381", 1, dict(lakzaRahetu="lakzaRa"), "paWan"),                    # 3.2.126
    ("01.0381", 1, dict(lakzaRahetu="hetu"), "paWan"),
    ("01.1157", 1, dict(samAnADikaraRa="apraTamA"), "yajamAnaH"),            # 3.2.128 (yaj: śānan, not śatṛ / śānac)
    ("01.1121", 1, dict(samAnADikaraRa="apraTamA"), "pavamAnaH"),            # pūṅ
    ("01.0381", 1, dict(tAcCIlyAdi="tAcCIlya"), "paWamAnaH"),                # 3.2.129 cānaś
    ("02.0003", 1, dict(amitra="amitra"), "dvizan"),                         # 3.2.131 द्विषन्
    ("05.0001", 1, dict(yajYasaMyoga="yajYasaMyoga"), "sunvAn"),             # 3.2.132 सुन्वन्
    ("01.0841", 1, dict(praSaMsA="praSaMsA"), "arhan"),                      # 3.2.133 अर्हन्
]


@pytest.mark.parametrize("ref,vib,kw,want", CASES, ids=lambda c: None)
def test_participle_meanings(ref, vib, kw, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, vib, 1, "pulliṅga", **VT, **kw))}
    assert want in got, sorted(got)


def test_without_the_meaning_nothing_is_attached():
    """3.2.131 needs amitra, 3.2.133 praśaṃsā: with only vartamāne, dviṣ gets no śatṛ from these sūtras."""
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta("02.0003", 1, 1, "pulliṅga", **VT))}
    assert "dvizan" not in got, sorted(got)
