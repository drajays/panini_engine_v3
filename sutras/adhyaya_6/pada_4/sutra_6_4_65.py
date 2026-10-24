"""
6.4.65  ईद्यति  —  VIDHI

Padaccheda: ईत् यति

ईद्यति (6.4.65)
Pāṭha: ashtadhyayi.com data.txt row i=64065 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology import mk

def _site(state: State):
    """ईद्यति — an ā-final aṅga before the kṛtya yat: ā → ī (dīya- → deya by 7.3.84, ghīya- → gheya)."""
    live = [t for t in state.terms if t.varnas]
    for left, nxt in zip(live, live[1:]):
        if "dhatu" in left.tags and left.varnas[-1].slp1 == "A" and nxt.meta.get("upadesha_slp1") == "yat" and "krt" in nxt.tags:
            return left
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas[-1] = mk("I")
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Idyati",
    text_dev              = "ईद्यति",
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke It yati kNiti AtaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके ईत् यति क्ङिति आतः",
    padaccheda_dev        = "ईत् यति",
    why_dev               = "(सूत्रम् 6.4.65) ईद्यति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
