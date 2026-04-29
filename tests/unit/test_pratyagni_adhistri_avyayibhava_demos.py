from __future__ import annotations

import sutras  # noqa: F401

from pipelines.pratyagni_adhistri_avyayibhava_demos import derive_adhistri, derive_pratyagni


def test_pratyagni() -> None:
    s = derive_pratyagni()
    assert s.flat_slp1() == "pratyagni"


def test_adhistri() -> None:
    s = derive_adhistri()
    assert s.flat_slp1() == "adhistri"

