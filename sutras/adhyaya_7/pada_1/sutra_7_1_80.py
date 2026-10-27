"""
7.1.80  आच्छीनद्योर्नुम्  —  VIDHI

Padaccheda: आत् शी-नद्योः नुम्

आच्छीनद्योर्नुम् (7.1.80)
Pāṭha: ashtadhyayi.com data.txt row i=71080 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_7.pada_1.sutra_7_1_81 import num_site, put_num


def _site(state: State):
    from engine.registry import get_sutra
    if get_sutra("7.1.81").cond(state):      # Sap / Syan: 7.1.81 is nitya, the apavāda
        return None
    return num_site(state, "Sa")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    if anga is not None:
        put_num(anga)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.80",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_scope        = lambda state: _site(state) is not None,     # the vā gate only where nuṃ has a site
    vibhasha_default      = True,
    r1_form_identity_exempt = True,
    text_slp1             = "AcCInadyornum",
    text_dev              = "आच्छीनद्योर्नुम्",
    samagra_slp1          = "aNgasya At SI-nadyoH num SatuH vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य आत् शी-नद्योः नुम् शतुः वा",
    padaccheda_dev        = "आत् शी-नद्योः नुम्",
    why_dev               = "(सूत्रम् 7.1.80) आच्छीनद्योर्नुम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
