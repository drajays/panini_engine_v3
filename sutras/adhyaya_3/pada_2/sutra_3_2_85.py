"""
3.2.85  करणे यजः  —  VIDHI

Padaccheda: करणे यजः

krt-suffix rule: करणे यजः (85)
Pāṭha: ashtadhyayi.com data.txt row i=32085 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, upapada_site, no_upasarga
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return upapada_site(state, "karaRa", dhatus=frozenset({"yaja~"})) if vivaksita(state, "kala", "BUta") else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    if policy_pick(state, "3.2.85", 2) == 1:      # beside niṣṭhā (3.2.102): decline and leave the tape to it
        return state
    return attach_krt(state, "Rin")      # SHORTCUT S12: ṇini is taken as ṇin (the final i of the sūtra's word as uccāraṇa)


SUTRA = SutraRecord(
    sutra_id              = "3.2.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karaRe yajaH",
    text_dev              = "करणे यजः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BUte karaRe yajaH kft RiniH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भूते करणे यजः कृत् णिनिः",
    padaccheda_dev        = "करणे यजः",
    why_dev               = "धातोः कृत्-प्रत्ययः [करणे यजः] विहितः (३.२.85)।",
    anuvritti_from        = ('3.1.1',),
    apavada_of            = ("3.2.102",),      # bhūte karmaṇi / kartari: the special kṛt takes the site from niṣṭhā
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
