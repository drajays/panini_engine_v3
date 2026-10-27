"""
7.3.44  प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः  —  VIDHI

Padaccheda: प्रत्ययस्थात् कात् पूर्वस्य अतः इत् आपि अ-सुपः

प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः (7.3.44)
Pāṭha: ashtadhyayi.com data.txt row i=73044 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.gates import adhikara_in_effect
from engine.state import State
from phonology    import mk


def _site(state: State):
    """An ā-final aṅga (āp) whose ā follows a ka that stands in its last pratyaya, with a short a before that ka: pāṭhaka + ā → pāṭhikā.
    Taparaḥ: only the short a. Not a sup's ā (asupaḥ): the aṅga's own ṭāp (``stri_wAp``) is what is meant; a pratyaya-less ka (śakā) stays."""
    if not adhikara_in_effect("7.3.44", state, "6.4.1"):
        return None
    for t in state.terms:
        v = [x.slp1 for x in t.varnas]
        if ("stri_wAp" in t.tags and "anga" in t.tags and origin.last_pratyaya(t) is not None
                and v[-3:] == ["a", "k", "A"] and not t.meta.get("7_3_44_done")):
            return t
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    t = _site(state)
    if t is not None:
        t.varnas[-3] = mk("i")
        t.meta["7_3_44_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratyayasTAt kAt pUrvasyAta idApyasupaH",
    text_dev              = "प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः",
    samagra_slp1          = "aNgasya pratyayasTAt kAt pUrvasya ataH it Api asupaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य प्रत्ययस्थात् कात् पूर्वस्य अतः इत् आपि असुपः",
    padaccheda_dev        = "प्रत्ययस्थात् कात् पूर्वस्य अतः इत् आपि अ-सुपः",
    why_dev               = "(सूत्रम् 7.3.44) प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
