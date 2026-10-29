"""
5.2.49  नान्तादसंख्यादेर्मट्  —  VIDHI

Padaccheda: न-अन्तात् अ-सङ्‍ख्या-आदेः मट्

नान्तादसंख्याऽऽदेर्मट् (5.2.49)
Pāṭha: ashtadhyayi.com data.txt row i=52049 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_49_nAntAdasaM_49"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.49", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.49"
    return state


# SHORTCUT S43: saṃkhyā / saṃkhyādi are lex: tags from the caller (S33)
from engine.taddhita_attach import taddhita_site
from engine.luk import live_taddhita
from engine.state import Term
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
from phonology.varna import parse_slp1_upadesha_sequence


def _site(state: State):
    i = live_taddhita(state, only_from=("5.2.48",), upadesha=("qaw",))
    if i is None or i == 0 or state.meta.get("done:5.2.49") or not vivaksita(state, "taddhitArtha", "tasyapUraRa"):
        return None
    t = state.terms[i - 1]
    flat = "".join(v.slp1 for v in t.varnas)
    return i if "lex:saMKyA" in t.tags and "lex:saMKyAdi" not in t.tags and flat.endswith("n") else None


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return _legacy_act(state)
    state.meta["done:5.2.49"] = True
    state.terms[i - 1].tags.discard("bha")           # SHORTCUT S41: 1.4.18 was given before maṭ stood before the pratyaya; the pratyaya now begins with m, so the stem is pada (1.4.17), not bha
    state.terms.insert(i, Term(kind="agama", varnas=list(parse_slp1_upadesha_sequence("maw")), tags={"agama", "upadesha"}, meta={"upadesha_slp1": "maw"}))
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'nAntAdasaMKyAdermaw',
    text_dev              = 'नान्तादसंख्यादेर्मट्',
    samagra_slp1          = "tasya pUraRe iti asaNKyAdeH nAntAt saNKyAyAH qawaH maw",
    samagra_dev           = "'तस्य पूरणे' (इति) असङ्ख्यादेः नान्तात् सङ्ख्यायाः डटः मट्",
    padaccheda_dev        = "न-अन्तात् अ-सङ्‍ख्या-आदेः मट्",
    why_dev               = "(सूत्रम् 5.2.49) नान्तादसंख्याऽऽदेर्मट्।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
