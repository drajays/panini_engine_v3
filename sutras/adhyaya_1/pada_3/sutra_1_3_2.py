"""
1.3.2  उपदेशेऽजनुनासिक इत्  —  SAMJNA

"In an upadeśa, a vowel (ac) marked with anunāsika is termed 'it'."

  su (सुँ) upadeśa = [s, u-anunasika] → 1.3.2 tags 'u' as it-candidate
  → 1.3.9 deletes it → leaves [s]

In our encoding, an anunāsika vowel carries tag 'anunasika' on its
Varna object.  This sūtra scans upadeśa-tagged Terms and tags every
anunāsika-marked vowel with 'it_candidate_anunasika' so 1.3.9 can
delete it.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import AC


def _eligible_vowels(state: State):
    """Yield (term_idx, varna_idx) of anunāsika-marked vowels in upadeśa."""
    for i, t in enumerate(state.terms):
        if "upadesha" not in t.tags:
            continue
        for j, v in enumerate(t.varnas):
            if v.slp1 not in AC:
                continue
            if "anunasika" not in v.tags:
                continue
            if ("it" in v.tags or
                "it_candidate_anunasika" in v.tags):
                continue
            yield i, j


def cond(state: State) -> bool:
    return next(_eligible_vowels(state), None) is not None


def act(state: State) -> State:
    for i, j in _eligible_vowels(state):
        state.terms[i].varnas[j].tags.add("it_candidate_anunasika")
        key = ("it_anunasika", i, j)
        state.samjna_registry[key] = frozenset({state.terms[i].varnas[j].slp1})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.3.2",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "upadeSe ajanunAsika it",
    text_dev       = "उपदेशेऽजनुनासिक इत्",
    padaccheda_dev = "उपदेशे अच् अनुनासिकः इत्",
    why_dev        = "उपदेशे अनुनासिक-अच् वर्णः 'इत्' संज्ञां लभते।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
