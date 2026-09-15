"""Gold tests for kṛ (qukfY, tanādi gana 8) liṭ kartari parasmaipada — full 9-cell.

Strong arm (Ral / Nal ādeśa, 3sg and 1sg):
  kṛ → dvitva (6.1.8) → 7.3.84 guṇa (ṛ→a) → 1.1.51 rapara (→ar)
  → 7.2.116 vṛddhi of a-upadha (→ār) → 7.4.66 abhyāsa ṛ→ā
  → 7.4.59 hrasva (ā→a) → 8.4.54 carc (k→c) → cakāra.

Weak arm no-iṭ forms (ṛ-final root + vowel suffix):
  6.1.77 yaṇ sandhi fires at root+suffix boundary: ṛ→r → cakratuH/cakruH/cakra.

Weak arm iṭ forms (ṛ + iṭ 'i'):
  6.1.77 fires at root kṛ + iṭ boundary: ṛ→r → cakriTa/cakriva/cakrima.
"""
from __future__ import annotations

import pytest
import sutras  # noqa: F401
from pipelines.tinanta import derive


def _fired(trace: list, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


# Full 9-cell gold table — SLP1 surface forms
_KF_LIT_KARTARI_PARASMAI = {
    (3, 1): "cakAra",    # Nal strong: guṇa+rapara+vṛddhi → cakāra
    (3, 2): "cakratuH",  # atuH: 6.1.77 ṛ→r
    (3, 3): "cakruH",    # uH: 6.1.77 ṛ→r
    (2, 1): "cakriTa",   # iṭ+TaL: 6.1.77 ṛ+i→r; cakritha
    (2, 2): "cakraTuH",  # aTuH: 6.1.77 ṛ→r
    (2, 3): "cakra",     # a: 6.1.77 ṛ→r
    (1, 1): "cakAra",    # Nal strong (same as 3sg)
    (1, 2): "cakriva",   # iṭ+va: 6.1.77 ṛ+i→r; cakriva
    (1, 3): "cakrima",   # iṭ+ma: 6.1.77 ṛ+i→r; cakrima
}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (p, v, exp) for (p, v), exp in _KF_LIT_KARTARI_PARASMAI.items()
])
def test_kf_lit_kartari_surface(purusha: int, vacana: int, expected: str) -> None:
    s = derive("kf", "liT", "kartari", purusha, vacana, pada="parasmai")
    assert s.flat_slp1() == expected


def test_cakAra_spine() -> None:
    s = derive("kf", "liT", "kartari", 3, 1, pada="parasmai")
    for sid in ("3.2.115", "6.1.8", "8.4.54", "7.3.84", "1.1.51", "7.2.116", "7.4.66", "7.4.59"):
        assert _fired(s.trace, sid), f"missing trace for {sid}"


def test_cakratuH_6_1_77_fires() -> None:
    s = derive("kf", "liT", "kartari", 3, 2, pada="parasmai")
    assert _fired(s.trace, "6.1.77"), "6.1.77 must fire for weak ṛ+vowel boundary"
