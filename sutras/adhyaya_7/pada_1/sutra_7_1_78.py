"""
7.1.78  नाभ्यस्ताच्छतुः  —  VIDHI

Padaccheda: न अभ्यस्तात् शतुः

नाभ्यस्ताच्छतुः (7.1.78)
Pāṭha: ashtadhyayi.com data.txt row i=71078 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.declension import anga_and_sup
from engine.state import State


def _site(state: State):
    """नाभ्यस्ताच्छतुः — a Śatṛ-anta aṅga that is abhyasta (the dhātu was reduplicated: dadat, jakṣat, bibhrat) does not take nuṃ (7.1.70):
    ददतौ, ददतः (not *ददन्तौ). The record of the stem's making is engine/origin's."""
    hit = anga_and_sup(state)   # like 7.1.70, which this bars: not waiting for the 6.4.1 step
    if hit is None or "7.1.70" in state.blocked_sutras:
        return None
    anga, _ = hit
    return anga if origin.last_pratyaya(anga) == "Satf~" and origin.is_abhyasta(anga) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    state.blocked_sutras.update(("7.1.70", "7.1.72"))   # the nuṃ adhikāra: every nuṃ of this stem; 7.1.79 gives it back (neuter, optional)
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.78",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "nAByastAcCatuH",
    text_dev              = "नाभ्यस्ताच्छतुः",
    samagra_slp1          = "aNgasya na aByastAt SatuH num",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य न अभ्यस्तात् शतुः नुम्",
    padaccheda_dev        = "न अभ्यस्तात् शतुः",
    why_dev               = "नाभ्यस्ताच्छतुः — अभ्यस्तात् परस्य शतुः नुम् (७.१.७०) न (ददतौ)।",
    anuvritti_from        = ('7.1.1',),
    blocks_sutra_ids      = ('7.1.70', '7.1.72'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
