"""8.3.17 / 8.3.18 / 8.3.19 / 8.3.20 / 8.3.22 on two padas side by side (Kāśikā 8.3.17-22: भो अत्र / भोयत्र, भो जनाः, देवा गच्छन्ति, क आस्ते / कयास्ते)."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.pada_samhita import join_tripadi


def _seam(left, right):
    return {" ".join("".join(v.slp1 for v in t.varnas) for t in b.state.terms) for b in explore(lambda: join_tripadi(left, right))}


def test_bho_before_haS_loses_the_y_always():                 # 8.3.17 then 8.3.22
    assert _seam("Bos", "janAH") == {"Bo janAH"}
    assert _seam("Bagos", "devAH") == {"Bago devAH"}
    assert _seam("aGos", "rAkzasAH") == {"aGo rAkzasAH"}
    assert _seam("Bos", "hasati") == {"Bo hasati"}


def test_bho_before_a_vowel_two_readings():                   # 8.3.20 drops the plain y; 8.3.18's lighter y stays
    assert _seam("Bos", "atra") == {"Bo atra", "Boy atra"}


def test_avarna_then_ru_before_haS():                         # देवास् गच्छन्ति → देवा गच्छन्ति
    assert _seam("devAs", "gacCanti") == {"devA gacCanti"}


def test_avarna_y_before_a_vowel_is_optional():               # 8.3.19 शाकल्य
    assert _seam("kas", "Asta") == {"ka Asta", "kay Asta"}


def test_other_ru_is_not_touched():                           # not bho/avarṇa: अग्निर् अत्र, and 8.3.15 before a khar
    assert _seam("agnis", "atra") == {"agnir atra"}
    assert _seam("vfkzas", "tarati") == {"vfkzas tarati"}       # 8.3.34 visarga → s before t
    assert _seam("vfkzas", "karoti") == {"vfkzaH karoti", "vfkzaZ karoti"}       # k stays ḥ (8.3.37)


def test_8_3_22_takes_the_y_only_not_the_v():
    """Vasu on 8.3.22: aśi qualifies hali, so वृक्षव् करोति keeps its v (k is not an aś); 8.3.22 names y alone."""
    assert _seam("vfkzav", "karoti") == {"vfkzav karoti"}
