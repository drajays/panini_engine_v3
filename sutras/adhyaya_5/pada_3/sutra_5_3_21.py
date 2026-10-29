"""
5.3.21  अनद्यतने र्हिलन्यतरस्याम्  —  VIDHI

Padaccheda: अन्-अद्यतने र्हिल् अन्यतरस्याम्

अनद्यतने र्हिलन्यतरस्याम् (5.3.21)
Pāṭha: ashtadhyayi.com data.txt row i=53021 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_21_anadyatane_21"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.21", state, "5.3.2"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.21"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
from sutras.adhyaya_1.pada_1.sutra_1_1_38 import META_ASARVA_VIBHAKTI_TADDHITA
from sutras.adhyaya_1.pada_3.sutra_1_3_4 import TAG_5_3_1_VIBHAKTI

_RULES = (
    ({'stems': ['aDara', 'adas', 'antara', 'anya', 'anyatara', 'apara', 'avara', 'bahu', 'dakziRa', 'eka', 'etad', 'itara', 'kim', 'nema', 'pUrva', 'para', 'qatama', 'qatara', 'sama', 'sarva', 'sima', 'sva', 'tad', 'tva', 'tvat', 'tyad', 'uBa', 'uBaya', 'uttara', 'viSva', 'yad']}, ('rhil', '-')),
)      # (the stems the sūtra names, the pratyaya or its readings)


def _attach(state: State):
    ok = vivaksita(state, "taddhitArtha", "kAle") and vivaksita(state, "arthaViSeSa", "anadyatana")
    if not ok:
        return None
    for kw, up in _RULES:
        if taddhita_site(state, None, ok=True, **{k: (frozenset(v) if k == "stems" else v) for k, v in kw.items()}) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.21")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.21", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.3.21"] = True
        return state
    state = attach_taddhita(state, up)
    state.terms[-1].meta[META_ASARVA_VIBHAKTI_TADDHITA] = True      # a vibhakti pratyaya (5.3.1) does not take every case: 1.1.38 makes the word an avyaya
    state.terms[-1].tags.add(TAG_5_3_1_VIBHAKTI)      # 5.3.1 prāg diśo vibhaktiḥ: its scope's pratyayas are vibhakti (1.3.4 keeps the final m of dānīm)
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anadyatane rhilanyatarasyAm",
    text_dev              = "अनद्यतने र्हिलन्यतरस्याम्",
    samagra_slp1          = "kim-sarvanAma-bahuByaH advyAdiByaH anadyatane kAle anyatarasyAm rhil",
    samagra_dev           = "किम्-सर्वनाम-बहुभ्यः अद्व्यादिभ्यः अनद्यतने काले अन्यतरस्याम् र्हिल्",
    padaccheda_dev        = "अन्-अद्यतने र्हिल् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 5.3.21) अनद्यतने र्हिलन्यतरस्याम्।",
    anuvritti_from        = ('5.3.2',),
    apavada_of     = ('5.3.15',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
