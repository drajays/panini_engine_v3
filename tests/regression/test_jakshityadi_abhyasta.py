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
