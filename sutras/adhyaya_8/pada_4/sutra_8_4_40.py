"""
8.4.40  ष्टुना ष्टुः  —  VIDHI (narrow: z + t → z + w)

Glass-box scope for `mArzwi`:
  After merging into one term in tripāḍī, if we see the cluster "zt" (ष् + त्),
  replace 't' with 'w' (ट्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    """
    *Tripāḍī* zone **or** ``state.meta["8_4_40_pre_tripadi_arm"]`` (e.g. *mṛṣ*+*t*
    before **8.2.1**) so *ṣ*+*t* → *ṣ*+*ṭ* does not trip the non–8.x *asiddha* gate.
    """
    if not (state.tripadi_zone or state.meta.get("8_4_40_pre_tripadi_arm")):
        return None
    if not state.terms:
        return None
    t = state.terms[0]
    if t.meta.get("8_4_40_zw_done"):
        return None
    for i in range(1, len(t.varnas)):
        if t.varnas[i - 1].slp1 == "z" and t.varnas[i].slp1 == "t":
            return (0, i)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, i = hit
    state.terms[ti].varnas[i] = mk("w")
    state.terms[ti].meta["8_4_40_zw_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.4.40",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "zwunA zwuH",
    text_dev       = "ष्टुना ष्टुः",
    padaccheda_dev = "ष्टुना / ष्टुः",
    why_dev        = "षकारस्य संयोगे तवर्गस्य टवर्गादेशः (ग्लास-बॉक्स् narrow)।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

