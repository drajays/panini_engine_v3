"""
7.2.13  कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि  —  VIDHI

Padaccheda: कृ-सृ-भृ-वृ-स्तु-द्रु-स्रु-श्रुवः लिटि

Special iṭ-agama privilege for the kṛsṛ… dhātus in liṭ context.
The "liṭi" context is structurally detected via the "abhyasa" tag: after
6.1.8 dvitva (liṭ-specific), an abhyāsa-tagged Term is on the tape.
The dhātu is checked by its post-lopa upadesha_slp1 root.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_13_kfsfBfvfst_13"

_KRSRBHR_ROOTS = frozenset({
    "kf", "sf", "Bf", "vf", "stu", "dru", "sru", "Sru",
    # normalised forms (after it-lopa):
    "kfN", "sfp", "BfY", "vfṃj",  # fallback raw keys
})


def _dhatu_in_group(state: State) -> bool:
    for t in state.terms:
        if "dhatu" not in t.tags:
            continue
        raw = (t.meta.get("upadesha_slp1") or "").replace("~", "").strip()
        # strip trailing it-markers (N, Y, R, etc.)
        base = raw.rstrip("NYRzZ")
        if base in _KRSRBHR_ROOTS or raw.split("~")[0] in _KRSRBHR_ROOTS:
            return True
        # Also check flat form
        flat = "".join(v.slp1 for v in t.varnas)
        if flat in _KRSRBHR_ROOTS:
            return True
    return False


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: liṭ dvitva context (abhyāsa on tape) + dhātu is in kṛsṛ… group
    if any("abhyasa" in t.tags for t in state.terms) and _dhatu_in_group(state):
        return True
    # Legacy arm path
    return bool(state.meta.get("liT_krsrbhr_recipe"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kfsfBfvfstudrusruSruvo liwi",
    text_dev              = "कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि",
    padaccheda_dev        = "कृ-सृ-भृ-वृ-स्तु-द्रु-स्रु-श्रुवः लिटि",
    why_dev               = "(सूत्रम् 7.2.13) कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
