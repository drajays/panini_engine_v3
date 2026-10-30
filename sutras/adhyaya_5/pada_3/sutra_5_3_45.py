"""
5.3.45  द्वित्र्योश्च धमुञ्  —  VIDHI

Padaccheda: द्वि-त्र्योः च धमुञ्

द्वित्र्योश्च धमुञ् (5.3.45)
Pāṭha: ashtadhyayi.com data.txt row i=53045 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_45_dvitryoSca_45"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.45", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.45"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
from sutras.adhyaya_1.pada_1.sutra_1_1_38 import META_ASARVA_VIBHAKTI_TADDHITA

_RULES = (
    ({'stems': ['dvi', 'tri']}, ('Damu~Y', '-')),
)      # (the stems the sūtra names, the pratyaya or its readings)


def _attach(state: State):
    ok = vivaksita(state, "taddhitArtha", "viDArTa") or vivaksita(state, "taddhitArtha", "aDikaraRavicAla")
    if not ok:
        return None
    for kw, up in _RULES:
        if taddhita_site(state, None, ok=True, **{k: (frozenset(v) if k == "stems" else v) for k, v in kw.items()}) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.45")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.45", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.3.45"] = True
        return state
    state = attach_taddhita(state, up)
    state.terms[-1].meta[META_ASARVA_VIBHAKTI_TADDHITA] = True      # a vibhakti pratyaya (5.3.1) does not take every case: 1.1.38 makes the word an avyaya
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvitryoSca DamuY",
    text_dev              = "द्वित्र्योश्च धमुञ्",
    samagra_slp1          = "saNKyAyAH viDArTe aDikaraRavicAle dvi-tryoH DaH DamuY anyatarasyAm",
    samagra_dev           = "सङ्ख्यायाः विधार्थे अधिकरणविचाले द्वि-त्र्योः धः धमुञ् अन्यतरस्याम्",
    padaccheda_dev        = "द्वि-त्र्योः च धमुञ्",
    why_dev               = "(सूत्रम् 5.3.45) द्वित्र्योश्च धमुञ्।",
    anuvritti_from        = ('4.1.76',),
    apavada_of     = ('5.3.42', '5.3.43'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
