"""
6.4.109  ये च  —  VIDHI

Padaccheda: ये च

ये च (6.4.109)
Pāṭha: ashtadhyayi.com data.txt row i=64109 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find(state: State):
    """ये च (उतश्च प्रत्ययात्… करोतेः 6.4.106/108): कृ's u-vikaraṇa drops before a
    y-initial pratyaya — कुरु+यात् → कुर्यात्."""
    for i in range(1, len(state.terms) - 1):
        u, nxt = state.terms[i], state.terms[i + 1]
        dh = state.terms[i - 1]
        if (u.meta.get("upadesha_slp1") or "").strip() != "u" or [v.slp1 for v in u.varnas] != ["u"]:
            continue
        if "dhatu" in dh.tags and "".join(v.slp1 for v in dh.varnas) == "kur" \
                and nxt.varnas and nxt.varnas[0].slp1 == "y":
            return u
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    _find(state).varnas = []
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.109",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "ye ca",
    text_dev              = "ये च",
    samagra_slp1          = "karoteH aNgasya utaH pratyayasya ye nityaM lopaH",
    samagra_dev           = "करोतेः अङ्गस्य उतः प्रत्ययस्य ये नित्यं लोपः",
    padaccheda_dev        = "ये च",
    why_dev               = "(सूत्रम् 6.4.109) ये च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
