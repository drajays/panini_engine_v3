from __future__ import annotations


def test_derive_viSiNQi_loT_rudhadi_P031():
    from phonology.joiner import slp1_to_devanagari
    from engine.it_phonetic import term_phonetic_varnas

    from pipelines.viSiNQi_loT_rudhadi_P031_demo import derive_viSiNQi_loT_rudhadi_P031

    s = derive_viSiNQi_loT_rudhadi_P031()
    assert s.render() == "viSiRQi"
    assert slp1_to_devanagari(term_phonetic_varnas(s.terms[0])) == "विशिण्ढि"
