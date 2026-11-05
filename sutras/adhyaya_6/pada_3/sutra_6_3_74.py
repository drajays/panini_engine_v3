"""
6.3.74  तस्मान्नुडचि  —  VIDHI

Padaccheda: तस्मात् नुट् अचि

तस्मान्नुडचि (6.3.74)
Pāṭha: ashtadhyayi.com data.txt row i=63074 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible
from phonology import mk

_GATE_KEY: str = "6_3_74_tasmAnnuqa_74"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.74", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.74"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _uttara(state: State, i: int):
    """The uttarapada of the pūrvapada at ``i``: the next Term with a sound that is not a sup."""
    return next((u for u in state.terms[i + 1:] if u.varnas and "sup" not in u.tags), None)

def _nan(t) -> bool:
    return (t.meta.get("upadesha_slp1") or "") == "naY" and "samasa_purvapada" in t.tags


_AC = frozenset("aAiIuUfFxXeEoO")


def _site(state: State):
    """तस्मान्नुडचि: after the nañ has lost its n (6.3.73), an ajādi uttarapada takes nuṭ (an-aśvaḥ, an-ajaḥ); nuṭ is ṭit: it stands first (1.1.46)."""
    for i, t in enumerate(state.terms[:-1]):
        if not (_nan(t) and t.meta.get("6_3_73_done")):
            continue
        u = _uttara(state, i)
        if u is not None and u.varnas[0].slp1 in _AC and not u.meta.get("6_3_74_done"):
            return u
    return None


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    u = _site(state)
    if u is None:
        return _legacy_act(state)
    u.varnas.insert(0, mk("n", "nuw_agama"))
    u.meta["6_3_74_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasmAnnuqaci",
    text_dev              = "तस्मान्नुडचि",
    samagra_slp1          = "uttarapade tasmAt nuw aci naYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे तस्मात् नुट् अचि नञः",
    padaccheda_dev        = "तस्मात् नुट् अचि",
    why_dev               = 'लुप्तनकारात् नञः परस्य अजादेः उत्तरपदस्य नुडागमः — अनश्वः, अनजः।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
