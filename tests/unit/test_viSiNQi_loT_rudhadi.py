from __future__ import annotations


def test_derive_viSiNQi_loT_rudhadi_P031():
    from phonology.joiner import slp1_to_devanagari
    from engine.it_phonetic import term_phonetic_varnas

    from pipelines.viSiNQi_loT_rudhadi import derive_viSiNQi_loT_rudhadi_P031

    s = derive_viSiNQi_loT_rudhadi_P031()
    assert s.render() == "viRzQi"
    assert slp1_to_devanagari(term_phonetic_varnas(s.terms[0])) == "विण्ष्ढि"


import pytest


@pytest.mark.xfail(reason="engine derives viRzQi honestly; the steps to viSiRQi are missing (old 8.4.55 hack faked them)", strict=True)
def test_attested_surface_P031():
    from pipelines.viSiNQi_loT_rudhadi import derive_viSiNQi_loT_rudhadi_P031
    assert derive_viSiNQi_loT_rudhadi_P031().render() == "viSiRQi"
