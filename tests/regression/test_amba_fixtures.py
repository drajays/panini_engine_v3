"""Goyal-Kulkarni-Behera (Amba) conflict fixtures (papers/REVIEW_new_batch.md section 1): the form AND the sutra order the paper's
visibility model (8.2.1, 6.4.22, 6.1.86) demands. SLP1 throughout."""
import pytest

import sutras  # noqa: F401
from pipelines.pada_samhita import join
from pipelines.subanta import derive as subanta
from pipelines.tinanta import derive as tinanta
from pipelines.prakftya_lyap_split_prakriyas import _upasarga

SID = lambda s, i: [t["sutra_id"] for t in s.trace].index(i)            # noqa: E731
APPLIED = lambda s, i: "APPLIED" in [t["status"] for t in s.trace if t["sutra_id"] == i]   # noqa: E731


def test_SAdhi():
    """SAs+hi -> SADi (Amba a). 6.4.101 + 8.2.25 fire. Amba also has 6.4.35 (SA hO) fire; see the xfail below."""
    s = tinanta("Adadi_02_0012", "loT", "kartari", 2, 1, pada="parasmai")
    assert s.flat_slp1() == "SADi" and APPLIED(s, "6.4.101")


@pytest.mark.xfail(strict=True, reason="Amba a: 6.4.35 (SA hO) should fire beside 6.4.101 (either order, 6.4.22). The engine reaches SADi via "
                   "6.4.101 (hu-jhalByo her Dir) + 8.2.25 on the unreduced SAs; 6.4.35 never applies (not even BLOCKED in the trace)")
def test_SAdhi_6_4_35_fires():
    s = tinanta("Adadi_02_0012", "loT", "kartari", 2, 1, pada="parasmai")
    assert APPLIED(s, "6.4.35")


def test_jahi_6_4_105_must_not_fire():
    """han+hi -> jahi (b): 6.4.36 (hano vaDa) fires; 6.4.105 (ato heH) must not (asiddhavat 6.4.22)."""
    s = tinanta("Adadi_02_0002", "loT", "kartari", 2, 1)
    assert s.flat_slp1() == "jahi" and APPLIED(s, "6.4.36") and not APPLIED(s, "6.4.105")


def test_adhItya_tuk_before_savarnadirgha():
    """aDi+i+lyap: 6.1.71 (tuk) before 6.1.101, giving aDItya not *aDIya (c; 6.1.86: the ekadesha is invisible to tuk)."""
    from core.canonical_pipelines import P00_gati_samasa, P00_vikarana_it_lopa
    from engine import apply_rule
    from engine.state import Term
    from engine.tape_init.krdanta import PURVAKALA_SAMANAKARTRKA, build_krdanta_state
    from phonology.varna import parse_slp1_upadesha_sequence
    d = Term(kind="prakriti", varnas=list(parse_slp1_upadesha_sequence("i")), tags={"dhatu", "anga", "prātipadika"},
             meta={"upadesha_slp1": "i"})
    s = build_krdanta_state([_upasarga("aDi"), d], **PURVAKALA_SAMANAKARTRKA)
    for step in ("3.4.21", P00_gati_samasa, "7.1.37", P00_vikarana_it_lopa, "6.1.71", "6.1.101"):
        s = apply_rule(step, s) if isinstance(step, str) else step(s)
    assert s.flat_slp1() == "aDItya"
    assert SID(s, "6.1.71") < SID(s, "6.1.101")


def test_kosicat_not_kozicat():
    """ko+asicat -> kosicat (d): the 6.1.109 ekadesha is invisible to 8.3.59, so no z."""
    s = join("ko", "asicat")
    assert s.flat_slp1() == "kosicat" and APPLIED(s, "6.1.109")


def test_vakti_8_2_30_before_8_4_40():
    """vac+ti -> vakti (e): 8.2.30 (coH kuH) before 8.4.40 (stoH ScunA ScuH) can act (8.2.1)."""
    s = tinanta("Adadi_02_0058", "laT", "kartari", 3, 1)
    assert s.flat_slp1() == "vakti" and APPLIED(s, "8.2.30") and not APPLIED(s, "8.4.40")


def test_rAmARAm():
    """rAma+Am -> rAmARAm (f): 7.1.54 over 6.1.87/6.1.101, then 6.4.3 (blocked by 6.4.22 asiddhavat/ordering), then 8.4.2."""
    s = subanta("rAma", 6, 3, "pulliṅga")
    assert s.flat_slp1() == "rAmARAm"
    assert APPLIED(s, "7.1.54") and APPLIED(s, "8.4.2")
    assert not APPLIED(s, "6.1.87") and not APPLIED(s, "6.1.101")


def test_rAmeByaH_7_3_103_over_7_3_102():
    """rAma+Byas -> rAmeByaH (g): 7.3.103 (bahuvacane jhalyet) wins; 7.3.102 (supi ca) is BLOCKED. Layer: it is the later sutra and
    the narrower one (bahuvacana, jhal-initial sup), so para and specificity agree; Arya reads para."""
    s = subanta("rAma", 5, 3, "pulliṅga")
    assert s.flat_slp1() == "rAmeByaH" and APPLIED(s, "7.3.103") and not APPLIED(s, "7.3.102")


def test_vAriRe_7_1_73_over_7_3_111():
    """vAri+Ne -> vAriRe (h): 7.1.73 (iko 'ci vibhaktau num) applies; 7.3.111 (gher ṅiti) never does (BLOCKED by name)."""
    s = subanta("vAri", 4, 1, "napuṃsaka")
    assert s.flat_slp1() == "vAriRe" and APPLIED(s, "7.1.73") and not APPLIED(s, "7.3.111")


def test_7_3_113_yat_fires_once():
    """rAmA+Ne (Amba 'Problems'): the yAw agama keeps Nit, so 7.3.113 must not re-trigger: it APPLIES exactly once."""
    s = subanta("rAmA", 4, 1, "strīliṅga")
    assert s.flat_slp1() == "rAmAyE"
    assert [t["sutra_id"] for t in s.trace if t["status"] == "APPLIED"].count("7.3.113") == 1


@pytest.mark.xfail(strict=True, raises=ValueError, reason="Amba: SivaH+arcya -> Sivorcya is the paper's exception to 8.2.1 (8.2.66 ru is "
                   "seen by sapadadhyayi 6.1.113). pipelines/pada_samhita.join refuses visarga seams: the tripadi across padas "
                   "(8.2.66 / 6.1.113 sthanivat route) is not built, so the engine yields no form")
def test_Sivorcya_exception_to_8_2_1():
    assert join("SivaH", "arcya").flat_slp1() == "Sivorcya"
