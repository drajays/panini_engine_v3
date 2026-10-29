"""
5.2.58  षष्ट्यादेश्चासंख्यादेः  —  VIDHI

Padaccheda: षष्टि-आदेः च अ-सङ्‍ख्या-आदेः

षष्ट्यादेश्चासंख्याऽऽदेः (5.2.58)
Pāṭha: ashtadhyayi.com data.txt row i=52058 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_58_zazwyAdeSc_58"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.58", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.58"
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
    return i if flat in {'zazwi', 'saptati', 'aSIti', 'navati'} and "lex:saMKyAdi" not in t.tags else None


def cond(state: State) -> bool:
    return _site(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    i = _site(state)
    if i is None:
        return _legacy_act(state)
    state.meta["done:tamaw"] = True
    state.terms.insert(i, Term(kind="agama", varnas=list(parse_slp1_upadesha_sequence("tamaw")), tags={"agama", "upadesha"}, meta={"upadesha_slp1": "tamaw"}))
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'zazwyAdeScAsaMKyAdeH',
    text_dev              = 'षष्ट्यादेश्चासंख्यादेः',
    samagra_slp1          = "tasya pUraRe iti asaNKyAdeH zazwyAdeH qawaH nityam tamaw ",
    samagra_dev           = "'तस्य पूरणे' (इति) असङ्ख्यादेः षष्ट्यादेः डटः नित्यम् तमट् ।",
    padaccheda_dev        = "षष्टि-आदेः च अ-सङ्‍ख्या-आदेः",
    why_dev               = "(सूत्रम् 5.2.58) षष्ट्यादेश्चासंख्याऽऽदेः।",
    anuvritti_from        = ('4.1.82',),
    apavada_of     = ('5.2.56',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
