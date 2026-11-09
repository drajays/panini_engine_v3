"""
7.4.12  शॄदॄप्रां ह्रस्वो वा  —  VIBHASHA

Padaccheda: शॄ-दॄ-प्राम् ह्रस्वः वा

शृदॄप्रां ह्रस्वो वा (7.4.12)
Pāṭha: ashtadhyayi.com data.txt row i=74012 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_ROOTS = frozenset({"SF", "dF", "pF"})      # śṝ, dṝ, pṝ
_BLOCKS = ("7.4.11",)                       # the hrasva reading leaves 7.4.11's guṇa out; the other reading keeps it


def _find(state: State):
    """शॄ दॄ पॄ in liṭ (Kāśikā: विशश्रतुः / विशशरतुः)."""
    from sutras.adhyaya_7.pada_4.sutra_7_4_11 import _lit_dhatu
    t = _lit_dhatu(state)
    if t is None or not t.varnas or t.varnas[-1].slp1 != "F":
        return None
    return t if (t.meta.get("upadesha_slp1") or "").replace("~", "").strip() in _ROOTS else None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    _find(state).varnas[-1] = mk("f")
    state.blocked_sutras.update(_BLOCKS)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.12",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = 'SFdFprAM hrasvo vA',
    text_dev              = 'शॄदॄप्रां ह्रस्वो वा',
    samagra_slp1          = "aNgasya SFdFprAm hrasvaH vA guRaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य शॄदॄप्राम् ह्रस्वः वा गुणः",
    padaccheda_dev        = "शॄ-दॄ-प्राम् ह्रस्वः वा",
    why_dev               = "(सूत्रम् 7.4.12) शृदॄप्रां ह्रस्वो वा।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = True,      # hrasva is the default reading; explore() gives the guṇa one
    vibhasha_scope        = cond,
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
