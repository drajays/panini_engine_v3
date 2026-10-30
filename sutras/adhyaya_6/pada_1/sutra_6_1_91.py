"""
6.1.91  उपसर्गादृति धातौ  —  VIDHI

Padaccheda: उपसर्गात् ऋति धातौ

उपसर्गादृति धातौ (6.1.91)
Pāṭha: ashtadhyayi.com data.txt row i=61091 (Art. 14).
Kāśikā 6.1.91: upārcchati, prārcchati, upārdhnoti — āl guṇāpavādaḥ; khaṭvarcchati (not an upasarga) is outside.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk


def _live(state):
    return [i for i, t in enumerate(state.terms) if t.varnas]

META = "vrddhi_6_1_91"


def _find(state: State):
    for i, (a, b) in enumerate(zip(state.terms, state.terms[1:])):
        if "upasarga" not in a.tags or "dhatu" not in b.tags or a.meta.get(META):
            continue
        if a.varnas and b.varnas and a.varnas[-1].slp1 in ("a", "A") and b.varnas[0].slp1 == "f":    # ṛ is tapara (ṛti, not ṝ)
            return i
    return None


def _new_cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    a, b = state.terms[i], state.terms[i + 1]
    del a.varnas[-1]                                   # the avarṇa and the ṛ give one vṛddhi: ār
    b.varnas[0:1] = [mk("A"), mk("r")]
    a.meta[META] = True
    state.meta["__why_now_dev__"] = "अवर्णान्त-उपसर्गात् ऋकारादौ धातौ वृद्धिः (आर्) एकादेशः — आद्गुणापवादः (६.१.९१)।"
    return state

def cond(state: State) -> bool:
    return _new_cond(state)


SUTRA = SutraRecord(
    sutra_id              = "6.1.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'upasargAdfti DAtO',
    text_dev              = 'उपसर्गादृति धातौ',
    samagra_slp1          = "At upasargAt fti DAtO pUrvaparayoH ekaH vfdDiH",
    samagra_dev           = "आत् उपसर्गात् ऋति धातौ पूर्वपरयोः एकः वृद्धिः",
    padaccheda_dev        = "उपसर्गात् ऋति धातौ",
    why_dev               = "काशिका ६.१.९१ — अवर्णान्तात् उपसर्गात् ऋकारादौ धातौ परे वृद्धिरेकादेशः (उपार्च्छति, प्रार्च्छति); आद्गुणस्य (६.१.८७) अपवादः।",
    apavada_of     = ("6.1.87",),   # अपवाद of 6.1.87 — sutra_ref_out resolver.apavada_of
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
