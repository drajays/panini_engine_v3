"""
6.1.133  स्यश्छन्दसि बहुलम्  —  VIDHI

Padaccheda: स्यः (षष्ठ्यर्थे प्रथमा) छन्दसि बहुलम्

स्यश्छन्दसि बहुलम् (6.1.133)
Pāṭha: ashtadhyayi.com data.txt row i=61133 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_133_syaSCandas_133"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.133", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.133"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


_HAL = frozenset("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")


def _site(state: State):
    """स्यः छन्दसि हलि बहुलं सोर्लोपः: the su of the stem sya (tyad) goes before a consonant-initial word, in the Veda (utá syá vājí)."""
    if not state.meta.get("chandas"):
        return None
    for i in range(len(state.terms) - 1):
        t, su = state.terms[i], state.terms[i + 1]
        if _flat(t) != "sya" or "sup" not in su.tags or not su.varnas or su.meta.get("6_1_133_done"):
            continue
        nxt = next((u for u in state.terms[i + 2:] if u.varnas), None)
        if nxt is not None and nxt.varnas[0].slp1 in _HAL:
            return su
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    su = _site(state)
    if su is None:
        return _legacy_act(state)
    su.varnas.clear()                       # lopa (1.1.60): the su is gone, the Term is kept for what reads the pratyaya
    su.meta["6_1_133_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.133",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "syaSCandasi bahulam",
    text_dev              = "स्यश्छन्दसि बहुलम्",
    samagra_slp1          = "syaH Candasi hali bahulaM sulopaH",
    samagra_dev           = "स्यः छन्दसि हलि बहुलं सुलोपः",
    padaccheda_dev        = "स्यः (षष्ठ्यर्थे प्रथमा) छन्दसि बहुलम्",
    why_dev               = 'छन्दसि स्य-शब्दात् परस्य सोः हलादौ परे बहुलं लोपः — उत स्य वाजी।',
    anuvritti_from        = ('6.1.1',),
    vibhasha_default      = False,
    vibhasha_scope        = _new_cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
