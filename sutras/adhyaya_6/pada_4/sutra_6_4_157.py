"""
6.4.157  प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः  —  VIDHI

Padaccheda: प्रिय-स्थिर-स्फिर-उरु-बहुल-गुरु-वृद्ध-तृप्र-दीर्घ-वृन्दारकाणाम् प्र-स्थ-वर्-बंहि-गर्-वर्षि-त्रप्-द्राघि-वृन्दाः

प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः (6.4.157)
Pāṭha: ashtadhyayi.com data.txt row i=64157 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_157_priyasTira_157"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.157", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.157"
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
# SHORTCUT S71: the ādeśas are given as they stand before the pratyaya: baṃhi, varṣi, drāghi without the i that 6.4.155 takes again, and the a-final pra, stha, spha, vṛnda as they meet iṣṭha (preṣṭha …)
_ADESA = {"priya": "pra", "sTira": "sTa", "sPira": "sPa", "uru": "var", "bahula": "baMh", "guru": "gar", "vfdDa": "varz", "tfpra": "trap", "dIrGa": "drAG", "vfndAraka": "vfnd"}


def _new_cond(state: State) -> bool:
    i = _ti_site(state)
    return i is not None and _flat(state.terms[i]) in _ADESA


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    t = state.terms[_ti_site(state)]
    t.varnas = [mk(x) for x in _ADESA[_flat(t)]]
    t.meta.update(_DONE)
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.157",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "priyasTirasPirorubahulaguruvfdDatfpradIrGavfndArakARAM prasTasPavarbaMhigarvarzitrabdrAGivfndAH",
    text_dev              = "प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya priya-sTira-sPira-uru-bahula-guru-vfdDa-tfpra-dIrGa-vfndArakARAm pra-sTa-sPa-var-baMhi-gar-varzi-trap-drAGi-vfndAH izWa-iman-Iyassu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य प्रिय-स्थिर-स्फिर-उरु-बहुल-गुरु-वृद्ध-तृप्र-दीर्घ-वृन्दारकाणाम् प्र-स्थ-स्फ-वर्-बंहि-गर्-वर्षि-त्रप्-द्राघि-वृन्दाः इष्ठ-इमन्-ईयस्सु",
    padaccheda_dev        = "प्रिय-स्थिर-स्फिर-उरु-बहुल-गुरु-वृद्ध-तृप्र-दीर्घ-वृन्दारकाणाम् प्र-स्थ-वर्-बंहि-गर्-वर्षि-त्रप्-द्राघि-वृन्दाः",
    why_dev               = "(सूत्रम् 6.4.157) प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.4.155', '6.4.156'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
