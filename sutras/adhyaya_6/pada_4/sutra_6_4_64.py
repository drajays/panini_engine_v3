"""
6.4.64  आतोऽर्थलोप इटि च  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=604064
- Kāśikā: आतोऽर्थलोप इटि च (क्ङिति-परे आ-लोपः)
- Cross-validation: tests/unit/test_yAyAvar_yang_varac_purvavidhau_lesson.py
  (**1.1.58** *vareya* blocks after **6.4.48** *yaṅ* *a*-lopa)

When the **aṅga** ends in long **ā** (``A``) before an **ārddhadhātuka** affix tagged
*kṅiti* whose effective segment begins with vowel ``i``, elide that terminal ``A``.
(*adita*: ``adA`` + ``i…``.)

Teaching JSON **P035** (*papatuḥ*): terminal ``A`` of **pā** before *liṭ* **atus**
(tagged *kit* → *kṅiti*) whose first phoneme is **a** — narrow ``इटि`` / *ārdhadhātuka*
reading for this glass-box spine.

Structural *varac* (*yāyāvar*): *aṅga* ending in ``A`` before *kṅiti* **varac** is
blocked when **1.1.58** is on and **6.4.48** has already lopa'd the *yaṅ* *a*
(*para-nimitta* — not *sthānivat* for this *pūrva-vidhi*).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_6.pada_4.sutra_6_4_48 import META_KTIC_A_LOPA, META_YA_G_A_LOPA

_GATE_1_1_58 = "1_1_58_na_padAnta_etc"
_VARAC_UPADESHA = frozenset({"varac", "vara"})


def _find_dhatu_idx(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            return i
    return None


def _blocked_by_1_1_58_vareya_after_6_4_48(state: State, dh) -> bool:
    if not state.paribhasha_gates.get(_GATE_1_1_58):
        return False
    if dh.meta.get("6_4_64_lopa_blocked"):
        return True
    return dh.meta.get("6_4_48_a_lopa_done") is True and (
        dh.meta.get(META_YA_G_A_LOPA) is True or dh.meta.get(META_KTIC_A_LOPA) is True
    )


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


def _varac_kngiti_idx(state: State, dhi: int) -> int | None:
    """First *varac* *kṅiti* *kṛt* after dhātu — *yāyāvar* lesson."""
    for j in range(dhi + 1, len(state.terms)):
        t = state.terms[j]
        if t.kind != "pratyaya" or "krt" not in t.tags:
            continue
        if "kngiti" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _VARAC_UPADESHA and not (t.varnas and t.varnas[0].slp1 == "v"):
            continue
        if t.meta.get("6_4_64_target_done"):
            continue
        return j
    return None


def _site_ic(state: State) -> bool:
    dhi = _find_dhatu_idx(state)
    if dhi is None:
        return False
    dh = state.terms[dhi]
    if not dh.varnas or dh.varnas[-1].slp1 != "A":
        return False
    if _blocked_by_1_1_58_vareya_after_6_4_48(state, dh):
        return False
    if dh.meta.get("6_4_64_lopa_blocked"):
        return False
    return _ic_pratyaya_idx(state, dhi) is not None


def _site_p035(state: State) -> bool:
    dhi = _find_dhatu_idx(state)
    if dhi is None:
        return False
    dh = state.terms[dhi]
    if not dh.varnas or dh.varnas[-1].slp1 != "A":
        return False
    if _blocked_by_1_1_58_vareya_after_6_4_48(state, dh):
        return False
    if dh.meta.get("6_4_64_lopa_blocked"):
        return False
    return _atus_pratyaya_idx(state, dhi) is not None


def _site_varac(state: State) -> bool:
    dhi = _find_dhatu_idx(state)
    if dhi is None:
        return False
    dh = state.terms[dhi]
    if not dh.varnas or dh.varnas[-1].slp1 != "A":
        return False
    if _blocked_by_1_1_58_vareya_after_6_4_48(state, dh):
        return False
    if dh.meta.get("6_4_64_lopa_blocked"):
        return False
    return _varac_kngiti_idx(state, dhi) is not None


def cond(state: State) -> bool:
    return _site_ic(state) or _site_p035(state) or _site_varac(state)


def act(state: State) -> State:
    dhi = _find_dhatu_idx(state)
    if dhi is None:
        return state
    dh = state.terms[dhi]
    if _site_varac(state):
        j = _varac_kngiti_idx(state, dhi)
        if j is None or not dh.varnas or dh.varnas[-1].slp1 != "A":
            return state
        dh.varnas.pop()
        state.terms[j].meta["6_4_64_target_done"] = True
        return state
    if _site_p035(state):
        j = _atus_pratyaya_idx(state, dhi)
        if j is None or not dh.varnas or dh.varnas[-1].slp1 != "A":
            return state
        dh.varnas.pop()
        state.terms[j].meta["6_4_64_target_done"] = True
        return state
    if _site_ic(state):
        j = _ic_pratyaya_idx(state, dhi)
        if j is None or not dh.varnas or dh.varnas[-1].slp1 != "A":
            return state
        dh.varnas.pop()
        state.terms[j].meta["6_4_64_target_done"] = True
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="6.4.64",
    sutra_type=SutraType.VIDHI,
    text_slp1="Ato arthalopa iw ca",
    text_dev="आतोऽर्थलोप इटि च",
    padaccheda_dev="आतः · अर्थ-लोपः · इटि · च",
    why_dev="आकारस्य लोपः क्ङिति-परे (इटि-मार्गः, अतुस्-मार्गः प०३५, वरच्-मार्गः)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
