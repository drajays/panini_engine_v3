"""
6.4.159  इष्ठस्य यिट् च  —  VIDHI

Padaccheda: इष्ठस्य यिट् च

इष्ठस्य यिट् च (6.4.159)
Pāṭha: ashtadhyayi.com data.txt row i=64159 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_159_izWasya_159"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.159", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.159"
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


def _new_cond(state: State) -> bool:
    i = _ti_site(state, ("izWan",))
    return i is not None and _flat(state.terms[i]) == "bahu"


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    i = _ti_site(state, ("izWan",))
    t = state.terms[i]
    t.varnas = [mk("B"), mk("U")]
    t.meta.update(_DONE)
    state.terms.insert(i + 1, Term(kind="agama", varnas=[mk("y")], tags={"agama"}, meta={"upadesha_slp1": "yiw"}))      # SHORTCUT S72: yiṭ is shown as its y (no upadeśa tag, so 1.3.x leave it alone); the uccāraṇārtha i and the ṭ are not modelled
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.159",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "izWasya yiw ca",
    text_dev              = "इष्ठस्य यिट् च",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya izWasya yiw ca izWa-iman-Iyassu bahoH BU",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य इष्ठस्य यिट् च इष्ठ-इमन्-ईयस्सु बहोः भू",
    padaccheda_dev        = "इष्ठस्य यिट् च",
    why_dev               = "(सूत्रम् 6.4.159) इष्ठस्य यिट् च।",
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.4.155',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
