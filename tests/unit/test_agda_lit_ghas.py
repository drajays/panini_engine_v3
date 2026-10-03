from __future__ import annotations


def test_derive_agda_lit_ghas_P033():
    from phonology.joiner import slp1_to_devanagari
    from engine.it_phonetic import term_phonetic_varnas

    from pipelines.agda_lit_ghas import derive_agda_lit_ghas_P033

    s = derive_agda_lit_ghas_P033()
    assert s.render() == "gda"
    assert slp1_to_devanagari(term_phonetic_varnas(s.terms[0])) == "ग्द"


import pytest


@pytest.mark.xfail(reason="engine derives gda honestly; the aṭ/2.4.40 steps to agda are not modelled (old 8.4.55 hack faked them)", strict=True)
def test_attested_surface_P033():
    from pipelines.agda_lit_ghas import derive_agda_lit_ghas_P033
    assert derive_agda_lit_ghas_P033().render() == "agda"
