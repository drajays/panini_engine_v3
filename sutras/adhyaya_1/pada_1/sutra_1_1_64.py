"""
1.1.64  अचोऽन्त्यादि टि  —  SAMJNA (narrow)

Demo use (भीषयते .md):
  Mark the final vowel of an ātmanepada tiṅ affix (e.g. `ta`) as `Ti` so that
  3.4.79 can rewrite it (a → e).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.pratyahara import is_dirgha, is_hrasva


def _is_ac(ch: str) -> bool:
    return bool(is_hrasva(ch) or is_dirgha(ch) or ch in {"e", "E", "o", "O"})


def _eligible(state: State):
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya" or "pratyaya" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() not in {"ta", "iw"}:
            continue
        for vi in range(len(t.varnas) - 1, -1, -1):
            v = t.varnas[vi]
            if _is_ac(v.slp1) and "Ti" not in v.tags:
                yield ti, vi
                break


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    hit = next(_eligible(state), None)
    if hit is None:
        return state
    ti, vi = hit
    state.terms[ti].varnas[vi].tags.add("Ti")
    state.samjna_registry[("1.1.64_Ti", ti, vi)] = True
    return state


SUTRA = SutraRecord(
    sutra_id="1.1.64",
    sutra_type=SutraType.SAMJNA,
    r1_form_identity_exempt=True,
    text_slp1="aco antyAdi Ti",
    text_dev="अचोऽन्त्यादि टि",
    padaccheda_dev="अचः अन्त्य-आदि टि",
    why_dev="प्रत्ययस्य अन्त्य-अच्-आदि-भागः ‘टि’ संज्ञकः (डेमो-स्लाइस)।",
    anuvritti_from=("1.1.63",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

