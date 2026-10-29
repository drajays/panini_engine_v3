"""T14c — 5.4.1 – 67 (the taddhita pratyayas of the last pāda before the samāsānta rules): pāda/śata vun, kan in a kind / not wholly / a cloak, cha for a relation,
the kṛtvasuc group's dhā, mayaṭ, tādarthya yat/ñya, lohita-kāla kan, ṭhak/aṇ in speech, tra, and the ḍāc senses (kṛñ-yoga, S58)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

T, A = "taddhitArtha", "arthaViSeSa"
N, S_, P_ = "napuṃsaka", "strīliṅga", "pulliṅga"
CASES = [   # (stem, lexical tags, vivakṣā, linga, a form that must be among the readings)
    ("dvipAda", {"lex:saMKyAdi"}, {A: "vIpsA"}, S_, "dvipadikA"),                      # 5.4.1
    ("dviSata", {"lex:saMKyAdi"}, {A: "vIpsA"}, S_, "dviSatikA"),
    ("dvipAda", {"lex:saMKyAdi"}, {A: "daRqa"}, S_, "dvipadikA"),                      # 5.4.2
    ("sTUla", None, {T: "prakAravacana"}, N, "sTUlakam"),                              # 5.4.3
    ("mAza", None, {T: "prakAravacana"}, N, "mAzakam"),
    ("Binna", {"lex:ktAnta"}, {T: "anatyantagati"}, N, "Binnakam"),                    # 5.4.4
    ("brAhmaRajAti", {"lex:jAtyanta"}, {T: "banDu"}, N, "brAhmaRajAtIyam"),            # 5.4.9
    ("pitfsTAna", None, {T: "sasTAna"}, N, "pitfsTAnIyam"),                            # 5.4.10
    ("pitfsTAna", None, {T: "sasTAna"}, N, "pitfsTAnam"),
    ("visArin", None, {T: "matsya"}, P_, "vEsAriRaH"),                                 # 5.4.16
    ("bahu", None, {T: "kriyAaByAvftti", A: "aviprakfzwakAla"}, N, "bahuDA"),          # 5.4.20
    ("anna", None, {T: "prakfta"}, N, "annamayam"),                                    # 5.4.21
    ("agnidevatA", None, {T: "tAdarTya"}, N, "agnidevatyam"),                          # 5.4.24
    ("arGa", None, {T: "tAdarTya"}, N, "arGyam"),                                      # 5.4.25
    ("atiTi", None, {T: "tAdarTya"}, N, "AtiTyam"),                                    # 5.4.26
    ("lohita", None, {T: "maRi"}, P_, "lohitakaH"),                                    # 5.4.30
    ("lohita", None, {T: "varRa", A: "anitya"}, P_, "lohitakaH"),                      # 5.4.31
    ("lohita", None, {T: "rakta"}, P_, "lohitakaH"),                                   # 5.4.32
    ("kAla", None, {T: "rakta"}, P_, "kAlakaH"),                                       # 5.4.33
    ("vAc", None, {T: "vyAhftArTA"}, N, "vAcikam"),                                    # 5.4.35
    ("karman", None, {T: "vyAhftArTA"}, N, "kArmaRam"),                                # 5.4.36
    ("ozaDi", None, {A: "ajAti"}, N, "OzaDam"),                                        # 5.4.37
    ("mfd", None, {A: "praSaMsA"}, S_, "mftsA"),                                       # 5.4.40
    ("mfd", None, {A: "praSaMsA"}, S_, "mftsnA"),
    ("deva", None, {T: "dvitIyAsaptamI"}, N, "devatrA"),                               # 5.4.56
    ("dvitIya", None, {T: "kfzi"}, N, "dvitIyA"),                                      # 5.4.58
    ("dviguRa", None, {T: "kfzi"}, N, "dviguRA"),                                      # 5.4.59
    ("samaya", None, {T: "yApanA"}, N, "samayA"),                                      # 5.4.60
    ("sapatra", None, {T: "ativyaTana"}, N, "sapatrA"),                                # 5.4.61
    ("nizkula", None, {T: "nizkozaRa"}, N, "nizkulA"),                                 # 5.4.62
    ("suKa", None, {T: "Anulomya"}, N, "suKA"),                                        # 5.4.63
    ("duHKa", None, {T: "prAtilomya"}, N, "duHKA"),                                    # 5.4.64
    ("SUla", None, {T: "pAkaviSaya"}, N, "SUlA"),                                      # 5.4.65
    ("satya", None, {T: "aSapaTa"}, N, "satyA"),                                       # 5.4.66
    ("madra", None, {T: "parivApaRa"}, N, "madrA"),                                    # 5.4.67
]
XFAIL = [   # (stem, lexical tags, vivakṣā, linga, the right form, why)
    ("bfhatI", None, {T: "AcCAdana"}, S_, "bfhatikA", "5.4.6: the ī of bṛhatī is shortened before kan (6.3.63 bahulam); not real, the engine gives bfhatIkA"),
    ("pAda", None, {T: "tAdarTya"}, N, "pAdyam", "5.4.25: 6.4.130 pādaḥ pat acts on a lone pād; Kāśikā keeps pādyam (6.3.53 atadarthe); the engine gives padyam"),
]


def _got(stem, og, vv, linga):
    return {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, linga, origin_tags=og, **vv))}


@pytest.mark.parametrize("stem,og,vv,linga,want", CASES, ids=lambda c: None)
def test_senses(stem, og, vv, linga, want):
    got = _got(stem, og, vv, linga)
    assert want in got, sorted(got)


@pytest.mark.parametrize("stem,og,vv,linga,want", [pytest.param(*c[:5], marks=pytest.mark.xfail(strict=True, reason=c[5])) for c in XFAIL], ids=lambda c: None)
def test_known_gaps(stem, og, vv, linga, want):
    assert want in _got(stem, og, vv, linga)
