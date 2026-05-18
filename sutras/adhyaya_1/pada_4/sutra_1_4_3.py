"""
1.4.3  यू स्त्र्याख्यौ नदी  (yū strīyākhyau nadī)  —  SAMJNA

**Pāṭha:** The sounds *ī* and *ū* (specifically: feminine prātipadikas
ending in long SLP1 *I* or *U*) receive the technical designation *nadī*.

v3: scans ``state.terms`` for any prātipadika–stri Term whose final vowel
is SLP1 ``I`` or ``U`` and which has not yet been tagged *nadi*, then adds
the tag and records the set in ``state.samjna_registry``.

cond() reads only Term.tags and Term.varnas (structural phonemic data) — not
vibhakti, vacana, or any gold/reference field (Constitution Art. 2).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State

# SLP1: long ī = I, long ū = U
_NADI_ENDINGS: frozenset = frozenset({"I", "U"})


def _eligible(state: State):
    for t in state.terms:
        if "prātipadika" not in t.tags:
            continue
        if "stri" not in t.tags:
            continue
        if "nadi" in t.tags:
            continue
        if not t.varnas:
            continue
        if t.varnas[-1].slp1 not in _NADI_ENDINGS:
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry["nadI"] = _NADI_ENDINGS
    for t in _eligible(state):
        t.tags.add("nadi")
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.3",
    sutra_type             = SutraType.SAMJNA,
    text_slp1              = "yU strIyAKyO nadI",
    text_dev               = "यू स्त्र्याख्यौ नदी",
    padaccheda_dev         = "यू / स्त्री-आख्यौ / नदी",
    why_dev                = "ई-उ-अन्तं स्त्रीलिङ्गं प्रातिपदिकं नदीसंज्ञकम् (हरी-वध्वादि)।",
    anuvritti_from         = ("1.4.1",),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
