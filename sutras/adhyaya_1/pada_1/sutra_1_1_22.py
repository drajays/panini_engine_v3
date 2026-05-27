"""
1.1.22  (tarap-tamapau ghaḥ)  —  SAMJNA; *devanāgarī* = ``_TEXT_DEV`` (ashtadhyayi *i* 11022 *s* line).

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11022):** the taddhita pratyāyas *tar* + *p* and *tama* + *p*
(***tarap***, ***tamap***) are termed *gha* (घ) — distinct from the **1.1.20** *ghu* (घु) *dhātu* *set*.

v3: ``samjna_registry['gha']`` = *frozenset* {``tarap`` , ``tamap``} in SLP1/Velthuis *upadeśa* shape; *vidhi* that
refers to *ghal* / *pratyaya* *gha* in this sense can use ``taddhita_pratyaya_upadesha_slp1_is_gha``.  No *Term* mutation.
"""
from __future__ import annotations

from typing import FrozenSet

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# Taddhita *upadeśa* in v3 (5.3.x *tara* / *tama*; **p** in *pratyaya* *upadeśa*).
GHA_TADDHITA_PRATYAYA_UPADESHA_SLP1: FrozenSet[str] = frozenset(
    {
        "tarap",  # तरप्
        "tamap",  # तमप्
    }
)

GHA_KEY: str = "gha"

# Exact ``s`` (i=11022).
_TEXT_DEV: str = "तरप्तमपौ घः"


def _state_has_gha_taddhita(state: State) -> bool:
    """True iff some Term is a *taddhita* *pratyaya* with *upadeśa*-SLP1 in
    the *gha* set. The registry-stamp fires only when a *tarap*/*tamap*
    *pratyaya* is on the tape (see audit P1a)."""
    for t in state.terms:
        if "taddhita" not in t.tags and t.kind != "pratyaya":
            continue
        u = (t.meta.get("upadesha_slp1") or "").strip()
        if u in GHA_TADDHITA_PRATYAYA_UPADESHA_SLP1:
            return True
    return False


def cond(state: State) -> bool:
    if state.samjna_registry.get(GHA_KEY) == GHA_TADDHITA_PRATYAYA_UPADESHA_SLP1:
        return False
    return _state_has_gha_taddhita(state)


def act(state: State) -> State:
    state.samjna_registry[GHA_KEY] = GHA_TADDHITA_PRATYAYA_UPADESHA_SLP1
    return state


def taddhita_pratyaya_upadesha_slp1_is_gha(state: State, upadesha_slp1: str) -> bool:
    m = state.samjna_registry.get(GHA_KEY)
    if not isinstance(m, frozenset):
        return False
    return upadesha_slp1 in m


def gha_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get(GHA_KEY) == GHA_TADDHITA_PRATYAYA_UPADESHA_SLP1


_WHY = (
    "तरप्-तमप्-औ, घ-संज्ञा — ईषद्-अतिशय-तम-प्रत्ययौ।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.22",
    sutra_type     = SutraType.SAMJNA,
    # Readable Velthuis; *e* compact: ``taraptamapaughah``
    text_slp1      = "tarap-tamapO ghaH",
    text_dev       = _TEXT_DEV,
    padaccheda_dev = "तरप्-तमपौ / घः",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
