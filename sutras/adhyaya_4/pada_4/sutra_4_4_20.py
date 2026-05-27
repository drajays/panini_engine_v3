"""
Vt. **4.4.20**  क्त्रेर्मम् नित्यम्  —  VIDHI (narrow **corrected-v2 P003**)

Teaching bundle row: obligatory **m** augment (*mam*) after *ktri* before *it*-*lopa*,
yielding ``ktrim`` upadeśa (**P003-A/B/C**).

Machine slice: ``state.meta['corrected_v2_P003_mam_augment_arm']`` + trailing *ktri*
``Term`` → rewrite to ``ktrim``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

META_ARM = "corrected_v2_P003_mam_augment_arm"


def cond(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    pr = state.terms[-1]
    if pr.kind != "pratyaya":
        return False
    if (pr.meta.get("upadesha_slp1") or "").strip() != "ktri":
        return False
    return True


def act(state: State) -> State:
    pr = state.terms[-1]
    pr.varnas = list(parse_slp1_upadesha_sequence("ktrim"))
    pr.meta["upadesha_slp1"] = "ktrim"
    return state


SUTRA = SutraRecord(
    sutra_id="4.4.20",
    sutra_type=SutraType.VIDHI,
    text_slp1="ktrem mam nityam",
    text_dev="क्त्रेर्मम् नित्यम्",
    padaccheda_dev="क्त्रेः मम् नित्यम्",
    why_dev="क्त्रि-प्रत्ययस्य नित्यं मम् आगमः (प००३ आर्म्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
