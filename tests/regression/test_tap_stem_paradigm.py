"""S2: a stem that gets its ṭāp by 4.1.4 (aja + ṭāp) declines exactly as the lexicon ā-stem (khaṭvā): the ṭāp's ekādeśa (6.1.101) is taken
inside the aṅga, so 7.3.105 / 7.3.106 / 7.3.113 and the ā-stem sup rules see an ā-final aṅga."""
import pytest

import sutras  # noqa: F401
from pipelines.subanta import derive

CELLS = [(v, c) for v in range(1, 9) for c in (1, 2, 3)]


@pytest.mark.parametrize("vib,vac", CELLS)
def test_tap_stem_declines_like_the_a_stem(vib, vac):
    got = derive("aja", vib, vac, "strīliṅga").flat_slp1()
    want = derive("KawvA", vib, vac, "strīliṅga").flat_slp1()
    assert got == "aj" + want[len("Kawv"):], (got, want)
