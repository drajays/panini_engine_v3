"""
7.1.79  वा नपुंसकस्य  —  VIDHI

Padaccheda: वा नपुंसकस्य

वा नपुंसकस्य (7.1.79)
Pāṭha: ashtadhyayi.com data.txt row i=71079 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra, origin
from engine.declension import anga_and_sup
from engine.state import State
from phonology    import mk
from phonology.varna import AC_DEV


def _site(state: State):
    """वा नपुंसकस्य: a neuter abhyasta Śatṛ-anta aṅga (the 7.1.78 case) takes nuṃ before a sarvanāmasthāna sup, or not (dadanti / dadati)."""
    hit = anga_and_sup(state)
    if hit is None or "7.1.70" not in state.blocked_sutras:
        return None
    anga, sup = hit
    if "napuṃsaka" not in anga.tags or "sarvanamasthana" not in sup.tags or anga.meta.get("7_1_79_done"):
        return None
    return anga if origin.last_pratyaya(anga) == "Satf~" and origin.is_abhyasta(anga) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    j = max(k for k, v in enumerate(anga.varnas) if v.slp1 in AC_DEV)
    n = mk("n")
    n.tags.add("mit")
    anga.varnas.insert(j + 1, n)
    anga.meta["7_1_79_done"] = True
    anga.meta["7_1_70_num_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.79",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    vibhasha_scope        = lambda state: _site(state) is not None,
    r1_form_identity_exempt = True,
    text_slp1             = "vA napuMsakasya",
    text_dev              = "वा नपुंसकस्य",
    samagra_slp1          = "aNgasya vA napuMsakasya num na aByastAt SatuH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य वा नपुंसकस्य नुम् न अभ्यस्तात् शतुः",
    padaccheda_dev        = "वा नपुंसकस्य",
    why_dev               = "(सूत्रम् 7.1.79) वा नपुंसकस्य।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
