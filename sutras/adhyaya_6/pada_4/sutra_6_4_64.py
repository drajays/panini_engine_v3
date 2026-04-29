"""
6.4.64  आतोऽर्थलोप इटि च  —  VIDHI (narrow demo)

When the **aṅga** ends in long **ā** (``A``) before an **ārddhadhātuka** affix tagged
*kṅiti* whose effective segment begins with vowel ``i``, elide that terminal ``A``.
(*adita*: ``adA`` + ``i…``.)

Recipe arms ``state.meta['6_4_64_A_lopa_kngitic_i_arm']``; requires ``kngiti`` on the
``i``‑initial pratyaya (set by **1.2.17** demo path for ``ic``).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find_dhatu_idx(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _ic_pratyaya_idx(state: State, dhi: int) -> int | None:
    """First pratyaya after dhātu with kngiti + initial ``i``."""
    for j in range(dhi + 1, len(state.terms)):
        t = state.terms[j]
        if t.kind != "pratyaya":
            continue
        if "kngiti" not in t.tags:
            continue
        if not t.varnas or t.varnas[0].slp1 != "i":
            continue
        if t.meta.get("6_4_64_target_done"):
            continue
        return j
    return None


def cond(state: State) -> bool:
    if not state.meta.get("6_4_64_A_lopa_kngitic_i_arm"):
        return False
    dhi = _find_dhatu_idx(state)
    if dhi is None:
        return False
    dh = state.terms[dhi]
    if not dh.varnas or dh.varnas[-1].slp1 != "A":
        return False
    if dh.meta.get("6_4_64_lopa_blocked"):
        return False
    j = _ic_pratyaya_idx(state, dhi)
    return j is not None


def act(state: State) -> State:
    dhi = _find_dhatu_idx(state)
    if dhi is None:
        return state
    dh = state.terms[dhi]
    j = _ic_pratyaya_idx(state, dhi)
    if j is None:
        return state
    if not dh.varnas or dh.varnas[-1].slp1 != "A":
        return state
    dh.varnas.pop()
    state.terms[j].meta["6_4_64_target_done"] = True
    state.meta["6_4_64_A_lopa_kngitic_i_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.64",
    sutra_type=SutraType.VIDHI,
    text_slp1="Ato arthalopa iw ca",
    text_dev="आतोऽर्थलोप इटि च",
    padaccheda_dev="आतः · अर्थ-लोपः · इटि · च",
    why_dev="घ्वादावङ्गान्तात् कार्य इट्प्रत्यये टे लोपोऽर्थवत् (अदित-संदर्भ)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
