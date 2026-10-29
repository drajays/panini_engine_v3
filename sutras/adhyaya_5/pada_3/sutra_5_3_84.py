"""
5.3.84  शेवलसुपरिविशालवरुणार्यमादीनां तृतीयात्  —  VIDHI

Padaccheda: शेवल-सुपरि-विशाल-वरुण-अर्यम-आदीनाम् तृतीयात्

शेवलसुपरिविशालवरुणार्यमादीनां तृतीयात् (5.3.84)
Pāṭha: ashtadhyayi.com data.txt row i=53084 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_84_Sevalasupa_84"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.84", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.84"
    return state


from engine.taddhita_attach import sense_in

_NAMES = ("Wac", "Gan", "ilac", "aqac", "vuc")      # the pratyayas of 5.3.78 – 80; ghan is ajādi once 7.1.2 has made it iya


def _site(state: State, n: int, only=None):
    """The stem Term whose letters after the n-th vowel go: a name before a ṭh-initial or vowel-initial taddhita of the anukampā group."""
    if not sense_in(state, "5.3.76", "5.3.77"):
        return None
    for i in range(len(state.terms) - 1):
        t, pr = state.terms[i], state.terms[i + 1]
        if "prātipadika" not in t.tags or t.meta.get("5_3_83_done") or not {"taddhita", "pratyaya"} <= pr.tags or not pr.varnas:
            continue
        first = pr.varnas[0].slp1
        if not (first == "W" or first in "aAiIuUfFxXeEoO" or pr.meta.get("upadesha_slp1") == "Gan"):      # SHORTCUT S56: ghan counts as ajādi (its iya is 7.1.2, a later phase)
            continue
        flat = "".join(v.slp1 for v in t.varnas)
        if only is not None and not flat.startswith(only):
            continue
        idx = [k for k, v in enumerate(t.varnas) if v.slp1 in "aAiIuUfFxXeEoO"]
        if len(idx) > n and idx[n - 1] + 1 < len(t.varnas) and "lex:manuzyanAman" in t.tags:
            return t, idx[n - 1]
    return None


def _new_cond(state: State) -> bool:
    return _site(state, 3, ("Sevala", "supari", "viSAla", "varuRa", "aryama")) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    s = _site(state, 3, ("Sevala", "supari", "viSAla", "varuRa", "aryama"))
    if s is None:
        return _legacy_act(state)
    t, k = s
    del t.varnas[k + 1:]      
    t.meta["5_3_83_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SevalasupariviSAlavaruRAryamAdInAM tftIyAt",
    text_dev              = "शेवलसुपरिविशालवरुणार्यमादीनां तृतीयात्",
    samagra_slp1          = "prAtipadikAt anukampAyAm Wa-ajAdO Sevala-supari-viSAla-varuRa-aryamA-AdInAm tftIyAt UrDvamacaH lopaH",
    samagra_dev           = "प्रातिपदिकात् अनुकम्पायाम् ठ-अजादौ शेवल-सुपरि-विशाल-वरुण-अर्यमा-आदीनाम् तृतीयात् ऊर्ध्वमचः लोपः",
    padaccheda_dev        = "शेवल-सुपरि-विशाल-वरुण-अर्यम-आदीनाम् तृतीयात्",
    why_dev               = "(सूत्रम् 5.3.84) शेवलसुपरिविशालवरुणार्यमादीनां तृतीयात्।",
    anuvritti_from        = ('5.3.70',),
    apavada_of     = ('5.3.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
