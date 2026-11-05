"""
6.3.128  विश्वस्य वसुराटोः  —  VIDHI

Padaccheda: विश्वस्य वसु-राटोः

विश्वस्य वसुराटोः (6.3.128)
Pāṭha: ashtadhyayi.com data.txt row i=63128 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from phonology import mk

_GATE_KEY: str = "6_3_128_viSvasya_128"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.128", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.128"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _uttara(state: State, i: int):
    """The uttarapada of the pūrvapada at ``i``: the next Term with a sound that is not a sup."""
    return next((u for u in state.terms[i + 1:] if u.varnas and "sup" not in u.tags), None)


def _site(state: State):
    """विश्वस्य वसुराटोः: viśva lengthens its final before vasu and before the form rāṭ (viśvāvasuḥ, viśvārāṭ); not before rāj- (viśvarājau)."""
    for i, t in enumerate(state.terms[:-1]):
        if "samasa_purvapada" not in t.tags or _flat(t) != "viSva" or t.meta.get("6_3_128_done"):
            continue
        u = _uttara(state, i)
        if u is not None and _flat(u) in ("vasu", "rAw"):
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
    t.varnas[-1] = mk("A")                 # antādeśa: the last a
    t.meta["6_3_128_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.128",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viSvasya vasurAwoH",
    text_dev              = "विश्वस्य वसुराटोः",
    samagra_slp1          = "uttarapade saMhitAyAm viSvasya vasu-rAwoH dIrGaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे संहितायाम् विश्वस्य वसु-राटोः दीर्घः",
    padaccheda_dev        = "विश्वस्य वसु-राटोः",
    why_dev               = 'वसु-शब्दे राट्-शब्दे च उत्तरपदे विश्व-शब्दस्य अन्त्यस्य दीर्घः — विश्वावसुः, विश्वाराट्।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
