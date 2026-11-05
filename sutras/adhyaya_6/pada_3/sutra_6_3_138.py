"""
6.3.138  चौ  —  VIDHI

Padaccheda: चौ

चौ (6.3.138)
Pāṭha: ashtadhyayi.com data.txt row i=63138 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from phonology import mk

_GATE_KEY: str = "6_3_138_cO_138"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.138", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.138"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _uttara(state: State, i: int):
    """The uttarapada of the pūrvapada at ``i``: the next Term with a sound that is not a sup."""
    return next((u for u in state.terms[i + 1:] if u.varnas and "sup" not in u.tags), None)


_DIRGHA = {"a": "A", "i": "I", "u": "U"}


def _site(state: State):
    """चौ: before the añcati that has lost its n and its a (just the c), the aṇ-final pūrvapada is lengthened (prāc, dadhīc, madhūc)."""
    live = [i for i, t in enumerate(state.terms) if t.varnas]
    for i, j in zip(live, live[1:]):
        t, d = state.terms[i], state.terms[j]
        if (d.meta.get("upadesha_slp1") or "").startswith("aYc") and _flat(d) == "c" and t.varnas[-1].slp1 in _DIRGHA and not t.meta.get("6_3_138_done") \
                and "sup" not in t.tags:
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
    t.varnas[-1] = mk(_DIRGHA[t.varnas[-1].slp1])
    t.meta["6_3_138_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cO",
    text_dev              = "चौ",
    samagra_slp1          = "cO parataH pUrvasya aRaH dIrGaH",
    samagra_dev           = "चौ परतः पूर्वस्य अणः दीर्घः",
    padaccheda_dev        = "चौ",
    why_dev               = 'लुप्तनकाराकारे अञ्चतौ परे पूर्वस्य अणः दीर्घः — प्राचः, दधीचः, मधूचः।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
