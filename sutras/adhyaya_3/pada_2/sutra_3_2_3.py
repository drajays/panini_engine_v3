"""
3.2.3  आतोऽनुपसर्गे कः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=32003
- Kāśikā: "गोपः, गोपिका। नृपः।"
  pratyudāharaṇa: "प्रपः" (with upasarga, ka does not apply)
- Cross-validation: tests/unit/test_bhattikavya_1_1.py (नृपः)

आकारान्त धातोः कर्म-उपपदे अनुपसर्गे क-प्रत्ययः। Remainder after kit-lopa is अ;
then **6.4.64** drops the dhātu's आ (पा + क → प).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from engine.krt_eligibility import krt_insertion_eligible, requested_krt_upadesha
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "3_2_3_Atonupasa_3"


def _dhatu(state: State):
    return next((t for t in state.terms if "dhatu" in t.tags), None)


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.3", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    if requested_krt_upadesha(state) != "ka":
        return False
    if any("krt" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    if any("upasarga" in t.tags for t in state.terms):
        return False
    dh = _dhatu(state)
    return bool(dh and dh.varnas and dh.varnas[-1].slp1 == "A")


def act(state: State) -> State:
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("ka")),
        tags={"pratyaya", "krt", "upadesha", "kngiti", "ardhadhatuka"},
        meta={"upadesha_slp1": "ka", "it_markers": {"k"}},
    )
    state.terms.append(pr)
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["krt_kind"] = "3.2.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.3",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = 'Atonupasarge kaH',
    text_dev              = 'आतोऽनुपसर्गे कः',
    padaccheda_dev        = "आतः अन्-उपसर्गे कः",
    why_dev               = "आकारान्त-धातोः कर्मोपपदे अनुपसर्गे क-प्रत्ययः (नृपः)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
