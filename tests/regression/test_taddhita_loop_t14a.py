"""T14a — 5.3.3 – 5.3.57: the vibhakti pratyayas (tasil, tral, dā, thāl … with the ādeśas of idam, etad, sarva), the dik pratyayas (astāti, atasuc, puras …),
dhā and its apavādas, bhāga / asahāya / yāpya senses, and tamap / tarap. The pratyayas are avyayas (1.1.38, 2.4.82): no sup shows."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

SAM, DIK = {"lex:saMKyA"}, {"lex:dikSabda"}
AN = {"arthaViSeSa": "anadyatana"}
DV = {"arthaViSeSa": "dvivacanavibhajya"}
CASES = [   # (sense, stem, lexical tags, extra vivakṣā, a form that must be among the readings)
    ("paYcamIvib", "tad", None, {}, "tataH"),                            # 5.3.7
    ("paYcamIvib", "yad", None, {}, "yataH"),
    ("paYcamIvib", "sarva", None, {}, "sarvataH"),
    ("paYcamIvib", "bahu", None, {}, "bahutaH"),
    ("paYcamIvib", "idam", None, {}, "itaH"),                            # 5.3.3 iś
    ("paYcamIvib", "etad", None, {}, "ataH"),                            # 5.3.5 etado 'n
    ("saptamIvib", "tad", None, {}, "tatra"),                            # 5.3.10
    ("saptamIvib", "sarva", None, {}, "sarvatra"),
    ("saptamIvib", "anya", None, {}, "anyatra"),
    ("saptamIvib", "idam", None, {}, "iha"),                             # 5.3.11
    ("saptamIvib", "etad", None, {}, "atra"),
    ("kAle", "tad", None, {}, "tadA"),                                   # 5.3.15
    ("kAle", "yad", None, {}, "yadA"),
    ("kAle", "eka", None, {}, "ekadA"),
    ("kAle", "sarva", None, {}, "sarvadA"),
    ("kAle", "sarva", None, {}, "sadA"),                                 # 5.3.6 sarvasya so 'nyatarasyāṃ di
    ("kAle", "idam", None, {}, "idAnIm"),                                # 5.3.18
    ("kAle", "tad", None, {}, "tadAnIm"),                                # 5.3.19
    ("kAle", "tad", None, AN, "tarhi"),                                  # 5.3.21
    ("kAle", "yad", None, AN, "yarhi"),
    ("kAle", "sarva", None, AN, "sarvarhi"),
    ("prakAravacana", "tad", None, {}, "taTA"),                          # 5.3.23
    ("prakAravacana", "yad", None, {}, "yaTA"),
    ("prakAravacana", "sarva", None, {}, "sarvaTA"),
    ("prakAravacana", "etad", None, {}, "aTA"),
    ("prakAravacana", "idam", None, {}, "itTam"),                        # 5.3.24 + 5.3.4 it
    ("dik", "pUrva", DIK, {}, "purastAt"),                               # 5.3.27 + 5.3.40
    ("dik", "aDara", DIK, {}, "aDastAt"),
    ("dik", "apara", DIK, {}, "aparastAt"),
    ("dik", "uttara", DIK, {}, "uttarataH"),                             # 5.3.28
    ("dik", "dakziRa", DIK, {}, "dakziRataH"),
    ("dik", "para", DIK, {}, "parataH"),                                 # 5.3.29
    ("dik", "para", DIK, {}, "parastAt"),
    ("dik", "avara", DIK, {}, "avastAt"),                                # 5.3.41
    ("dik", "avara", DIK, {}, "avarastAt"),
    ("viDArTa", "eka", SAM, {}, "ekaDA"),                                # 5.3.42
    ("viDArTa", "dvi", SAM, {}, "dviDA"),
    ("viDArTa", "catur", SAM, {}, "caturDA"),
    ("viDArTa", "bahu", SAM, {}, "bahuDA"),
    ("viDArTa", "paYcan", SAM, {}, "paYcaDA"),
    ("aDikaraRavicAla", "dvi", SAM, {}, "dviDA"),                        # 5.3.43
    ("viDArTa", "eka", SAM, {}, "EkaDyam"),                              # 5.3.44
    ("viDArTa", "dvi", SAM, {}, "dvEDam"),                               # 5.3.45
    ("viDArTa", "tri", SAM, {}, "trEDam"),
    ("viDArTa", "dvi", SAM, {}, "dveDA"),                                # 5.3.46
    ("viDArTa", "tri", SAM, {}, "treDA"),
    ("yApya", "yAjaka", None, {}, "yAjakapASam"),                        # 5.3.47
    ("BAga", "tftIya", None, {}, "tftIyam"),                             # 5.3.48
    ("BAga", "paYcama", None, {}, "paYcamam"),                           # 5.3.49
    ("BAga", "zazWa", None, {}, "zazWam"),
    ("BAga", "zazWa", None, {}, "zAzWam"),                               # 5.3.50
    ("BAga", "azwama", None, {}, "Azwamam"),
    ("asahAya", "eka", None, {}, "ekAkini"),                             # 5.3.52
    ("asahAya", "eka", None, {}, "ekakam"),
    ("atiSAyana", "sundara", None, {}, "sundaratamam"),                  # 5.3.55
    ("atiSAyana", "sundara", None, DV, "sundarataram"),                  # 5.3.57
]
XFAIL = [   # the pratyaya is the sūtra's own; the form waits for the rule named in the reason
    ("paYcamIvib", "kim", None, {}, "kutaH", "7.2.103 – 105 (kim → ku / ka / kva) are not real for a taddhita vibhakti"),
    ("saptamIvib", "kim", None, {}, "kutra", "7.2.104 (kuḥ ti) is a stub"),
    ("saptamIvib", "kim", None, {}, "kva", "7.2.105 (kva ati) is a stub"),
    ("kAle", "kim", None, {}, "kadA", "7.2.103 for a taddhita vibhakti is not real"),
    ("prakAravacana", "kim", None, {}, "kaTam", "7.2.103 for a taddhita vibhakti is not real"),
    ("kAle", "idam", None, {}, "etarhi", "S52: 5.3.16 and 5.3.18 both teach a pratyaya for idam in the same sense; the loop does not explore a choice between two sūtras"),
    ("atiSAyana", "paWu", None, {}, "paWizWam", "S54: 6.4.154 – 159 (ṭi-lopa before iṣṭha) are not real, and 5.3.55 does not yet teach iṣṭhan"),
]


@pytest.mark.parametrize("sense,stem,og,extra,want", CASES, ids=lambda c: None)
def test_senses(sense, stem, og, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "napuṃsaka", origin_tags=og, taddhitArtha=sense, **extra))}
    assert want in got, sorted(got)


@pytest.mark.parametrize("sense,stem,og,extra,want,why", XFAIL, ids=lambda c: None)
@pytest.mark.xfail(strict=True, reason="known gap")
def test_known_gaps(sense, stem, og, extra, want, why):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "napuṃsaka", origin_tags=og, taddhitArtha=sense, **extra))}
    assert want in got, why


def test_vibhakti_pratyaya_is_an_avyaya():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("tad", 1, 1, "puṃliṅga", taddhitArtha="saptamIvib"))}
    assert "tatra" in got and "tatraH" not in got, sorted(got)      # 2.4.82 took the sup away
