"""Gold tests for kṛ liṭ karmaṇi and bhāve ātmanepada — full 9-cell.

kṛ liṭ karmaṇi/bhāve has no strong arm (all ātmanepada, uniform weak).
6.1.77 yaṇ sandhi fires at root kṛ (ṛ-final) + vowel-initial suffix/iṭ
boundary: ṛ→r.  7.4.66 urat converts abhyāsa ṛ→ā (then 7.4.59 ā→a,
8.4.54 k→c) → abhyāsa 'ca'.

3sg and 1sg share 'e' ādeśa: ca+kr+e = cakre.
3du: ca+kr+āte = cakrāte, 3pl (ire, iṭ): ca+kr+ire = cakrire.
"""
from __future__ import annotations

import pytest
import sutras  # noqa: F401
from pipelines.tinanta import derive


_KF_LIT_KARMANI = {
    (3, 1): "cakre",      # eS: ca+kr+e
    (3, 2): "cakrAte",    # Ate: ca+kr+āte
    (3, 3): "cakrire",    # irec: ca+kr+ire (iṭ+re)
    (2, 1): "cakrize",    # iṭ+se → ṣe (8.3.59 ṣatvam)
    (2, 2): "cakrATe",    # ATe: ca+kr+āthe
    (2, 3): "cakriDve",   # iṭ+dhve (8.3.78 dh→ḍh)
    (1, 1): "cakre",      # same as 3sg
    (1, 2): "cakrivahe",  # iṭ+vahe
    (1, 3): "cakrimahe",  # iṭ+mahe
}

# bhāve liṭ uses the same forms as karmaṇi (no yaḳ difference for kṛ here)
_KF_LIT_BHAVE = dict(_KF_LIT_KARMANI)


@pytest.mark.parametrize("purusha,vacana,expected", [
    (p, v, exp) for (p, v), exp in _KF_LIT_KARMANI.items()
])
def test_kf_lit_karmani_surface(purusha: int, vacana: int, expected: str) -> None:
    s = derive("kf", "liT", "karmani", purusha, vacana)
    assert s.flat_slp1() == expected


@pytest.mark.parametrize("purusha,vacana,expected", [
    (p, v, exp) for (p, v), exp in _KF_LIT_BHAVE.items()
])
def test_kf_lit_bhave_surface(purusha: int, vacana: int, expected: str) -> None:
    s = derive("kf", "liT", "bhave", purusha, vacana)
    assert s.flat_slp1() == expected
