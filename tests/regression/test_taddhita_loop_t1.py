"""T1 — the taddhita in the loop (apatya): 4.1.92 opens the frame (vivakṣā taddhitArtha=apatya); 4.1.83 aṇ is the general pratyaya and the
special ones (4.1.84 aṇ, 85 ṇya, 86 añ, 95 iñ, 96 iñ, 101 phak, 104 añ, 105 yañ, 112 aṇ, 138 gha) are its apavādas by declaration. The loop
does it-lopa, vṛddhi (7.2.117), bha (1.4.18), a/i-lopa (6.4.148), guṇa of the u (6.4.146) and 7.1.2 by itself. Kāśikā / Laghukaumudī udāharaṇas."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

A = dict(taddhitArtha="apatya")
G = dict(taddhitArtha="apatya", apatyaBeda="gotra")
CASES = [   # (stem, origin tags, vivakṣā, form that must be one of the readings)
    ("upagu", None, A, "OpagavaH"),            # औपगवः (4.1.83 aṇ; u → o before the taddhita, 6.4.146)
    ("dakza", None, A, "dAkziH"),              # दाक्षिः (4.1.95 iñ, the apavāda of aṇ)
    ("garga", None, A, "gArgiH"),              # anantara apatya: iñ
    ("garga", None, G, "gArgyaH"),             # गार्ग्यः (4.1.105 yañ, gotra)
    ("bAhu", None, A, "bAhaviH"),              # बाहविः (4.1.96)
    ("Siva", None, A, "SEvaH"),                # शैवः (4.1.112)
    ("diti", None, A, "dEtyaH"),               # दैत्यः (4.1.85 ṇya)
    ("utsa", None, A, "OtsaH"),                # औत्सः (4.1.86 añ)
    ("aSvapati", None, A, "ASvapataH"),        # आश्वपतः (4.1.84 aṇ, not ṇya)
    ("prajApati", None, A, "prAjApatyaH"),     # patyuttarapada: ṇya
    ("kzatra", None, A, "kzatriyaH"),          # क्षत्रियः (4.1.138 gha → iya)
    ("bida", None, G, "bEdaH"),                # बैदः (4.1.104 añ)
    ("gArgya", {"origin_pratyaya:yaY"}, A, "gArgyAyaRaH"),    # गार्ग्यायणः (4.1.101 phak: the yuvan)
    ("dAkzi", {"origin_pratyaya:iY"}, A, "dAkzAyaRaH"),       # दाक्षायणः
]


@pytest.mark.parametrize("stem,og,kw,want", CASES, ids=lambda c: None)
def test_apatya(stem, og, kw, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "pulliṅga", origin_tags=og, **kw))}
    assert want in got, sorted(got)


def test_apavada_takes_the_site_from_an():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("dakza", 1, 1, "pulliṅga", **A))}
    assert not any(w.startswith("dAkzaH") for w in got), sorted(got)       # aṇ (dākṣaḥ) must not be a reading: iñ is the apavāda
