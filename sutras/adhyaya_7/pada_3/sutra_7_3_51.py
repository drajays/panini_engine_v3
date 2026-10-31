"""
7.3.51  इसुसुक्तान्तात् कः  —  VIDHI

Padaccheda: इस्-उस्-उक्-तान्तात् कः

इसुसुक्तान्तात् कः (7.3.51)
Pāṭha: ashtadhyayi.com data.txt row i=73051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import TADDHITA_PRATYAYATVA, adesha_substitute_varnas
from engine.taddhita_attach import tha_site


def _angantya_ok(anga) -> bool:
    """The aṅga ends in is, us (the letters themselves), in uk (u, ṛ, ḷ) or in t."""
    v = [x.slp1 for x in anga.varnas]
    return bool(v) and (v[-1] == "t" or v[-1] in "uUfFxX" or (len(v) > 1 and v[-1] == "s" and v[-2] in "iu"))


def _find(state: State):
    hit = tha_site(state)
    return hit if hit is not None and _angantya_ok(hit[1]) else None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    pr = state.terms[hit[0]]
    adesha_substitute_varnas(pr, "ka", state, sutra_id="7.3.51", gunadharmas=frozenset({TADDHITA_PRATYAYATVA}))      # ṭh -> k (not ik); the a of ṭha stays
    pr.meta["7_3_50_Tak_to_ika_done"] = True       # the ṭh has been taken: 7.3.50 has no site left
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "isusuktAntAt kaH",
    text_dev              = "इसुसुक्तान्तात् कः",
    samagra_slp1          = "is-us-uk-t-antAt aNgAt Wasya kaH",
    samagra_dev           = "इस्-उस्-उक्-त्-अन्तात् अङ्गात् ठस्य कः",
    padaccheda_dev        = "इस्-उस्-उक्-तान्तात् कः",
    why_dev               = "(सूत्रम् 7.3.51) इसुसुक्तान्तात् कः।",
    anuvritti_from        = ('7.1.1',),
    apavada_of            = ('7.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
