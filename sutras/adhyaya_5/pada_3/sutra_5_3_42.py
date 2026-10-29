"""
5.3.42  संख्याया विधार्थे धा  —  VIDHI

Padaccheda: संख्यायाः विधा-अर्थे धा

संख्याया विधाऽर्थे धा (5.3.42)
Pāṭha: ashtadhyayi.com data.txt row i=53042 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_42_saMKyAyA_42"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.42", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.42"
    return state


from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
from sutras.adhyaya_1.pada_1.sutra_1_1_38 import META_ASARVA_VIBHAKTI_TADDHITA
from sutras.adhyaya_1.pada_3.sutra_1_3_4 import TAG_5_3_1_VIBHAKTI

_RULES = (
    ({'tag': 'saMKyA'}, 'DA'),
)      # (the stems the sūtra names, the pratyaya or its readings)


def _attach(state: State):
    ok = vivaksita(state, "taddhitArtha", "viDArTa")
    if not ok:
        return None
    for kw, up in _RULES:
        if taddhita_site(state, None, ok=True, **{k: (frozenset(v) if k == "stems" else v) for k, v in kw.items()}) is not None:
            return up
    return None


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.42")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.42", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside and the general pratyaya stays
        state.meta["declined:5.3.42"] = True
        return state
    state = attach_taddhita(state, up)
    state.terms[-1].meta[META_ASARVA_VIBHAKTI_TADDHITA] = True      # a vibhakti pratyaya (5.3.1) does not take every case: 1.1.38 makes the word an avyaya
    state.terms[-1].tags.add(TAG_5_3_1_VIBHAKTI)      # 5.3.1 prāg diśo vibhaktiḥ: its scope's pratyayas are vibhakti (1.3.4 keeps the final m of dānīm)
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'saMKyAyA viDArTe DA',
    text_dev              = 'संख्याया विधार्थे धा',
    samagra_slp1          = "saNKyAyAH viDArTe DA",
    samagra_dev           = "सङ्ख्यायाः विधार्थे धा",
    padaccheda_dev        = "संख्यायाः विधा-अर्थे धा",
    why_dev               = "(सूत्रम् 5.3.42) संख्याया विधाऽर्थे धा।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
