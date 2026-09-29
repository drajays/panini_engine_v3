"""
7.1.59  शे मुचादीनाम्  —  VIDHI (narrow demo)

Demo slice (मुञ्चति.md):
  When dhātu `muc` is followed by vikaraṇa `Sa`, insert nuṃ (`n`) after the
  last vowel of the dhātu (1.1.47 placement).

Engine:
  - recipe-armed by ``state.meta['7_1_59_num_arm']``.
  - performs the insertion directly on the dhātu term.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk
from phonology.pratyahara import is_dirgha, is_hrasva


def _is_ac(ch: str) -> bool:
    return bool(is_hrasva(ch) or is_dirgha(ch) or ch in {"e", "E", "o", "O"})


def _tudadi_nasal_upadha(dh) -> bool:
    """तृम्फादि read structurally: a tudādi upadeśa with a nasal upadhā (तृन्फँ,
    तुन्पँ, शुन्भँ, तृन्हूँ) — 6.4.24 drops it before श, the vārttika's num restores it."""
    if dh.meta.get("gana") != 6:
        return False
    up = (dh.meta.get("upadesha_slp1") or "").rstrip("~").rstrip("aAiIuUfFxeEoO~")
    return len(up) >= 2 and up[-2] in "nYRNmM"


def _dhatu(state: State):
    """मुचादि (मुच्, लुप्, विद्, लिप्, सिच्, कृत्, खिद्, पिश्) and, by the vārttika
    शे तृम्फादीनां नुम् वाच्यः, तृम्फादि — before the vikaraṇa श."""
    for i, dh in enumerate(state.terms[:-1]):
        if "dhatu" not in dh.tags or dh.meta.get("7_1_59_num_done"):
            continue
        if not ({"मुचादिः", "तुम्फादिः"} & set(dh.meta.get("antarganas") or ())
                or _tudadi_nasal_upadha(dh)):
            continue
        if (state.terms[i + 1].meta.get("upadesha_slp1") or "").strip() == "Sa":
            return dh
    return None


def _matches(state: State) -> bool:
    return _dhatu(state) is not None


def cond(state: State) -> bool:
    return _matches(state)


def act(state: State) -> State:
    if not _matches(state):
        return state
    dh = _dhatu(state)
    j = None
    for i in range(len(dh.varnas) - 1, -1, -1):
        if _is_ac(dh.varnas[i].slp1):
            j = i
            break
    if j is None:
        return state
    dh.varnas.insert(j + 1, mk("n"))
    dh.meta["7_1_59_num_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="7.1.59",
    sutra_type=SutraType.VIDHI,
    text_slp1="Se mucAdInAm (num)",
    text_dev="शे मुचादीनाम्",
    padaccheda_dev="शे / मुच-आदीनाम्",
    why_dev="श-विकरणे परे मुच्-आदीनां नुम्-आगमः (डेमो: मुञ्चति)।",
    anuvritti_from=("6.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

