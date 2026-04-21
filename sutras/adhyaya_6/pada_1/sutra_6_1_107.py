"""
6.1.107  अमि पूर्वः  —  VIDHI

"When अ meets the अम्-pratyaya (which starts with अ), the PRECEDING
 vowel alone remains (i.e. pūrva-rūpa, not sav-dīrgha)."

So a + am → am (short), NOT ām.

  cell 2-1: rAma + am → rAm + am → rAmam → रामम्

This is a PRATISHEDHA-style exception to 6.1.101 sav-dīrgha.  We
implement it as a VIDHI that fires BEFORE 6.1.101 has a chance,
producing the short-a outcome.  Alternative: make 6.1.107 block
6.1.101 via state.blocked_sutras — but only for this specific
boundary.  Since only one context matters (a + am), simpler to
do the merge here directly.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _find_target(state: State):
    """
    Find boundary where a vowel meets pratyaya 'am' (am upadeśa).

    v3.4:
      - if the aṅga ends in 'a', delete the aṅga-final 'a' (legacy behaviour).
      - otherwise (e.g. hari + am), delete the pratyaya-initial 'a' so that
        i + am → im.
    """
    if len(state.terms) < 2:
        return None
    for i in range(len(state.terms) - 1):
        anga = state.terms[i]
        nxt  = state.terms[i + 1]
        if not anga.varnas or not nxt.varnas:
            continue
        if "anga" not in anga.tags:
            continue
        if nxt.meta.get("upadesha_slp1") != "am":
            continue
        if anga.meta.get("ami_purva_done"):
            continue
        if nxt.varnas[0].slp1 != "a":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    i = _find_target(state)
    if i is None:
        return state
    anga = state.terms[i]
    nxt  = state.terms[i + 1]
    if anga.varnas and anga.varnas[-1].slp1 == "a":
        # Legacy: a + am → am (keep pratyaya a)
        del anga.varnas[-1]
    else:
        # General pūrvarūpa at am-boundary: keep preceding vowel.
        del nxt.varnas[0]
    state.terms[i].meta["ami_purva_done"] = True
    # Also block 6.1.101 for safety.
    state.blocked_sutras.add("6.1.101")
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.107",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "ami pUrvaH",
    text_dev       = "अमि पूर्वः",
    padaccheda_dev = "अमि पूर्वः",
    why_dev        = "अम्-प्रत्यये परे पूर्व-रूपम् एकादेशः "
                     "(अ+अ → अ, दीर्घ-निषेधः)।",
    anuvritti_from = ("6.1.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
