"""
6.1.114  हशि च  —  VIDHI

Padaccheda: हशि · च

हशि च (6.1.114)
Pāṭha: ashtadhyayi.com data.txt row i=61114 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from phonology.pratyahara import build_pratyahara

HAS = build_pratyahara("h", "S")


def _next_varna(state: State, ti: int, vi: int):
    t = state.terms[ti]
    if vi + 1 < len(t.varnas):
        return t.varnas[vi + 1]
    return next((u.varnas[0] for u in state.terms[ti + 1:] if u.varnas), None)


def _find(state: State):
    """haśi ca (6.1.114): ru after a, before a haś (h, y v r l, ñ m ṅ ṇ n, jh bh, gh ḍh dh, j b g ḍ d) → u: manobhyām, manobhiḥ."""
    for ti, t in enumerate(state.terms):
        for vi, v in enumerate(t.varnas):
            if "ru_intermediate" not in v.tags or vi == 0:
                continue
            if t.varnas[vi - 1].slp1 != "a":                      # ato roḥ: a (hrasva) before the ru
                continue
            nx = _next_varna(state, ti, vi)
            if nx is not None and nx.slp1 in HAS:
                return ti, vi
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is not None:
        ti, vi = hit
        state.terms[ti].varnas[vi] = mk("u")                      # then 6.1.87 ād guṇaḥ: a + u → o
        state.meta["__why_now_dev__"] = "अतः परस्य रु-इत्यस्य हशि परे उत्व (६.१.११४)।"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.114",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "haSi ca",
    text_dev              = "हशि च",
    samagra_slp1          = "aplutAt ataH roH ut haSi",
    samagra_dev           = "अप्लुतात् अतः रोः उत् हशि",
    padaccheda_dev        = "हशि · च",
    why_dev               = "(सूत्रम् 6.1.114) हशि च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
