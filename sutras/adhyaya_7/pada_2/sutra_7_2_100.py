"""
7.2.100  अचि र ऋतः  —  VIDHI

Padaccheda: अचि रः ऋतः

अचि र ऋतः (7.2.100)
Pāṭha: ashtadhyayi.com data.txt row i=72100 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, is_stem, vowel_initial
from phonology import mk

def _site(state: State):
    """अचि र ऋतः — the ṛ of तिसृ / चतसृ becomes r before an ac-initial vibhakti: तिस्रः, चतस्रः (apavāda of guṇa, dīrgha and 6.1.77)."""
    hit = anga_and_sup(state, "7.2.100")
    if hit is None:
        return None
    anga, sup = hit
    if not anga.meta.get("7_2_99_done") or anga.meta.get("7_2_100_done") or not vowel_initial(sup):
        return None
    if (sup.meta.get("upadesha_slp1") or "").strip() == "Am":
        return None            # आमि नुट् takes it first (Kāśikā 6.4.4: पूर्वविप्रतिषेधेन): तिसृणाम्, not *तिस्राम्
    return anga if anga.varnas[-1].slp1 == "f" else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    anga.varnas[-1] = mk("r")
    anga.meta["7_2_100_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.2.100",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "aci ra ftaH",
    text_dev              = "अचि र ऋतः",
    samagra_slp1          = "tisfcatasf aci viBaktO ftaH raH",
    samagra_dev           = "तिसृचतसृ अचि विभक्तौ ऋतः रः",
    padaccheda_dev        = "अचि रः ऋतः",
    why_dev               = "(सूत्रम् 7.2.100) अचि र ऋतः।",
    anuvritti_from        = ('7.1.1',),
    apavada_of            = ("7.3.110", "6.1.102", "6.1.103", "6.1.111", "6.1.77"),     # Kāśikā 7.2.100: पूर्वसवर्णोत्त्वङिसर्वनामस्थानगुणानामपवादः
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
