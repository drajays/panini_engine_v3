"""Samāsa machine slice 2 (docs/SAMASA_MACHINE.md): the vākya (stem + sup per member) → compound by the 2.1.x / 2.2.x sūtras → 2.4.71 → 2.4.17 / 2.4.18 / 2.4.26
→ sup; the seam reaches 5.4.69, 6.3.46 and 8.4.12 as tags. Kāśikā forms cited in each sūtra file."""
import pytest

import sutras  # noqa: F401
from pipelines import chain


def _forms(members, cells, **viv):
    st = chain.samasa(members, **viv)
    return st, [chain.sup(st, v, c).flat_slp1() for v, c in cells]


def _fired(st):
    return set(st.trace[-1][1])


@pytest.mark.parametrize("members,cells,expect,vidhi", [
    ([("rAjan", 6, 1), ("puruza", 1, 1)], [(1, 1), (1, 3), (3, 1)], ["rAjapuruzaH", "rAjapuruzAH", "rAjapuruzeRa"], "2.2.8"),           # 8.2.7 at the seam
    ([("kfzRa", 2, 1), ("Srita", 1, 1)], [(1, 1)], ["kfzRaSritaH"], "2.1.24"),
    ([("vfka", 5, 2), ("Baya", 1, 1)], [(1, 1)], ["vfkaBayaH"], "2.1.37"),
    ([("akza", 7, 2), ("SORqa", 1, 1)], [(1, 1)], ["akzaSORqaH"], "2.1.40"),
    ([("nIla", 1, 1, {"lex:viSezaRa"}), ("utpala", 1, 1)], [(1, 1), (1, 2)], ["nIlotpalaH", "nIlotpalO"], "2.1.57"),                      # 6.1.87 across the seam
])
def test_tatpurusha_members(members, cells, expect, vidhi):
    st, got = _forms(members, cells)
    assert got == expect
    assert vidhi in _fired(st) and "2.4.71" in _fired(st)


def test_2_1_36_tadartha_and_2_1_37_not_taken_for_each_other():
    with pytest.raises(ValueError):
        chain.samasa([("vfka", 4, 1), ("Baya", 1, 1)])             # Baya needs paYcamI (2.1.37), not caturthI


def test_maharzi_raparatva_across_the_seam():
    st, got = _forms([("mahat", 1, 1, {"lex:viSezaRa"}), ("fzi", 1, 1)], [(1, 1), (1, 3)])
    assert got == ["maharziH", "maharzayaH"]                          # 6.3.46 mahat -> mahA, 6.1.87 A + f -> ar (1.1.51)
    assert "6.3.46" in {s["sutra_id"] for s in chain.sup(st, 1, 1).trace if s.get("status") == "APPLIED"}


def test_5_4_69_surAjA_through_the_machine():
    st, got = _forms([("su", 1, 1, {"lex:pUjana"}), ("rAjan", 1, 1)], [(1, 1), (3, 1)])
    assert got == ["surAjA", "surAjYA"]
    assert "2.2.18" in _fired(st)
    tr = {s["sutra_id"]: s["status"] for s in chain.sup(st, 1, 1).trace if s.get("sutra_id") in ("5.4.69", "5.4.91")}
    assert "5.4.91" not in tr or tr["5.4.91"] != "APPLIED"


def test_8_4_12_vibhakti_and_num_natva():
    st, got = _forms([("kzIra", 6, 1), ("pa", 1, 1)], [(1, 1), (3, 1), (6, 3)])
    assert got == ["kzIrapaH", "kzIrapeRa", "kzIrapARAm"]
    st = chain.samasa([("kzIra", 6, 1), ("pa", 1, 1, set(), "napuṃsaka")])
    assert chain.sup(st, 1, 3).flat_slp1() == "kzIrapARi"             # nuM, then dIrGa: kzIrapa + n + i -> kzIrapARi (Kasika 8.4.12)


def test_dvandva_cArTa_needs_the_vivaksha():
    st, got = _forms([("Darma", 1, 1), ("arTa", 1, 1)], [(1, 2), (1, 3)], arthaViSeSa="cArTa")
    assert got == ["DarmArTO", "DarmArTAH"] and "2.2.29" in _fired(st)
    with pytest.raises(ValueError):                                    # no cArTa: nothing makes a compound
        chain.samasa([("Darma", 1, 1), ("arTa", 1, 1)])


def test_dvigu_neuter_and_strI():
    st, got = _forms([("paYcan", 1, 3, {"lex:saNKyA"}), ("pUla", 1, 3)], [(1, 1)], arthaViSeSa="samAhAra")
    assert got == ["paYcapUlam"] and {"2.1.51", "2.1.52", "2.4.17"} <= _fired(st)
    u = chain.strI(st)                                                 # 4.1.21 dvigoH: pañcapūlī
    assert chain.sup(u, 1, 1).flat_slp1() == "paYcapUlI"


def test_avyayibhava_is_neuter():
    st, got = _forms([("upa", 1, 1, {"avyaya"}), ("kumBa", 6, 1)], [(1, 1)], arthaViSeSa="samIpa")
    assert got == ["upakumBam"] and {"2.1.6", "2.4.18"} <= _fired(st)
