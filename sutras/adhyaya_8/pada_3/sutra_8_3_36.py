"""
8.3.36  वा शरि  —  VIDHI

Padaccheda: वा । शरि

वा शरि (8.3.36)
Pāṭha: ashtadhyayi.com data.txt row i=83036 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from sutras.adhyaya_8.pada_3._visarga import KU_PU, SHAR, seam


def _site(state: State):
    """a śar after the visarga: ḥ stays or goes by 8.3.34 (vṛkṣaḥ śete / vṛkṣaśśete — Kāśikā 8.3.36)."""
    h = seam(state)
    return h[0] if h and h[1] in SHAR and h[2] not in SHAR else None


def cond(state: State) -> bool:
    return _site(state) is not None

def act(state: State) -> State:
    _site(state).tags.add("visarga_settled")      # the visarga stays; declined, 8.3.34 makes it s
    return state

SUTRA = SutraRecord(
    sutra_id              = "8.3.36",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    r1_form_identity_exempt = True,
    text_slp1             = "vA Sari",
    text_dev              = "वा शरि",
    samagra_slp1          = "visarjanIyasya Sari vA visarjanIyaH",
    samagra_dev           = "विसर्जनीयस्य शरि वा विसर्जनीयः",
    padaccheda_dev        = "वा । शरि",
    why_dev               = "(सूत्रम् 8.3.36) वा शरि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
