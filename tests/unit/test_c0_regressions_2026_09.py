"""
One Vidyut-confirmed form per rule family fixed in the 2026-09 C0 sweep
(branch lsk-practice), so a later reordering can't silently undo one.
Each is derived by pāṭha id or unambiguous upadeśa.
"""
import pytest

from pipelines.tinanta import derive

CASES = [
    # (dhātu, lakāra, prayoga, puruṣa, vacana, pada, expected)             family
    ("skudi~", "laT", "kartari", 3, 1, None, "स्कुन्दते"),     # 7.1.58 idit num
    ("SIkf~", "laT", "kartari", 1, 2, None, "शीकावहे"),       # guṇa scope (non-laghu)
    ("zvada~", "laT", "kartari", 3, 1, None, "स्वदते"),        # 6.1.64 ṣ→s
    ("vftu~", "laT", "kartari", 3, 1, None, "वर्तते"),         # 1.1.51 upadhā ṛ
    ("eDa~", "laT", "kartari", 3, 2, None, "एधेते"),           # 7.2.81 duals
    ("eDa~", "lRT", "kartari", 2, 2, None, "एधिष्येथे"),
    ("eDa~", "laG", "kartari", 3, 1, None, "ऐधत"),             # 6.4.72 āṭ + 6.1.90
    ("eDa~", "laG", "kartari", 3, 2, None, "ऐधेताम्"),         # laṅ dual (order!)
    ("eDa~", "laG", "kartari", 1, 3, None, "ऐधामहि"),          # 3.4.100 parasmai-only
    ("eDa~", "loT", "kartari", 3, 1, None, "एधताम्"),          # 3.4.90
    ("eDa~", "loT", "kartari", 1, 1, None, "एधै"),             # 3.4.93
    ("eDa~", "liT", "kartari", 3, 1, None, "एधाञ्चक्रे"),       # ām-liṭ
    ("sparDa~", "liT", "kartari", 1, 3, "atmane", "पस्पर्धिमहे"),  # ātmane liṭ
    ("qukfY", "liT", "kartari", 1, 3, "parasmai", "चकृम"),     # 7.2.13
    ("qukfY", "liT", "kartari", 2, 1, "parasmai", "चकर्थ"),    # thal pit → guṇa
    ("qukfY", "laT", "karmani", 3, 1, None, "क्रियते"),        # 7.4.28 riṅ
    ("BU", "laT", "bhave", 3, 1, None, "भूयते"),               # bhāve = karmaṇi (yak)
    ("qupaca~z", "luT", "kartari", 3, 1, None, "पक्ता"),       # aniṭ 7.2.10 + 8.2.30
    ("qupaca~z", "lRT", "kartari", 3, 1, None, "पक्ष्यति"),     # 8.3.59 after ku
    ("RIY", "luG", "kartari", 3, 1, None, "अनैषीत्"),          # 7.2.1 + 7.3.96
    ("hf~", "luG", "kartari", 3, 2, None, "अहार्ष्टाम्"),        # sic vṛddhi + ṣatva after r
    ("BU", "luG", "kartari", 3, 1, None, "अभूत्"),             # 2.4.77 sic-luk
    ("pura~", "laT", "kartari", 3, 1, None, "पुरति"),          # tudādi: no guṇa
    ("hf~", "liT", "kartari", 3, 1, None, "जहार"),             # 7.4.62
    ("divu~", "laT", "kartari", 3, 1, None, "दीव्यति"),         # 8.2.77
    ("gamx~", "liT", "kartari", 3, 2, None, "जग्मतुः"),         # 6.4.98
    ("10.0001", "laT", "kartari", 3, 1, None, "चोरयति"),       # curādi ṇic
    ("10.0001", "liT", "kartari", 3, 1, None, "चोरयाञ्चकार"),   # 3.1.35 + 6.4.55
    ("05.0001", "laT", "kartari", 3, 1, None, "सुनोति"),        # śnu, own guṇa
    ("05.0001", "loT", "kartari", 2, 1, None, "सुनु"),          # 6.4.106
    ("05.0006", "laT", "kartari", 3, 1, None, "स्तृणोति"),      # ṇatva
    ("09.0001", "laT", "kartari", 3, 3, None, "क्रीणन्ति"),     # 6.4.112
    ("09.0016", "laT", "kartari", 3, 1, None, "लुनाति"),        # 7.3.80 pvādi
    ("02.0062", "laT", "kartari", 3, 1, None, "रोदिति"),        # 7.2.76
    ("02.0062", "laG", "kartari", 3, 1, None, "अरोदीत्"),       # 7.3.98
    ("02.0058", "laT", "kartari", 3, 1, None, "वक्ति"),         # data fix + 8.2.30
    ("ruDi~r", "laG", "kartari", 3, 1, None, "अरुणत्"),         # 6.1.68 tiṅ branch
    ("Banjo~", "laT", "kartari", 3, 1, None, "भनक्ति"),         # 6.4.23 + cu→ku
]


@pytest.mark.parametrize("dhatu,lakara,prayoga,purusha,vacana,pada,expected", CASES,
                         ids=[f"{c[0]}-{c[1]}-{c[2]}-{c[3]}{c[4]}" for c in CASES])
def test_c0_family(dhatu, lakara, prayoga, purusha, vacana, pada, expected):
    kw = {"pada": pada} if pada else {}
    assert derive(dhatu, lakara, prayoga, purusha, vacana, **kw).flat_dev() == expected
