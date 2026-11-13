"""व्युत्पत्तिः (core/vyutpatti.py): kośa text → proposals; Kāśikā / uṇādi citations; the search box."""
from __future__ import annotations

import pytest

from core import abhyasa as A
from core import vyutpatti as V

BHARATI = "(स्त्री) गर्गस्य वंशजा स्त्री । गर्ग+यञ्+ङीप् । ‘गर्गादिभ्यो यञ्’ ४.१.१०५,‘यञ्श्च’ ४.१.१६,‘ततो हलस्तद्धितस्य’ ६.४.१५० यलोपः"
SKD_GARGA = "गर्गः, पुं, (गृणाति वेदध्वनिना शब्दायते स्तौति इत्यर्थः । गॄ गि शब्दे + “मुदिग्रोर्गग्गौ ।” उणां । १ । १२७ । इति गः ।)"


@pytest.fixture(autouse=True)
def _inventory(monkeypatch):
    """The pratyaya inventory without a Vidyut worker: the few this test needs."""
    inv = {"yaY": "taddhita", "aR": "taddhita", "iY": "taddhita", "lyuw": "krt", "tfc": "krt", "NIp": "stri", "ga": "unadi"}
    monkeypatch.setattr(V, "_pratyayas", lambda: inv)


def test_formula_and_sutra_numbers_from_a_kosha_entry():
    p = V._parse(BHARATI)
    assert {"base_dev": "गर्ग", "pratyayas": ["yaY", "NIp"]} in p["formulas"]
    assert [s["id"] for s in p["sutras"]] == ["4.1.105", "4.1.16", "6.4.150"]
    assert all(s["text"] for s in p["sutras"])


def test_unadi_quote_and_dhatu_with_its_artha():
    p = V._parse(SKD_GARGA)
    un = [s for s in p["sutras"] if s["kind"] == "unadi"]
    assert un and un[0]["text"] == "मुदिग्रोर्गग्गौ"            # matched by its text, not the SK number (1.127 ≠ 1.125)
    assert "ga" in p["iti"]
    assert any(d["dev"] == "गॄ" and "शब्दे" in d["artha"] for d in p["dhatus"])


def test_kashika_cites_gargi_under_its_making_sutras():
    if not V._kashika():
        pytest.skip("docs/data/sutras.json not built")
    ids = {k["id"] for k in V._kashika_hits("गार्गी", [])}
    assert {"4.1.16", "6.4.150"} <= ids


def test_unadi_examples_name_garga():
    if not V._unadi():
        pytest.skip("uṇādi pāṭha missing")
    assert any(u["text"] == "मुदिग्रोर्गग्गौ" for u in V._unadi_hits("गर्ग", ["गर्गः"]))


def test_guess_bases_undoes_adi_vrddhi():
    assert "garga" in V._guess_bases("gArgI")


def test_search_finds_the_word_a_form_belongs_to():
    if not A.corpus():
        pytest.skip("ashtadhyayi.com shabda corpus not fetched")
    r = A.search("रामस्य")
    assert any(f["stem"] == "rAma" and f["cell"] == "षष्ठी एकवचनम्" for f in r["form_of"])
    assert r["stem"] == "rAma" and r["linga"] == "pulliṅga"


def test_search_any_new_stem_gets_a_linga():
    r = A.search("गार्गी")
    assert r["stem"] == "gArgI" and r["linga"] == "strīliṅga"
