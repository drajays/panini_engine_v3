"""
3.2.38  प्रियवशे वदः खच्  —  VIDHI

Padaccheda: प्रिय-वशे वदः खच्

krt-suffix rule: प्रियवशे वदः खच् (38)
Pāṭha: ashtadhyayi.com data.txt row i=32038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, upapada_site, no_upasarga
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return upapada_site(state, "karman", dhatus=frozenset({"vada~"}), stems=frozenset({"priya", "vaSa"})) if no_upasarga(state) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_krt(state, "Kac")


SUTRA = SutraRecord(
    sutra_id              = "3.2.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "priyavaSe vadaH Kac",
    text_dev              = "प्रियवशे वदः खच्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH priyavaSe vadaH Kac kft karmaRi anupasarge supi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः प्रियवशे वदः खच् कृत् कर्मणि अनुपसर्गे सुपि",
    padaccheda_dev        = "प्रिय-वशे वदः खच्",
    why_dev               = "धातोः कृत्-प्रत्ययः [प्रियवशे वदः खच्] विहितः (३.२.38)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
