"""
8.2.1  पूर्वत्रासिद्धम्  —  ADHIKARA

"(All sūtras from here, 8.2.1, to the end of the Aṣṭādhyāyī, 8.4.68,
 are) asiddha (invisible) to the preceding (pūrvatra) sūtras."

Opens the Tripāḍī zone.  Sets state.tripadi_zone = True so that
engine.gates.asiddha_violates can refuse any non-tripāḍī sūtra that
tries to fire after this point.

Pushes an adhikāra entry covering (8.2.1, 8.4.68).
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def cond(state: State) -> bool:
    # Enter only once.
    return not state.tripadi_zone


def act(state: State) -> State:
    state.tripadi_zone = True
    state.adhikara_stack.append({
        "id"        : "8.2.1",
        "scope_end" : "8.4.68",
        "text_dev"  : "पूर्वत्रासिद्धम्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.1",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "pUrvatrAsiddham",
    text_dev       = "पूर्वत्रासिद्धम्",
    padaccheda_dev = "पूर्वत्र असिद्धम्",
    why_dev        = "८.२.१ तः ८.४.६८ पर्यन्तम् (त्रिपादी) पूर्व-सूत्रेभ्यः असिद्धम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("8.2.1", "8.4.68"),
)

register_sutra(SUTRA)
