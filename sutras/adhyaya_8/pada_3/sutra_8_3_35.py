"""
8.3.35  शर्परे विसर्जनीयः  —  VIDHI

Padaccheda: शर्परे । विसर्जनीयः

शर्परे विसर्जनीयः (8.3.35)
Pāṭha: ashtadhyayi.com data.txt row i=83035 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from sutras.adhyaya_8.pada_3._visarga import KU_PU, SHAR, seam


def _site(state: State):
    """khar followed by a śar (kṣ, ps, ts …): the visarga stays, neither s (8.3.34) nor jihvāmūlīya / upadhmānīya (8.3.37) — Kāśikā: vāsaḥ kṣaumam, adbhiḥ psātam."""
    h = seam(state)
    return h[0] if h and h[2] in SHAR else None


def cond(state: State) -> bool:
    return _site(state) is not None

def act(state: State) -> State:
    _site(state).tags.add("visarga_settled")
    return state

SUTRA = SutraRecord(
    sutra_id              = "8.3.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Sarpare visarjanIyaH",
    text_dev              = "शर्परे विसर्जनीयः",
    samagra_slp1          = "Sar-pare Kari visarjanIyasya visarjanIyaH",
    samagra_dev           = "शर्-परे खरि विसर्जनीयस्य विसर्जनीयः",
    padaccheda_dev        = "शर्परे । विसर्जनीयः",
    why_dev               = "(सूत्रम् 8.3.35) शर्परे विसर्जनीयः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
