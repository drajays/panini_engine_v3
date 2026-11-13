"""1.1.40 क्त्वातोसुन्कसुनः + 2.4.82 अव्ययादाप्सुपः: a ktvā-anta kṛdanta is declined into itself in every vibhakti (gatvā, never *gatvāḥ*).
And dudāñ vidhiliṅ: 6.4.112 takes the ā of the abhyasta dā / dhā before the ṅit yāsuṭ — dadyāt, dadhyāt (not *dadāyāt*)."""
import pytest

import sutras  # noqa: F401
from engine.tape_init.krdanta import PURVAKALA_SAMANAKARTRKA
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta
from pipelines.tinanta import derive


@pytest.mark.parametrize("ref,want", [("BvAdi_01_1137", "gatvA"), ("BvAdi_01_0381", "paWitvA")])
@pytest.mark.parametrize("vib,vac", [(1, 1), (2, 3), (3, 2), (6, 1), (7, 1)])
def test_ktva_stays_undeclined(ref, want, vib, vac):
    assert derive_krdanta(ref, vib, vac, "pulliṅga", **PURVAKALA_SAMANAKARTRKA).flat_slp1() == want


@pytest.mark.parametrize("dhatu,want", [("03.0010", "dadyA"), ("03.0011", "daDyA")])
def test_dada_dha_vidhi_ling(dhatu, want):
    got = {b.surface_slp1 for b in explore(lambda: derive(dhatu, "liG", "kartari", 3, 1))}
    assert got == {want + "d", want + "t"}      # 8.4.56 vā: d / t at the pada end
