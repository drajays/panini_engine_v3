"""T13b — 5.2.46 – 88: adhika (ḍa), guṇasya nimāne (mayaṭ), the pūraṇa group (ḍaṭ with maṭ / thuk / tithuk / ithuk / tamaṭ, tīya), the matvartha specials
(cha, aṇ, vun), kuśala, kāma, prasita, the kan senses 5.2.68 – 79, annaprāya, and the ini senses 5.2.85 – 88."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

SK, SKD, SA, SM = {"lex:saMKyA"}, {"lex:saMKyA", "lex:saMKyAdi"}, {"lex:svANga"}, {"lex:samAsa"}
P = "tasyapUraRa"
CASES = [   # (sense, stem, lexical tags, extra vivakṣā, a form that must be among the readings)
    ("tadasminnaDika", "viMSati", None, {}, "viMSam"),                    # 5.2.46
    ("tadasminnaDika", "triMSat", None, {}, "triMSam"),
    ("guRanimAna", "dvi", SK, {}, "dvimayam"),                            # 5.2.47
    (P, "ekAdaSan", SKD, {}, "ekAdaSam"),                                  # 5.2.48
    (P, "daSan", SK, {}, "daSamam"),                                       # 5.2.49
    (P, "paYcan", SK, {}, "paYcamam"),
    (P, "zaz", SK, {}, "zazWam"),                                          # 5.2.51
    (P, "kati", SK, {}, "katiTam"),
    (P, "catur", SK, {}, "caturTam"),
    (P, "bahu", SK, {}, "bahutiTam"),                                      # 5.2.52
    (P, "pUga", SK, {}, "pUgatiTam"),
    (P, "tAvat", SK, {}, "tAvatiTam"),                                     # 5.2.53
    (P, "dvi", SK, {}, "dvitIyam"),                                        # 5.2.54
    (P, "tri", SK, {}, "tftIyam"),                                         # 5.2.55
    (P, "viMSati", SK, {}, "viMSatitamam"),                                # 5.2.56
    (P, "viMSati", SK, {}, "viMSam"),
    (P, "Sata", SK, {}, "Satatamam"),                                      # 5.2.57
    (P, "mAsa", SK, {}, "mAsatamam"),
    (P, "zazwi", SK, {}, "zazwitamam"),                                    # 5.2.58
    ("matvartha", "acCAvAka", None, {"arthaViSeSa": "sUkta"}, "acCAvAkIyam"),    # 5.2.59
    ("matvartha", "yajYAyajYa", None, {"arthaViSeSa": "sAman"}, "yajYAyajYIyam"),
    ("matvartha", "vimukta", None, {"arthaViSeSa": "aDyAya"}, "vEmuktam"),       # 5.2.61
    ("matvartha", "gozada", None, {"arthaViSeSa": "anuvAka"}, "gozadakam"),      # 5.2.62
    ("kuSala", "paTin", None, {}, "paTakam"),                             # 5.2.63
    ("kuSala", "Akarza", None, {}, "Akarzakam"),                          # 5.2.64
    ("kAma", "Dana", None, {}, "Danakam"),                                # 5.2.65
    ("kAma", "hiraRya", None, {}, "hiraRyakam"),
    ("prasita", "keSa", SA, {}, "keSakam"),                               # 5.2.66
    ("prasita", "udara", None, {"arthaViSeSa": "AdyUna"}, "Odarikam"),    # 5.2.67
    ("parijAta", "sasya", None, {}, "sasyakam"),                          # 5.2.68
    ("aMSaMhArI", "aMSa", None, {}, "aMSakam"),                           # 5.2.69
    ("acirApahfta", "tantra", None, {}, "tantrakam"),                     # 5.2.70
    ("kAriRi", "SIta", None, {}, "SItakam"),                              # 5.2.72
    ("kAriRi", "uzRa", None, {}, "uzRakam"),
    ("anvicCati", "pArSva", None, {}, "pArSvakam"),                       # 5.2.75
    ("anvicCati", "ayaHSUla", None, {}, "AyaHSUlikam"),                   # 5.2.76
    ("anvicCati", "daRqAjina", None, {}, "dARqAjinikam"),
    ("grahaRa", "tAvatiTa", None, {}, "tAvatiTakam"),                     # 5.2.77
    ("grahaRa", "tAvatiTa", None, {}, "tAvatiTam"),                       # lug vā
    ("grAmaRI", "devadatta", None, {}, "devadattakam"),                   # 5.2.78
    ("bandhana", "SfNKala", None, {"arthaViSeSa": "karaBa"}, "SfNKalakam"),      # 5.2.79
    ("annaprAya", "guqa", None, {"arthaViSeSa": "saMjYA"}, "guqakam"),    # 5.2.82
    ("annaprAya", "kulmASa", None, {"arthaViSeSa": "saMjYA"}, "kOlmASam"),       # 5.2.83
    ("SrAddhaBukta", "SrAddha", None, {}, "SrAddhi"),                     # 5.2.85
    ("SrAddhaBukta", "SrAddha", None, {}, "SrAddhikam"),
    ("anena", "pUrva", None, {}, "pUrvi"),                                # 5.2.86
    ("anena", "kftapUrva", SM, {}, "kftapUrvi"),                          # 5.2.87
    ("anena", "izwa", None, {}, "izwi"),                                  # 5.2.88
]


@pytest.mark.parametrize("sense,stem,og,extra,want", CASES, ids=lambda c: None)
def test_senses(sense, stem, og, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "napuṃsaka", origin_tags=og, taddhitArtha=sense, **extra))}
    assert want in got, sorted(got)
