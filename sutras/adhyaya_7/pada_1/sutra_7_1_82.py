"""
7.1.82  सावनडुहः  —  VIDHI

Padaccheda: सौ अनडुहः

सावनडुहः (7.1.82)
Pāṭha: ashtadhyayi.com data.txt row i=71082 (Art. 14).
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
    """सावनडुहः — अनडुह् (with tadantavidhi) before su (sau, also the sambuddhi): नुम् after the last vowel: अनड्वान्, हे अनड्वन्."""
    hit = anga_and_sup(state, "7.1.82")
    if hit is None:
        return None
    anga, sup = hit
    if not is_stem(anga, "anaquh", tadanta=True) or anga.meta.get("7_1_82_done"):
        return None
    if (sup.meta.get("upadesha_slp1") or "").strip() not in {"s~", "su", "su~"}:
        return None
    return anga if (anga.meta.get("7_1_98_done") or anga.meta.get("7_1_99_done")) else None     # the vowel it stands after is āM's / aM's


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    anga = _site(state)
    k = _last_ac(anga)
    n = mk("n"); n.tags.add("mit")
    anga.varnas.insert(k + 1, n)
    anga.meta["7_1_82_done"] = True
    return state

SUTRA = SutraRecord(
    sutra_id              = "7.1.82",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "sAvanaquhaH",
    text_dev              = "सावनडुहः",
    samagra_slp1          = "anaquhaH aNgasya At sO num",
    samagra_dev           = "अनडुहः अङ्गस्य आत् सौ नुम्",
    padaccheda_dev        = "सौ अनडुहः",
    why_dev               = "(सूत्रम् 7.1.82) सावनडुहः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
