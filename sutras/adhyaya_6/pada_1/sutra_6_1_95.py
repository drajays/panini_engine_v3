"""
6.1.95  ओमाङोश्च  —  VIDHI

Padaccheda: ओम्-आङोः च

ओमाङोश्च (6.1.95)
Pāṭha: ashtadhyayi.com data.txt row i=61095 (Art. 14).
Kāśikā 6.1.95: kā om ityavocat → komityavocat; Laghukaumudī: śivāyom namaḥ — vṛddhirecer apavādaḥ.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology import mk


def _live(state):
    return [i for i, t in enumerate(state.terms) if t.varnas]

META = "pararupa_6_1_95"


def _find(state: State):
    live = _live(state)
    for i, j in zip(live, live[1:]):
        a, b = state.terms[i], state.terms[j]
        if a.meta.get(META):
            continue
        flat_b = "".join(v.slp1 for v in b.varnas)
        # SHORTCUT S76: only the om branch; the āṅ branch needs āṅ as a pada of its own on the tape
        if a.varnas[-1].slp1 in ("a", "A") and (flat_b == "om" or (b.meta.get("upadesha_slp1") or "").strip() == "om"):
            return i
    return None


def _new_cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    a = state.terms[i]
    del a.varnas[-1]                                   # pararūpa: the following o stays, the avarṇa goes
    a.meta[META] = True
    state.meta["__why_now_dev__"] = "अवर्णान्तात् ओमि परे पररूपम् एकादेशः (६.१.९५)।"
    return state

def cond(state: State) -> bool:
    return _new_cond(state)


SUTRA = SutraRecord(
    sutra_id              = "6.1.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'omANoSca',
    text_dev              = 'ओमाङोश्च',
    samagra_slp1          = "om-ANoH At pUrvaparayoH ekaH pararUpam",
    samagra_dev           = "ओम्-आङोः आत् पूर्वपरयोः एकः पररूपम्",
    padaccheda_dev        = "ओम्-आङोः च",
    why_dev               = "काशिका ६.१.९५ — अवर्णान्तात् ओमि परे पररूपमेकादेशः (शिवायों नमः); वृद्धिरेचि (६.१.८८) इत्यस्यापवादः। आङ्-पक्षः S76।",
    apavada_of     = ("6.1.88",),   # अपवाद of 6.1.88 — sutra_ref_out resolver.apavada_of
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
