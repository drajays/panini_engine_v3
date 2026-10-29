"""
5.3.4  एतेतौ रथोः  —  VIDHI

Padaccheda: एत-इतौ र-थोः

एतेतौ रथोः (5.3.4)
Pāṭha: ashtadhyayi.com data.txt row i=53004 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_4_etetO_4"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.4", state, "5.3.2"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.4"
    return state


from engine.vikalpa import policy_pick
from phonology import mk
from sutras.adhyaya_1.pada_1.sutra_1_1_38 import META_ASARVA_VIBHAKTI_TADDHITA

_RULES = {'idam': [('r', ('e', 't', 'a')), ('T', ('i', 't'))]}      # {the sthānin: ((the first letter of the pratyaya or None, the ādeśa), ...)}
_PRATYAYAS = ()      # the pratyayas the ādeśa is taught before (empty: any vibhakti pratyaya of 5.3.2 ff.)


def _site(state: State):
    for i in range(len(state.terms) - 1):
        t, pr = state.terms[i], state.terms[i + 1]
        if t.meta.get("upadesha_slp1") not in _RULES or t.meta.get("adesha_done:5.3.4") or t.meta.get("adesha_of_stem"):
            continue
        if _PRATYAYAS and pr.meta.get("upadesha_slp1") not in _PRATYAYAS:
            continue
        if "taddhita" not in pr.tags or not pr.meta.get(META_ASARVA_VIBHAKTI_TADDHITA) or not pr.varnas:
            continue
        for first, new in _RULES[t.meta["upadesha_slp1"]]:
            if first is None or pr.varnas[0].slp1 == first:
                return t, new
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None and not state.meta.get("declined:5.3.4")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    site = _site(state) if _new_cond(state) else None
    if site is None:
        return _legacy_act(state)
    t, new = site
    t.varnas = [mk(c) for c in new]
    t.meta["adesha_sthani"] = t.meta["upadesha_slp1"]
    t.meta["upadesha_slp1"] = "".join(new)      # the ādeśa is the word now (not a tyadādi member: 1.2.72 / 7.2.102 leave it)
    t.tags.discard("tyadadi")
    t.meta["adesha_of_stem"] = "5.3.4"
    t.meta["adesha_done:5.3.4"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "etetO raToH",
    text_dev              = "एतेतौ रथोः",
    samagra_slp1          = "prAgdiSaH idamaH raTO eta-itO",
    samagra_dev           = "प्राग्दिशः इदमः रथौ एत-इतौ",
    padaccheda_dev        = "एत-इतौ र-थोः",
    why_dev               = "(सूत्रम् 5.3.4) एतेतौ रथोः।",
    anuvritti_from        = ('5.3.2',),
    apavada_of     = ('5.3.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
