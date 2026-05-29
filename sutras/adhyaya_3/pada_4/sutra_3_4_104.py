"""
3.4.104  किदाशिषि  —  VIDHI

Two operational paths:
  1. Arm ``3_4_104_arm``: legacy gate-setter.
  2. Arm ``ashir_yasut_recipe``: āśīr-liṅ — insert the yāsuṭ augment
     [y,A,s] (after u~/T it-lopa) immediately before the tiṅ ādeśa, tagged
     as KIT.  The kit-mark on yāsuṭ causes 1.1.5 (kṅiti ca) to block guṇa
     on the dhātu (hence bhūyāt not bhaveyāt).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk

_GATE_KEY: str = "3_4_104_kidASizi_104"


def _find_tin_index(state: State) -> int | None:
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" in t.tags:
            return i
    return None


def cond(state: State) -> bool:
    # Structural path: kit-yāsuṭ insertion in āśīr-liṅ before the tiṅ ādeśa.
    # (The legacy gate-setter arm path is dead — no caller sets ``3_4_104_arm``
    # and the gate it produced is read by no other sūtra.  Art.7: no arm read.)
    if state.meta.get("ashir_yasut_recipe"):
        if state.meta.get("3_4_104_yasut_done"):
            return False
        return _find_tin_index(state) is not None
    return False


def act(state: State) -> State:
    if state.meta.get("ashir_yasut_recipe") and not state.meta.get("3_4_104_yasut_done"):
        idx = _find_tin_index(state)
        if idx is None:
            return state
        # yāsuṭ upadeśa = y+ā+s+u~+T; after u~/T it-lopa → [y,A,s].
        # Tagged KIT (k-it) so that 1.1.5 kṅiti ca blocks guṇa on dhātu.
        yasut = Term(
            kind="pratyaya",
            varnas=[mk("y"), mk("A"), mk("s")],
            tags={"pratyaya", "yasut_agama", "kit"},
            meta={"upadesha_slp1": "yAsuT", "yasut_agama": True, "kit": True},
        )
        state.terms.insert(idx, yasut)
        state.meta["3_4_104_yasut_done"] = True
        state.meta.pop("ashir_yasut_recipe", None)
        state.samjna_registry["3.4.104_yasut_inserted"] = True
        return state
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kidASizi",
    text_dev              = "किदाशिषि",
    padaccheda_dev        = "कित् आशिषि",
    why_dev               = (
        "आशीर्-लिङि यासुट्-आगमः किद्-भूतः — तेन १.१.५ (क्ङिति च) "
        "द्वारा धातोः गुण-निषेधः।"
    ),
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
