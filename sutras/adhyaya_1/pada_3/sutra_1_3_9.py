"""
1.3.9  तस्य लोपः  —  VIDHI

"Of that (the 'it'-marker), there is lopa (deletion)."

This is the workhorse VIDHI that actually REMOVES it-tagged varṇas.
It reads tags added by 1.3.2 / 1.3.3 / 1.3.5 / 1.3.7 / 1.3.8 and
deletes the marked varṇas from their terms.

R1 is NOT exempt here: if this fires, it MUST delete at least one
varṇa.  The dispatcher will raise R1Violation on silent no-op.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


_IT_TAGS = (
    "it",                          # already-confirmed it
    "it_candidate_halantyam",      # from 1.3.3
    "it_candidate_anunasika",      # from 1.3.2
    "it_candidate_nit_tu_du",      # from 1.3.5
    "it_candidate_cutu",           # from 1.3.7
    "it_candidate_lasaku",         # from 1.3.8
    # NOTE: 'it_candidate_nut_t' was historically used by 7.1.54 but
    # incorrectly caused the inserted 'n' to be lopa-ed.  It is now
    # renamed to 'nut_agama_inserted' (non-it) and does not belong here.
)


def _has_it_varna(term) -> bool:
    return any(
        any(tag in v.tags for tag in _IT_TAGS)
        for v in term.varnas
    )


def cond(state: State) -> bool:
    return any(_has_it_varna(t) for t in state.terms)


def act(state: State) -> State:
    for t in state.terms:
        t.varnas = [
            v for v in t.varnas
            if not any(tag in v.tags for tag in _IT_TAGS)
        ]
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.9",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "tasya lopaH",
    text_dev       = "तस्य लोपः",
    padaccheda_dev = "तस्य लोपः",
    why_dev        = "इत्-संज्ञकस्य वर्णस्य लोपः भवति।",
    anuvritti_from = ("1.3.2", "1.3.3"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
