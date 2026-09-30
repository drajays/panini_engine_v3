"""
3.1.135  इगुपधज्ञाप्रीकिरः कः  —  VIDHI

Sources consulted:
- ashtadhyayi.com data.txt row i=31135
- Kāśikā: "बुधः, कृशः, ज्ञः, प्रियः, किरः।"
- Cross-validation: tests/unit/test_bhattikavya_1_1.py (विबुध)

इक्-उपध (and ज्ञा/प्री/कृ) take **क**. बुध् → बुध.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from engine.krt_eligibility import krt_insertion_eligible, requested_krt_upadesha
from phonology.pratyahara import IK
from phonology.varna import parse_slp1_upadesha_sequence

_GATE_KEY: str = "3_1_135_igupaDajYApr_135"
_NAMED = frozenset({"jYA", "prI", "kF"})


def _dhatu(state: State):
    return next((t for t in state.terms if "dhatu" in t.tags), None)


def _ig_upadha(dh) -> bool:
    cons = [v.slp1 for v in dh.varnas if v.slp1 not in "aAiIuUfFxXeEoO"]
    vows = [v.slp1 for v in dh.varnas if v.slp1 in "aAiIuUfFxXeEoO"]
    if len(vows) >= 1 and vows[-1] in IK:
        return True
    # CVC: the vowel before the final consonant is upadha.
    slp = [v.slp1 for v in dh.varnas]
    for i in range(len(slp) - 2, -1, -1):
        if slp[i] in "aAiIuUfFxXeEoO":
            return slp[i] in IK
    return False


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.135", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    if requested_krt_upadesha(state) != "ka":
        return False
    if any("krt" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    dh = _dhatu(state)
    if dh is None:
        return False
    up = (dh.meta.get("upadesha_slp1") or "").strip()
    flat = "".join(v.slp1 for v in dh.varnas)
    return up in _NAMED or flat in _NAMED or _ig_upadha(dh)


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
    state.meta["krt_kind"] = "3.1.135"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.135",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "igupaDajYAprIkiraH kaH",
    text_dev              = "इगुपधज्ञाप्रीकिरः कः",
    padaccheda_dev        = "इक्-उपध-ज्ञा-प्री-किरः कः",
    why_dev               = "इगुपध-ज्ञा-प्री-किरः क-प्रत्ययः (बुध → विबुध)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
