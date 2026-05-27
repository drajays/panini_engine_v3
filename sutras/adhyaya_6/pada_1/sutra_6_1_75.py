"""
6.1.75  दीर्घात्  —  VIDHI

Full rule (with anuvṛtti from 6.1.73 hrasvaḥ [tuk] che ca):
  dīrghāt [tuk] — from a dīrgha vowel [tuk before C].

A dīrgha vowel ('A', 'I', 'U', 'e', 'E', 'o', 'O', 'F', 'X') immediately
followed by 'C' (cha) gets tuk (= 't') inserted after it.

Example: mleCCa (म्लेछँ) + anīya → mleC + anīya:
  'e' (dīrgha) before 'C' within the dhātu → insert t: mle-t-C
  → by 8.4.40 ścutva (t+C→c): mle-c-C + anīya = "mlecCanIya" (म्लेच्छनीय)

By 1.1.46 (āntaṭakitau): tuk is kit, placed after the dīrgha vowel.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import is_dirgha


def _find_dirgha_C(state: State):
    """Return (term_idx, vowel_idx) for dīrgha vowel immediately before C."""
    for ti, t in enumerate(state.terms):
        if t.meta.get("6_1_75_done"):
            continue
        for j in range(len(t.varnas) - 1):
            if is_dirgha(t.varnas[j].slp1) and t.varnas[j + 1].slp1 == "C":
                return (ti, j)
    # Cross-term: last varṇa of term[ti] is dīrgha, first of term[ti+1] is C
    for ti in range(len(state.terms) - 1):
        t0, t1 = state.terms[ti], state.terms[ti + 1]
        if t0.meta.get("6_1_75_done"):
            continue
        if t0.varnas and t1.varnas:
            if is_dirgha(t0.varnas[-1].slp1) and t1.varnas[0].slp1 == "C":
                return (ti, len(t0.varnas) - 1)
    return None


def cond(state: State) -> bool:
    return _find_dirgha_C(state) is not None


def act(state: State) -> State:
    hit = _find_dirgha_C(state)
    if hit is None:
        return state
    ti, j = hit
    state.terms[ti].varnas.insert(j + 1, mk("t"))
    state.terms[ti].meta["6_1_75_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.75",
    sutra_type=SutraType.VIDHI,
    text_slp1="dIrGAt (tuk Cet)",
    text_dev="दीर्घात्",
    padaccheda_dev="दीर्घात्",
    why_dev=(
        "दीर्घस्वरात् परः अव्यवहितः छकारः विद्यते चेत् दीर्घस्वरस्य 'तुक्' आगमः।"
        " आद्यन्तौ टकितौ १.१.४६ इत्यनेन स्वरात् अनन्तरम्।"
    ),
    anuvritti_from=("6.1.73",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
