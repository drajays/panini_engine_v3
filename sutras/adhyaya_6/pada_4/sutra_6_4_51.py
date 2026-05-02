"""
6.4.51  णेरनिटि  —  VIDHI (narrow demo)

Demo slice (हिडनीय.md):
  Before an **anid** *ārdhadhātuka* affix (here ``anIya`` from ``anIyar`` after
  it-lopa), the preceding ṇic residue on the stem closes by **luk** — modeled as
  deleting the final ``i`` that originated from ṇic on ``hiqi``.

Narrow **P037** (*āṭīṭat*): stem-final ``i`` (``Awi`` shape) before ``caY`` + *tiṅ*
residue ``t`` similarly drops (``6_4_51`` + ``P037_6_4_51_arm``).

Sets ``sthānivat_nic_block_guna`` so **7.3.86** guṇa does not re-apply (1.1.57
interaction; see note’s “ghost ṇic” story).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _matches_p037(state: State) -> bool:
    """ṇic ``i``-lopa before empty *caṅ* marker + *tin* (**P037** teaching row)."""
    if not state.meta.get("P037_6_4_51_arm"):
        return False
    if len(state.terms) < 3:
        return False
    for i in range(len(state.terms) - 2):
        anga, ca, _tin = state.terms[i], state.terms[i + 1], state.terms[i + 2]
        if "anga" not in anga.tags or "dhatu" not in anga.tags:
            continue
        if anga.meta.get("P037_6_4_51_done"):
            continue
        if not anga.varnas or anga.varnas[-1].slp1 != "i":
            continue
        if ca.meta.get("P037_caN") is not True:
            continue
        if "tin_adesha_3_4_78" not in state.terms[i + 2].tags:
            continue
        return True
    return False


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pr = state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "pratyaya" not in pr.tags:
        return False
    if anga.meta.get("6_4_51_nic_tail_i") is not True:
        return False
    if anga.meta.get("6_4_51_Reraniwi_done"):
        return False
    if pr.meta.get("krtya_anIya_pratyaya") is not True:
        return False
    if pr.meta.get("anit_ardhadhatuka") is not True:
        return False
    if not anga.varnas or anga.varnas[-1].slp1 != "i":
        return False
    return True


def cond(state: State) -> bool:
    return _matches_p037(state) or _matches(state)


def act(state: State) -> State:
    if _matches_p037(state):
        for i in range(len(state.terms) - 2):
            anga = state.terms[i]
            ca = state.terms[i + 1]
            tin = state.terms[i + 2]
            if "anga" not in anga.tags or "dhatu" not in anga.tags:
                continue
            if anga.meta.get("P037_6_4_51_done"):
                continue
            if not anga.varnas or anga.varnas[-1].slp1 != "i":
                continue
            if ca.meta.get("P037_caN") is not True:
                continue
            if "tin_adesha_3_4_78" not in tin.tags:
                continue
            anga.varnas.pop()
            anga.meta["sthānivat_nic_block_guna"] = True
            anga.meta["P037_6_4_51_done"] = True
            state.meta["6_4_51_Reraniwi"] = True
            state.meta.pop("P037_6_4_51_arm", None)
            return state
        return state
    if not _matches(state):
        return state
    anga = state.terms[-2]
    pr = state.terms[-1]
    anga.varnas.pop()
    anga.meta["6_4_51_Reraniwi_done"] = True
    anga.meta.pop("6_4_51_nic_tail_i", None)
    # Block **7.3.86** guṇa as if ṇic were still “present” for mitāḥ-prakriyā.
    anga.meta["sthānivat_nic_block_guna"] = True
    state.meta["6_4_51_Reraniwi"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.51",
    sutra_type=SutraType.VIDHI,
    text_slp1="Reraniwi",
    text_dev="णेरनिटि",
    padaccheda_dev="णेः / अनिटि",
    why_dev="अनिडित आर्धधातुके परे णिचः लुक् (हिडि→हिड्)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
