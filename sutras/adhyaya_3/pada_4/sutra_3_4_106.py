"""
3.4.106  इटोऽत्  —  VIDHI

Padaccheda: इटः अत्

In the āśīr-liṅ ātmanepada frame: the 1sg tiṅ ādeśa iṭ (= iw after
IT-lopa of w → [i]) is replaced by 'a'. This gives the 1sg ending sīya
(sīyuṭ + a) instead of sīyuṭ + i.

Engine: arm ``iT_a_recipe`` + ``ashir_liG`` + finds term tagged
``tin_adesha_3_4_78`` with single varṇa 'i'.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology     import mk

_GATE_KEY: str = "3_4_106_iwot_106"


def _find_it_i(state: State) -> int | None:
    """Find the 1sg iṭ-derived [i] tiṅ ādeśa term."""
    for i, t in enumerate(state.terms):
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_106_done"):
            continue
        if len(t.varnas) != 1:
            continue
        if t.varnas[0].slp1 != "i":
            continue
        return i
    return None


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not state.meta.get("iT_a_recipe"):
        return False
    if not state.meta.get("ashir_liG"):
        return False
    return _find_it_i(state) is not None


def act(state: State) -> State:
    if not state.meta.get("ashir_liG"):
        state.paribhasha_gates[_GATE_KEY] = True
        state.samjna_registry[_GATE_KEY]  = True
        state.meta["krt_kind"] = "3.4.106"
        return state
    idx = _find_it_i(state)
    if idx is None:
        return state
    state.terms[idx].varnas = [mk("a")]
    state.terms[idx].meta["upadesha_slp1"] = "a"
    state.terms[idx].meta["3_4_106_done"] = True
    state.meta.pop("iT_a_recipe", None)
    state.samjna_registry["3.4.106_it_to_a"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.106",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iwo't",
    text_dev              = "इटोऽत्",
    padaccheda_dev        = "इटः अत्",
    why_dev               = (
        "आशीर्-लिङि आत्मनेपदे १-एक-वचने इट्-जन्य-इकारस्य अकारादेशः — "
        "सीय् + इ → सीय् + अ = सीया ।"
    ),
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
