"""
6.1.197  ञ्णित्यादिर्नित्यम्  —  ANUVADA (narrow demos)

**Pāṭha (Kāśikā on *Aṣṭ*. 6.1.197):** *ñaṇityādir nityam* — for *ṇit* / *ñit*
suffixes the first syllable is *udātta* (*ādyudātta*).

Narrow v3:
  • ``prakriya_29`` — ``gaurAvaskandin`` vocative (``sAmantrita`` + ``prakriya_29_Riti_pratyaya_demo``).
  • ``prakriya_31`` — ``imam`` accusative (*इदम्* + ``अम्`` spine in RV **इमं मे …** commentary):
    ``prakriya_31_idam_acc_demo`` + ``prakriya_31_Riti_pratyaya_demo`` →
    ``meta['prakriya_31_imam_first_udAtta_note']``.

No *svara* columns on ``Varna`` rows.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _prakriya_29_site(state: State) -> bool:
    if not state.meta.get("prakriya_29_6_1_197_arm"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if "sAmantrita" not in t0.tags:
        return False
    if t0.meta.get("upadesha_slp1") != "gaurAvaskandin":
        return False
    if "prakriya_29_Riti_pratyaya_demo" not in t0.tags:
        return False
    if t0.meta.get("prakriya_29_YiRityAdi_first_udAtta_note"):
        return False
    return True


def _prakriya_31_imam_site(state: State) -> bool:
    if not state.meta.get("prakriya_31_6_1_197_arm"):
        return False
    if not state.terms:
        return False
    t0 = state.terms[0]
    if t0.meta.get("upadesha_slp1") != "imam":
        return False
    if "prakriya_31_idam_acc_demo" not in t0.tags:
        return False
    if "prakriya_31_Riti_pratyaya_demo" not in t0.tags:
        return False
    if t0.meta.get("prakriya_31_imam_first_udAtta_note"):
        return False
    return True


def cond(state: State) -> bool:
    return _prakriya_29_site(state) or _prakriya_31_imam_site(state)


def act(state: State) -> State:
    if _prakriya_31_imam_site(state):
        state.terms[0].meta["prakriya_31_imam_first_udAtta_note"] = True
        state.meta.pop("prakriya_31_6_1_197_arm", None)
        return state
    if _prakriya_29_site(state):
        state.terms[0].meta["prakriya_29_YiRityAdi_first_udAtta_note"] = True
        state.meta.pop("prakriya_29_6_1_197_arm", None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.197",
    sutra_type=SutraType.ANUVADA,
    text_slp1="YiRityAdir nityam",
    text_dev="ञ्णित्यादिर्नित्यम्",
    padaccheda_dev="ञ्णित्यादिः / नित्यम्",
    why_dev="ञिति-निति-प्रत्यये आदिरुदात्तः (*prakriya_29* / *31*)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
