"""T3 — the taddhita senses of 4.3: tatra jātaḥ / bhavaḥ, tata āgataḥ, nivāsaḥ open their frames (and the śeṣa group, 4.2.92 – 4.3.134, they lie in), so the
śaiṣika specials of 4.2 (rāṣṭriya, avārapārīṇa) apply in them too; and 4.3.1–2 yuṣmad / asmad (cha, khañ, the ādeśa yuṣmāka / asmāka)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

CASES = [   # (stem, lexical tags, sense, form that must be one of the readings)
    ("rAzwra", None, "jAta", "rAzwriyaH"),                       # 4.3.25 + 4.2.93 gha
    ("utsa", None, "jAta", "OtsaH"),                             # 4.1.86 añ holds in every sense
    ("avArapAra", None, "jAta", "avArapArIRaH"),
    ("prAvfz", None, "jAta", "prAvfzeRyaH"),                     # 4.3.26 eṇya
    ("koSa", None, "Bava", "kOSeyaH"),                           # 4.3.42 ḍhañ
    ("danta", {"lex:SarIrAvayava"}, "Bava", "dantyaH"),          # 4.3.55 yat
    ("SAlA", None, "Bava", "SAlIyaH"),                           # 4.2.114 in the bhava sense
    ("devadatta", {"lex:hetumanuzya"}, "Agata", "devadattarUpyaH"),   # 4.3.81 rūpya
    ("yuzmad", None, "Seza", "yuzmadIyaH"),                      # 4.3.1 cha
    ("yuzmad", None, "Seza", "yOzmAkIRaH"),                      # 4.3.1 khañ + 4.3.2 yuṣmāka
    ("asmad", None, "Seza", "AsmAkInaH"),
    ("mAsa", {"lex:kAla"}, "Seza", "mAsikaH"),                   # 4.3.11 ṭhañ
    ("saMvatsara", {"lex:kAla"}, "Seza", "sAMvatsarikaH"),
    ("rAzwra", None, "prAyaBava", "rAzwriyaH"),                  # 4.3.39 frame
    ("SArIraka", None, "granTa", "SArIrakIyaH"),                 # 4.3.87 (adhikṛtya kṛte granthe) + 4.2.114
    ("upagu", None, "idam", "OpagavaH"),                         # 4.3.120 tasyedam
    ("Sara", None, "vikAra", "SaramayaH"),                       # 4.3.144 mayaṭ (śarādi)
    ("Amra", None, "vikAra", "AmramayaH"),                       # vṛddha
    ("go", None, "vikAra", "gavyaH"),                            # 4.3.160 yat (+ 6.1.79)
    ("payas", None, "vikAra", "payasyaH"),
]


@pytest.mark.parametrize("stem,og,sense,want", CASES, ids=lambda c: None)
def test_sense(stem, og, sense, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "pulliṅga", origin_tags=og, taddhitArtha=sense))}
    assert want in got, sorted(got)
