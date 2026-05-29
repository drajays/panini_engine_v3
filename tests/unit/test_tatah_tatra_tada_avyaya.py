from __future__ import annotations

import sutras  # noqa: F401

from pipelines.tatah_tatra_tada_vina_nana_avyaya_demo import (
    derive_nAnA,
    derive_tadA,
    derive_tataH,
    derive_tatra,
    derive_vinA,
    derive_yadA,
    derive_yataH,
    derive_yatra,
)


def test_tataH_yataH() -> None:
    assert derive_tataH().flat_slp1() == "tataH"
    assert derive_yataH().flat_slp1() == "yataH"


def test_tatra_yatra() -> None:
    assert derive_tatra().flat_slp1() == "tatra"
    assert derive_yatra().flat_slp1() == "yatra"


def test_tadA_yadA() -> None:
    assert derive_tadA().flat_slp1() == "tadA"
    assert derive_yadA().flat_slp1() == "yadA"


def test_vinA_nAnA() -> None:
    assert derive_vinA().flat_slp1() == "vinA"
    assert derive_nAnA().flat_slp1() == "nAnA"

