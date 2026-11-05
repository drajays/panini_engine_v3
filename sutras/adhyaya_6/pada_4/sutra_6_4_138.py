"""
6.4.138  अचः  —  VIDHI

Padaccheda: अचः

अचः (6.4.138)
Pāṭha: ashtadhyayi.com data.txt row i=64138 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_138_acaH_138"


def _legacy_cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.138", gate_key=_GATE_KEY)


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.138"
    return state


def _flat(t) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _live_before(state: State, i: int):
    """The Term with sounds right before ``i``."""
    return next((state.terms[k] for k in range(i - 1, -1, -1) if state.terms[k].varnas), None)


def _anc(t) -> bool:
    return (t.meta.get("upadesha_slp1") or "").startswith("aYc") and "bha" in t.tags and _flat(t) == "ac"      # lupta-nakāra añcu


def _site(state: State):
    """अचः: the a of a bha añcu that has lost its n goes (dadhīcaḥ: dadhi + ac + as → dadhi + c + as, then 6.3.138)."""
    if not (adhikara_in_effect("6.4.138", state, "6.4.1") and adhikara_in_effect("6.4.138", state, "6.4.129")):
        return None
    return next((t for t in state.terms if _anc(t)), None)


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    t = _site(state)
    if t is None:
        return _legacy_act(state)
    del t.varnas[0]
    t.meta["6_4_138_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "acaH",
    text_dev              = "अचः",
    samagra_slp1          = "acaH Basya aNgasya at-lopaH",
    samagra_dev           = "अचः भस्य अङ्गस्य अत्-लोपः",
    padaccheda_dev        = "अचः",
    why_dev               = 'लुप्तनकारस्य अञ्चतेः भस्य अकारस्य लोपः — दधीचः, मधूचः, प्राचः।',
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
