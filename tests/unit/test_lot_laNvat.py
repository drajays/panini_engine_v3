"""लोटो लङ्वत् (3.4.85): loṭ takes laṅ's *pratyaya*-kārya (3.4.99, 3.4.101) but not its aṅga-kārya (6.4.71 aṭ);
loṭ's own ādeśas win as apavāda (3.4.86 over 3.4.100, 3.4.89 over 3.4.101).

Gold: the user-supplied bhū loṭ prakriyā (भूसत्तायाम्, 2026-10-03) and the Kāśikā text on 3.4.85/99/100/101.
Every cell is derived by the loop — the scheduler and resolver choose the rules, no recipe orders them."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY
from tools.autonomy_report import run_autonomously, start_state

BHU_LOT = {  # (puruṣa, vacana) → SLP1 (the user's reference file, one prakriyā per cell)
    (3, 1): "Bavatu", (3, 2): "BavatAm", (3, 3): "Bavantu",
    (2, 1): "Bava", (2, 2): "Bavatam", (2, 3): "Bavata",
    (1, 1): "BavAni", (1, 2): "BavAva", (1, 3): "BavAma",
}


def _run(dhatu, purusha, vacana, lakara="loT", **kw):
    case = NS(kind="tinanta", args=(dhatu, lakara, purusha, vacana), **kw)
    return run_autonomously(start_state(case), "", dhatu, 150)


@pytest.mark.parametrize("cell,gold", sorted(BHU_LOT.items()))
def test_bhu_lot_cell_derives_by_the_loop(cell, gold):
    assert _run("BU", *cell).surface == gold


def test_laNvat_is_applied_and_aT_is_not():
    run = _run("BU", 2, 2)                      # thas → tam by 3.4.101, reached only through 3.4.85
    ids = [s[0] for s in run.steps]
    assert "3.4.85" in ids and "3.4.101" in ids
    assert ids.index("3.4.85") < ids.index("3.4.101")
    assert not run.surface.startswith("aB")     # 6.4.71 is aṅga-kārya: loṭ gets no aṭ


def test_s_lopa_of_ngit_reaches_loT_vas_mas():
    assert _run("BU", 1, 2).surface == "BavAva" and _run("BU", 1, 3).surface == "BavAma"   # 3.4.99


def test_apavadas_are_declared_not_engineered():
    assert "3.4.100" in SUTRA_REGISTRY["3.4.86"].apavada_of
    assert "3.4.101" in SUTRA_REGISTRY["3.4.89"].apavada_of


def test_lat_does_not_get_laNvat():
    ids = [s[0] for s in _run("BU", 2, 2, "laT").steps]
    assert "3.4.85" not in ids and "3.4.101" not in ids      # laṭ keeps its tiṅ: bhavathaH, not *bhavatam


def test_hi_and_ni_keep_their_i_against_3_4_100():
    assert _run("BU", 2, 1).surface == "Bava"       # hi (3.4.87) then 6.4.105, never itaś ca
    assert _run("BU", 1, 1).surface == "BavAni"     # ni (3.4.89) keeps its i
