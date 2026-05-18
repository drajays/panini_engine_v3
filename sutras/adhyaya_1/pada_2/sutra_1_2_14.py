"""
1.2.14  हनः सिच्  —  NIYAMA

Anuvṛtti: aniṭ domain (from 1.2.1 adhikāra).

Meaning: The root "han" (√han, to kill; upadesha_slp1 = "han") before
the suffix "sic" (सिच्; the luṅ-lakāra suffix) is aniṭ — it does NOT
take the iṭ augment before sic.

Engine:
  - Requires a dhātu Term with upadesha_slp1 == "han".
  - Requires a following pratyaya Term with upadesha_slp1 == "si~c".
  - Guards re-entry via dhātu meta["aniT_1_2_14"].
  - Tags the dhātu "aniT" (no surface change → r1_form_identity_exempt=True).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_HAN_UPADESHA: frozenset = frozenset({"han"})
_SIC_UPADESHA: frozenset = frozenset({"si~c", "sic"})


def _find(state: State) -> int | None:
    han_idx: int | None = None
    sic_found: bool = False

    for i, t in enumerate(state.terms):
        if "dhatu" in t.tags:
            up = (t.meta.get("upadesha_slp1") or "").strip()
            if up in _HAN_UPADESHA and not t.meta.get("aniT_1_2_14"):
                han_idx = i
        elif han_idx is not None and "pratyaya" in t.tags:
            up = (t.meta.get("upadesha_slp1") or "").strip()
            if up in _SIC_UPADESHA:
                sic_found = True
                break

    if han_idx is not None and sic_found:
        return han_idx
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("aniT")
    state.terms[i].meta["aniT_1_2_14"] = True
    state.samjna_registry["1_2_14_han_sic_aniT"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.14",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "hanaH sic",
    text_dev              = "हनः सिच्",
    padaccheda_dev        = "हनः / सिच् (अनिट्)",
    why_dev               = ("√हन्-धातुः सिच्-परः अनिट् — "
                             "लुङि इडागमः न भवति।"),
    anuvritti_from        = ("1.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
