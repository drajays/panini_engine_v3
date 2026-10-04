"""Other gaṇas through the loop: śap-luk (2.4.72) must not be undone by a second 3.1.68; śnam displaces śap; an apit
vikaraṇa that arrives after the tiṅ (śnu, śnā) is kit by 1.2.4 (cinuvaH, not *cenuvaH)."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,lakara,p,v,want", [
    ("dviza~", "laT", 1, 1, "dvezmi"), ("duha~", "laT", 1, 1, "dohmi"), ("ada~", "laT", 1, 1, "admi"),
    ("ciY", "laT", 1, 2, "cinuvaH"), ("ciY", "laT", 3, 1, "cinoti"),
    ("ruDi~r", "laT", 1, 1, "ruRaDmi"), ("BU", "laT", 3, 1, "Bavati"),
])
def test_cell(dhatu, lakara, p, v, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, p, v))), "", dhatu, 250).surface == want


@pytest.mark.parametrize("dhatu,lakara,p,v,want", [        # gaṇa 3 (ślu), 4 (śyan: ñit-ṇit only), 7 (śnam n kept), 8 (u: kit only before m/v)
    ("hu", "laT", 1, 1, "juhomi"), ("hu", "laT", 3, 1, "juhoti"), ("pf", "laT", 1, 1, "piparmi"), ("quBfY", "laT", 1, 1, "biBarmi"),
    ("zRasu~", "laT", 1, 1, "snasyAmi"), ("divu~", "laT", 3, 1, "dIvyati"),
    ("ruDi~r", "laT", 1, 2, "runDvaH"), ("kftI~", "laT", 1, 1, "kfntAmi"),
    ("kziRu~", "laT", 1, 1, "kzeRomi"), ("qukfY", "laT", 1, 2, "kurvaH"), ("qukfY", "laT", 1, 1, "karomi"),
])
def test_other_gana_cells(dhatu, lakara, p, v, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, p, v))), "", dhatu, 250).surface == want


@pytest.mark.parametrize("dhatu,lakara,p,v,want", [        # checked against Vidyut (tools/tri_compare.py)
    ("hana~", "laT", 3, 2, "hataH"), ("hana~", "laT", 3, 3, "Gnanti"), ("hana~", "laT", 2, 2, "haTaH"), ("hana~", "laT", 3, 1, "hanti"),
    ("Riji~r", "laT", 3, 1, "nenekti"), ("o~hAk", "laT", 3, 3, "jahati"), ("o~hAk", "laT", 3, 2, "jahItaH"),
    ("Basa~", "laT", 3, 3, "bapsati"), ("f", "liT", 3, 1, "Ara"),
])
def test_vs_vidyut_gana_2_3(dhatu, lakara, p, v, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, p, v))), "", dhatu, 250).surface == want


@pytest.mark.parametrize("ref,p,v,want", [("JuhotyAdi_03_0017", 3, 1, "iyarti"), ("JuhotyAdi_03_0017", 3, 2, "iyftaH"),
                                          ("JuhotyAdi_03_0007", 3, 1, "mimIte"), ("divAdi_04_0044", 3, 2, "jAyete"),
                                          ("Adadi_02_0009", 2, 1, "Iqize")])
def test_by_row_id(ref, p, v, want):             # an upadeśa repeats across gaṇas: the row id disambiguates
    assert run_autonomously(start_state(NS(kind="tinanta", args=(ref, "laT", p, v))), "", ref, 250).surface == want
