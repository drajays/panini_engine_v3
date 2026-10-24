"""
7.1.99  अम् सम्बुद्धौ  —  VIDHI

Padaccheda: अम् सम्बुद्धौ

अम् सम्बुद्धौ (7.1.99)
Pāṭha: ashtadhyayi.com data.txt row i=71099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.declension import anga_and_sup, is_stem, vowel_initial
from phonology import mk


def _last_ac(anga):
    ix = [k for k, v in enumerate(anga.varnas) if v.slp1 in "aAiIuUfFxXeEoO"]
    return ix[-1] if ix else None


def _site(state: State):
    """अम् सम्बुद्धौ — चतुर् / अनडुह् before the sambuddhi su: अम् (m is it → a) after the last vowel: हे अनड्वन् (अनडु + अ + ह्)."""
    hit = anga_and_sup(state, "7.1.99")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "catur", "anaquh", tadanta=True) or "sambuddhi" not in sup.tags or anga.meta.get("7_1_99_done"):
        return None
    return anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    k = _last_ac(anga)
    anga.varnas.insert(k + 1, mk("a"))
    anga.meta["7_1_99_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.1.99",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "am sambudDO",
    text_dev              = "अम् सम्बुद्धौ",
    samagra_slp1          = "catur-anaquhoH aNgasya sambudDO am",
    samagra_dev           = "चतुर्-अनडुहोः अङ्गस्य सम्बुद्धौ अम्",
    padaccheda_dev        = "अम् सम्बुद्धौ",
    why_dev               = "(सूत्रम् 7.1.99) अम् सम्बुद्धौ।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
