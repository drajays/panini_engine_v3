"""6.1.6 जक्षित्यादयः षट् (Kāśikā: अभ्यस्तमिति वर्तते): the dhātupāṭha antargaṇa जक्षित्यादिः is abhyasta,
so 7.1.4 gives jhi → ati (जक्षति, जाग्रति, दरिद्रति, चकासति) while an ordinary adādi root keeps 7.1.3 (अदन्ति)."""
import pytest

from pipelines.tinanta import derive


@pytest.mark.parametrize("root,form", [("jakz", "jakzati"), ("cakAs", "cakAsati"),
                                       ("jAgf", "jAgrati"), ("daridrA", "daridrati")])
def test_jakshityadi_jhi_is_ati(root, form):
    assert derive(root, "laT", "kartari", 3, 3).render() == form


@pytest.mark.parametrize("root,form", [("ad", "adanti"), ("yA", "yAnti")])
def test_other_adadi_roots_keep_anti(root, form):
    assert derive(root, "laT", "kartari", 3, 3).render() == form


@pytest.mark.parametrize("root,form", [("jakz", "jakzatu"), ("cakAs", "cakAsatu"), ("jAgf", "jAgratu"),
                                       ("daridrA", "daridratu"), ("ad", "adantu"), ("yA", "yAntu")])
def test_lot_3pl(root, form):
    assert derive(root, "loT", "kartari", 3, 3).render() == form


@pytest.mark.parametrize("root,form", [("jakz", "ajakzuH"), ("cakAs", "acakAsuH"), ("jAgf", "ajAgaruH"),
                                       ("daridrA", "adaridruH"), ("BI", "abiBayuH"), ("hu", "ajuhavuH"),
                                       ("DA", "adaDuH"), ("ad", "Adan"), ("BU", "aBavan")])
def test_lan_3pl_jus_after_abhyasta(root, form):
    """3.4.109 सिजभ्यस्तविदिभ्यश्च: jhi → jus after an abhyasta aṅga; ordinary roots keep 7.1.3."""
    assert derive(root, "laG", "kartari", 3, 3).render() == form
