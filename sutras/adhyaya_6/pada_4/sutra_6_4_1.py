"""
6.4.1  अङ्गस्य  —  ADHIKARA

"(The following sūtras, up to 7.4.97, operate) on the aṅga."

Pushes a scope entry covering 6.4.1 through 7.4.97.  Subsequent
VIDHIs in this span (e.g. 6.4.148 yasyeti ca, 7.1.54 hrasvanadyāpo
nuṭ, etc.) check the scope via engine.gates.adhikara_in_effect.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    # Push only once.
    return not any(e.get("id") == "6.4.1" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.4.1",
        "scope_end" : "7.4.97",
        "text_dev"  : "अङ्गस्य",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.1",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "aNgasya",
    text_dev       = "अङ्गस्य",
    padaccheda_dev = "अङ्गस्य",
    why_dev        = "६.४.१ तः ७.४.९७ पर्यन्तानि सूत्राणि अङ्गस्य विधयः।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.4.1", "7.4.97"),
)

register_sutra(SUTRA)
