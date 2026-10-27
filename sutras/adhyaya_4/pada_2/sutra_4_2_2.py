"""
4.2.2  लाक्षारोचनाशकलकर्दमाट्ठक्  —  VIDHI

Padaccheda: लाक्षा-रोचनात् (शकलकर्दमात् ) ठक्

लाक्षारोचना(शकलकर्दमा)ट्ठक् (4.2.2)
Pāṭha: ashtadhyayi.com data.txt row i=42002 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return taddhita_site(state, ok=vivaksita(state, "taddhitArtha", "rakta"), stems=frozenset({"lAkzA","rocanA","Sakala","kardama"}))


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, "Wak")


SUTRA = SutraRecord(
    sutra_id              = "4.2.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'lAkzArocanASakalakardamAwWak',
    text_dev              = 'लाक्षारोचनाशकलकर्दमाट्ठक्',
    samagra_slp1          = "tena raktaM rAgAt iti lAkzA-rocanA-Sakala-kardamAt Wak pratyayaH",
    samagra_dev           = "'तेन रक्तं रागात्' (इति) लाक्षा-रोचना-शकल-कर्दमात् ठक् प्रत्ययः",
    padaccheda_dev        = "लाक्षा-रोचनात् (शकलकर्दमात् ) ठक्",
    why_dev               = "(सूत्रम् 4.2.2) लाक्षारोचना(शकलकर्दमा)ट्ठक्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
