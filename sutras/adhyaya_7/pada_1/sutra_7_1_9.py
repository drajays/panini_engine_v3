"""
7.1.9  अतो भिस ऐस्  —  VIDHI

"After an a-stem aṅga, the pratyaya 'bhis' is replaced by 'ais' (= Es)."

  cell 3-3: rAma + Bis → rAma + Es (via 7.1.9)
                        → rAm + Es    (via 7.3.103 a→e? no — 7.1.9 must
                                       fire BEFORE 7.3.103 because it
                                       changes the pratyaya that 7.3.103
                                       keys off.  Actually 7.3.103 keys
                                       off 'Bis' upadesha — once we
                                       replace to 'Es', 7.3.103's trigger
                                       no longer matches and it won't
                                       fire on this cell.  Good.)
                        → rAm + E + s via 6.1.88 vṛddhi (a + Es → Es)
                          actually 6.1.88 matches (a, E) → E; so output
                          is rAm + E + s.
                        → after tripāḍī s→ru→H: rAmEH → रामैः.

So the classical pipeline: run 7.1.9 EARLY in stage 4 (before 7.3.103
and before 7.3.102), so pratyaya becomes 'Es' and later rules see that.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State
from phonology     import mk


def _matches(state: State) -> bool:
    if len(state.terms) < 2:
        return False
    anga = state.terms[-2]
    pratyaya = state.terms[-1]
    if "anga" not in anga.tags:
        return False
    if "sup" not in pratyaya.tags:
        return False
    if pratyaya.meta.get("upadesha_slp1") != "Bis":
        return False
    if pratyaya.meta.get("bhis_to_ais_done"):
        return False
    if not anga.varnas:
        return False
    if anga.varnas[-1].slp1 != "a":
        return False
    return True


def cond(state: State) -> bool:
    if not adhikara_in_effect("7.1.9", state, "6.4.1"):
        return False
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    pratyaya = state.terms[-1]
    pratyaya.varnas = [mk("E"), mk("s")]
    pratyaya.meta["bhis_to_ais_done"] = True
    pratyaya.meta["upadesha_slp1_original"] = "Bis"
    pratyaya.meta["upadesha_slp1"] = "Es"
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.9",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ato Bisa aisa",
    text_dev       = "अतो भिस ऐस्",
    padaccheda_dev = "अतः भिसः ऐस्",
    why_dev        = "अदन्त-अङ्गात् परस्य 'भिस्'-प्रत्ययस्य 'ऐस्'-आदेशः।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
