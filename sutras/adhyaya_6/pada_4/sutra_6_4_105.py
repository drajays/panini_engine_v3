"""
6.4.105  अतो हेः  —  VIDHI (narrow: *vidhi-liṅ* *uṭ* residue)

Teaching **P038** step **n7**: trim the *uṭ* tail ``u`` + ``w`` (SLP1 *ṭ*) from the
*liṅ* *sīyuṭ* residue after **7.2.79**, leaving ``Iy`` (``ī`` + *y*) before *ran*.

Narrow: ``state.meta['P038_6_4_105_uw_trim_arm']`` + ``ling_sIyuw`` ``Term`` whose
varṇa tail is ``… y u w``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find(state: State) -> int | None:
    if not state.meta.get("P038_6_4_105_uw_trim_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "ling_sIyuw" not in t.tags:
            continue
        if t.meta.get("P038_6_4_105_done"):
            continue
        vs = t.varnas
        if len(vs) < 4:
            continue
        if vs[-2].slp1 == "u" and vs[-1].slp1 == "w":
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    idx = _find(state)
    if idx is None:
        return state
    t = state.terms[idx]
    t.varnas = t.varnas[:-2]
    t.meta["P038_6_4_105_done"] = True
    state.meta.pop("P038_6_4_105_uw_trim_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.105",
    sutra_type=SutraType.VIDHI,
    text_slp1="ato heH",
    text_dev="अतो हेः",
    padaccheda_dev="अतः / हेः",
    why_dev="विधि-लिङ्-सीयुट्-अवशेषात् उट्-लोपः (P038)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
