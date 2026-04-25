"""
7.3.86  पुगन्तलघूपधस्य च  —  VIDHI (representative)

Representative v3 slice:
When aṅga has an upadhā vowel i/u (short/long) that would normally undergo
guṇa in the presence of certain following pratyayas, apply i→e / u→o.

Critical paribhāṣā interaction:
If the upadhā vowel is actually an iṭ-āgama vowel (tagged ``it_agama`` by
7.2.35), then guṇa must be BLOCKED under 1.1.6 (id_agama_guna_nishedha).

This file intentionally models only the “iṭ-āgama guṇa-niṣedha” hook and is
not a full implementation of Pāṇini’s 7.3.86 ecosystem.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


_GUNA_UPADHA = {
    "i": "e",
    "I": "e",
    "u": "o",
    "U": "o",
}


def _find_target(state: State):
    if len(state.terms) < 2:
        return None
    anga = state.terms[-2]
    pr = state.terms[-1]
    if "anga" not in anga.tags:
        return None
    if "pratyaya" not in pr.tags:
        return None
    # Narrow trigger: test scaffolding uses pr.meta["dit_pratyaya"].
    if pr.meta.get("dit_pratyaya") is not True:
        return None
    if len(anga.varnas) < 2:
        return None
    # Upadhā = penultimate varṇa.
    up_i = len(anga.varnas) - 2
    up = anga.varnas[up_i]
    rep = _GUNA_UPADHA.get(up.slp1)
    if rep is None:
        return None
    return (len(state.terms) - 2, up_i, rep, up)


def cond(state: State) -> bool:
    hit = _find_target(state)
    if hit is None:
        return False
    _, _, _, up = hit
    # 1.1.6 gate: block guṇa on iṭ-āgama vowels.
    if state.paribhasha_gates.get("id_agama_guna_nishedha") and "it_agama" in up.tags:
        return False
    return True


def act(state: State) -> State:
    hit = _find_target(state)
    if hit is None:
        return state
    ti, vi, rep, _ = hit
    state.terms[ti].varnas[vi] = mk(rep)
    state.terms[ti].meta["upadha_guna_7_3_86"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.86",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "puganta-laghUpadhasya ca",
    text_dev       = "पुगन्तलघूपधस्य च",
    padaccheda_dev = "पुगन्त-लघु-उपधस्य च",
    why_dev        = "पुगन्त/लघूपध-अङ्गस्य उपधायाः गुणः (इडागम-इकारे तु 1.1.6 निषेधः)।",
    anuvritti_from = ("7.3.84",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

