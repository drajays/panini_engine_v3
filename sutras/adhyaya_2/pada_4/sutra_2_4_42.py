"""
2.4.42  हनो वध लिङि  —  VIDHI

Padaccheda: हनः वध (लुप्तप्रथमान्तनिर्देशः) लिङि

han root is replaced by vadha in lin.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.sthanivat import DHATUTVA, adesha_substitute_varnas


def _han_dhatu(state: State):
    """हन् before āśīr-liṅ (the ārdhadhātuka liṅ, 3.4.116): वध्यात् — a vowel-initial affix gives vadh-a → vadh by 6.4.48."""
    if not any("ashir_liG" in t.tags for t in state.terms):
        return None
    for dh in state.terms:
        if "dhatu" not in dh.tags or dh.meta.get("2_4_42_han_vadh_done"):
            continue
        up = (dh.meta.get("upadesha_slp1") or "").strip()
        if up in {"han", "hana~", "han~"} or "".join(v.slp1 for v in dh.varnas) == "han":
            return dh
    return None


def cond(state: State) -> bool:
    return _han_dhatu(state) is not None


def act(state: State) -> State:
    dh = _han_dhatu(state)
    if dh is not None:
        adesha_substitute_varnas(dh, "vaDa", state, sutra_id="2.4.42", gunadharmas=frozenset({DHATUTVA}))
        dh.meta["2_4_42_han_vadh_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "hano vaDa liNi",
    text_dev              = "हनो वध लिङि",
    padaccheda_dev        = "हनः वध (लुप्तप्रथमान्तनिर्देशः) लिङि",
    why_dev               = "हनः वध लिङि (२.४.४२)।",
    anuvritti_from        = ('2.4.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
