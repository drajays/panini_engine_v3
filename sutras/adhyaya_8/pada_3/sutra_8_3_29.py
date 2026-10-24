"""
8.3.29  डः सि धुट्  —  VIDHI

Padaccheda: डः सि धुट्

डः सि धुट् (8.3.29)
Pāṭha: ashtadhyayi.com data.txt row i=83029 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from engine.krt_eligibility import tripadi_gate_eligible

def _site(state: State):
    """ङः सि धुट् वा — a pada-final ḍ before the s of su (saptamī plural): धुट् (t) may stand between: ध्रुट्सु / ध्रुट्त्सु, लिट्सु / लिट्त्सु."""
    if not state.tripadi_zone or len(state.terms) != 1:
        return None
    t = state.terms[0]
    for k in range(len(t.varnas) - 1):
        if t.varnas[k].slp1 == "q" and t.varnas[k + 1].slp1 == "s" and "pratyaya_start_v" in t.varnas[k + 1].tags \
                and not t.meta.get("8_3_29_done"):
            return t, k
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t, k = _site(state)
    t.varnas.insert(k + 1, mk("t"))
    t.meta["8_3_29_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.29",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    text_slp1             = "qaH si Duw",
    text_dev              = "डः सि धुट्",
    samagra_slp1          = "padasya qaH si Duw vA",
    samagra_dev           = "पदस्य डः सि धुट् वा",
    padaccheda_dev        = "डः सि धुट्",
    why_dev               = "(सूत्रम् 8.3.29) डः सि धुट्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
