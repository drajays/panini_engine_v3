"""
7.1.54  ह्रस्वनद्यापो नुट्  —  VIDHI

"After an aṅga ending in a hrasva vowel (or an aṅga tagged 'nadī' or
 'āp'), before the pratyaya आम्, insert the nuṭ āgama (न् with ṭ as
 it-marker) at the beginning of the pratyaya."

Reading after anuvṛtti from 6.4.1 (aṅgasya).
The inserted न् carries the tag 'it_candidate_nut_t' — the ṭ it-marker
is in the sūtra's śabda, added here so that 1.3.9 knows to delete it.
"""
from engine        import SutraType, SutraRecord, register_sutra
from engine.gates  import adhikara_in_effect
from engine.state  import State, Varna
from phonology     import mk


_HRASVA = frozenset({"a", "i", "u", "f", "x"})


def _find_target(state: State):
    """Return the pratyaya Term index whose upadeśa is आम् and whose
    preceding Term is a qualifying aṅga."""
    for i in range(1, len(state.terms)):
        pratyaya = state.terms[i]
        if pratyaya.meta.get("upadesha_slp1") != "Am":
            continue
        if "sup" not in pratyaya.tags:
            continue
        anga = state.terms[i - 1]
        if "anga" not in anga.tags:
            continue
        # v3.5: adant sarvanāma (sarva) uses suṭ (7.1.52), not nuṭ.
        if "sarvanama" in anga.tags:
            continue
        if not anga.varnas:
            continue
        last = anga.varnas[-1]
        if (last.slp1 in _HRASVA
            or "nadi" in anga.tags
            or "Ap"   in anga.tags):
            # Guard idempotency: if pratyaya already has 'n' at front
            # with the nuṭ-it-tag, we've fired — don't fire again.
            if pratyaya.varnas and "nut_agama_inserted" in pratyaya.varnas[0].tags:
                continue
            return i
    return None


def cond(state: State) -> bool:
    if not adhikara_in_effect("7.1.54", state, "6.4.1"):
        return False
    return _find_target(state) is not None


def act(state: State) -> State:
    i = _find_target(state)
    if i is None:
        return state
    nut = mk("n", "nut_agama_inserted")
    state.terms[i].varnas.insert(0, nut)
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.1.54",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "hrasvanadyApo nuw",
    text_dev       = "ह्रस्वनद्यापो नुट्",
    padaccheda_dev = "ह्रस्व-नदी-आपाम् नुट्",
    why_dev        = "ह्रस्वान्त-अङ्ग / नदी-आप्-अङ्गात् परस्य आम्-प्रत्ययस्य "
                     "पराद्यौ 'नुट्' आगमः।",
    anuvritti_from = ("6.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
