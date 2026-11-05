"""
6.3.81  अव्ययीभावे चाकाले  —  VIDHI

Padaccheda: अव्ययीभावे च अकाले

अव्ययीभावे चाकाले (6.3.81)
Pāṭha: ashtadhyayi.com data.txt row i=63081 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from phonology import mk

_GATE_KEY: str = "6_3_81_avyayIBAve_81"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.81", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.81"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _uttara(state: State, i: int):
    """The uttarapada of the pūrvapada at ``i``: the next Term with a sound that is not a sup."""
    return next((u for u in state.terms[i + 1:] if u.varnas and "sup" not in u.tags), None)


def _site(state: State):
    """अव्ययीभावे चाकाले: sahasya saḥ — saha becomes sa in an avyayībhāva whose uttarapada is not a word for a time (sacakram, sadhuram; not sahapūrvāhṇam)."""
    for i, t in enumerate(state.terms[:-1]):
        if "samasa_purvapada" not in t.tags or "avyayibhava" not in t.tags or _flat(t) != "saha":
            continue
        u = _uttara(state, i)
        if u is not None and "lex:kAla" not in u.tags:
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
    t.varnas[:] = [mk("s"), mk("a")]       # saha -> sa, the whole (1.1.55)
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avyayIBAve cAkAle",
    text_dev              = "अव्ययीभावे चाकाले",
    samagra_slp1          = "uttarapade avyayIBAve ca akAle sahasya saH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे अव्ययीभावे च अकाले सहस्य सः",
    padaccheda_dev        = "अव्ययीभावे च अकाले",
    why_dev               = 'अव्ययीभावे समासे अकालवाचिनि उत्तरपदे सहस्य सः — सचक्रम्, सधुरम्।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
