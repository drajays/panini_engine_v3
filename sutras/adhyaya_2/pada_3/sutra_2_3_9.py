"""
2.3.9  यस्मादधिकं यस्य चेश्वरवचनं तत्र सप्तमी  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: यस्मात् / अधिकम् / यस्य / च / ईश्वरवचनम् / तत्र / सप्तमी

Śāstra: the seventh vibhakti (locative/saptamī) is prescribed when the noun
denotes something that is (*a*) exceeded by another or (*b*) the object of
a lord's command (*īśvaravacana*).

Engine: registers the adhika/īśvaravacana→saptamī gate. ``cond`` checks only
the gate flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_9_yasmad_adhikam_ishvaravachana_saptami"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.9",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "yasmAd aXikam yasya ca ISvaravacanaM tatra saptamI",
    text_dev              = "यस्मादधिकं यस्य चेश्वरवचनं तत्र सप्तमी",
    padaccheda_dev        = "यस्मात् / अधिकम् / यस्य / च / ईश्वरवचनम् / तत्र / सप्तमी",
    why_dev               = (
        "अधिकत्वे ईश्वरवचने च सप्तमी-विभक्तिः — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1",),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
