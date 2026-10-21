"""
3.4.21  समानकर्तृकयोः पूर्वकाले  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=34021 · padaccheda समान-कर्त्तृकयोः पूर्व-काले ·
  anuvṛtti 31001 प्रत्ययः | 31002 परः च | 31091 धातोः | 31093 कृत् | 34018 क्त्वा
- Kāśikā: "समानः कर्ता ययोर्धात्वर्थयोस्तत्र पूर्वकाले धात्वर्थे वर्तमानाद् धातोः क्त्वाप्रत्ययो भवति।
  भुक्त्वा व्रजति। पीत्वा व्रजति। द्विवचनमतन्त्रम्। स्नात्वा पीत्वा भुक्त्वा दत्त्वा व्रजति।"
  pratyudāharaṇa: "समानकर्तृकयोरिति किम्? भुक्तवति ब्राह्मणे व्रजति देवदत्तः। पूर्वकाल इति किम्? व्रजति च जल्पति च"
- Cross-validation: regression test tests/regression/test_ktva_3_4_21_vivaksha.py (the pratyudāharaṇas leave the
  tape alone); lyap spine tests/unit/test_prakftya_lyap_split_prakriyas.py, tests/unit/test_lyap_6_4_38_nitya.py

Both conditions are the speaker's meaning, not the tape: the cond asks `vivaksita` for kāla pUrvakAla and
samAnakartfka (AMENDMENT 25; both words stand in this sūtra's samagra), recorded by engine/tape_init/krdanta.
DAtoH … paraH (3.1.91, 3.1.2): the dhātu must end the tape, so the affix is attached once. The act appends the
upadeśa ktvA itself, a kṛt (3.1.93 by anuvṛtti); its k is left to the it-prakaraṇa (1.3.8) and its ārdhadhātuka-saṃjñā
to 3.4.114.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from engine.vivaksha import vivaksita
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not (vivaksita(state, "kala", "pUrvakAla") and vivaksita(state, "samAnakartfka", "samAnakartfka")):
        return False
    return bool(state.terms) and "dhatu" in state.terms[-1].tags


def act(state: State) -> State:
    state.terms.append(Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("ktvA")),
        tags={"pratyaya", "krt", "upadesha"},
        meta={"upadesha_slp1": "ktvA"},
    ))
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.21",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = 'samAnakartfkayoH pUrvakAle',
    text_dev       = 'समानकर्तृकयोः पूर्वकाले',
    samagra_slp1   = "pratyayaH paraSca AdyudAttaSca DAtoH samAnakarttfkayoH pUrvakAle kft ktvA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev    = "प्रत्ययः परश्च आद्युदात्तश्च धातोः समानकर्त्तृकयोः पूर्वकाले कृत् क्त्वा",
    padaccheda_dev = "समानकर्तृकयोः / पूर्वकाले",
    why_dev        = "समानकर्तृकयोर्धात्वर्थयोः पूर्वकाले धात्वर्थे धातोः क्त्वा।",
    anuvritti_from = ("3.1.1", "3.1.2", "3.1.3", "3.1.91"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
