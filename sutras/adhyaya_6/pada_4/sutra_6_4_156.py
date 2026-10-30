"""
6.4.156  स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः  —  VIDHI

Padaccheda: स्थूल-दूर-युव-ह्रस्व-क्षिप्र-क्षुद्राणाम् यण्-आदि-परम् पूर्वस्य च गुणः

स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः (6.4.156)
Pāṭha: ashtadhyayi.com data.txt row i=64156 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_156_sTUladUray_156"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.156", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.156"
    return state


from engine.state import State, Term
from phonology import mk

_PR = ("izWan", "imanic", "Iyasu~n")      # iṣṭhan, imanic, īyasun
_FAM = "6_4_155_family_done"                # the ṭi of this aṅga has been dealt with by one of 6.4.154 – 159 / 5.3.61 – 64
_AC = frozenset("aAiIuUfFxXeEoO")
_DONE = {_FAM: True, "6_4_143_dit_done": True, "6_4_148_lopa_done": True}      # the aṅga's ṭi is dealt with: the existing guards of 6.4.148 / 6.4.134 keep them from acting on it again


def _flat(t: Term) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _ti_site(state: State, prs=_PR):
    """The bha aṅga Term standing before iṣṭhan / imanic / īyasun (its pratyaya Term follows it), not yet dealt with by the ṭi-lopa family."""
    for i in range(len(state.terms) - 1):
        t, pr = state.terms[i], state.terms[i + 1]
        if {"anga", "bha"} <= t.tags and not t.meta.get(_FAM) and "taddhita" in pr.tags and any(f"origin_pratyaya:{u}" in pr.tags for u in prs):
            return i
    return None
_STEMS = frozenset({"sTUla", "dUra", "yuvan", "hrasva", "kzipra", "kzudra"})
_GUNA = {"i": "e", "I": "e", "u": "o", "U": "o", "f": "ar", "F": "ar"}


def _new_cond(state: State) -> bool:
    i = _ti_site(state)
    return i is not None and _flat(state.terms[i]) in _STEMS


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    t = state.terms[_ti_site(state)]
    k = max(n for n, v in enumerate(t.varnas) if v.slp1 in "yvrl")      # yaṇādi param: from the last yaṇ letter to the end
    del t.varnas[k:]
    j = max(n for n, v in enumerate(t.varnas) if v.slp1 in _AC)
    g = _GUNA.get(t.varnas[j].slp1)
    if g:
        t.varnas[j:j + 1] = [mk(x) for x in g]      # pūrvasya ca guṇaḥ
    t.meta.update(_DONE)
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.156",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTUladUrayuvahrasvakziprakzudrARAM yaRAdiparaM pUrvasya ca guRaH",
    text_dev              = "स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya sTUla-dUra-yuva-hrasva-kzipra-kzudrARAm yaRAdiparam pUrvasya ca guRaH izWa-iman-Iyassu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य स्थूल-दूर-युव-ह्रस्व-क्षिप्र-क्षुद्राणाम् यणादिपरम् पूर्वस्य च गुणः इष्ठ-इमन्-ईयस्सु",
    padaccheda_dev        = "स्थूल-दूर-युव-ह्रस्व-क्षिप्र-क्षुद्राणाम् यण्-आदि-परम् पूर्वस्य च गुणः",
    why_dev               = "(सूत्रम् 6.4.156) स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.4.155',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
