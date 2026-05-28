"""
3.4.99  नित्यं ङितः  —  VIDHI

Two operational paths:
  1. Arm ``3_4_99_arm``: legacy gate-setter (krt_kind = 3.4.99).
  2. Lakāra-based ṅit s-lopa: when state.meta["lakara"] is one of the ṅit
     lakāras {laG, liG, AsIrliG, luG, lRG, loT}, drop the final 's' of
     ṅit tiṅ ādeśas 'vas' and 'mas'.

In laṅ, 'vas' and 'mas' are ṅit (mandatorily applied); 3.4.99 deletes their
final 's' so the tiṅ ādeśa ends with the prātipadika consonant alone.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_99_nityaM_99"

# ṅit tiṅ ādeśas whose final 's' is dropped.
_NGIT_S_FINAL: frozenset[str] = frozenset({"vas", "mas"})

# Lakāras in which 3.4.99 ṅit s-lopa applies.
_NGIT_LAKARA_SET: frozenset[str] = frozenset({"laG", "liG", "AsIrliG", "luG", "lRG", "loT"})


def _find_ngit_s_term(state: State):
    """Find a ṅit tiṅ ādeśa (vas/mas) ending in 's' for ṅit-lakāra s-lopa."""
    if state.meta.get("lakara") not in _NGIT_LAKARA_SET:
        return None
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _NGIT_S_FINAL:
            continue
        if t.meta.get("3_4_99_s_lopa_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "s":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_ngit_s_term(state) is not None


def act(state: State) -> State:
    j = _find_ngit_s_term(state)
    if j is not None:
        t = state.terms[j]
        # Drop final 's': vas→v, mas→m
        if t.varnas and t.varnas[-1].slp1 == "s":
            del t.varnas[-1]
        t.meta["3_4_99_s_lopa_done"] = True
        state.samjna_registry["3.4.99_ngit_s_lopa"] = (
            state.samjna_registry.get("3.4.99_ngit_s_lopa", 0) + 1
        )
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityaM NitaH",
    text_dev              = "नित्यं ङितः",
    padaccheda_dev        = "नित्यम् ङितः",
    why_dev               = "धातोः प्रत्ययः (३.4.99)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
