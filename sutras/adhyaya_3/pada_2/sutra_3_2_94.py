"""
3.2.94  दृशेः क्वनिप्  —  VIDHI

Padaccheda: दृशेः क्वनिप्

krt-suffix rule: दृशेः क्वनिप् (94)
Pāṭha: ashtadhyayi.com data.txt row i=32094 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, upapada_site, no_upasarga
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return upapada_site(state, "karman", dhatus=frozenset({"dfSi~r"})) if vivaksita(state, "kala", "BUta") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    if policy_pick(state, "3.2.94", 2) == 1:      # beside niṣṭhā (3.2.102): decline and leave the tape to it
        return state
    return attach_krt(state, "kvanp")      # SHORTCUT S12: the i of kvanip only lets the it-letter p be said; held as kvanp


SUTRA = SutraRecord(
    sutra_id              = "3.2.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dfSeH kvanip",
    text_dev              = "दृशेः क्वनिप्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BUte dfSeH kvanip kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भूते दृशेः क्वनिप् कृत्",
    padaccheda_dev        = "दृशेः क्वनिप्",
    why_dev               = "धातोः कृत्-प्रत्ययः [दृशेः क्वनिप्] विहितः (३.२.94)।",
    anuvritti_from        = ('3.1.1',),
    apavada_of            = ("3.2.102",),      # bhūte karmaṇi / kartari: the special kṛt takes the site from niṣṭhā
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
