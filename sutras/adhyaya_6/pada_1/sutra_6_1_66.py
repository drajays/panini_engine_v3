"""
6.1.66  हल्ङ्याब्भ्यो दीर्घात् सुतिपृक्तं हल्  —  VIDHI

Narrow v3: elide apṛkta **s** (``su`` after it-lopa) after a long-vowel
upadhā **tṛc** stem — ``cetAn`` + ``s`` → ``cetAn``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import HAL
from phonology.pratyahara import is_dirgha


def cond(state: State) -> bool:
    if not state.meta.get("trc_nom_sg_pipeline"):
        return False
    if len(state.terms) < 2:
        return False
    ang = state.terms[0]
    sup = state.terms[-1]
    if "prātipadika" not in ang.tags or "sup" not in sup.tags:
        return False
    if ang.meta.get("apṛkta_hal_lopa_6_1_66_done"):
        return False
    vs = ang.varnas
    if len(vs) < 3:
        return False
    if vs[-1].slp1 != "n":
        return False
    if not is_dirgha(vs[-2].slp1):
        return False
    if len(sup.varnas) != 1:
        return False
    if sup.varnas[0].slp1 != "s":
        return False
    if sup.varnas[0].slp1 not in HAL:
        return False
    return True


def act(state: State) -> State:
    state.terms.pop()
    state.meta["apṛkta_hal_lopa_6_1_66_done"] = True
    state.meta["pratyaya_lopa_nimitta"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.66",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "halNyAByo dIrGAt suti pfktam hal",
    text_dev       = "हल्ङ्याब्भ्यो दीर्घात् सुतिपृक्तं हल्",
    padaccheda_dev = "हल्-ङि-आप्-भ्यः दीर्घात् सुति पृक्तं हल्",
    why_dev        = "दीर्घात् परस्य अपृक्त हल्-लोपः (सु→स्) — तृच्-पथ।",
    anuvritti_from = ("6.1.65",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
