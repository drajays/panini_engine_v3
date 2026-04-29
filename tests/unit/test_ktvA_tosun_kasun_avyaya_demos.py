from __future__ import annotations

import sutras  # noqa: F401

from pipelines.ktvA_tosun_kasun_avyaya_demos import derive_paThitvA, derive_udetoH


def test_paThitvA_su_luk() -> None:
    s = derive_paThitvA()
    assert s.flat_slp1() == "paThitvA"
    assert "luk_lopa" in s.terms[-1].tags


def test_udetoH_visarga_and_su_luk() -> None:
    s = derive_udetoH()
    assert s.flat_slp1() == "udetoH"
    # final pada has visarga
    assert s.terms[0].varnas[-1].slp1 == "H"

