"""ātmanepada liṅ through the loop: 3.4.102 sīyuṭ read off the tape (not a recipe flag), 7.2.79 s-lopa only before
sārvadhātuka, 7.2.35 one iṭ per affix (sīyuṭ + tiṅ). Parasmaipada keeps yāsuṭ."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,lakara,p,v,want", [
    ("eDa~", "liG", 1, 1, "eDeya"), ("eDa~", "liG", 3, 1, "eDeta"), ("eDa~", "liG", 3, 3, "eDeran"),
    ("eDa~", "AsIrliG", 1, 1, "eDizIya"), ("eDa~", "AsIrliG", 1, 2, "eDizIvahi"), ("eDa~", "AsIrliG", 3, 3, "eDizIran"),
    ("BU", "liG", 2, 3, "Baveta"), ("BU", "AsIrliG", 2, 3, "BUyAsta"),
])
def test_liG_cell(dhatu, lakara, p, v, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, p, v))), "", dhatu, 250).surface == want


@pytest.mark.parametrize("dhatu,lakara,p,v,want", [        # 3.4.107 suṭ (ātmanepada); its s goes in vidhi-liṅ (7.2.79), stays in āśīr
    ("eDa~", "liG", 3, 1, "eDeta"), ("eDa~", "liG", 2, 1, "eDeTAH"), ("eDa~", "liG", 3, 2, "eDeyAtAm"),
    ("eDa~", "AsIrliG", 3, 1, "eDizIzwa"), ("eDa~", "AsIrliG", 2, 1, "eDizIzWAH"), ("eDa~", "AsIrliG", 3, 2, "eDizIyAstAm"),
])
def test_suT_atmane(dhatu, lakara, p, v, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, p, v))), "", dhatu, 250).surface == want


@pytest.mark.parametrize("dhatu,lakara,p,v,want", [        # iṭ undoes the jhal-kit of 1.2.11 (muda~: modizi); ṣīdhvam/liṭ dhvam → ḍhvam (8.3.78)
    ("muda~", "luG", 1, 1, "amodizi"), ("muda~", "AsIrliG", 1, 2, "modizIvahi"), ("muda~", "AsIrliG", 3, 1, "modizIzwa"),
    ("eDa~", "AsIrliG", 2, 3, "eDizIQvam"), ("eDa~", "liG", 2, 3, "eDeDvam"), ("eDa~", "liT", 2, 3, "eDAYcakfQve"),
    ("eDa~", "luG", 2, 3, "EDiDvam"),
])
def test_it_kit_and_dhvam(dhatu, lakara, p, v, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, p, v))), "", dhatu, 250).surface == want
