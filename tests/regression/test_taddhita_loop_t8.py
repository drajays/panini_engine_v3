"""T8 — taddhita luk / lup (1.1.60–63, 1.2.49, 1.2.51, 1.2.53; 4.3.163, 166–168; 4.4.24, 79): the pratyaya is taken away by luk or lup (engine.luk), stays as a
zero-width ghost, and no aṅgakārya is done on its account (1.1.63)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

TREE = {"lex:vfkza"}
PHALA = dict(taddhitArtha="avayava", vikAraBeda="Pala")
# (stem, origin tags, linga, vivakṣā, stem_linga, the readings that must all be there)
CASES = [
    ("bilva", TREE, "napuṃsaka", PHALA, None, {"bilvam"}),                          # 4.3.163 luk; no vṛddhi (1.1.63)
    ("badarI", TREE | {"origin_pratyaya:NIz"}, "napuṃsaka", PHALA, None, {"badaram"}),      # + 1.2.49 the ṅīṣ goes too
    ("AmalakI", TREE | {"origin_pratyaya:NIz"}, "napuṃsaka", PHALA, None, {"Amalakam"}),
    ("jambU", TREE | {"origin_pratyaya:UN"}, "napuṃsaka", PHALA, "strīliṅga", {"jAmbavam", "jambUH", "jambu"}),   # 4.3.165 aṇ / 166 lup (1.2.51 strī) / luk + 1.2.49
    ("jambU", TREE | {"origin_pratyaya:UN"}, "napuṃsaka", dict(PHALA, arthaViSeSa="saMjYA"), "strīliṅga", {"jambU"}),   # 1.2.53: a name — no yuktavad
    ("harItakI", TREE, "napuṃsaka", PHALA, "strīliṅga", {"harItakI"}),                  # 4.3.167 lup, strī by 1.2.51
    ("plakza", TREE, "napuṃsaka", PHALA, None, {"plAkzam"}),                               # 4.3.164 keeps the aṇ
    ("kaMsIya", {"origin_pratyaya:Ca"}, "pulliṅga", dict(taddhitArtha="vikAra"), None, {"kAMsyaH"}),     # 4.3.168
    ("parSavya", {"origin_pratyaya:yat"}, "pulliṅga", dict(taddhitArtha="vikAra"), None, {"pArSavaH"}),
    ("lavaRa", None, "pulliṅga", dict(taddhitArtha="saMsfzwa"), None, {"lavaRaH"}),          # 4.4.24
    ("lavaRa", None, "strīliṅga", dict(taddhitArtha="saMsfzwa"), None, {"lavaRA"}),          # lumat ṭhak: ṭāp, not ṅīp
    ("ekaDurA", {"origin_pratyaya:wAp"}, "pulliṅga", dict(taddhitArtha="vahati"), None, {"ekaDurIRaH", "ekaDuraH"}),   # 4.4.79
]


@pytest.mark.parametrize("stem,og,linga,viv,sl,want", CASES, ids=lambda c: None)
def test_luk(stem, og, linga, viv, sl, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, linga, origin_tags=og, stem_linga=sl, **viv))}
    assert want <= got, sorted(got)


def test_no_luk_without_the_fruit_meaning():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("bilva", 1, 1, "pulliṅga", origin_tags=TREE, taddhitArtha="avayava"))}
    assert "bElvaH" in got and not any(g.startswith("bilva") for g in got)


def test_the_ghost_is_named_and_empty():
    from engine.luk import lopa_kind
    from engine.tape_init.taddhita import build_taddhita_state
    from tools.autonomy_report import run_autonomously

    s = build_taddhita_state("bilva", TREE, **PHALA)
    s.phase = "upadesha"
    st = run_autonomously(s, "", "bilva", 300, stop_before_tripadi=True).state
    ghost = st.terms[-1]
    assert lopa_kind(ghost) == "luk" and not ghost.varnas and "taddhita" in ghost.tags
