"""
6.4.37  अनुदात्तोपदेशवनतितनोत्यादीनाम् अनुनासिकलोपो झलि क्ङिति  —  VIDHI (narrow demo)

Narrow v3 (संगसीष्ट / ``saGgasIzwa``):
  When the *dhātu* ``gam`` retains a final *anunāsika* ``m`` before a *jhal*‑initial
  *kṅiti* pratyaya (here: **3.4.102** ``ling_sIyuw`` tagged ``kngiti``), drop that
  trailing ``m``.

Engine:
  - recipe arms ``state.meta['6_4_37_gam_anunasika_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import JHAL


def cond(state: State) -> bool:
    if not state.meta.get("6_4_37_gam_anunasika_arm"):
        return False
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "gam":
            continue
        if not t.varnas or t.varnas[-1].slp1 != "m":
            continue
        if t.meta.get("6_4_37_gam_m_lopa_done"):
            return False
        if i + 1 >= len(state.terms):
            return False
        nxt = state.terms[i + 1]
        if "ling_sIyuw" not in nxt.tags or "kngiti" not in nxt.tags:
            return False
        if not nxt.varnas:
            return False
        return nxt.varnas[0].slp1 in JHAL
    return False


def act(state: State) -> State:
    if not cond(state):
        return state
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != "gam":
            continue
        if t.varnas and t.varnas[-1].slp1 == "m":
            t.varnas.pop()
            t.meta["6_4_37_gam_m_lopa_done"] = True
            state.meta["6_4_37_gam_anunasika_arm"] = False
            break
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.37",
    sutra_type=SutraType.VIDHI,
    text_slp1="anudAttopadeza vanatitanotyAdInAm anunAsika lopaH Jali kNiti",
    text_dev=(
        "अनुदात्तोपदेशवनतितनोत्यादीनामनुनासिकलोप झलि क्ङिति (डेमो-खण्डः)"
    ),
    padaccheda_dev=(
        "अनुदात्तोपदेश-… / अनुनासिकस्य / लोपः / झलि / क्ङिति"
    ),
    why_dev="\"गम्\"-ङ्गे झलादौ क्ङिति परे म्-लोपः (संगसीष्ट)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
