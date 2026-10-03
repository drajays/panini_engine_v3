"""
7.2.4  नेटि  —  VIDHI

Padaccheda: न इटि

नेटि (7.2.4)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_4_newi_4"


def _sic_with_it(state: State) -> bool:
    """A sic that already begins with its iṭ (7.2.35) stands right after the aṅga."""
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" not in t.tags:
            continue
        nxt = next((u for u in state.terms[i + 1:] if u.varnas), None)
        return (nxt is not None and (nxt.meta.get("upadesha_slp1") or "").strip() == "sic"
                and "it_agama" in nxt.varnas[0].tags)
    return False


def _sic(state: State):
    for i, t in enumerate(state.terms[:-1]):
        if "dhatu" in t.tags:
            return next((u for u in state.terms[i + 1:] if u.varnas), None)
    return None


def cond(state: State) -> bool:
    return not state.paribhasha_gates.get(_GATE_KEY) and _sic_with_it(state)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    _sic(state).tags.add("neti_7_2_4")
    state.meta["__why_now_dev__"] = "सिच्-प्रत्यये इट्-आगमे सति सिचि वृद्धिः (७.२.१, ७.२.३) न भवति।"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.4",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "newi",
    text_dev              = "नेटि",
    padaccheda_dev        = "न इटि",
    why_dev               = "(सूत्रम् 7.2.4) नेटि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
