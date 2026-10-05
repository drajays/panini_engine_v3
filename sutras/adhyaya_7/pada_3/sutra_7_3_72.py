"""
7.3.72  क्सस्याचि  —  VIDHI

Padaccheda: क्सस्य अचि

क्सस्याचि (7.3.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State):
    """क्सस्याचि: the a of ksa (3.1.45) drops before an ac-initial ending — अधुक्षि, अधुक्षाताम्, अविक्षन्त (KV 7.3.72)."""
    for i, t in enumerate(state.terms[:-1]):
        if (t.meta.get("upadesha_slp1") or "").strip() != "ksa" or t.meta.get("7_3_72_done"):
            continue
        if len(t.varnas) != 2 or t.varnas[0].slp1 != "s" or t.varnas[-1].slp1 != "a":      # after the it-lopa of k
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        if nxt is not None and nxt.varnas[0].slp1 in "aAiIuUfFxXeEoO":
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        t.varnas.pop()
        t.tags.discard("upadesha")          # the s is no upadeśa-final: 1.3.3 must not take it for a halantyam it
        t.meta["7_3_72_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "ksasyAci",
    text_dev              = "क्सस्याचि",
    padaccheda_dev        = "क्सस्य अचि",
    why_dev               = "(सूत्रम् 7.3.72) क्सस्याचि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
