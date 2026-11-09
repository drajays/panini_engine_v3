"""
8.2.69  रोऽसुपि  —  VIDHI

Padaccheda: रोः · असुपि

रोऽसुपि (8.2.69)
Pāṭha: ashtadhyayi.com data.txt row i=82069 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def _site(state: State):
    """अहन् → अहर् (a plain r, not ru) when the next word is not a sup (Kāśikā 8.2.69: अहर्ददाति, अहर्भुङ्क्ते; अहोभ्याम् keeps 8.2.68's ru). Built for the two-pada seam."""
    if not state.tripadi_zone or len(state.terms) < 2:
        return None
    left, right = state.terms[0], state.terms[1]
    if "pada" not in left.tags or "pada" not in right.tags or "sup" in right.tags:
        return None
    return left if "".join(v.slp1 for v in left.varnas) == "ahan" else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas[-1] = mk("r")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'rosupi',
    text_dev              = 'रोऽसुपि',
    samagra_slp1          = "padasya ahnaH asupi raH",
    samagra_dev           = "पदस्य अह्नः असुपि रः",
    padaccheda_dev        = "रोः · असुपि",
    why_dev               = "(सूत्रम् 8.2.69) रोऽसुपि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
