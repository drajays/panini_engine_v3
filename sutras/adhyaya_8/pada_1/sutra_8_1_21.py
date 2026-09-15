"""
8.1.21  बहुवचने वस्नसौ  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=801021
- Kāśikā: युष्माकम् → वस् (बहुवचन-पदस्य आदेशः)
- Cross-validation: pipelines/sthanivat_anal_ashrita_lesson.py

**1.1.56** extends *padatva* to *vas* for **8.2.66** *padānta* rules.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import PADATVA, adesha_substitute_varnas


def _find_pada(state: State) -> int | None:
    if state.meta.get("8_1_21_vas_done"):
        return None
    if not (
        state.meta.get("sthanivat_lesson_8_1_21")
        or state.meta.get("prakriya_yuSmAkam_vas_adesha")
    ):
        return None
    for i, t in enumerate(state.terms):
        if "pada" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in {"yuSmAkam", "yuSmAkamH"} and not t.meta.get("8_1_21_vas_done"):
            return i
    return None


def cond(state: State) -> bool:
    if state.tripadi_zone and not state.meta.get("sthanivat_lesson_8_1_21"):
        return False
    return _find_pada(state) is not None


def act(state: State) -> State:
    i = _find_pada(state)
    if i is None:
        return state
    t = state.terms[i]
    adesha_substitute_varnas(
        t,
        "vas",
        state,
        sutra_id="8.1.21",
        gunadharmas=frozenset({PADATVA}),
    )
    t.meta["8_1_21_vas_done"] = True
    state.meta["8_1_21_vas_done"] = True
    state.meta["sandhi_kind"] = "8.1.21"
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.21",
    sutra_type=SutraType.VIDHI,
    r1_form_identity_exempt=True,
    text_slp1="bahuvacane vasnasO",
    text_dev="बहुवचने वस्नसौ",
    padaccheda_dev="बहुवचनस्य वस्-नसौ",
    why_dev="बहुवचन-पदस्य वस्-आदेशः; स्थानिवद्भावेन पदत्वम् (८.२.६६)।",
    anuvritti_from=("8.1.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
