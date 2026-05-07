"""
7.3.78  पाघ्राध्मास्थाम्नादण्ड्या…  —  VIDHI (narrow: corrected-v2 **P010** *yam* → *yacch*)

*Śāstra (laghu):* **pā-ghrā-dhmā-sthmā-mnā-daṇḍyā…** block includes *yam* → *yacch* before a
following *sārvadhātuka* *vikaraṇa* *śap* residue (*ac*).

Engine: ``corrected_v2_P010_7_3_78_arm`` — *dhātu* ``yam`` immediately before a ``Term``
whose sole phoneme is ``a`` (*śap* residue).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence

_META_ARM = "corrected_v2_P010_7_3_78_arm"


def _hit(state: State) -> int | None:
    if not state.meta.get(_META_ARM):
        return None
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        if "".join(v.slp1 for v in t.varnas) != "yam":
            continue
        nxt = state.terms[i + 1]
        if len(nxt.varnas) != 1 or nxt.varnas[0].slp1 != "a":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _hit(state) is not None


def act(state: State) -> State:
    i = _hit(state)
    if i is None:
        return state
    state.terms[i].varnas = list(parse_slp1_upadesha_sequence("yacC"))
    state.samjna_registry["7.3.78_P010_yam_to_yacC"] = True
    state.meta.pop(_META_ARM, None)
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.78",
    sutra_type=SutraType.VIDHI,
    text_slp1="pA GsnA ... yacC ... (narrow P010)",
    text_dev="पाघ्राध्मास्थाम्ना… (यम्→यच्छ्, प०१०)",
    padaccheda_dev="पा-घ्रा-ध्मा-स्था-म्ना-दण्ड्या…",
    why_dev="यम्-धातोः यच्छ्-आदेशः — प०१० संक्षिप्तम्।",
    anuvritti_from=("7.3.69",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
