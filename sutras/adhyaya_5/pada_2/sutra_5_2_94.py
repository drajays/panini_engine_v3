"""
5.2.94  तदस्यास्त्यर्थे मतुप्  —  VIDHI (narrow)

Glass-box: when a recipe arms ``state.meta["5_2_94_matup_arm"]`` and the tape is
``[prātipadika, internal sup]`` (second ``Term`` tagged ``sup``), append the
*matup* *upadeśa* ``matu~p`` (``u`` with *anunāsika* for **1.3.2**) as a
*taddhita* ``Term``.

Cross-check *pāṭha*: ``data/sutrANi.tsv`` / machine row *i*=50294.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def cond(state: State) -> bool:
    if not state.meta.get("5_2_94_matup_arm"):
        return False
    if len(state.terms) != 2:
        return False
    if "sup" not in state.terms[1].tags:
        return False
    if state.meta.get("5_2_94_matup_done"):
        return False
    return True


def act(state: State) -> State:
    if not state.meta.get("5_2_94_matup_arm"):
        return state
    if len(state.terms) != 2 or "sup" not in state.terms[1].tags:
        return state
    if state.meta.get("5_2_94_matup_done"):
        return state
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("matu~p"),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": "matu~p"},
    )
    state.terms.append(pr)
    state.meta["5_2_94_matup_arm"] = False
    state.meta["5_2_94_matup_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "5.2.94",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tad asyAsti-arthe matup",
    text_dev       = "तदस्यास्त्यर्थे मतुप्",
    padaccheda_dev = "तद्-अस्य / अस्ति-अर्थे / मतुप्",
    why_dev        = "‘तदस्य अस्ति’ इत्यर्थे मतुप्-प्रत्ययः (गोमान्-प्रक्रिया)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
