"""
3.1.32  सनाद्यन्ता धातवः  —  SAMJNA (narrow)

Glass-box role: when a sanādi pratyaya (e.g. yaG) has been attached, the whole
base is treated as dhātu again.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if state.samjna_registry.get("3.1.32_sanadyanta_dhatu"):
        return False
    return any("sanadi" in t.tags for t in state.terms)


def act(state: State) -> State:
    # P025: *ṇic* residue stays a separate ``pratyaya`` ``Term``; only the stem
    # *prakṛti* (not the *sanādi* ``Term`` itself) receives *dhātu* here.
    if state.meta.get("P025_3_1_32_arm"):
        for t in state.terms:
            if t.kind != "prakriti":
                continue
            if "sanadi" in t.tags:
                continue
            if "prātipadika" not in t.tags:
                continue
            t.tags.add("dhatu")
            t.tags.add("anga")
    else:
        for t in state.terms:
            if "sanadi" in t.tags:
                t.tags.add("dhatu")
                t.tags.add("anga")
    state.samjna_registry["3.1.32_sanadyanta_dhatu"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.32",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "sanAdyantA DAtavaH",
    text_dev       = "सनाद्यन्ता धातवः",
    padaccheda_dev = "सनादि-अन्ताः / धातवः",
    why_dev        = "सनादि-प्रत्ययान्तः समुदायः धातु-संज्ञकः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

