"""
5.3.62  वृद्धस्य च  —  VIDHI

Padaccheda: वृद्धस्य च

वृद्धस्य च (5.3.62)
Pāṭha: ashtadhyayi.com data.txt row i=53062 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_62_vfdDasya_62"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.62", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.62"
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
from engine.vikalpa import policy_pick

_AJADI = ("izWan", "Iyasu~n")      # the ajādi pratyayas of 5.3.58
_ADESA = {'vfdDa': ('jya', '-')}


def _new_cond(state: State) -> bool:
    i = _ti_site(state, _AJADI)
    return i is not None and _flat(state.terms[i]) in _ADESA and not state.meta.get("declined:5.3.62")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if not _new_cond(state):
        return _legacy_act(state)
    i = _ti_site(state, _AJADI)
    t = state.terms[i]
    up = _ADESA[_flat(t)]
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.62", len(up))]
    if up == "-":
        state.meta["declined:5.3.62"] = True
        return state
    t.varnas = [mk(x) for x in up]
    t.meta.update(_DONE)
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vfdDasya ca",
    text_dev              = "वृद्धस्य च",
    samagra_slp1          = "atiSAyane vfdDasya ajAdyoH jyaH",
    samagra_dev           = "अतिशायने वृद्धस्य अजाद्योः  ज्यः",
    padaccheda_dev        = "वृद्धस्य च",
    why_dev               = "(सूत्रम् 5.3.62) वृद्धस्य च।",
    anuvritti_from        = ('4.1.76',),
    apavada_of            = ('6.4.155',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
