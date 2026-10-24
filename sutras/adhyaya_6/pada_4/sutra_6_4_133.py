"""
6.4.133  श्वयुवमघोनामतद्धिते  —  VIDHI

Padaccheda: श्व-युव-मघोनाम् अ-तद्धिते

श्वयुवमघोनामतद्धिते (6.4.133)
Pāṭha: ashtadhyayi.com data.txt row i=64133 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup, is_stem, vowel_initial
from phonology import mk
from engine.state import State

def _site(state: State):
    """श्वयुवमघोनामतद्धिते — the aṅgas श्वन्, युवन्, मघवन् (with tadantavidhi: अतिश्वन्) as a bha (before an ac-initial sup that is not
    sarvanāmasthāna): the v takes samprasāraṇa — शुनः, यूनः, मघोनः (6.1.108 pūrvarūpa, 6.1.87 / 6.1.101 join what is left)."""
    hit = anga_and_sup(state, "6.4.133")
    if hit is None:
        return None
    anga, sup = hit
    if not sup.varnas or not (vowel_initial(sup) or sup.varnas[0].slp1 == "y"):
        return None                  # (bha is yaci: the loose onset of 1.4.18 also tags the stem before su, which is a pada)
    if "bha" not in anga.tags or anga.meta.get("6_4_133_done") or not is_stem(anga, "Svan", "yuvan", "maGavan", tadanta=True):
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    stem = "".join(v.slp1 for v in anga.varnas)
    if stem.endswith("Svan"):
        new, n = "un", 3        # v a n → u n          (S v a n → S u n)
    elif stem.endswith("yuvan"):
        new, n = "Un", 4        # u v a n → U n        (y u v a n → y U n)
    else:
        new, n = "on", 4        # a v a n → o n        (ma G a v a n → ma G o n)
    anga.varnas[-n:] = [mk(x) for x in new]
    anga.meta["6_4_133_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.133",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "SvayuvamaGonAmatadDite",
    text_dev              = "श्वयुवमघोनामतद्धिते",
    samagra_slp1          = "Sva-yuva-maGonAm Basya aNgasya atadDite samprasAraRam",
    samagra_dev           = "श्व-युव-मघोनाम् भस्य अङ्गस्य अतद्धिते सम्प्रसारणम्",
    padaccheda_dev        = "श्व-युव-मघोनाम् अ-तद्धिते",
    why_dev               = "(सूत्रम् 6.4.133) श्वयुवमघोनामतद्धिते।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ("6.4.134",),     # allopo 'naḥ would drop the a first: the specific samprasāraṇa takes श्वन् / युवन् / मघवन् away from it
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
