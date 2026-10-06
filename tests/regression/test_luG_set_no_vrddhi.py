"""7.2.4 neṭi: a seṭ root's sic has its iṭ first (7.2.35), so no vṛddhi (7.2.3). Guards the 7.2.35→7.2.3 ordering."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,want", [("vana~", "avanizam"), ("yama~", "ayaMsizam"), ("pac", "apAkzam")])
def test_luG_1sg(dhatu, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, "luG", 1, 1))), "", dhatu, 250).surface == want


@pytest.mark.parametrize("dhatu,want", [("ata~", "AtIH"), ("citI~", "acetIH")])
def test_luG_2sg_seT_Iw(dhatu, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, "luG", 2, 1))), "", dhatu, 250).surface == want
