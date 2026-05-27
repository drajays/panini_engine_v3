"""
7.3.78  पाघ्राध्मास्थाम्नादण्ड्या…  —  VIDHI (yam → yacch, P010 spine)

*Narrow scope (repository):* *dhātu* ``yam`` immediately before *śap* residue ``a``
(*ś*/*p* it-lopa per **1.3.8** / **1.3.9**) → substitute ``yacC`` (यच्छ्).

Full *pā-ghrā-dhmā-sthmā-mnā-daṇḍyā…* block is not exhaustively implemented here.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _hit(state: State) -> int | None:
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "yam":
            continue
        nxt = state.terms[i + 1]
        if len(nxt.varnas) == 1 and nxt.varnas[0].slp1 == "a":
            return i
        up = (nxt.meta.get("upadesha_slp1") or "").strip()
        if up == "Sap" and len(nxt.varnas) == 1 and nxt.varnas[0].slp1 == "a":
            return i
    return None


def cond(state: State) -> bool:
    if state.samjna_registry.get("7.3.78_yam_to_yacC"):
        return False
    return _hit(state) is not None


def act(state: State) -> State:
    i = _hit(state)
    if i is None:
        return state
    state.terms[i].varnas = list(parse_slp1_upadesha_sequence("yacC"))
    state.terms[i].meta["upadesha_slp1"] = "yacC"
    state.samjna_registry["7.3.78_yam_to_yacC"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.78",
    sutra_type=SutraType.VIDHI,
    text_slp1="pA GsnA ... yacC ... (yam P010)",
    text_dev="पाघ्राध्मास्थाम्ना… (यम्→यच्छ्)",
    padaccheda_dev="पा-घ्रा-ध्मा-स्था-म्ना-दण्ड्या…",
    why_dev="यम्-धातोः यच्छ्-आदेशः — P010 / सार्वधातुके शप्-पूर्वम्।",
    anuvritti_from=("7.3.69",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
