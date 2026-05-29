"""
6.1.5  उभे अभ्यस्तम्  —  VIDHI

Padaccheda: उभे अभ्यस्तम्

Both the abhyāsa (reduplication copy) and the dhātu together are called
"abhyasta". This sūtra fires when dvitva (6.1.4 + 6.1.8) has created an
"abhyasa"-tagged term on the tape.

Structural trigger: any Term on the tape carries the "abhyasa" tag — which
6.1.8 sets on the newly created reduplication copy.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_5_uBe_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: dvitva has placed an abhyāsa term on the tape (6.1.8)
    if any("abhyasa" in t.tags for t in state.terms):
        return True
    # Legacy arm path (backward-compat)
    return bool(state.meta.get("sandhi_6_1_5_recipe"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uBe aByastam",
    text_dev              = "उभे अभ्यस्तम्",
    padaccheda_dev        = "उभे अभ्यस्तम्",
    why_dev               = "(सूत्रम् 6.1.5) उभे अभ्यस्तम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
