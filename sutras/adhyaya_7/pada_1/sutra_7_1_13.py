"""
7.1.13  ङेर्यः  —  VIDHI

"After an अ-ending aṅga (= ato'ṅga, anuvṛtti from 7.1.9), the ṅe
 (dative-singular) pratyaya is replaced by ya."

  cell 4-1:  rAma + Ne → rAma + ya → ... → rAmAya (after 7.3.102)

Mirrors 7.1.12 in shape — but replacing Ne → ya only.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State
from phonology     import mk


def _find_target(state: State):
    if len(state.terms) < 2:
        return None
    pratyaya = state.terms[-1]
    if "sup" not in pratyaya.tags:
        return None
    upa = pratyaya.meta.get("upadesha_slp1")
    if upa != "Ne":
        return None
    if pratyaya.meta.get("ne_to_ya_done"):
        return None

    anga = state.terms[-2]
    if "anga" not in anga.tags:
        return None
    if not anga.varnas:
        return None
    last = anga.varnas[-1]
    if last.slp1 != "a":
        return None

    return len(state.terms) - 1


def cond(state: State) -> bool:
    if not adhikara_in_effect("7.1.13", state, "6.4.1"):
        return False
    return _find_target(state) is not None


def act(state: State) -> State:
    idx = _find_target(state)
    if idx is None:
        return state
    pratyaya = state.terms[idx]
    pratyaya.varnas = [mk("y"), mk("a")]
    pratyaya.meta["ne_to_ya_done"] = True
    pratyaya.meta["upadesha_slp1_original"] = pratyaya.meta.get("upadesha_slp1")
    pratyaya.meta["upadesha_slp1"] = "ya"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.13",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "Ner yaH (ataH aNgasya)",
    text_dev       = "ङेर्यः",
    padaccheda_dev = "ङेः यः — अतः अङ्गात्",
    why_dev        = "अदन्त-अङ्गात् परस्य ङे-प्रत्ययस्य 'य'-आदेशः।",
    anuvritti_from = ("6.4.1", "7.1.9", "7.1.12"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
