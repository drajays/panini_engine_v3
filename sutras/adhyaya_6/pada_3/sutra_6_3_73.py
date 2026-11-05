"""
6.3.73  नलोपो नञः  —  VIDHI

Padaccheda: न-लोपः नञः

नलोपो नञः (6.3.73)
Pāṭha: ashtadhyayi.com data.txt row i=63073 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_73_nalopo_73"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.73", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.73"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _uttara(state: State, i: int):
    """The uttarapada of the pūrvapada at ``i``: the next Term with a sound that is not a sup."""
    return next((u for u in state.terms[i + 1:] if u.varnas and "sup" not in u.tags), None)

def _nan(t) -> bool:
    return (t.meta.get("upadesha_slp1") or "") == "naY" and "samasa_purvapada" in t.tags


def _site(state: State):
    """नलोपो नञः: the n of the nañ goes before an uttarapada (a-brāhmaṇaḥ, a-vṛṣalaḥ, a-somapaḥ)."""
    for i, t in enumerate(state.terms[:-1]):
        if _nan(t) and t.varnas and t.varnas[0].slp1 == "n" and not t.meta.get("6_3_73_done") and _uttara(state, i) is not None:
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
    del t.varnas[0]
    t.meta["6_3_73_done"] = True           # lupta-nakāra: 6.3.74 reads it
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nalopo naYaH",
    text_dev              = "नलोपो नञः",
    samagra_slp1          = "uttarapade na lopaH naYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे न लोपः नञः",
    padaccheda_dev        = "न-लोपः नञः",
    why_dev               = 'उत्तरपदे परे नञः नकारस्य लोपः — अब्राह्मणः, अवृषलः, असोमपः।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
