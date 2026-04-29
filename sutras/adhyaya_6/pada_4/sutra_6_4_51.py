"""
6.4.51  णेरनिटि  —  VIDHI (narrow demo)

Demo slice (हिडनीय.md):
  Before an **anid** *ārdhadhātuka* affix (here ``anIya`` from ``anIyar`` after
  it-lopa), the preceding ṇic residue on the stem closes by **luk** — modeled as
  deleting the final ``i`` that originated from ṇic on ``hiqi``.

Sets ``sthānivat_nic_block_guna`` so **7.3.86** guṇa does not re-apply (1.1.57
interaction; see note’s “ghost ṇic” story).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


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
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    anga = state.terms[-2]
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
