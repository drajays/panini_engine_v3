"""7.2.103 – 105: kim → ka / ku / kva before a vibhakti — a sup, or a taddhita pratyaya of 5.3.1's scope (Kāśikā 7.2.103 kaḥ, 7.2.104 kutaḥ kutra (t / h initial), 7.2.105 kva)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive as derive_subanta
from pipelines.taddhita_loop import derive_taddhita

TADDHITA = [   # (sense, a form that must be among the readings, the one that must not)
    ("paYcamIvib", "kutaH", "kyataH"),        # 5.3.7 tasil: 7.2.104 (t-initial) beats 7.2.103 and 7.2.102
    ("saptamIvib", "kutra", "kyatra"),        # 5.3.10 tral
    ("kAle", "kadA", "kyadA"),                # 5.3.15 dā: 7.2.103
    ("prakAravacana", "kaTam", "kyaTam"),     # 5.3.24 thamu
]


@pytest.mark.parametrize("sense,want,never", TADDHITA)
def test_taddhita_vibhakti(sense, want, never):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("kim", 1, 1, "napuṃsaka", taddhitArtha=sense))}
    assert want in got and never not in got, sorted(got)


def test_sup_kim_unchanged():
    for vac, want in ((1, "kaH"), (2, "kO")):
        got = {b.surface_slp1 for b in explore(lambda: derive_subanta("kim", 1, vac, "puṃliṅga"))}
        assert want in got, (vac, sorted(got))
