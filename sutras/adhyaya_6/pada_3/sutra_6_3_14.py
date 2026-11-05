"""
6.3.14  तत्पुरुषे कृति बहुलम्  —  VIDHI

Padaccheda: तत्पुरुषे कृति बहुलम्

तत्पुरुषे कृति बहुलम् (6.3.14)
Pāṭha: ashtadhyayi.com data.txt row i=63014 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_14_tatpuruze_14"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.14", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.14"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _alug_sup(state: State, vib: str, ok):
    """A samāsa tape: the pūrvapada stem (``samasa_purvapada``), its sup still on the tape (not yet luk-ed by 2.4.71), then the uttarapada.
    Returns the sup Term when ``ok(stem Term)`` holds and the sup carries the vibhakti saṃjñā ``vib``."""
    for i, t in enumerate(state.terms[:-2]):
        s = state.terms[i + 1]
        if "samasa_purvapada" not in t.tags or "sup" not in s.tags or vib not in s.tags or not s.varnas or s.meta.get("alug"):
            continue
        if any(u.varnas and "sup" not in u.tags for u in state.terms[i + 2:]) and ok(t):
            return s
    return None


def _site(state: State):
    """तत्पुरुषे कृति बहुलम्: in a tatpuruṣa whose uttarapada ends in a kṛt, the saptamī sup of the pūrvapada stays only sometimes (sarasijam; saroja)."""
    def ok(t):
        i = state.terms.index(t)
        return "tatpurusha" in t.tags and any("krt" in u.tags for u in state.terms[i + 2:])
    return _alug_sup(state, "vib_saptami", ok)


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    s = _site(state)
    if s is None:
        return _legacy_act(state)
    s.tags.add("alug")                     # the sup stays (alug): 2.4.71's luk does not take it
    s.meta["alug"] = "6.3.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.14",
    sutra_type            = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1             = "tatpuruze kfti bahulam",
    text_dev              = "तत्पुरुषे कृति बहुलम्",
    samagra_slp1          = "alug uttarapade tatpuruze kfti bahulam haladantAt saptamyAH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अलुग् उत्तरपदे तत्पुरुषे कृति बहुलम् हलदन्तात् सप्तम्याः",
    padaccheda_dev        = "तत्पुरुषे कृति बहुलम्",
    why_dev               = 'तत्पुरुषे कृदन्ते उत्तरपदे सप्तम्याः बहुलम् अलुक् — सरसिजम्, न च कुरुचरः।',
    anuvritti_from        = ('6.1.1',),
    vibhasha_default      = False,
    vibhasha_scope        = _new_cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
