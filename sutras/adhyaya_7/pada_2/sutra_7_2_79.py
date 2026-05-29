"""
7.2.79  लोपः सीयुट्स्योऽनिटि  —  VIDHI

Two operational paths:
  1. Arm ``7_2_79_sIyuw_s_lopa_arm``: original ātmanepada sīyuṭ s-lopa.
  2. Arm ``7_2_79_liG_yasut_arm``: vidhi-liṅ parasmaipada — drop the final
     's' from the yāsuṭ augment term [y,A,s] → [y,A]; additionally, for
     the *adādi* 3pl path (dhātu directly precedes yasut, i.e. previous term
     ends in HAL) and the tiṅ 'us' starts with u/U, drop the 'A' → [y].
     This gives ad+y+us → adyuḥ.  For bhvādi (śap-a before yasut), rule
     7.2.80 handles yā+us → iy+us via a separate transformation.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import HAL


def _find_sIyuw(state: State) -> int | None:
    if not state.meta.get("7_2_79_sIyuw_s_lopa_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "ling_sIyuw" not in t.tags:
            continue
        if t.meta.get("7_2_79_sIyuw_done"):
            continue
        if not t.varnas or t.varnas[0].slp1 != "s":
            continue
        return i
    return None


def _find_yasut(state: State) -> int | None:
    """Find the yāsuṭ augment term ending in 's' for vidhi-liṅ s-lopa."""
    if not state.meta.get("7_2_79_liG_yasut_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "yasut_agama" not in t.tags:
            continue
        if t.meta.get("7_2_79_yasut_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "s":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_sIyuw(state) is not None or _find_yasut(state) is not None


def act(state: State) -> State:
    idx = _find_sIyuw(state)
    if idx is not None:
        t = state.terms[idx]
        del t.varnas[0]
        t.meta["7_2_79_sIyuw_done"] = True
        state.meta.pop("7_2_79_sIyuw_s_lopa_arm", None)
        return state

    idx = _find_yasut(state)
    if idx is not None:
        t = state.terms[idx]
        del t.varnas[-1]  # drop final 's' from [y,A,s] → [y,A]
        # For adādi 3pl: when the term BEFORE yasut ends in a HAL (consonant),
        # the dhātu directly precedes the agama (no śap-a between them).  In
        # that case, if the following tiṅ starts with u/U, also drop 'A' → [y],
        # giving ad+y+us → adyuḥ.
        # When there IS a vowel-final term before yasut (e.g. bhū-śap-a), rule
        # 7.2.80 handles the yā+us → iy+us conversion instead — leave A intact.
        if (t.varnas and t.varnas[-1].slp1 == "A"
                and idx + 1 < len(state.terms)
                and idx > 0):
            nxt = state.terms[idx + 1]
            prev = state.terms[idx - 1]
            prev_last = prev.varnas[-1].slp1 if prev.varnas else ""
            if (nxt.varnas and nxt.varnas[0].slp1 in {"u", "U"}
                    and prev_last in HAL):
                del t.varnas[-1]  # drop 'A' from [y,A] → [y]
                state.samjna_registry["7.2.79_yasut_A_lopa"] = True
        t.meta["7_2_79_yasut_done"] = True
        state.meta.pop("7_2_79_liG_yasut_arm", None)
        state.samjna_registry["7.2.79_yasut_s_lopa"] = True
        return state

    return state


SUTRA = SutraRecord(
    sutra_id="7.2.79",
    sutra_type=SutraType.VIDHI,
    text_slp1="lopaH sIyutsyo'niwi",
    text_dev="लोपः सीयुट्स्योऽनिटि",
    padaccheda_dev="लोपः / सीयुट्स्यः / अनिटि",
    why_dev="सीयुटः/यासुटः सकारस्य लोपः — विधि-लिङ्-पथः।",
    anuvritti_from=("7.2.76",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
