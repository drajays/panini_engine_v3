"""K8 — the strī pratyaya of the kṛdantas, one per kṛt: 4.1.15 (ṭit / aṇ / añ … → ṅīp, the apavāda of ṭāp), 4.1.4 ṭāp otherwise, 4.1.6 ugit → ṅīp
(ktavatu: ktavat, Śatṛ), 4.1.5 (tṛc)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

CASES = [   # (dhātu id, vibhakti, vacana, derive_krdanta kwargs, form that must be one of the readings)
    ("qukfY", 1, 1, dict(upapada=("kumBa", "karman")), "kumBakArI"),     # aṇ (4.1.15, not ṭāp)
    ("qukfY", 3, 1, dict(upapada=("kumBa", "karman")), "kumBakAryA"),
    ("lUY", 1, 1, dict(upapada=("kARqa", "karman")), "kARqalAvI"),
    ("qudAY", 1, 1, dict(upapada=("go", "karman")), "godA"),            # ka is no ṭit: ṭāp
    ("qudAY", 3, 1, dict(upapada=("go", "karman")), "godayA"),
    ("01.0001", 1, 1, dict(kala="BUta", artha="kartf"), "BUtavatI"),    # ktavatu: ugit
    ("01.0381", 1, 1, dict(kala="BUta", artha="kartf"), "paWitavatI"),
    ("01.0001", 1, 1, dict(kala="BUta", artha="karman"), "BUtA"),       # kta: ṭāp
    ("01.0381", 3, 1, dict(kala="BUta", artha="karman"), "paWitayA"),
    ("01.0001", 1, 1, dict(krt="kftya"), "BavanIyA"),                   # anīyar: ṭāp
]


@pytest.mark.parametrize("ref,vib,vac,kw,want", CASES, ids=lambda c: None)
def test_krdanta_feminine(ref, vib, vac, kw, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, vib, vac, "strīliṅga", **kw))}
    assert want in got, sorted(got)
    assert not any(w.endswith("kArA") for w in got if w.startswith("kumBa")), sorted(got)     # ṭāp must not beat 4.1.15
