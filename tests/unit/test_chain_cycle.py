"""pipelines/chain.py: every arrow of the cycle on one word, each by the loop (no recipe knows the form).

    aja —strī→ ajA —nāmadhātu (kyac)→ ajIya —sanādi (ṇic)→ ajIyi —kṛt (Ṇvul)→ ajIyaka —taddhita (iñ)→ AjIyaki —sup→ AjIyakiH
                                                   └─────────────── tiṅ (laṭ tip) → ajIyayati

Every link is taught with an example in the Kāśikā: ajā (4.1.4), putrīyati / mālīyati / khaṭvīyati (3.1.8, 7.4.33, 2.4.71), kārayati (3.1.26), pācakaḥ (3.1.133),
dākṣiḥ (4.1.95), pacati-type śap + guṇa (3.1.68, 7.3.84, 6.1.78). The word itself is a derivation, not an attested one: the lakṣaṇa licenses it."""
import functools

import sutras  # noqa: F401
from pipelines import chain


def _ids(stem_or_dhatu, stage):
    return {i for st, ids in stem_or_dhatu.trace if st == stage for i in ids}


@functools.cache
def _chain():
    s = chain.strI(chain.Stem("aja"))
    d = chain.nama_dhatu(s)
    e = chain.sanadi(d, hetumat="hetumat")
    k = chain.krt(e, krt="Rvultfc", kala="vartamAna")
    t = chain.taddhita(k, taddhitArtha="apatya")
    return s, d, e, k, t


def test_every_arrow_forms():
    s, d, e, k, t = _chain()
    assert (s.slp1, d.slp1, e.slp1, k.slp1, t.slp1) == ("ajA", "ajIya", "ajIyi", "ajIyaka", "AjIyaki")
    assert chain.sup(t, 1, 1).flat_slp1() == "AjIyakiH"


def test_each_stage_fires_its_sutras():
    _, _, _, _, t = _chain()
    need = {
        "strI": {"4.1.3", "4.1.4", "6.1.101"},                      # striyām · ajādyataṣṭāp · a + ā → ā
        "nama_dhatu": {"3.1.8", "2.4.71", "3.1.32", "7.4.33"},      # kyac · sup-luk · sanādyantā dhātavaḥ · kyaci ca (ajA → ajI)
        "sanadi": {"3.1.26", "3.1.32", "6.4.148"},                  # hetumati ca (ṇic) · yasyeti ca
        "krt": {"3.1.133", "6.4.51", "7.1.1"},                      # ṇvul · ṇer aniṭi · yuvoranākau
        "taddhita": {"4.1.92", "4.1.95", "7.2.117", "6.4.148"},     # tasyāpatyam · ata iñ · taddhiteṣvacāmādeḥ
    }
    for stage, ids in need.items():
        assert ids <= _ids(t, stage), (stage, ids - _ids(t, stage))


def test_sup_trace():
    _, _, _, _, t = _chain()
    assert "8.3.15" in {e.get("sutra_id") for e in chain.sup(t, 1, 1).trace if isinstance(e, dict)}      # kharavasānayor visarjanīyaḥ


def test_tinanta_from_the_same_derived_dhatu():
    _, _, e, _, _ = _chain()
    st = chain.tinanta(e, "laT", 3, 1)
    assert st.flat_slp1() == "ajIyayati"
    fired = {x.get("sutra_id") for x in st.trace if isinstance(x, dict)}
    assert {"3.2.123", "3.4.78", "3.1.68", "7.3.84", "6.1.78"} <= fired


def test_kyac_on_an_a_stem_putriya():
    """Kāśikā 3.1.8 / 7.4.33 / 2.4.71: ātmanaḥ putram icchati → putrīyati (the apavāda of 7.4.25 gives ī, not dīrgha)."""
    d = chain.nama_dhatu(chain.Stem("putra"))
    assert d.slp1 == "putrIya"
    assert chain.tinanta(d, "laT", 3, 1).flat_slp1() == "putrIyati"


def test_krt_then_stri_reaches_7_3_44():
    """pāṭhaka + ṭāp: the a before the ka of the pratyaya becomes i (pāṭhikā), not pāṭhakā."""
    s = chain.strI(chain.krt("01.0381", krt="Rvultfc"))
    assert s.slp1 == "pAWikA" and "7.3.44" in _ids(s, "strI")
