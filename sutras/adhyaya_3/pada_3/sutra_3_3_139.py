"""
3.3.139  लिङ्निमित्ते लृङ् क्रियातिपत्तौ  —  VIDHI (narrow: *lṛṅ* placeholder)

Two operational paths:
  1. ``corrected_v2_P019_3_3_139_lRG_arm``: P019 path for *vṛt* dhātu only.
  2. ``3_3_139_lRG_arm``: general glass-box path — attach *lṛṅ* for any dhātu
     (counterfactual / *kriyātipatti* mood, e.g. bhū → abhavaṣyat).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

AT_AGAMA_CONTEXT_TAG = "aT_agama_context"


def _already_has_lRG(state: State) -> bool:
    return any((t.meta.get("upadesha_slp1") or "").strip() == "lRG" for t in state.terms)


def _site_p019(state: State) -> bool:
    if _already_has_lRG(state):
        return False
    for t in state.terms:
        if "dhatu" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "vft":
            return True
    return False


def _site_general(state: State) -> bool:
    if not state.meta.get("3_3_139_lRG_arm"):
        return False
    if _already_has_lRG(state):
        return False
    return any("dhatu" in t.tags for t in state.terms)


def _attach_lRG(state: State) -> State:
    for term in state.terms:
        if "dhatu" in term.tags:
            term.tags.add(AT_AGAMA_CONTEXT_TAG)
    lit = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("lRG")),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "lRG"},
    )
    if lit.varnas and lit.varnas[-1].slp1 == "G":
        del lit.varnas[-1]
    state.terms.append(lit)
    return state


def cond(state: State) -> bool:
    return _site_p019(state) or _site_general(state)


def act(state: State) -> State:
    if _site_p019(state):
        _attach_lRG(state)
        return state
    if _site_general(state):
        _attach_lRG(state)
        state.meta.pop("3_3_139_lRG_arm", None)
        return state
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.139",
    sutra_type=SutraType.VIDHI,
    text_slp1="liN-nimitte lRG kriyAtipattO",
    text_dev="लिङ्निमित्ते लृङ् क्रियातिपत्तौ",
    padaccheda_dev="लिङ्निमित्ते / लृङ् / क्रियातिपत्तौ",
    why_dev="क्रियातिपत्तौ लृङ्-लकार-स्थापनम् (P019)।",
    anuvritti_from=("3.3.138",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
