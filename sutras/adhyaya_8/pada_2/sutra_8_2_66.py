"""
8.2.66  ससजुषो रुः  —  VIDHI

"A final 's' or 'sajus' → ru."

Tripāḍī sūtra.  Converts a pada-final 's' into 'ru' (the intermediate
form that 8.3.15 will then convert to visarga at pāda-end).
For this representative file, we operate on the LAST varṇa of the
LAST pada-tagged Term.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State, Varna
from phonology     import mk


def _target(state: State):
    """Return (term_idx, varna_idx) of a pada-final 's', else None."""
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if "pada" not in t.tags:
            continue
        if not t.varnas:
            continue
        last = t.varnas[-1]
        if last.slp1 == "s":
            return (i, len(t.varnas) - 1)
        # If last is inherent-a after consonant, look past.
        if last.slp1 == "a" and last.dev == "" and len(t.varnas) >= 2:
            prev = t.varnas[-2]
            if prev.slp1 == "s":
                return (i, len(t.varnas) - 2)
        return None
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _target(state) is not None


def act(state: State) -> State:
    hit = _target(state)
    if hit is None:
        return state
    ti, vi = hit
    # Replace 's' with 'r' tagged 'ru_intermediate' so 8.3.15 can find it.
    ru = mk("r", "ru_intermediate")
    state.terms[ti].varnas[vi] = ru
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.66",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "sasajuzo ruH",
    text_dev       = "ससजुषो रुः",
    padaccheda_dev = "स-सजुषः रुः",
    why_dev        = "पदान्त-सकारस्य सजुषः च रु-आदेशः (त्रिपादी)।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
    skip_detail_cond_false=(
        "जयति का अन्त्य वर्ण 'i' (इ) = स्वर; पदान्त 'स्' नास्ति → "
        "ससजुषो रुः N/A।"
    ),
)

register_sutra(SUTRA)
