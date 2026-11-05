"""
6.4.139  उद ईत्  —  VIDHI

Padaccheda: उदः ईत्

उद ईत् (6.4.139)
Pāṭha: ashtadhyayi.com data.txt row i=64139 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from phonology import mk

_GATE_KEY: str = "6_4_139_uda_139"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.139", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.139"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _live_before(state: State, i: int):
    """The Term with sounds right before ``i``."""
    return next((state.terms[k] for k in range(i - 1, -1, -1) if state.terms[k].varnas), None)


def _site(state: State):
    """उद ईत्: the a of the bha ac (añcu, n lost) after ud becomes ī, not lopa (udīcaḥ); apavāda of 6.4.138."""
    if not (adhikara_in_effect("6.4.139", state, "6.4.1") and adhikara_in_effect("6.4.139", state, "6.4.129")):
        return None
    for i, t in enumerate(state.terms):
        if (t.meta.get("upadesha_slp1") or "").startswith("aYc") and "bha" in t.tags and _flat(t) == "ac" and not t.meta.get("6_4_139_done"):
            before = _live_before(state, i)
            if before is not None and _flat(before) == "ud":
                return t
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return _legacy_act(state)
    t.varnas[0] = mk("I")
    t.meta["6_4_139_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.139",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uda It",
    text_dev              = "उद ईत्",
    samagra_slp1          = "udaH acaH Basya It",
    samagra_dev           = "उदः अचः भस्य ईत्",
    padaccheda_dev        = "उदः ईत्",
    why_dev               = 'उत् इत्यस्मात् परस्य भस्य अचः अकारस्य ईकारादेशः — उदीचः, उदीचा।',
    anuvritti_from        = ('6.1.1',),
    apavada_of            = ('6.4.138',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
