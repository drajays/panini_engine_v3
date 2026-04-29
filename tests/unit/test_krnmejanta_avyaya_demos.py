from __future__ import annotations

import sutras  # noqa: F401

from pipelines.krnmejanta_avyaya_demos import derive_svAdu_kAraM, derive_vakSe


def test_svAdu_kAraM_su_luk_tail() -> None:
    s = derive_svAdu_kAraM()
    assert s.flat_slp1() == "svAdukAram"
    assert "luk_lopa" in s.terms[-1].tags  # su ghost


def test_vakSe_su_luk_tail() -> None:
    s = derive_vakSe()
    assert s.flat_slp1() == "vakse"
    assert "luk_lopa" in s.terms[-1].tags

