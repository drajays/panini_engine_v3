"""
6.4.64  आतोऽर्थलोप इटि च  —  VIDHI (narrow demo)

When the **aṅga** ends in long **ā** (``A``) before an **ārddhadhātuka** affix tagged
*kṅiti* whose effective segment begins with vowel ``i``, elide that terminal ``A``.
(*adita*: ``adA`` + ``i…``.)

Teaching JSON **P035** (*papatuḥ*): terminal ``A`` of **pā** before *liṭ* **atus**
(tagged *kit* → *kṅiti*) whose first phoneme is **a** — narrow ``इटि`` / *ārdhadhātuka*
reading for this glass-box spine.

Engine:
  • **ic** path: ``state.meta['6_4_64_A_lopa_kngitic_i_arm']`` + ``i``‑initial *kṅiti*.
  • **P035** path: ``state.meta['P035_6_4_64_A_lopa_atus_arm']`` + **atus** *kṅiti*
    (``lit_atus`` / ``upadesha_slp1 == 'atus'``) with initial **a**.
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


def _atus_pratyaya_idx(state: State, dhi: int) -> int | None:
    """First *liṭ* *atus* pratyaya (*kṅiti*, initial ``a``) after dhātu — P035."""
    for j in range(dhi + 1, len(state.terms)):
        t = state.terms[j]
        if t.kind != "pratyaya":
            continue
        if "kngiti" not in t.tags:
            continue
        if not t.varnas or t.varnas[0].slp1 != "a":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if not (t.meta.get("lit_atus") is True or up == "atus"):
            continue
        if t.meta.get("6_4_64_target_done"):
            continue
        return j
    return None


def _site_ic(state: State) -> bool:
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
    return _ic_pratyaya_idx(state, dhi) is not None


def _site_p035(state: State) -> bool:
    if not state.meta.get("P035_6_4_64_A_lopa_atus_arm"):
        return False
    dhi = _find_dhatu_idx(state)
    if dhi is None:
        return False
    dh = state.terms[dhi]
    if not dh.varnas or dh.varnas[-1].slp1 != "A":
        return False
    if dh.meta.get("6_4_64_lopa_blocked"):
        return False
    return _atus_pratyaya_idx(state, dhi) is not None


def cond(state: State) -> bool:
    return _site_ic(state) or _site_p035(state)


def act(state: State) -> State:
    dhi = _find_dhatu_idx(state)
    if dhi is None:
        return state
    dh = state.terms[dhi]
    if _site_p035(state):
        j = _atus_pratyaya_idx(state, dhi)
        if j is None or not dh.varnas or dh.varnas[-1].slp1 != "A":
            return state
        dh.varnas.pop()
        state.terms[j].meta["6_4_64_target_done"] = True
        state.meta.pop("P035_6_4_64_A_lopa_atus_arm", None)
        return state
    if _site_ic(state):
        j = _ic_pratyaya_idx(state, dhi)
        if j is None or not dh.varnas or dh.varnas[-1].slp1 != "A":
            return state
        dh.varnas.pop()
        state.terms[j].meta["6_4_64_target_done"] = True
        state.meta["6_4_64_A_lopa_kngitic_i_arm"] = False
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.64",
    sutra_type=SutraType.VIDHI,
    text_slp1="Ato arthalopa iw ca",
    text_dev="आतोऽर्थलोप इटि च",
    padaccheda_dev="आतः · अर्थ-लोपः · इटि · च",
    why_dev="आकारस्य लोपः क्ङिति-परे (इटि-मार्गः, अतुस्-मार्गः प०३५) — अदित-दृष्टान्तः।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
