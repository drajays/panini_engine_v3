"""
6.4.132  वाह ऊठ्  —  VIDHI

Padaccheda: वाहः ऊठ्

वाह ऊठ् (6.4.132)
Pāṭha: ashtadhyayi.com data.txt row i=64132 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_132_vAha_132"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.132", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.132"
    return state


from engine.state import State
from phonology import mk

def _find(state: State):
    for i, t in enumerate(state.terms[:-1]):
        flat = [v.slp1 for v in t.varnas]
        if {"anga", "bha"} <= t.tags and len(flat) >= 3 and flat[-3:] == ["v", "A", "h"] and not t.meta.get("6_4_132_done"):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    t = state.terms[hit]
    t.varnas[-3] = mk("U")                  # प्रष्ठवाह् → प्रष्ठूह्: ūṭh (its ṭh are it); 6.1.89 then gives प्रष्ठौहः
    del t.varnas[-2]
    t.meta["6_4_132_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.132",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vAha UW",
    text_dev              = "वाह ऊठ्",
    samagra_slp1          = "vAhaH samprasAraRam UW",
    samagra_dev           = "वाहः सम्प्रसारणम् ऊठ्",
    padaccheda_dev        = "वाहः ऊठ्",
    why_dev               = "वाह-अन्तस्य भस्य सम्प्रसारणम् ऊठ् — प्रष्ठौहः, दित्यौहः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
