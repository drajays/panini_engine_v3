"""S21: 6.4.144 नस्तद्धिते for the an-stems, with its prakṛtibhāva exceptions 6.4.145 (ahan), 6.4.167 (an before aṇ), 6.4.168 (y-initial), 6.4.169 (ātman / adhvan before kha)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

CASES = [   # (sense, stem, extra origin tags, a form that must be among the readings, a form that must not)
    ("tasmaiPraBavati", "karman", None, "kArmukam", "kArmaRukam"),      # 5.1.103: the ṭi (an) goes before ukañ
    ("alaMgAmI", "aDvan", None, "aDvanyam", "aDvyam"),                  # 6.4.168: an stays before a y-initial yat
    ("alaMgAmI", "aDvan", None, "aDvanInam", "aDvInam"),                # 6.4.169: an stays before kha
]


@pytest.mark.parametrize("sense,stem,og,want,nowant", CASES, ids=lambda c: None)
def test_an_stems(sense, stem, og, want, nowant):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "napuṃsaka", origin_tags=og, taddhitArtha=sense))}
    assert want in got and nowant not in got, sorted(got)
