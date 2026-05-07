"""
7.4.25  अकृत्सार्वधातुकयोर्दीर्घः  —  VIDHI (narrow)

Teaching **P016**: before a following *sārvadhātuka* vowel affix (here *śap*
``a``), lengthen the stem-final short **a** that stands immediately before
final **y** in **``lohitay``** → **``lohitAy``** (*a* → *ā*).

Engine:
  • ``state.meta['corrected_v2_P016_7_4_25_arm']``
  • *dhātu* tape **``lohitay``** + following ``pratyaya`` whose ``upadesha_slp1``
    is **``a``** (``Sap`` residue).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _site(state: State) -> bool:
    if not state.meta.get("corrected_v2_P016_7_4_25_arm"):
        return False
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "lohitay":
            continue
        if len(t.varnas) < 2:
            continue
        if t.varnas[-1].slp1 != "y" or t.varnas[-2].slp1 != "a":
            continue
        nxt = state.terms[i + 1]
        if nxt.kind != "pratyaya":
            continue
        up_n = (nxt.meta.get("upadesha_slp1") or "").strip()
        sap_surface = len(nxt.varnas) == 1 and nxt.varnas[0].slp1 == "a"
        if up_n not in {"a", "Sap"} and not sap_surface:
            continue
        if t.meta.get("7_4_25_dirgha_done"):
            continue
        return True
    return False


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "lohitay":
            continue
        nxt = state.terms[i + 1]
        up_n = (nxt.meta.get("upadesha_slp1") or "").strip()
        sap_surface = len(nxt.varnas) == 1 and nxt.varnas[0].slp1 == "a"
        if up_n not in {"a", "Sap"} and not sap_surface:
            continue
        t.varnas[-2] = mk("A")
        t.meta["7_4_25_dirgha_done"] = True
        state.meta.pop("corrected_v2_P016_7_4_25_arm", None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.25",
    sutra_type=SutraType.VIDHI,
    text_slp1="akftsArvadhAtukayor dIrGaH",
    text_dev="अकृत्सार्वधातुकयोर्दीर्घः",
    padaccheda_dev="अकृतः / सार्वधातुकयोः / दीर्घः",
    why_dev="अकृदङ्गात् परस्मिन् सार्वधातुके अचि परे अङ्गकार्यम् (P016: लोहितय→लोहिताय)।",
    anuvritti_from=("7.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
