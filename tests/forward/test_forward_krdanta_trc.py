from __future__ import annotations

import pytest

import sutras  # noqa: F401

from phonology.joiner import slp1_to_devanagari
from pipelines.krdanta import derive_chetA, derive_tfc_pratipadika, derive_trc


def test_ciY_tfc_stem():
    s = derive_tfc_pratipadika("ciY", udatta_dhatu=False)
    assert s.flat_slp1() == "cetf"


@pytest.mark.parametrize(
    "dhatu_id,expected_slp1,expected_dev",
    [
        ("BvAdi_ciY", "cetA", "चेता"),
        ("BvAdi_nIY", "netA", "नेता"),
        ("BvAdi_zwuY", "stotA", "स्तोता"),
        ("BvAdi_DukfY", "kartA", "कर्ता"),
        ("BvAdi_hfY", "hartA", "हर्ता"),
        ("BvAdi_BU", "BavitA", "भविता"),
        ("divAdi_tF", "taritA", "तरिता"),
    ],
)
def test_trc_nom_sg_surfaces(dhatu_id, expected_slp1, expected_dev):
    s = derive_trc(dhatu_id)
    assert s.terms
    assert s.flat_slp1() == expected_slp1
    assert slp1_to_devanagari(s.terms[0].varnas) == expected_dev


def test_cheta_nom_sg_surface():
    s = derive_chetA()
    assert s.terms
    assert s.flat_slp1() == "cetA"
    assert slp1_to_devanagari(s.terms[0].varnas) == "चेता"


def test_trc_krdanta_it_block_order():
    s = derive_tfc_pratipadika("ciY", udatta_dhatu=False)
    path = [e.get("sutra_id") for e in s.trace if isinstance(e, dict)]
    assert path.index("7.2.10") < path.index("7.2.35")


def test_trc_sew_it_not_blocked_by_7_2_10():
    s = derive_tfc_pratipadika("BU", udatta_dhatu=True)
    path = [e.get("sutra_id") for e in s.trace if isinstance(e, dict)]
    assert path.index("7.2.10") < path.index("7.2.35")
    # iṭ remains in the merged tṛc prātipadika (भो + इतृ्… → भवितृ्…)
    assert s.flat_slp1() == "Bavitf"


def test_trc_subanta_nom_order():
    s = derive_chetA()
    path = [e.get("sutra_id") for e in s.trace if isinstance(e, dict)]
    assert path.index("7.1.94") < path.index("6.4.11")
    assert path.index("6.4.11") < path.index("6.1.66")
    assert path.index("8.2.1") < path.index("8.2.7")
