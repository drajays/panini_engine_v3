"""
1.1.43  सुडनपुंसकस्य  —  SAMJNA

Narrow v3: when a recipe arms ``state.meta["1_1_43_arm"]`` and the final
``Term`` is a *sup* whose *upadeśa* begins with ``s`` (e.g. *su*-*m* row),
that affix receives the *sarvanāmasthāna* label via ``tags`` (read by **7.1.70**
/ **7.1.72** without consulting ``(vibhakti, vacana)`` in those *cond* paths).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

TAG = "sarvanamasthana"


def cond(state: State) -> bool:
    if not state.meta.get("1_1_43_arm"):
        return False
    if not state.terms:
        return False
    pr = state.terms[-1]
    if pr.kind != "pratyaya" or "sup" not in pr.tags:
        return False
    if not pr.varnas:
        return False
    if pr.varnas[0].slp1 != "s":
        return False
    if TAG in pr.tags:
        return False
    return True


def act(state: State) -> State:
    pr = state.terms[-1]
    pr.tags.add(TAG)
    state.samjna_registry["1.1.43_su_sarvanamasthana"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.43",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "suDanapuMsakasya",
    text_dev       = "सुडनपुंसकस्य",
    padaccheda_dev = "सुड्-अनपुंसकस्य",
    why_dev        = "सु-प्रत्ययः (नपुंसकाद् भिन्नः) सर्वनामस्थान-संज्ञकः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
