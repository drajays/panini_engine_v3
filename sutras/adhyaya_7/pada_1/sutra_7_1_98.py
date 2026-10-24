"""
7.1.98  चतुरनडुहोरामुदात्तः  —  VIDHI

Padaccheda: चतुर्-अनडुहोः आम् उदात्तः

चतुरनडुहोरामुदात्तः (7.1.98)
Pāṭha: ashtadhyayi.com data.txt row i=71098 (Art. 14).
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
    """चतुरनडुहोरामुदात्तः — चतुर् / अनडुह् (with tadantavidhi) before a sarvanāmasthāna sup that is not sambuddhi: आम् (m is it, so only आ stands) is
    inserted after the last vowel — अनडु + आ + ह्, चतु + आ + र् (6.1.77 then gives अनड्वाह्, चत्वार्)."""
    hit = anga_and_sup(state, "7.1.98")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "catur", "anaquh", tadanta=True) or "sarvanamasthana" not in sup.tags or "sambuddhi" in sup.tags:
        return None
    return None if anga.meta.get("7_1_98_done") else anga


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    k = _last_ac(anga)
    a = mk("A"); a.tags.add("agama_Am")
    anga.varnas.insert(k + 1, a)
    anga.meta["7_1_98_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.1.98",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "caturanaquhorAmudAttaH",
    text_dev              = "चतुरनडुहोरामुदात्तः",
    samagra_slp1          = "catur-anaquhoH aNgasya sarvanAmasTAne AmudAttaH",
    samagra_dev           = "चतुर्-अनडुहोः अङ्गस्य सर्वनामस्थाने आमुदात्तः",
    padaccheda_dev        = "चतुर्-अनडुहोः आम् उदात्तः",
    why_dev               = "(सूत्रम् 7.1.98) चतुरनडुहोरामुदात्तः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
