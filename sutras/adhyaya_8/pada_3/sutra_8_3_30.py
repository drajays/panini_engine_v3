"""
8.3.30  नश्च  —  VIDHI

Padaccheda: नः च

नश्च (8.3.30)
Pāṭha: ashtadhyayi.com data.txt row i=83030 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

_AGAMA = "D"        # dhuṭ minus its it ṭ; 8.4.55 (khari ca) turns the dh to t before the s: भवान्त्साये


def _site(state: State):
    """नश्च: after a pada-final n, the s of the next pada (here the s of su) may take dhuṭ: प्रशान्त्सु / प्रशान्सु."""
    if not state.tripadi_zone or len(state.terms) != 1:
        return None
    t = state.terms[0]
    for k in range(len(t.varnas) - 1):
        if (t.varnas[k].slp1 == "n" and t.varnas[k + 1].slp1 == "s" and "pratyaya_start_v" in t.varnas[k + 1].tags
                and not t.meta.get("8_3_30_done")):
            return t, k
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, k = _site(state)
    v = mk(_AGAMA)
    v.tags.add("dhut_agama")
    t.varnas.insert(k + 1, v)
    t.meta["8_3_30_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.30",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    text_slp1             = "naSca",
    text_dev              = "नश्च",
    samagra_slp1          = "padasya naH si Duw vA",
    samagra_dev           = "पदस्य नः सि धुट् वा",
    padaccheda_dev        = "नः च",
    why_dev               = "(सूत्रम् 8.3.30) नश्च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
