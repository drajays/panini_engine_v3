"""
7.4.1  णौ चङ्युपधाया ह्रस्वः  —  VIDHI

Padaccheda: णौ चङि उपधायाः ह्रस्वः

णौ चङ्युपधाया ह्रस्वः (7.4.1)
Pāṭha: ashtadhyayi.com data.txt row i=74001 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_SHORT = {"A": "a", "I": "i", "U": "u", "F": "f", "X": "x", "e": "i", "E": "i", "o": "u", "O": "u"}


def _find(state: State):
    """णौ चङ्युपधाया ह्रस्वः: the upadhā of the aṅga before a caṅ-para ṇi is
    shortened — चोर् → चुर् (अचूचुरत्), भाल् → भल् (अबीभलत्); not after ak-lopa."""
    if not any((t.meta.get("upadesha_slp1") or "").strip() == "caG" for t in state.terms):
        return None
    dh = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if dh is None or not (dh.meta.get("nijanta") or dh.meta.get("ni_lopa_done")) or dh.meta.get("aglopa") or dh.meta.get("7_4_1_done"):
        return None
    if len(dh.varnas) < 2 or dh.varnas[-2].slp1 not in _SHORT:
        return None
    up = (dh.meta.get("upadesha_slp1_original") or dh.meta.get("dhatu_upadesha") or "")
    if "ṛdit" in str(dh.meta.get("it_samjna_names") or "") or "fit" in str(dh.meta.get("it_samjna_names") or "") \
            or dh.meta.get("rdit"):
        return None        # नाग्लोपिशास्वृदिताम् (7.4.2): ṛdit roots (कुद्रि: अचुकोदत्) keep the long upadhā
    return dh


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    dh = _find(state)
    dh.varnas[-2] = mk(_SHORT[dh.varnas[-2].slp1])
    dh.meta["7_4_1_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.1",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "RO caNyupaDAyA hrasvaH",
    text_dev              = "णौ चङ्युपधाया ह्रस्वः",
    samagra_slp1          = "aNgasya RO caNi upaDAyAH hrasvaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य णौ चङि उपधायाः ह्रस्वः",
    padaccheda_dev        = "णौ चङि उपधायाः ह्रस्वः",
    why_dev               = "चङ्परे णौ अङ्गस्य उपधायाः ह्रस्वः (अचूचुरत्)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
