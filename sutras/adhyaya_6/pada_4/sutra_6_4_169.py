"""
6.4.169  आत्माध्वानौ खे  —  VIDHI

Padaccheda: आत्म-अध्वानौ खे

आत्माध्वानौ खे (6.4.169)
Pāṭha: ashtadhyayi.com data.txt row i=64169 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_169_AtmADvAnO_169"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.169", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.169"
    return state


from engine.state import State

def barred(state: State, t, pr) -> bool:
    """आत्मन् / अध्वन् before kha: the an stays (आत्मनीनः, अध्वनीनः). Read by 6.4.144 as well."""
    flat = "".join(v.slp1 for v in t.varnas)
    org = next((x.split(":", 1)[1] for x in pr.tags if x.startswith("origin_pratyaya:")), pr.meta.get("upadesha_slp1") or "")      # kha may already stand as īna (7.1.2)
    return flat in ("Atman", "aDvan") and org == "Ka"


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
    sutra_id              = "6.4.169",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtmADvAnO Ke",
    text_dev              = "आत्माध्वानौ खे",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya AtmA-aDvAnO Ke prakftyA aRi an",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य आत्मा-अध्वानौ खे प्रकृत्या अणि अन्",
    padaccheda_dev        = "आत्म-अध्वानौ खे",
    why_dev               = "आत्मन्-अध्वन्-शब्दौ खे परे प्रकृत्या भवतः — आत्मनीनः, अध्वनीनः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
