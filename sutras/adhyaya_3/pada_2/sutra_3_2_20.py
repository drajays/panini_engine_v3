"""
3.2.20  कृञो हेतुताच्छील्यानुलोम्येषु  —  VIDHI

Padaccheda: कृञः हेतु-ताच्छील्य-आनुलोम्येषु

krt-suffix rule: कृञो हेतुताच्छील्यानुलोम्येषु (20)
Pāṭha: ashtadhyayi.com data.txt row i=32020 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, upapada_site, no_upasarga
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return upapada_site(state, "karman", dhatus=frozenset({"qukfY"})) if no_upasarga(state) and (vivaksita(state, "hetutAcCIlyAnulomya", "hetu") or vivaksita(state, "hetutAcCIlyAnulomya", "tAcCIlya") or vivaksita(state, "hetutAcCIlyAnulomya", "Anulomya")) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_krt(state, "wa")


SUTRA = SutraRecord(
    sutra_id              = "3.2.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kfYo hetutAcCIlyAnulomyezu",
    text_dev              = "कृञो हेतुताच्छील्यानुलोम्येषु",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kfYaH hetu-tAcCIlya-anulomyezu kft karmaRi anupasarge supi waH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कृञः हेतु-ताच्छील्य-अनुलोम्येषु कृत् कर्मणि अनुपसर्गे सुपि टः",
    padaccheda_dev        = "कृञः हेतु-ताच्छील्य-आनुलोम्येषु",
    why_dev               = "धातोः कृत्-प्रत्ययः [कृञो हेतुताच्छील्यानुलोम्येषु] विहितः (३.२.20)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
