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


def _matches_nvul(state: State) -> bool:
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


def _matches_lyuw(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    pr = state.terms[-1]
    if "krt" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "lyuw":
        return False
    if pr.meta.get("yu_to_ana_done"):
        return False
    if "".join(v.slp1 for v in pr.varnas) != "yu":
        return False
    return True


def _matches_tyup(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    pr = state.terms[-1]
    if "taddhita" not in pr.tags:
        return False
    if pr.meta.get("upadesha_slp1") != "tyup":
        return False
    if pr.meta.get("tyu_to_tana_done"):
        return False
    if "".join(v.slp1 for v in pr.varnas) != "tyu":
        return False
    return True


def _matches(state: State) -> bool:
    return _matches_nvul(state) or _matches_lyuw(state) or _matches_tyup(state)


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if _matches_nvul(state):
        pr = state.terms[-1]
        pr.varnas = [mk("a"), mk("k")]
        pr.meta["vu_to_ak_done"] = True
        pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "Nvul")
        pr.meta["upadesha_slp1"] = "ak"
        return state
    if _matches_lyuw(state):
        pr = state.terms[-1]
        pr.varnas = [mk("a"), mk("n"), mk("a")]
        pr.meta["yu_to_ana_done"] = True
        pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "lyuw")
        pr.meta["upadesha_slp1"] = "ana"
        return state
    if _matches_tyup(state):
        pr = state.terms[-1]
        pr.varnas = [mk("t"), mk("a"), mk("n"), mk("a")]
        pr.meta["tyu_to_tana_done"] = True
        pr.meta["upadesha_slp1_original"] = pr.meta.get("upadesha_slp1_original", "tyup")
        pr.meta["upadesha_slp1"] = "tana"
        return state
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.1",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "yuvor anAkau",
    text_dev       = "युवोरनाकौ",
    padaccheda_dev = "युवोः अनाकौ",
    why_dev        = "‘यु’-‘वु’-स्थाने ‘अन्’-‘अक्’ आदेशः (ण्वुल् / ल्युट् इति संकीर्णम्)।",
    anuvritti_from = ("7.1.0",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

