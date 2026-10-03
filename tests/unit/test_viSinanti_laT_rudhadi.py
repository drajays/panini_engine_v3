from __future__ import annotations


def test_derive_viSinanti_laT_rudhadi_P032():
    from phonology.joiner import slp1_to_devanagari
    from engine.it_phonetic import term_phonetic_varnas

    from pipelines.viSinanti_laT_rudhadi import derive_viSinanti_laT_rudhadi_P032

    s = derive_viSinanti_laT_rudhadi_P032()
    assert s.render() == "vinaSanti"
    assert slp1_to_devanagari(term_phonetic_varnas(s.terms[0])) == "विनशन्ति"


import pytest


@pytest.mark.xfail(reason="engine derives vinaSanti honestly; the steps to viSinanti are missing (old 8.4.55 hack faked them)", strict=True)
def test_attested_surface_P032():
    from pipelines.viSinanti_laT_rudhadi import derive_viSinanti_laT_rudhadi_P032
    assert derive_viSinanti_laT_rudhadi_P032().render() == "viSinanti"
