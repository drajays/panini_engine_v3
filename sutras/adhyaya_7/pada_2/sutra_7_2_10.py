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


# ārdhadhātuka val-initial affixes that would take iṭ by 7.2.35 (sya, tās,
# sic, sīyuṭ); liṭ endings are not here — there 7.2.13 (krādi-niyama) decides.
_VALADI_ARDHADHATUKA = frozenset({"sya", "tAs", "tAsi", "tAsi~", "sic", "sIyuw", "sIy"})


def _anudatta_ekac_before_valadi(state: State) -> bool:
    """एकाच उपदेशेऽनुदात्तात् — from the dhātu's own upadeśa properties (the
    dhātupāṭha's anudātta/aniṭ flag, one vowel), before a val-ādi ārdhadhātuka.
    7.2.70 ऋद्धनोः स्ये is its apavāda: ṛ-final roots and हन् take iṭ before sya."""
    dh = next((t for t in state.terms if "dhatu" in t.tags and "abhyasa" not in t.tags), None)
    if dh is None or not dh.meta.get("anit_dhatu"):
        return False
    if sum(v.slp1 in "aAiIuUfFxXeEoO" for v in dh.varnas) != 1:
        return False
    rest = state.terms[state.terms.index(dh) + 1:]
    after = [(t.meta.get("upadesha_slp1") or "").strip() for t in rest]
    hit = next((u for u in after if u in _VALADI_ARDHADHATUKA), None)
    if hit is None and any(t.meta.get("source_lakara_upadesha") == "liG" and "ardhadhatuka" in t.tags and t.varnas
                           and t.varnas[0].slp1 not in "aAiIuUfFxXeEoOy" for t in rest):
        hit = "sIyuw"                                  # āśīrliṅ is ārdhadhātuka (3.4.116): कृषीष्ट
    if hit is None:
        return False
    if hit == "sya" and (dh.varnas[-1].slp1 == "f"
                         or (dh.meta.get("upadesha_slp1") or "").strip() == "hana~"):
        return False                                   # 7.2.70: करिष्यति, हनिष्यति
    return True


def cond(state: State) -> bool:
    if not state.meta.get("ekac_dhatu"):
        return _anudatta_ekac_before_valadi(state) and "7.2.35" not in state.blocked_sutras
    if state.meta.get("udatta_dhatu"):
        return False
    if "7.2.35" in state.blocked_sutras:
        return False
    # *Luṭ* *tāsi* / *lṛṭ* *sya* spine (अद् … अत्ता / अत्स्यति): block iṭ on ekāc *ad*.
    if (
        state.meta.get("luT_ad_ekac_spine")
        or state.meta.get("lRT_ad_ekac_spine")
        or state.meta.get("lRG_ad_ekac_spine")
    ):
        return True
    # Default narrow v3: kṛt ārdhadhātuka.
    if any("krt" in t.tags and "ardhadhatuka" in t.tags for t in state.terms):
        return True
    # Opt-in luṅ: treat sic as ārdhadhātuka locus (glass-box).
    if state.meta.get("7_2_10_allow_sic") and state.meta.get("luN_sic_ardhadhatuka"):
        return any((t.meta.get("upadesha_slp1") or "").strip() == "sic" for t in state.terms)
    return _anudatta_ekac_before_valadi(state)


def act(state: State) -> State:
    return state


SUTRA = SutraRecord(
    sutra_id         = "7.2.10",
    sutra_type       = SutraType.PRATISHEDHA,
    text_slp1        = 'ekAca upadeSenudAttAt',
    text_dev         = 'एकाच उपदेशेऽनुदात्तात्',
    padaccheda_dev   = "एकाच् उपदेशे अनुदात्तात्",
    why_dev          = "एकाच् धातौ आर्धधातुके इट्-प्रतिषेधः (त्रिच्-पथ)।",
    anuvritti_from   = (),
    cond             = cond,
    act              = act,
    blocks_sutra_ids = ("7.2.35",),
)

register_sutra(SUTRA)
