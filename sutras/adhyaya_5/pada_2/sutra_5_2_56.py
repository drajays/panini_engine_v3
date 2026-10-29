"""
5.2.56  विंशत्यादिभ्यस्तमडन्यतरस्याम्  —  VIDHI

Padaccheda: विंशति-आदिभ्यः तमट् अन्यतरस्याम्

विंशत्यादिभ्यस्तमडन्यतरस्याम् (5.2.56)
Pāṭha: ashtadhyayi.com data.txt row i=52056 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_56_viMSatyAdi_56"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.56", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.56"
    return state


from engine.taddhita_attach import taddhita_site
from engine.luk import live_taddhita
from engine.state import Term
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
from phonology.varna import parse_slp1_upadesha_sequence


# SHORTCUT S42: the saṃkhyā lists of this sūtra (viṃśatyādi, śatādi, ṣaṣṭyādi, māsa …) are inline stem sets, not gaṇapāṭha lookups
def _site(state: State):
    i = live_taddhita(state, only_from=("5.2.48",), upadesha=("qaw",))
    if i is None or i == 0 or state.meta.get("done:tamaw") or not vivaksita(state, "taddhitArtha", "tasyapUraRa"):
        return None
    t = state.terms[i - 1]
    flat = "".join(v.slp1 for v in t.varnas)
    return i if flat in {'viMSati', 'triMSat', 'catvAriMSat', 'paYcASat', 'zazwi', 'saptati', 'aSIti', 'navati'} else None


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return _legacy_act(state)
    state.meta["done:tamaw"] = True
    if policy_pick(state, "5.2.56", 2) == 1:              # vā: no āgama
        return state
    state.terms.insert(i, Term(kind="agama", varnas=list(parse_slp1_upadesha_sequence("tamaw")), tags={"agama", "upadesha"}, meta={"upadesha_slp1": "tamaw"}))
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viMSatyAdiByastamaqanyatarasyAm",
    text_dev              = "विंशत्यादिभ्यस्तमडन्यतरस्याम्",
    samagra_slp1          = "tasya pUraRe iti viMSati-AdiByaH qawaH anyatarasyAm tamaw",
    samagra_dev           = "'तस्य पूरणे' (इति) विंशति-आदिभ्यः डटः अन्यतरस्याम् तमट्",
    padaccheda_dev        = "विंशति-आदिभ्यः तमट् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 5.2.56) विंशत्यादिभ्यस्तमडन्यतरस्याम्।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
