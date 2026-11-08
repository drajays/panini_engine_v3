"""
7.2.45  रधादिभ्यश्च  —  VIBHASHA

Padaccheda: रध-आदिभ्यः च

रधादिभ्यश्च (7.2.45)
Pāṭha: ashtadhyayi.com data.txt row i=72045 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_7.pada_2.sutra_7_2_44 import _BLOCKS, site, toggle_it

_NAMES = frozenset({"raDa","RaSa","tfpa","dfpa","druha","muha","zRuha","zRiha"})


def _site(state: State):
    """रधादिभ्यश्च — radh, naś, tṛp, dṛp, druh, muh, snuh, snih: the iṭ before a val-initial ārdhadhātuka is optional."""
    return site(state, _NAMES)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return toggle_it(state)


SUTRA = SutraRecord(
    sutra_id              = "7.2.45",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = "raDAdiByaSca",
    text_dev              = "रधादिभ्यश्च",
    samagra_slp1          = "aNgasya raDAdiByaH ca ArDaDAtukasya iw valAdeH vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य रधादिभ्यः च आर्धधातुकस्य इट् वलादेः वा",
    padaccheda_dev        = "रध-आदिभ्यः च",
    why_dev               = "(सूत्रम् 7.2.45) रधादिभ्यश्च।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # the default reading is 7.2.35 / 7.2.10 as they stand; explore() gives the other
    vibhasha_scope        = cond,
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
