"""
4.2.8  कलेर्ढक्  —  VIDHI

Padaccheda: कलेः ढक्

कलेर्ढक् (4.2.8)
Pāṭha: ashtadhyayi.com data.txt row i=42008 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "dfzwa"), stems=frozenset({"kali"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "Qak")


SUTRA = SutraRecord(
    sutra_id              = "4.2.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kalerQak",
    text_dev              = "कलेर्ढक्",
    samagra_slp1          = "tena dfzwaM sAma iti kaleH Qak",
    samagra_dev           = "'तेन दृष्टं साम' (इति) कलेः ढक्",
    padaccheda_dev        = "कलेः ढक्",
    why_dev               = "(सूत्रम् 4.2.8) कलेर्ढक्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.2.7',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
