"""
8.2.72  वसुस्रंसुध्वंस्वनडुहां दः  —  VIDHI

Padaccheda: वसु-स्रंसु-ध्वंसु-अनडुहाम् दः

वसुस्रंसुध्वंस्वनडुहां दः (8.2.72)
Pāṭha: ashtadhyayi.com data.txt row i=82072 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import HAL

def _site(state: State):
    """वसुस्रंसुध्वंस्वनडुहां दः — the final of अनडुह् (वसु…, with the s-final words) at the pada end → d. Before the pada is cut: the stem followed by a
    hal-initial svādi sup that is not sarvanāmasthāna (1.4.17): अनडुद्भ्याम्, अनडुत्सु (8.4.55 then devoices)."""
    if len(state.terms) < 2:
        return None
    stem, sup = state.terms[-2], state.terms[-1]
    if "sup" not in sup.tags or "prātipadika" not in stem.tags or not sup.varnas or sup.varnas[0].slp1 not in HAL:
        return None
    if "sarvanamasthana" in sup.tags or stem.meta.get("8_2_72_done"):
        return None
    if (stem.meta.get("upadesha_slp1") or "").strip().endswith("anaquh") and stem.varnas and stem.varnas[-1].slp1 == "h":
        return stem
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    stem = _site(state)
    stem.varnas[-1] = mk("d")
    stem.meta["8_2_72_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.72",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "vasusraMsuDvaMsvanaquhAM daH",
    text_dev              = "वसुस्रंसुध्वंस्वनडुहां दः",
    samagra_slp1          = "saH vasu~-sraMsu-DvaMsu-anaquhAm padasya daH",
    samagra_dev           = "सः वसुँ-स्रंसु-ध्वंसु-अनडुहाम् पदस्य दः",
    padaccheda_dev        = "वसु-स्रंसु-ध्वंसु-अनडुहाम् दः",
    why_dev               = "(सूत्रम् 8.2.72) वसुस्रंसुध्वंस्वनडुहां दः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
