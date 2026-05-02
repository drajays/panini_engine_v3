from __future__ import annotations


def test_derive_agda_lit_ghas_P033():
    from phonology.joiner import slp1_to_devanagari
    from engine.it_phonetic import term_phonetic_varnas

    from pipelines.agda_lit_ghas_P033_demo import derive_agda_lit_ghas_P033

    s = derive_agda_lit_ghas_P033()
    assert s.render() == "agda"
    assert slp1_to_devanagari(term_phonetic_varnas(s.terms[0])) == "अग्द"
