"""8.4.64 halo yamAM yami lopaH and 8.4.65 Jaro Jari savarRe: optional drop of the middle letter of a cluster (cucyate beside cucyyate)."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.tinanta import derive


def _r(dhatu):
    return {b.surface_slp1: {t["sutra_id"] for t in b.state.trace if t.get("status") == "APPLIED"} for b in explore(lambda: derive(dhatu, "laT", "karmani", 3, 1))}


def test_yam_before_savarna_yam_8_4_64():
    for d, kept, dropped in (("01.0591", "cucyyate", "cucyate"), ("01.0585", "mavyyate", "mavyate"), ("01.0592", "haryyate", "haryate")):
        r = _r(d)
        assert kept in r and dropped in r and "8.4.64" in r[dropped] and "8.4.64" not in r[kept]


def test_agnyA_keeps_its_n():
    # n and y are not savarna: 8.4.64 must not touch a cluster of two different yam
    from engine.state import State
    from phonology import mk
    import sutras.adhyaya_8.pada_4.sutra_8_4_64 as m
    from engine.state import Term
    t = Term(kind="prakriti", varnas=[mk(c) for c in "agnyA"], tags=set(), meta={})
    s = State(terms=[t], meta={}, trace=[])
    s.tripadi_zone = True
    assert not m.cond(s)


def test_jhar_before_savarna_jhar_8_4_65():
    from engine.state import State
    from phonology import mk
    import sutras.adhyaya_8.pada_4.sutra_8_4_65 as m
    from engine.state import Term
    t = Term(kind="prakriti", varnas=[mk(c) for c in "kfntTa"], tags=set(), meta={})
    s = State(terms=[t], meta={}, trace=[])
    s.tripadi_zone = True
    assert m.cond(s)
    m.act(s)
    assert "".join(v.slp1 for v in t.varnas) == "kfnTa"
