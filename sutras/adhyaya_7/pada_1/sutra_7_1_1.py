"""
7.1.1  युवोरनाकौ  —  VIDHI

Operational role (v3.8, kṛt Nvul agent nouns):
  After it-lopa, Nvul leaves 'vu'. This rule replaces 'vu' with 'ak'.

We implement narrowly:
  - last term is a kṛt pratyaya whose original upadeśa was Nvul and whose
    recorded it-markers include 'N' (ṇit), and whose current surface is 'vu'
  - replace pratyaya varṇas with 'a','k' and update its identity to 'ak'
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    pr = state.terms[-1]
    if "krt" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "Nvul":
        return False
    itm = pr.meta.get("it_markers", set())
    if not isinstance(itm, set) or not ("N" in itm or "R" in itm):
        return False
    if pr.meta.get("vu_to_ak_done"):
        return False
    if "".join(v.slp1 for v in pr.varnas) != "vu":
        return False
    return True


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pr = state.terms[-1]
    pr.varnas = [mk("a"), mk("k")]
    pr.meta["vu_to_ak_done"] = True
    pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "Nvul")
    pr.meta["upadesha_slp1"] = "ak"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.1",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "yuvor anAkau",
    text_dev       = "युवोरनाकौ",
    padaccheda_dev = "युवोः अनाकौ",
    why_dev        = "ण्वुल्-प्रत्ययस्य ‘वु’ शेषे ‘अक्’ आदेशः (पाचक)।",
    anuvritti_from = ("7.1.0",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

