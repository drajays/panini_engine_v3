"""
6.4.150  हलस्तद्धितस्य  —  VIDHI

Padaccheda: हलः तद्धितस्य

हलस्तद्धितस्य (6.4.150)
Pāṭha: ashtadhyayi.com data.txt row i=64150 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_150_halastadDi_150"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.150", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.150"
    return state


from engine.state import State

def _find(state: State):
    for i, t in enumerate(state.terms[:-1]):
        n = state.terms[i + 1]
        flat = [v.slp1 for v in t.varnas]
        if (len(flat) >= 3 and flat[-2:] == ["y", "a"] and flat[-3] not in "aAiIuUfFxXeEoO" and not t.meta.get("6_4_150_done")
                and any(x.startswith("origin_pratyaya:y") for x in t.tags) and n.kind == "pratyaya" and n.varnas and n.varnas[0].slp1 == "I"):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    t = state.terms[hit]
    del t.varnas[-2]                        # गार्ग्य + ई → गार्ग + ई (the a goes by 6.4.148): गार्गी, वात्सी
    t.meta["6_4_150_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.150",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "halastadDitasya",
    text_dev              = "हलस्तद्धितस्य",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya halaH tadDitasya lopaH Iti upaDAyAH yaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य हलः तद्धितस्य लोपः ईति उपधायाः यः",
    padaccheda_dev        = "हलः तद्धितस्य",
    why_dev               = "हलः उत्तरस्य तद्धित-यकारस्य ईकारे परे लोपः — गार्गी, वात्सी।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
