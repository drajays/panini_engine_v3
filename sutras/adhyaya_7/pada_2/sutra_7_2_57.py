"""
7.2.57  सेऽसिचि कृतचृतच्छृदतृदनृतः  —  VIBHASHA

Padaccheda: से अ-सिचि कृत-चृत-च्छृद-तृद-नृतः

सेऽसिचि कृतचृतच्छृदतृदनृतः (7.2.57)
Pāṭha: ashtadhyayi.com data.txt row i=72057 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from sutras.adhyaya_7.pada_2.sutra_7_2_44 import _BLOCKS, site, toggle_it

_NAMES = frozenset({"kftI","cftI","CfdI","uCfdir","utfdir","nftI"})


def _site(state: State):
    """सेऽसिचि कृतचृतच्छृदतृदनृतः — kṛt, cṛt, chṛd, tṛd, nṛt: the iṭ before an s-initial ārdhadhātuka that is not sic is optional (tartsyate)."""
    return site(state, _NAMES, first="s")


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return toggle_it(state)


SUTRA = SutraRecord(
    sutra_id              = "7.2.57",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = 'sesici kftacftacCfdatfdanftaH',
    text_dev              = 'सेऽसिचि कृतचृतच्छृदतृदनृतः',
    samagra_slp1          = "aNgasya se asici kftacftacCfdatfdanftaH ArDaDAtukasya iw valAdeH vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य से असिचि कृतचृतच्छृदतृदनृतः आर्धधातुकस्य इट् वलादेः वा",
    padaccheda_dev        = "से अ-सिचि कृत-चृत-च्छृद-तृद-नृतः",
    why_dev               = "(सूत्रम् 7.2.57) सेऽसिचि कृतचृतच्छृदतृदनृतः।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # the default reading is 7.2.35 / 7.2.10 as they stand; explore() gives the other
    vibhasha_scope        = cond,
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
