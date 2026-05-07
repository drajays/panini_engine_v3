"""
7.3.37  शाच्छासाह्वाव्यावेपां युक्  —  VIDHI (narrow)

*Śā* / *chā* / *sā* / *hvā* / *vyā* / *vepā* / *pā* before *ṇic* (*Ric*): insert
*y* (*yuk*) at the end of the *dhātu* *aṅga* immediately preceding the *ṇic*
``Term`` (SLP1 ``y`` = semivowel य्).

Engine: eligibility is the sūtra’s own stem list in SLP1 (``pA`` = पा, ``SA`` =
śā, …). *Nimitta:* following ``Term`` has ``nic`` / ``sanadi`` and
``upadesha_slp1`` ``Ric`` / ``Nic`` after *it* marking is irrelevant here — we
run after *ṇ*/*c* lopa so the trigger is ``nic`` tag + residual ``i`` shape
or full ``Ric`` tape not yet merged.

Idempotency: ``Term.meta['7_3_37_yuk_augment_done']`` on the *dhātu*.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk

# SLP1 bases listed in **7.3.37** (śā…vepā…pā) — halanta in upadeśa is stripped.
_YUK_NIC_DHATU_UPADESHA_BASES: frozenset[str] = frozenset(
    {
        "SA",  # śā
        "CA",  # chā
        "sA",  # sā
        "hvA",  # hvā
        "vyA",  # vyā
        "vepA",  # vepā
        "pA",  # pā
    }
)


def _norm_upa(up: str) -> str:
    t = (up or "").strip()
    if t.endswith("~"):
        t = t[:-1]
    return t


def _following_is_nic(state: State, di: int) -> bool:
    if di + 1 >= len(state.terms):
        return False
    nxt = state.terms[di + 1]
    if "nic" not in nxt.tags and "sanadi" not in nxt.tags:
        return False
    up = _norm_upa(nxt.meta.get("upadesha_slp1") or "")
    if up not in {"Ric", "Nic"}:
        return False
    return True


def _find(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("7_3_37_yuk_augment_done"):
            continue
        base = _norm_upa(t.meta.get("upadesha_slp1") or "")
        if base not in _YUK_NIC_DHATU_UPADESHA_BASES:
            continue
        if not _following_is_nic(state, i):
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas.append(mk("y"))
    t.meta["7_3_37_yuk_augment_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.3.37",
    sutra_type=SutraType.VIDHI,
    text_slp1="SAcCAsAhvAvyAvepAM yuk",
    text_dev="शाच्छासाह्वाव्यावेपां युक्",
    padaccheda_dev="श-आदिभ्यः / च-आदिभ्यः / … / युक्",
    why_dev="णिच्-परे शाच्छादिभ्यो युक्-आगमः (पाययते)।",
    anuvritti_from=("7.3.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
