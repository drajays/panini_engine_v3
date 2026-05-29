"""
3.4.103  यासुट् परस्मैपदेषूदात्तो ङिच्च  —  VIDHI

Two operational paths:
  1. Arm ``3_4_103_arm``: legacy gate-setter (krt_kind = 3.4.103).
  2. Arm ``yasut_recipe``: vidhi-liṅ — insert the *yāsuṭ* augment
     Term ``[y, A, s]`` (pre-processed: u~ and T already conceptually removed)
     immediately before the rightmost tiṅ ādeśa Term.

The yāsuṭ Term is tagged ``yasut_agama`` (not ``upadesha``) so that 1.3.3 does
not mis-mark its 's' as halantyam-it before 7.2.79 drops it.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology    import mk

_GATE_KEY: str = "3_4_103_yAsuw_103"


def _find_tin_index(state: State) -> int | None:
    """Return index of the rightmost tiṅ ādeśa pratyaya after dhātu."""
    for i in range(len(state.terms) - 1, -1, -1):
        t = state.terms[i]
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" in t.tags:
            return i
    return None


def cond(state: State) -> bool:
    # Structural path: yāsuṭ insertion in vidhi-liṅ before the tiṅ ādeśa.
    # (The legacy gate-setter arm path is dead — no caller sets ``3_4_103_arm``
    # and the gate it produced is read by no other sūtra.  Art.7: no arm read.)
    if state.meta.get("yasut_recipe"):
        if state.meta.get("3_4_103_yasut_done"):
            return False
        return _find_tin_index(state) is not None
    return False


def act(state: State) -> State:
    if state.meta.get("yasut_recipe") and not state.meta.get("3_4_103_yasut_done"):
        idx = _find_tin_index(state)
        if idx is None:
            return state
        # yāsuṭ upadeśa = y+ā+s+u~+ṭ.  Pre-process: u~ and T are it-markers
        # conceptually removed here; 1.3.2/1.3.3/1.3.9 calls in pipeline are trace-only.
        yasut = Term(
            kind="pratyaya",
            varnas=[mk("y"), mk("A"), mk("s")],
            tags={"pratyaya", "yasut_agama"},
            meta={"upadesha_slp1": "yAsuT", "yasut_agama": True},
        )
        state.terms.insert(idx, yasut)
        state.meta["3_4_103_yasut_done"] = True
        state.meta.pop("yasut_recipe", None)
        state.samjna_registry["3.4.103_yasut_inserted"] = True
        return state
    # Legacy gate path
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yAsuw parasmEpadezUdAtto Nicca",
    text_dev              = "यासुट् परस्मैपदेषूदात्तो ङिच्च",
    padaccheda_dev        = "यासुट् परस्मैपदेषु उदात्तः ङित् च",
    why_dev               = (
        "विधि-लिङि परस्मैपदे धातोः परे यासुट्-आगमः; "
        "उदात्तः ङिच्च — अनुदात्त-ङित्-संज्ञा।"
    ),
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
