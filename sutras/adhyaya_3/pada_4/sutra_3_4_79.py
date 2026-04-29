"""
3.4.79  टित आत्मनेपदानां टेरे  —  VIDHI (narrow)

Demo slice (भीषयते .md):
  For the ātmanepada 3sg ending `ta`, once its vowel is marked `Ti` (1.1.64),
  replace that `a` with `e` to yield `te`.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() not in {"ta", "iw"}:
            continue
        if t.meta.get("3_4_79_ter_done"):
            continue
        for vi in range(len(t.varnas) - 1, -1, -1):
            v = t.varnas[vi]
            if "Ti" in v.tags and v.slp1 in {"a", "i"}:
                return ti, vi
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    ti, vi = hit
    t = state.terms[ti]
    t.varnas[vi] = mk("e")
    t.meta["upadesha_slp1_original"] = t.meta.get("upadesha_slp1_original", t.meta.get("upadesha_slp1"))
    t.meta["upadesha_slp1"] = "te"
    t.meta["3_4_79_ter_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="3.4.79",
    sutra_type=SutraType.VIDHI,
    text_slp1="Tita AtmanepAdAnAM were",
    text_dev="टित आत्मनेपदानां टेरे",
    padaccheda_dev="टित् / आत्मनेपदानाम् / टेरे",
    why_dev="आत्मनेपद-प्रत्यये टि-भागे ‘अ’ स्थानि ‘ए’ (ते-आदेशः) — डेमो।",
    anuvritti_from=("3.4.78",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

