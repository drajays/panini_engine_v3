from __future__ import annotations


def test_derive_viSinanti_laT_rudhadi_P032():
    from phonology.joiner import slp1_to_devanagari
    from engine.it_phonetic import term_phonetic_varnas

    from pipelines.viSinanti_laT_rudhadi_P032_demo import derive_viSinanti_laT_rudhadi_P032

    s = derive_viSinanti_laT_rudhadi_P032()
    assert s.render() == "viSinanti"
    assert slp1_to_devanagari(term_phonetic_varnas(s.terms[0])) == "विशिनन्ति"
