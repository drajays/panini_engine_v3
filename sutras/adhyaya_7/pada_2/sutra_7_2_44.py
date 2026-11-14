"""
7.2.44  स्वरतिसूतिसूयतिधूञूदितो वा  —  VIBHASHA

Padaccheda: स्वरति-सूति-सूयति-धूञ्-ऊदितः वा

स्वरतिसूतिसूयतिधूञूदितो वा (7.2.44)
Pāṭha: ashtadhyayi.com data.txt row i=72044 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import HAL

_BLOCKS = ("7.2.35",)      # the iṭ-less branch
_NOT_UDIT = frozenset({"BU~"})     # 2.4.52 stamps the bhū it puts for as with the dhātupāṭha spelling BU~; that ~ is not an ū-it (bhū is not ūdit: bhaviṣyanti, not *BUsyaJi)
_NAMES = frozenset({"svf", "sUN", "sU", "DUY"})     # svarati, sūti, sūyati, dhūñ; every other root is ūdit


def site(state: State, names, first=None, ud: bool = False):
    """The dhātu (upadeśa in ``names``, or ūdit when ``ud``) before an ārdhadhātuka that begins with ``first`` (a val consonant by default)."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags or "abhyasa" in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if not (up.replace("~", "") in names or (ud and "U~" in up and up not in _NOT_UDIT)):
            continue
        for u in state.terms[i + 1:]:
            if "ardhadhatuka" in u.tags and u.varnas and (u.varnas[0].slp1 == first if first else u.varnas[0].slp1 in HAL and u.varnas[0].slp1 not in ("y", "h")):
                return t
            if u.varnas:
                break
    return None


def toggle_it(state: State) -> State:
    """The vibhāṣā on iṭ: the default reading keeps 7.2.35's iṭ (or, for an aniṭ dhātu, lacks it); the other reading reverses it."""
    if "7.2.35" in state.blocked_sutras:      # an aniṭ dhātu (7.2.10): this branch gives the iṭ back
        state.blocked_sutras.discard("7.2.35")
    else:
        state.blocked_sutras.update(_BLOCKS)
    return state


def _site(state: State):
    return site(state, _NAMES, ud=True)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    return toggle_it(state)


SUTRA = SutraRecord(
    sutra_id              = "7.2.44",
    sutra_type            = SutraType.VIBHASHA,
    text_slp1             = "svaratisUtisUyatiDUYUdito vA",
    text_dev              = "स्वरतिसूतिसूयतिधूञूदितो वा",
    samagra_slp1          = "aNgasya svaratisUtisUyatiDUYUditaH vA ArDaDAtukasya iw valAdeH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य स्वरतिसूतिसूयतिधूञूदितः वा आर्धधातुकस्य इट् वलादेः",
    padaccheda_dev        = "स्वरति-सूति-सूयति-धूञ्-ऊदितः वा",
    why_dev               = "(सूत्रम् 7.2.44) स्वरतिसूतिसूयतिधूञूदितो वा।",
    anuvritti_from        = ('7.1.1',),
    vibhasha_default      = False,     # the iṭ is the default reading; explore() gives the iṭ-less one
    vibhasha_scope        = cond,
    blocks_sutra_ids      = _BLOCKS,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
