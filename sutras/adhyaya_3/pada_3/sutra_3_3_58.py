"""
3.3.58  ग्रहवृदृनिश्चिगमश्च  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=33058
- Kāśikā: "ग्रहः, वरः, दरः, निश्चयः, गमः।"
- Cross-validation: tests/unit/test_bhattikavya_1_1.py (वरः)

ग्रह/वृ/दृ/निश्चि/गम् take **अप्** in karma/bhāva. Remainder अ; **7.3.84** गुण of ऋ.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from engine.krt_eligibility import krt_insertion_eligible, requested_krt_upadesha
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "3_3_58_grahavfdfn_58"
_DHATUS = frozenset({"grah", "graha", "vf", "vfY", "vfN", "df", "dfY", "gam", "gamx~"})


def _dhatu(state: State):
    return next((t for t in state.terms if "dhatu" in t.tags), None)


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.3.58", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    if requested_krt_upadesha(state) != "ap":
        return False
    if any("krt" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    dh = _dhatu(state)
    if dh is None:
        return False
    up = (dh.meta.get("upadesha_slp1") or "").strip().rstrip("~")
    flat = "".join(v.slp1 for v in dh.varnas)
    return up in _DHATUS or flat in {"vf", "grah", "df", "gam"} or flat.startswith("vf")


def act(state: State) -> State:
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("ap")),
        tags={"pratyaya", "krt", "upadesha", "ardhadhatuka"},
        meta={"upadesha_slp1": "ap", "it_markers": {"p"}},
    )
    state.terms.append(pr)
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    state.meta["krt_kind"] = "3.3.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.58",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "grahavfdfniScigamaSca",
    text_dev              = "ग्रहवृदृनिश्चिगमश्च",
    padaccheda_dev        = "ग्रह-वृ-दृ-निश्चि-गमः च",
    why_dev               = "ग्रह-वृ-दृ-निश्चि-गमेभ्यः अप् (वरः)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
