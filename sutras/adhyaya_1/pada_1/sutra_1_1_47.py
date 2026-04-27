"""
1.1.47  मिदचोऽन्त्यात्परः  —  NIYAMA

"(An ādeśa marked with) 'mit' is placed AFTER the last vowel (ac)
 of the aṅga — not at some other position."

NIYAMA: narrows a (potential) VIDHI that would otherwise place an
augment at a different slot.  Sets state.niyama_gates[<augment-rule-id>]
with a per-position restriction predicate.

Because augment-placement rules key off this niyama, we record it as
a fact in niyama_gates['mit_placement'] = 'after_last_ac'.  The VIDHI
that inserts a mit-augment reads this and honours it.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    # Only fire if not already set (idempotent — R1 bites mutating steps
    # but NIYAMA is not r1_exempt; we guard by checking the gate).
    return state.niyama_gates.get("mit_placement") != "after_last_ac"


def act(state: State) -> State:
    state.niyama_gates["mit_placement"] = "after_last_ac"
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.47",
    sutra_type     = SutraType.NIYAMA,
    r1_form_identity_exempt=True,
    text_slp1      = "midaco antyAt paraH",
    text_dev       = "मिदचोऽन्त्यात्परः",
    padaccheda_dev = "मित् अचः अन्त्यात् परः",
    why_dev        = "मित्-आदेशः अङ्गस्य अन्त्य-अच् वर्णात् परः स्थाप्यते।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
