"""
7.1.91  णलुत्तमो वा  —  VIDHI

Padaccheda: णल् उत्तमः वा

ṇal (liṭ perfect 1sg ādeśa "Ral") is optionally used for uttama (1st person)
in liṭ context. Structurally: fires when the tiṅ ādeśa "Ral" is present on
the tape (this is the liṭ parasmaipada 1sg ādeśa, only reachable in
first-person liṭ derivation).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_91_Raluttamo_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: ṇal (Ral) tiṅ ādeśa is on the tape (liṭ 1sg context)
    for t in state.terms:
        if "tin_adesha_3_4_78" in t.tags:
            up = t.meta.get("upadesha_slp1") or ""
            if up in ("Ral", "al"):  # Ral = ṇal; al = reduced form
                return True
        # Also match by current varnas (Ral → R,a,l after partial processing)
        flat = "".join(v.slp1 for v in t.varnas)
        if flat in ("Ral", "al") and "pratyaya" in t.tags:
            return True
    # Legacy arm path
    return bool(state.meta.get("Nal_uttama_recipe"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Raluttamo vA",
    text_dev              = "णलुत्तमो वा",
    padaccheda_dev        = "णल् उत्तमः वा",
    why_dev               = "(सूत्रम् 7.1.91) णलुत्तमो वा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
