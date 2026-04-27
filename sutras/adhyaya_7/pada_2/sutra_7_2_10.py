"""
7.2.10  एकाच उपदेशेऽनुदात्तात्  —  PRATISHEDHA

Narrow v3: blocks **7.2.35** (iṭ-āgama) when the pipeline marks a one-vowel
(ekāc) **anudātta** dhātu — ``state.meta['ekac_dhatu']`` and **not**
``state.meta['udatta_dhatu']`` (seṭ / udātta-śāstra rows from
``pipelines/krdanta`` / JSON ``flags.udatta``).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("ekac_dhatu"):
        return False
    if state.meta.get("udatta_dhatu"):
        return False
    if "7.2.35" in state.blocked_sutras:
        return False
    # Default narrow v3: kṛt ārdhadhātuka.
    if any("krt" in t.tags and "ardhadhatuka" in t.tags for t in state.terms):
        return True
    # Opt-in luṅ: treat sic as ārdhadhātuka locus (glass-box).
    if state.meta.get("7_2_10_allow_sic") and state.meta.get("luN_sic_ardhadhatuka"):
        return any((t.meta.get("upadesha_slp1") or "").strip() == "sic" for t in state.terms)
    return False


def act(state: State) -> State:
    return state


SUTRA = SutraRecord(
    sutra_id         = "7.2.10",
    sutra_type       = SutraType.PRATISHEDHA,
    text_slp1        = "ekAc upadeSe anudAttAt",
    text_dev         = "एकाच उपदेशेऽनुदात्तात्",
    padaccheda_dev   = "एकाच् उपदेशे अनुदात्तात्",
    why_dev          = "एकाच् धातौ आर्धधातुके इट्-प्रतिषेधः (त्रिच्-पथ)।",
    anuvritti_from   = (),
    cond             = cond,
    act              = act,
    blocks_sutra_ids = ("7.2.35",),
)

register_sutra(SUTRA)
