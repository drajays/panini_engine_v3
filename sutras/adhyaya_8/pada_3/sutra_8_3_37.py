"""
8.3.37  कुप्वोः ≍क≍पौ च  —  VIDHI

Padaccheda: कुप्वोः । XकXपौ । च

कुप्वोः XकXपौ च (8.3.37)
Pāṭha: ashtadhyayi.com data.txt row i=83037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from sutras.adhyaya_8.pada_3._visarga import KU_PU, SHAR, seam


def _site(state: State):
    """a k/p-varga letter after the visarga: jihvāmūlīya / upadhmānīya, or the visarga itself (cakāra) — vṛkṣa(ḥ) karoti, vṛkṣa(ḥ) phalati."""
    h = seam(state)
    return h[0] if h and h[1] in KU_PU and h[2] not in SHAR else None


def cond(state: State) -> bool:
    return _site(state) is not None

def act(state: State) -> State:
    st = state
    left, nxt, _ = seam(st)
    left.varnas[-1] = mk("Z" if nxt in "kK" else "V")      # kapau uccāraṇārthau: jihvāmūlīya / upadhmānīya
    left.tags.add("visarga_settled")
    return st

SUTRA = SutraRecord(
    sutra_id              = "8.3.37",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    r1_form_identity_exempt = True,
    text_slp1             = 'kupvoH kapO ca',
    text_dev              = 'कुप्वोः ≍क≍पौ च',
    samagra_slp1          = "visarjanIyasya kupvoH kapO visarjanIyaH ca",
    samagra_dev           = "विसर्जनीयस्य कुप्वोः ≍क≍पौ विसर्जनीयः च",
    padaccheda_dev        = "कुप्वोः । XकXपौ । च",
    why_dev               = "(सूत्रम् 8.3.37) कुप्वोः XकXपौ च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
