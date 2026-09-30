"""
3.2.39  द्विषत्परयोस्तापेः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=32039
- Kāśikā: "परंतपः, द्विषत्तपः।"
- Cross-validation: tests/unit/test_bhattikavya_1_1.py (परंतपः)

णिजन्त तप् with उपपद पर/द्विषत् takes **खच्**. Remainder after it-lopa is अ
(*khit* → **6.4.94** hrasva, **6.3.67** mum).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from engine.krt_eligibility import krt_insertion_eligible
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "3_2_39_dvizatpara_39"
_TAP = frozenset({"tap", "tAp", "tapa~"})


def _dhatu(state: State):
    return next((t for t in state.terms if "dhatu" in t.tags), None)


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.39", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    if state.meta.get("krt_upadesha_slp1") != "Kac":
        return False
    if any("krt" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    dh = _dhatu(state)
    if dh is None:
        return False
    up = (dh.meta.get("upadesha_slp1") or "").strip()
    flat = "".join(v.slp1 for v in dh.varnas)
    return up in _TAP or flat in _TAP


def act(state: State) -> State:
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Kac")),
        tags={"pratyaya", "krt", "upadesha", "kngiti", "ardhadhatuka"},
        meta={"upadesha_slp1": "Kac", "it_markers": {"K", "c"}, "khit": True},
    )
    state.terms.append(pr)
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["krt_kind"] = "3.2.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.39",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "dvizatparayostApeH",
    text_dev              = "द्विषत्परयोस्तापेः",
    padaccheda_dev        = "द्विषत्-परयोः तापेः",
    why_dev               = "पर/द्विषत्-उपपदे णिजन्त-तपेः खच् (परंतपः)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
