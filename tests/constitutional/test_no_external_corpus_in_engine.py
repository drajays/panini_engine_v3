"""Second-opinion corpora (Krishnan-Kulkarni-Huet DCS/Heritage, Subhastini data) are learning aids only: no engine code may read them."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
BANNED = re.compile(r"data_krishnan|_dcs_sh|alignment_3_normalized|subhastini", re.I)


def test_engine_never_reads_second_opinion_data():
    bad = [str(p.relative_to(ROOT)) for d in ("engine", "pipelines", "sutras", "data")
           if (ROOT / d).is_dir() for p in (ROOT / d).rglob("*.py") if BANNED.search(p.read_text(errors="ignore"))]
    assert not bad, bad
