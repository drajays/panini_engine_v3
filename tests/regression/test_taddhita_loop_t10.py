"""T10 — 5.1.38 – 63: the other senses of the ārhīya group (nimitta, īśvara, vidita, vāpa, vṛddhyādi dīyate, bhāra-hāra, saṃbhavati …, aṃśa-vasna-bhṛti,
parimāṇa, arhati). Each opener opens its frame (default ṭhañ 5.1.18 / ṭhak 5.1.19); the specials 5.1.39 – 55, 62 are their apavādas."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

SA, PA, DV = {"lex:saMKyA"}, {"lex:parimARa"}, {"lex:aDyarDapUrvadvigu"}
CASES = [   # (sense, stem, lexical tags, extra vivakṣā, a form that must be among the readings)
    ("nimitta", "SvetacCatra", None, {}, "SvEtacCatrikam"),          # the default (ṭhak 5.1.19)
    ("nimitta", "pARi", None, {}, "pARyam"),                        # pāṇi is dvyac: 5.1.39
    ("nimitta", "Sata", SA, {}, "Satikam"),                         # 5.1.21 ṭhan
    ("nimitta", "Sata", SA, {}, "Satyam"),                          # 5.1.21 yat
    ("nimitta", "sahasra", None, {}, "sAhasram"),                   # 5.1.27
    ("nimitta", "go", None, {}, "gavyam"),                          # 5.1.39
    ("nimitta", "Dana", None, {}, "Danyam"),                        # dvyac
    ("nimitta", "svarga", None, {}, "svargyam"),
    ("nimitta", "aSva", None, {}, "ASvikam"),                       # aśvādi: not yat (ṭhak)
    ("nimitta", "putra", None, {}, "putrIyam"),                     # 5.1.40
    ("nimitta", "putra", None, {}, "putryam"),
    ("nimitta", "sarvaBUmi", None, {}, "sArvaBOmam"),               # 5.1.41 aṇ (anuśatikādi: both vṛddhi)
    ("nimitta", "pfTivI", None, {}, "pArTivam"),                    # añ
    ("Izvara", "sarvaBUmi", None, {}, "sArvaBOmam"),                # 5.1.42
    ("Izvara", "pfTivI", None, {}, "pArTivam"),
    ("vidita", "sarvaBUmi", None, {}, "sArvaBOmam"),                # 5.1.43
    ("vidita", "pfTivI", None, {}, "pArTivam"),
    ("vidita", "loka", None, {}, "lOkikam"),                        # 5.1.44 ṭhañ
    ("vidita", "sarvaloka", None, {}, "sArvalOkikam"),
    ("vApa", "prasTa", PA, {}, "prAsTikam"),                        # 5.1.45
    ("vApa", "droRa", PA, {}, "drORikam"),
    ("vApa", "pAtra", None, {}, "pAtrikam"),                        # 5.1.46 ṣṭhan
    ("vfdDyAdi", "paYcan", SA, {}, "paYcakam"),                     # 5.1.47
    ("vfdDyAdi", "dvitIya", {"lex:pUraRa"}, {}, "dvitIyikam"),      # 5.1.48 ṭhan
    ("vfdDyAdi", "arDa", None, {}, "arDikam"),
    ("vfdDyAdi", "BAga", None, {}, "BAgyam"),                       # 5.1.49
    ("vfdDyAdi", "BAga", None, {}, "BAgikam"),
    ("bhArahAra", "vaMSaBAra", None, {}, "vAMSaBArikam"),           # 5.1.50
    ("bhArahAra", "kuwajaBAra", None, {}, "kOwajaBArikam"),
    ("bhArahAra", "vasna", None, {}, "vasnikam"),                   # 5.1.51
    ("bhArahAra", "dravya", None, {}, "dravyakam"),
    ("samBavati", "prasTa", PA, {}, "prAsTikam"),                   # 5.1.52
    ("pacati", "prasTa", PA, {}, "prAsTikam"),
    ("avaharati", "AQaka", PA, {}, "AQakInam"),                     # 5.1.53 kha
    ("avaharati", "AQaka", PA, {}, "AQakikam"),                     # or the ṭhañ that stays
    ("samBavati", "Acita", PA, {}, "AcitInam"),
    ("samBavati", "dvyAQaka", DV | PA, {}, "dvyAQakInam"),          # 5.1.54 kha / ṣṭhan / ṭhañ-luk
    ("samBavati", "dvyAQaka", DV | PA, {}, "dvyAQakikam"),
    ("samBavati", "dvyAQaka", DV | PA, {}, "dvyAQakam"),
    ("samBavati", "kulija", PA, {}, "kulijInam"),                   # 5.1.55 kha
    ("samBavati", "kulija", PA, {}, "kulijam"),                     # luk
    ("samBavati", "kulija", PA, {}, "kOlijikam"),                   # ṭhañ stays
    ("aMSavasnaBfti", "paYcan", SA, {}, "paYcakam"),                # 5.1.56
    ("tadasyaparimARam", "prasTa", PA, {}, "prAsTikam"),            # 5.1.57
    ("tadasyaparimARam", "Sata", SA, {}, "Satikam"),
    ("tadasyaparimARam", "sahasra", None, {}, "sAhasram"),
    ("tadasyaparimARam", "triMSat", SA, {"arthaViSeSa": "brAhmaRasaMjYA"}, "trEMSam"),          # 5.1.62 ḍaṇ
    ("tadasyaparimARam", "catvAriMSat", SA, {"arthaViSeSa": "brAhmaRasaMjYA"}, "cAtvAriMSam"),
    ("arhati", "SvetacCatra", None, {}, "SvEtacCatrikam"),          # 5.1.63
    ("arhati", "Sata", SA, {}, "Satyam"),
]


@pytest.mark.parametrize("sense,stem,og,extra,want", CASES, ids=lambda c: None)
def test_senses(sense, stem, og, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "napuṃsaka", origin_tags=og, taddhitArtha=sense, **extra))}
    assert want in got, sorted(got)
