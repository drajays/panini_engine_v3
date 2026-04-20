"""
8.3.15  खरवसानयोर्विसर्जनीयः  —  VIDHI

"At the end of a word (avasāna) or before a khar phoneme, ru becomes
 visarga (ḥ)."

Tripāḍī.  Replaces a 'ru_intermediate'-tagged 'r' with 'H' (visarga).
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk


def _find(state: State):
    # Operate on the last term only (word-final context).
    for ti in range(len(state.terms) - 1, -1, -1):
        t = state.terms[ti]
        for vi in range(len(t.varnas) - 1, -1, -1):
            v = t.varnas[vi]
            if "ru_intermediate" in v.tags:
                return (ti, vi)
        return None
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi] = mk("H")
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.3.15",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Kara avasAnayor visarjanIyaH",
    text_dev       = "खरवसानयोर्विसर्जनीयः",
    padaccheda_dev = "खर्-अवसानयोः विसर्जनीयः",
    why_dev        = "खर्-वर्णे परे अवसाने च रु-आदेशस्य विसर्गः।",
    anuvritti_from = ("8.2.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
