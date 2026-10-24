"""K2 — the kṛtya lists of 3.1.109–126 through the loop from a vivakṣā (krt=kftya): kyap (109, 110, 112, 113, 120) and the ṇyat list (126), each beside the
tavya-anīya readings and as apavāda of yat / ṇyat. Forms are Kāśikā udāharaṇas."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

KRTYA = dict(krt="kftya")

CASES = [   # (dhātu id, form that must be one of the readings, form that must not be)
    ("02.0040", "ityam", "eyam"),            # iR  3.1.109
    ("02.0038", "stutyam", None),      # zwuY
    pytest.param("02.0070", "Sizyam", None, marks=pytest.mark.xfail(reason="ṣatva 8.3.60 does not reach the kṛdanta stem", strict=True)),             # SAsu~ anuśiṣṭau (6.4.34; ṣatva 8.3.60 does not yet reach the kṛdanta stem)
    ("06.0008", "juzyam", None),             # juzI~
    ("05.0008", "vftyam", "vAryam"),         # vfY 3.1.109 (svādi)
    ("01.0862", "vftyam", "vArtyam"),        # vftu~ 3.1.110
    ("01.0863", "vfDyam", "vArDyam"),        # vfDu~
    ("01.1020", "Keyam", None),              # Kanu~ 3.1.111 (Ka-ī + ya → Keya)
    ("01.0866", "karpyam", "kftyam"),        # kfpU~ is barred from 3.1.110 (akxpicfteH); ṇyat vṛddhi of the kḷ-upadha is not modelled (kAlpyam)
    ("03.0006", "BftyaH", None),             # quBfY 3.1.112
    ("02.0061", "mfjyam", None),             # mfjU~ 3.1.113
    ("02.0061", "mArjyam", None),
    ("05.0007", "kftyam", None),             # kfY 3.1.120
    ("05.0007", "kAryam", None),
    ("02.0027", "yAvyam", "yavyam"),         # yu 3.1.126
]


@pytest.mark.parametrize("ref,want,never", CASES, ids=lambda c: None)
def test_kftya_lists(ref, want, never):
    linga = "pulliṅga" if want.endswith("H") else "napuṃsaka"
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, 1, 1, linga, **KRTYA))}
    assert want in got, sorted(got)
    if never:
        assert never not in got, sorted(got)
