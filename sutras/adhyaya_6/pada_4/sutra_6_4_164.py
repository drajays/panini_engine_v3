"""
6.4.164  इनण्यनपत्ये  —  VIDHI

Padaccheda: इन् अणि अन्-अपत्ये

इनण्यनपत्ये (6.4.164)
Pāṭha: ashtadhyayi.com data.txt row i=64164 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_164_inaRyanapa_164"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.164", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.164"
    return state


from engine.state import State

def barred(state: State, t, pr) -> bool:
    """इन्नन्त before an aṇ that does not mean the offspring: the in stays (साङ्कूटिनम्). Read by 6.4.144 as well."""
    flat = [v.slp1 for v in t.varnas]
    return (len(flat) >= 3 and flat[-2:] == ["i", "n"] and (pr.meta.get("upadesha_slp1") or "") == "aR"
            and not any(e.get("artha") == "apatya" for e in state.adhikara_stack))


def _find(state: State):
    for i, t in enumerate(state.terms[:-1]):
        n = state.terms[i + 1]
        if ({"bha", "anga"} <= t.tags and "taddhita" in n.tags and "pratyaya" in n.tags and not t.meta.get("6_4_144_ti_done")
                and barred(state, t, n)):
            return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _legacy_cond(state)


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return _legacy_act(state)
    state.terms[hit].meta["6_4_144_ti_done"] = True    # प्रकृत्या: the ṭi stays — the guard 6.4.144 reads
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.164",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "inaRyanapatye",
    text_dev              = "इनण्यनपत्ये",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya in aRi anapatye prakftyA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य इन् अणि अनपत्ये प्रकृत्या",
    padaccheda_dev        = "इन् अणि अन्-अपत्ये",
    why_dev               = "इन्नन्तं भसंज्ञकम् अनपत्ये अणि प्रकृत्या भवति — साङ्कूटिनम्, स्राग्विणम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
