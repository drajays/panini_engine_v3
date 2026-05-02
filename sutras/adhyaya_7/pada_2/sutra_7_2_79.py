"""
7.2.79  लोपः सीयुट्स्योऽनिटि  —  VIDHI (narrow: *vidhi-liṅ* *sīyuṭ* *s*-lopa)

Teaching **P038** step **n6**: the initial ``s`` of the *sīyuṭ* augment drops in the
*anidiṭ* *ātmanepada* *liṅ* row, leaving a long ``I`` onset on the residue.

Narrow: ``state.meta['P038_7_2_79_sIyuw_s_lopa_arm']`` + ``ling_sIyuw`` ``Term``
whose first varṇa is ``s``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find(state: State) -> int | None:
    if not state.meta.get("P038_7_2_79_sIyuw_s_lopa_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "ling_sIyuw" not in t.tags:
            continue
        if t.meta.get("P038_7_2_79_done"):
            continue
        if not t.varnas or t.varnas[0].slp1 != "s":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    idx = _find(state)
    if idx is None:
        return state
    t = state.terms[idx]
    del t.varnas[0]
    t.meta["P038_7_2_79_done"] = True
    state.meta.pop("P038_7_2_79_sIyuw_s_lopa_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="7.2.79",
    sutra_type=SutraType.VIDHI,
    text_slp1="lopaH sIyutsyo'niwi",
    text_dev="लोपः सीयुट्स्योऽनिटि",
    padaccheda_dev="लोपः / सीयुट्स्यः / अनिटि",
    why_dev="सीयुटः सकारस्य लोपः — विधि-लिङ्-पथः (P038)।",
    anuvritti_from=("7.2.76",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
