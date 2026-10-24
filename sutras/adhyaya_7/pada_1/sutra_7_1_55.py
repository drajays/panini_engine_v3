"""
7.1.55  षट्चतुर्भ्यश्च  —  VIDHI

Padaccheda: षट्-चतुर्भ्यः च

षट्चतुर्भ्यश्च (7.1.55)
Pāṭha: ashtadhyayi.com data.txt row i=71055 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, is_stem
from phonology import mk

_SHAT = ("zaz", "paYcan", "saptan", "azwan", "navan", "daSan")      # ṣaṭ-saṃjñā (1.1.24): the ṣ- / ṇ-final numerals


def _site(state: State):
    """षट्चतुर्भ्यश्च — a ṣaṭ numeral or चतुर् (tadantavidhi) before आम्: नुट् (चतुर्णाम्, पञ्चानाम्, षण्णाम्)."""
    hit = anga_and_sup(state, "7.1.55")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "catur", *_SHAT, tadanta=True):
        return None
    if (sup.meta.get("upadesha_slp1") or "").strip() != "Am" or (sup.varnas and "nut_agama_inserted" in sup.varnas[0].tags):
        return None
    return sup


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    sup = _site(state)
    sup.varnas.insert(0, mk("n", "nut_agama_inserted"))
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.1.55",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "zawcaturByaSca",
    text_dev              = "षट्चतुर्भ्यश्च",
    samagra_slp1          = "zaw-caturByaH Ami nuw ca",
    samagra_dev           = "षट्-चतुर्भ्यः आमि नुट् च",
    padaccheda_dev        = "षट्-चतुर्भ्यः च",
    why_dev               = "(सूत्रम् 7.1.55) षट्चतुर्भ्यश्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
