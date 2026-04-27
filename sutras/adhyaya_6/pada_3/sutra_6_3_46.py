"""
6.3.46  आन्महतः समानाधिकरणजातीययोः  —  VIDHI (narrow: mahAt → mahA before fzi)

Glass-box scope for `maharsiH`:
  When the left member is the stem `mahat` and the right member begins with
  vocalic ṛ (f), replace the final 't' of `mahat` with 'A'.

This models the ān-ādeśa of *mahat* in the specified semantic condition, without
attempting a general samāsa engine.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _find(state: State):
    if not state.terms:
        return None
    left = state.terms[0]
    if left.kind != "prakriti":
        return None
    upa = (left.meta.get("upadesha_slp1") or "").strip()
    if not (upa == "mahat" or upa.startswith("mahat")):
        return None
    if left.meta.get("6_3_46_An_done"):
        return None
    if not left.varnas:
        return None
    # In merged samāsa prātipadikas (via 1.2.46), right member is in the same term.
    # We locate the 'mahat' segment at the start and replace its final 't'.
    if len(left.varnas) < 5:
        return None
    if "".join(v.slp1 for v in left.varnas[:5]) != "mahat":
        return None
    if left.varnas[4].slp1 != "t":
        return None
    return 0


def cond(state: State) -> bool:
    # Glass-box arming: pipeline must opt-in.
    if not state.meta.get("6_3_46_An_mahat_arm"):
        return False
    return _find(state) is not None


def act(state: State) -> State:
    if _find(state) is None:
        return state
    left = state.terms[0]
    left.varnas[4] = mk("A")
    left.meta["6_3_46_An_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.3.46",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "An mahatH samAnADikaraRajAtIyayoH",
    text_dev       = "आन्महतः समानाधिकरणजातीययोः",
    padaccheda_dev = "आन् / महतः / समानाधिकरणजातीययोः",
    why_dev        = "समानाधिकरणे (कर्मधारयादौ) महत्-शब्दस्य अन्त्य-तकारस्थाने आकारादेशः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

