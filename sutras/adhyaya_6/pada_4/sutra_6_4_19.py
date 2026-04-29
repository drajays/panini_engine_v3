"""
6.4.19  छ्छ्वोः शूडनुनासिके च  —  VIDHI (narrow demo)

Demo slice (पृष्ट्वा):
  After samprasāraṇa, for dhātu `pfcC` (pracch), replace final `cC` (cch) by `S`
  (ś) before a kṅit/kitvat suffix (tagged ``kngiti``).

Engine:
  - requires a following pratyaya tagged ``kngiti``.
  - narrow: operates only on the primary dhātu term with upadeśa `pfcC`.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _kngiti_present(state: State) -> bool:
    return any("kngiti" in t.tags for t in state.terms if "pratyaya" in t.tags)


def cond(state: State) -> bool:
    if not _kngiti_present(state):
        return False
    if not state.terms:
        return False
    dh = state.terms[0]
    if "dhatu" not in dh.tags:
        return False
    if (dh.meta.get("upadesha_slp1") or "").strip() != "pfcC":
        return False
    if dh.meta.get("6_4_19_cch_to_sh_done"):
        return False
    if len(dh.varnas) < 2:
        return False
    return dh.varnas[-2].slp1 == "c" and dh.varnas[-1].slp1 == "C"


def act(state: State) -> State:
    if not cond(state):
        return state
    dh = state.terms[0]
    # Replace final cC by S.
    dh.varnas = dh.varnas[:-2] + [mk("S")]
    dh.meta["6_4_19_cch_to_sh_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.19",
    sutra_type=SutraType.VIDHI,
    text_slp1="cCvoH SUq anunAsike ca (narrow)",
    text_dev="च्छ्वोः शूडनुनासिके च",
    padaccheda_dev="च्छ्वोः / शूड् / अनुनासिके / च",
    why_dev="क्ङिति परे (पृच्छ्) अन्त्य-च्छ् → श् (पृष्ट्वा-पूर्वम्)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

