"""
6.4.158  बहोर्लोपो भू च बहोः  —  VIDHI

Padaccheda: बहोः लोपः भू (लुप्तप्रथमान्तनिर्देशः) च बहोः

बहोर्लोपो भू च बहोः (6.4.158)
Pāṭha: ashtadhyayi.com data.txt row i=64158 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_158_bahorlopo_158"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.158", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.158"
    return state


from engine.it_samjna import META_LOPA_DONE
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


def _new_cond(state: State) -> bool:
    i = _ti_site(state, ("imanic", "Iyasu~n"))
    return i is not None and _flat(state.terms[i]) == "bahu"


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    i = _ti_site(state, ("imanic", "Iyasu~n"))
    t, pr = state.terms[i], state.terms[i + 1]
    t.varnas = [mk("B"), mk("U")]
    del pr.varnas[0]
    pr.meta[META_LOPA_DONE] = ((pr.meta.get("upadesha_slp1") or "").strip(), "".join(v.slp1 for v in pr.varnas))      # the residue after this lopa / ādeśa is not aupadeśika: 1.3.2 – 1.3.8 do not name its letters it again      # the lopa of the first letter of imanic / īyasun (iṣṭhan is the case of 6.4.159)
    t.meta.update(_DONE)
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.158",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahorlopo BU ca bahoH",
    text_dev              = "बहोर्लोपो भू च बहोः",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya bahoH lopaH BU ca izWa-iman-Iyassu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य बहोः लोपः भू च इष्ठ-इमन्-ईयस्सु",
    padaccheda_dev        = "बहोः लोपः भू (लुप्तप्रथमान्तनिर्देशः) च बहोः",
    why_dev               = "(सूत्रम् 6.4.158) बहोर्लोपो भू च बहोः।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.4.155',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
