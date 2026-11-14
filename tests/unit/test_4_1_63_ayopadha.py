"""4.1.63 jāter astrīviṣayād ayopadhāt: a yopadha jāti word (kṣatriya) takes ṭāp, not ṅīṣ; the vārttika's five stay (hayī, gavayī, mukayī, matsyī, manuṣyī) — Kāśikā 4.1.63."""
import pytest

import sutras  # noqa: F401
from pipelines import chain


def _f(stem):
    u = chain.strI(chain.Stem(stem, frozenset({"lex:jAti"})))
    return u.slp1, "4.1.63" in set(u.trace[-1][1])


def test_yopadha_takes_wap_not_ngiz():
    assert _f("kzatriya")[0].endswith("A") and not _f("kzatriya")[1]


@pytest.mark.parametrize("stem,want", [("kukkuwa", "kukkuwI"), ("haya", "hayI"), ("gavaya", "gavayI"), ("matsya", "matsyI"), ("manuzya", "manuzyI")])
def test_ngiz_stays(stem, want):
    assert _f(stem) == (want, True)
