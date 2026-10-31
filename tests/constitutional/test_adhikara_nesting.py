"""Art. 24 §3: the adhikāra ranges of the Aṣṭādhyāyī nest/overlap as the Kāśikā-graded table says (owner's diagram: 3.1.1 ⊃ 4.1.1 ⊃ 4.1.76; 4.1.3 overlaps 4.1.76)."""
import json
from pathlib import Path

H = json.loads((Path(__file__).resolve().parents[2] / "data/inputs/adhikara_nesting.json").read_text())["heads"]


def test_taddhita_inside_pratipadika_inside_pratyaya():
    assert H["3.1.1"]["end"] == H["4.1.1"]["end"] == H["4.1.76"]["end"] == "5.4.160"
    assert {"3.1.1", "4.1.1"} <= set(H["4.1.76"]["inside"])


def test_stri_overlaps_taddhita_without_containing_it():
    assert "4.1.76" in H["4.1.3"]["overlaps"] and "4.1.76" not in H["4.1.3"]["contains"]


def test_the_heads_the_kashika_names_are_graded_K():
    assert all(H[h]["grade"] == "K" for h in ("3.1.1", "4.1.1", "4.1.3", "4.1.76"))
