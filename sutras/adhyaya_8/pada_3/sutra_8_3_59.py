"""
8.3.59  आदेशप्रत्यययोः  —  VIDHI

"(The s, in the substitutes mentioned by 8.3.55–58, OR in a pratyaya,)
 after an in-kuk preceding vowel, becomes ṣ."

Operational narrow reading: when an 's' appears in a sup-pratyaya
whose preceding varṇa is i/I/u/U/f/F/e/E/o/O (any in+kuk vowel in
this context — we use the simpler 'any non-a vowel'), the 's' is
replaced by 'ṣ' (SLP1 'z').

  cell 7-3 rAme + su (after 7.3.103) → rAmesu → rAmeSu
                        the 's' of 'su' is after 'e' → becomes z → 'z u'
                        then joiner renders as षु.

Tripādī (8.x), but operates on the pratyaya's s.  We detect this
after pada-merge and the other tripāḍī sūtras have run.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import mk


# Preceding vowels that trigger ṣatva (simplified "in+kuk").
_IN_KUK_PREV = frozenset({"i", "I", "u", "U", "f", "F", "e", "E", "o", "O"})


def _find_target(state: State):
    """
    After pada-merge, state has ONE term.  Scan for an 's' whose
    preceding varṇa is in IN_KUK_PREV and that has not been processed.
    """
    if not state.terms:
        return None
    t = state.terms[0]
    for i in range(1, len(t.varnas)):
        v = t.varnas[i]
        if v.slp1 != "s":
            continue
        if "satva_done" in v.tags:
            continue
        prev = t.varnas[i - 1]
        if prev.slp1 not in _IN_KUK_PREV:
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    return _find_target(state) is not None


def act(state: State) -> State:
    i = _find_target(state)
    if i is None:
        return state
    new_varna = mk("z")
    new_varna.tags.add("satva_done")
    state.terms[0].varnas[i] = new_varna
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.3.59",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "AdeSapratyayayoH",
    text_dev       = "आदेशप्रत्यययोः",
    padaccheda_dev = "आदेश-प्रत्यययोः",
    why_dev        = "इन्-कुक्-पूर्वे स-कारस्य (प्रत्ययस्थस्य) 'ष'-आदेशः "
                     "(त्रिपादी)।",
    anuvritti_from = ("8.2.1", "8.3.55"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
