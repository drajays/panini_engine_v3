"""
5.3.81  जातिनाम्नः कन्  —  VIDHI

Padaccheda: जातिनाम्नः कन्

जातिनाम्नः कन् (5.3.81)
Pāṭha: ashtadhyayi.com data.txt row i=53081 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_81_jAtinAmnaH_81"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.81", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.81"
    return state


from engine.taddhita_attach import sense_in, taddhita_site, attach_taddhita
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita


def _attach(state: State):
    t = taddhita_site(state, None, ok=sense_in(state, "5.3.76", "5.3.77"), tag="jAtinAman")
    return ("kan", "-") if t is not None and "lex:manuzyanAman" in t.tags else None      # vā: ka


def _new_cond(state: State) -> bool:
    return _attach(state) is not None and not state.meta.get("declined:5.3.81")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    up = _attach(state) if _new_cond(state) else None
    if up is None:
        return _legacy_act(state)
    if not isinstance(up, str):
        up = up[policy_pick(state, "5.3.81", len(up))]
    if up == "-":                                  # the vā: this sūtra stands aside
        state.meta["declined:5.3.81"] = True
        return state
    return attach_taddhita(state, up)


SUTRA = SutraRecord(
    sutra_id              = "5.3.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAtinAmnaH kan",
    text_dev              = "जातिनाम्नः कन्",
    samagra_slp1          = "anukampAyAm nItO tadyuktAt manuzyanAmnaH jAtinAmnaH kan vA",
    samagra_dev           = "अनुकम्पायाम् नीतौ तद्युक्तात्  मनुष्यनाम्नः जातिनाम्नः कन् वा",
    padaccheda_dev        = "जातिनाम्नः कन्",
    why_dev               = "(सूत्रम् 5.3.81) जातिनाम्नः कन्।",
    anuvritti_from        = ('5.3.70',),
    apavada_of     = ('5.3.70',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
