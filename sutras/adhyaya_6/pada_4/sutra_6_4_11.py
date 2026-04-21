"""
6.4.11  अप्तृन्तृच्…  —  VIDHI

Narrow v3: lengthen the **upadhā** (vowel before final ``n`` of ``…an``)
to **dīrgha** when **trc_nom_sg_pipeline** applies — ``cetan`` → ``cetAn``
before ``s``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import is_hrasva


def cond(state: State) -> bool:
    if not state.meta.get("trc_nom_sg_pipeline"):
        return False
    if len(state.terms) < 2:
        return False
    ang = state.terms[0]
    sup = state.terms[-1]
    if "prātipadika" not in ang.tags or "sup" not in sup.tags:
        return False
    if ang.meta.get("upadha_dirgha_6_4_11_done"):
        return False
    vs = ang.varnas
    if len(vs) < 3:
        return False
    if vs[-1].slp1 != "n":
        return False
    # Upadhā vowel before final n (…a n).
    penult_v = vs[-2].slp1
    if not is_hrasva(penult_v):
        return False
    if not sup.varnas or sup.varnas[0].slp1 != "s":
        return False
    return True


def act(state: State) -> State:
    ang = state.terms[0]
    i = len(ang.varnas) - 2
    v = ang.varnas[i].slp1
    long_map = {"a": "A", "i": "I", "u": "U", "f": "F", "x": "X"}
    rep = long_map.get(v, v)
    ang.varnas[i] = mk(rep)
    ang.meta["upadha_dirgha_6_4_11_done"] = True
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
