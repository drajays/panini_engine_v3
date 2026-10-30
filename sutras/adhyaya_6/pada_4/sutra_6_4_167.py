"""
6.4.167  अन्  —  VIDHI

Padaccheda: अन्

अन् (6.4.167)
Pāṭha: ashtadhyayi.com data.txt row i=64167 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_167_an_167"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.167", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.167"
    return state


from engine.state import State

def barred(state: State, t, pr) -> bool:
    """अन्नन्त before an aṇ (the offspring sense or not): the an stays (सामनः). Read by 6.4.144 as well."""
    flat = [v.slp1 for v in t.varnas]
    return len(flat) >= 3 and flat[-2:] == ["a", "n"] and (pr.meta.get("upadesha_slp1") or "") == "aR"


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
    sutra_id              = "6.4.167",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "an",
    text_dev              = "अन्",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya an prakftyA aRi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य अन् प्रकृत्या अणि",
    padaccheda_dev        = "अन्",
    why_dev               = "अन्नन्तं भसंज्ञकम् अणि परे प्रकृत्या भवति (अपत्ये अनपत्ये च) — सामनः, वैमनः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
