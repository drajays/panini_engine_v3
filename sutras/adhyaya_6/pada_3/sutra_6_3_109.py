"""
6.3.109  पृषोदरादीनि यथोपदिष्टम्  —  NIPATANA  (representative)

"पृषोदर and similar forms — (they are) as upadeśa-given: irregular
 forms are accepted as-is (niyama-exception)."

This is the archetypal NIPATANA: a fixed, irregular form is stamped
in wholesale and further vidhis are frozen on the state.

For this representative file, when any Term has tag 'prishodara' and
the recipe passes step['nipatana_form_slp1'], we write the given
varṇa sequence into the last Term and set state.nipatana_flag = True.

If step does not pass a form, we fall back to rec.nipatana_form_slp1.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk


def cond(state: State) -> bool:
    return any("prishodara" in t.tags for t in state.terms) and not state.nipatana_flag


def act(state: State) -> State:
    # Pick the most recent 'prishodara' term; default form 'pfzodara'.
    for t in reversed(state.terms):
        if "prishodara" in t.tags:
            target_form = t.meta.get("nipatana_form_slp1", "pfzodara")
            t.varnas = [mk(ch) for ch in target_form]
            break
    state.nipatana_flag = True
    return state


SUTRA = SutraRecord(
    sutra_id           = "6.3.109",
    sutra_type         = SutraType.NIPATANA,
    text_slp1          = "pfzodarAdIni yaTopadizwam",
    text_dev           = "पृषोदरादीनि यथोपदिष्टम्",
    padaccheda_dev     = "पृषोदर-आदीनि यथा-उपदिष्टम्",
    why_dev            = "पृषोदर-आदयः शब्दाः यथा उपदिष्टाः तथैव साधवः (निपातनम्)।",
    anuvritti_from     = (),
    cond               = cond,
    act                = act,
    nipatana_form_slp1 = "pfzodara",
)

register_sutra(SUTRA)
