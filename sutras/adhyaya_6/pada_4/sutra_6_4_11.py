"""
6.4.11  अप्तृन्तृच्…  —  VIDHI

Narrow v3:
  • ``…an`` + ``s``-initial *sup* (``cetan`` → ``cetAn`` before ``su``).
  • ``prakriya_21`` — ``hotar``-shaped *tṛc* stem (``…a`` + ``r`` finale) before
    ``am`` *sarvanāmasthāna*: penultimate hrasa ``a`` → **dīrgha** (``hotAr``).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import is_hrasva


def _eligible_cetan_path(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    ang = state.terms[0]
    sup = state.terms[-1]
    if "krt_tfc" not in ang.tags or "prātipadika" not in ang.tags or "sup" not in sup.tags:
        return False
    if ang.meta.get("upadha_dirgha_6_4_11_done"):
        return False
    vs = ang.varnas
    if len(vs) < 3:
        return False
    if vs[-1].slp1 != "n":
        return False
    penult_v = vs[-2].slp1
    if not is_hrasva(penult_v):
        return False
    if not sup.varnas or sup.varnas[0].slp1 != "s":
        return False
    return True


def _eligible_hotr_prakriya_21(state: State) -> bool:
    if not state.meta.get("prakriya_21_6_4_11_arm"):
        return False
    if len(state.terms) < 2:
        return False
    ang = state.terms[-2]
    sup = state.terms[-1]
    if "krt_tfc" not in ang.tags or "prātipadika" not in ang.tags:
        return False
    if "sup" not in sup.tags:
        return False
    if (sup.meta.get("upadesha_slp1") or "").strip() != "am":
        return False
    if ang.meta.get("upadha_dirgha_6_4_11_hotr_done"):
        return False
    vs = ang.varnas
    if len(vs) < 2:
        return False
    if vs[-1].slp1 != "r":
        return False
    penult_v = vs[-2].slp1
    if penult_v != "a":
        return False
    return True


def cond(state: State) -> bool:
    return _eligible_cetan_path(state) or _eligible_hotr_prakriya_21(state)


def act(state: State) -> State:
    if _eligible_cetan_path(state):
        ang = state.terms[0]
        i = len(ang.varnas) - 2
        v = ang.varnas[i].slp1
        long_map = {"a": "A", "i": "I", "u": "U", "f": "F", "x": "X"}
        rep = long_map.get(v, v)
        ang.varnas[i] = mk(rep)
        ang.meta["upadha_dirgha_6_4_11_done"] = True
        return state
    if _eligible_hotr_prakriya_21(state):
        ang = state.terms[-2]
        i = len(ang.varnas) - 2
        v = ang.varnas[i].slp1
        long_map = {"a": "A", "i": "I", "u": "U", "f": "F", "x": "X"}
        rep = long_map.get(v, v)
        ang.varnas[i] = mk(rep)
        ang.meta["upadha_dirgha_6_4_11_hotr_done"] = True
        state.meta.pop("prakriya_21_6_4_11_arm", None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.11",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "aptfntfc svf... (narrow)",
    text_dev       = "अप्तृन्तृच्…",
    padaccheda_dev = "अप्तृन्-तृच्-…",
    why_dev        = "तृण्-विषये उपधा-दीर्घः सर्वनामस्थाने (चेता-पथ)।",
    anuvritti_from = ("6.4.10",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
