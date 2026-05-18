"""
7.2.80  अतो येयः  —  VIDHI

Two operational paths:
  1. Arm ``7_2_80_arm``: legacy gate-setter.
  2. Arm ``7_2_80_liG_yasut_arm``: vidhi-liṅ — the yāsuṭ remnant [y,A]
     (after 7.2.79 s-lopa) is replaced by [i,y] when the preceding term
     ends in 'a'.  This creates the 'i' that undergoes 6.1.87 ādguṇaḥ
     (a + i → e), producing the characteristic 'e' of vidhi-liṅ forms.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_GATE_KEY: str = "7_2_80_ato_80"


def _find_yasut_ya(state: State) -> int | None:
    """Find the yāsuṭ term [y,A] preceded by a term ending in 'a'."""
    if not state.meta.get("7_2_80_liG_yasut_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "yasut_agama" not in t.tags:
            continue
        if t.meta.get("7_2_80_yasut_iy_done"):
            continue
        vs = t.varnas
        if len(vs) != 2 or vs[0].slp1 != "y" or vs[1].slp1 != "A":
            continue
        if i == 0:
            continue
        prev = state.terms[i - 1]
        if not prev.varnas or prev.varnas[-1].slp1 != "a":
            continue
        return i
    return None


def cond(state: State) -> bool:
    if _find_yasut_ya(state) is not None:
        return True
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_80_arm") is True


def act(state: State) -> State:
    idx = _find_yasut_ya(state)
    if idx is not None:
        t = state.terms[idx]
        # [y, A] → [i, y]
        t.varnas = [mk("i"), mk("y")]
        t.meta["7_2_80_yasut_iy_done"] = True
        state.meta.pop("7_2_80_liG_yasut_arm", None)
        state.samjna_registry["7.2.80_yasut_iya"] = True
        return state

    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ato yeyaH",
    text_dev              = "अतो येयः",
    padaccheda_dev        = "अतः या (लुप्तषष्ठ्यन्तनिर्देशः) इयः",
    why_dev               = (
        "विधि-लिङि अकारान्त-विकरणपरस्य यासुट्-अवशेषस्य [y,A] → [i,y]; "
        "एवं ६.१.८७ द्वारा अ+इ → ए।"
    ),
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
