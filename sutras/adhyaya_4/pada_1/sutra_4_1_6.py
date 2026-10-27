"""
4.1.6  उगितश्च  —  VIDHI

Padaccheda: उक्-इतः च

उगितश्च (4.1.6)
Pāṭha: ashtadhyayi.com data.txt row i=41006 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State):
    """The prātipadika that ends in an ugit pratyaya (u/ṛ/ḷ as its it-letter), before any sup or strī pratyaya (4.1.3 open)."""
    if not any(e.get("id") == "4.1.3" for e in state.adhikara_stack):
        return None
    if any(t.kind == "pratyaya" for t in state.terms):
        return None
    for t in state.terms:
        if t.kind == "prakriti" and "prātipadika" in t.tags and "strīliṅga" in t.tags and origin.is_ugit(t):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    state.terms.append(Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("NIp")),
        tags={"pratyaya", "upadesha", "stri_pratyaya", "prātipadika", "strīliṅga", "anga"},   # ṅyāp-prātipadika (4.1.1): the aṅga of the sup
        meta={"upadesha_slp1": "NIp"},
    ))
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ugitaSca",
    text_dev              = "उगितश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm ugitaH ca NIp",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् उगितः च ङीप्",
    padaccheda_dev        = "उक्-इतः च",
    why_dev               = "(सूत्रम् 4.1.6) उगितश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
