"""
1.3.3  हलन्त्यम्  —  SAMJNA

"The final consonant of an upadeśa is termed 'it'."

(Anuvṛtti carries 'upadeśe' from 1.3.2 — already baked into text_slp1.)

Fires on any Term whose final Varna is a consonant AND which has the
tag 'upadesha' (meaning it's being read in upadeśa state).  Tags that
final Varna with 'it_candidate_halantyam'.  A separate VIDHI 1.3.9
(tasya lopaḥ) then deletes it.

This SAMJNA updates state.samjna_registry[('it', term_id)] to track
which Term got an it-tag; R2 watches the registry for change.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import HAL


def _eligible_terms(state: State):
    """Yield (index, term) pairs with an unmarked final consonant that
    are still in upadeśa state."""
    for i, t in enumerate(state.terms):
        if "upadesha" not in t.tags:
            continue
        # v3.1 correction: sup pratyayas in our inventory are already
        # post-halantyam (the JSON entries like "jas", "am", "Sas" are
        # the surface upadeśas without halant-it-markers).  1.3.3 only
        # applies to upadeśas that classically CARRY halant-its:
        # dhātus (like cikIrz~) and a handful of lit-style pratyayas.
        # We mark those with tag 'has_halant_it'; if absent, we skip.
        if "sup" in t.tags and "has_halant_it" not in t.tags:
            continue
        if not t.varnas:
            continue
        last = t.varnas[-1]
        if last.slp1 not in HAL:
            continue
        if "it" in last.tags or "it_candidate_halantyam" in last.tags:
            continue
        yield i, t


def cond(state: State) -> bool:
    return next(_eligible_terms(state), None) is not None


def act(state: State) -> State:
    for i, t in _eligible_terms(state):
        t.varnas[-1].tags.add("it_candidate_halantyam")
        key = ("it_halantyam", i)
        state.samjna_registry[key] = frozenset({t.varnas[-1].slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.3",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "hal antyam (upadeze it)",
    text_dev       = "हलन्त्यम् (उपदेशे इत्)",
    padaccheda_dev = "हल् अन्त्यम् उपदेशे इत्",
    why_dev        = "उपदेशे अन्त्यः हल् वर्णः 'इत्' संज्ञां लभते।",
    anuvritti_from = ("1.3.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
