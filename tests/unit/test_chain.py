"""pipelines/chain.py: composing stages gives what the one-shot entry points give, and a kṛdanta stem can feed the taddhita loop."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines import chain
from pipelines.krdanta import derive_krdanta

V = dict(krt="Rvultfc", kala="vartamAna")


def _forms(f):
    return {b.surface_slp1 for b in explore(f)}


def test_krt_then_sup_equals_derive_krdanta():
    assert _forms(lambda: chain.sup(chain.krt("01.0381", **V), 1, 1)) == _forms(lambda: derive_krdanta("01.0381", 1, 1, "pulliṅga", **V))


def test_krt_then_taddhita_then_sup():
    st = chain.taddhita(chain.krt("01.0381", **V), taddhitArtha="Bava")
    assert st.slp1.startswith("pAWak") and st.slp1 != "pAWaka"
    assert _forms(lambda: chain.sup(st, 1, 1)) == {st.slp1 + "H"}


def test_taddhita_loops_on_its_own_output():
    """prātipadika + taddhita = prātipadika: the result of one taddhita is a stem the next taddhita takes (apatya after apatya)."""
    once = chain.taddhita(chain.Stem("upagu"), taddhitArtha="apatya")
    twice = chain.taddhita(once, taddhitArtha="apatya")
    assert once.slp1 != "upagu" and twice.slp1 != once.slp1, (once, twice)
