"""
7.2.48  तीषसहलुभरुषरिषः  —  VIBHASHA

Padaccheda: ति इष-सह-लुभ-रुष-रिषः

तीषसहलुभरुषरिषः (7.2.48)
Pāṭha: ashtadhyayi.com data.txt row i=72048 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_7.pada_2.sutra_7_2_44 import _BLOCKS, site, toggle_it

_NAMES = frozenset({"iza","izu","zaha","luBa","ruza","riza"})


def _site(state: State):
    """तीषसहलुभरुषरिषः — iṣ, sah, lubh, ruṣ, riṣ: the iṭ before a ta-initial ārdhadhātuka is optional (eṣṭā / eṣitā)."""
    return site(state, _NAMES, first="t")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return toggle_it(state)


SUTRA = SutraRecord(
    sutra_id              = "7.2.48",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = "tIzasahaluBaruzarizaH",
    text_dev              = "तीषसहलुभरुषरिषः",
    samagra_slp1          = "aNgasya ti izasahaluBaruzarizaH ArDaDAtukasya iw valAdeH vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ति इषसहलुभरुषरिषः आर्धधातुकस्य इट् वलादेः वा",
    padaccheda_dev        = "ति इष-सह-लुभ-रुष-रिषः",
    why_dev               = "(सूत्रम् 7.2.48) तीषसहलुभरुषरिषः।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # the default reading is 7.2.35 / 7.2.10 as they stand; explore() gives the other
    vibhasha_scope        = cond,
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
