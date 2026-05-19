"""
8.2.25  धि च  —  VIDHI

In luṭ karmani 2pl: the final `s` of tāsi drops before `dh` (D in SLP1) of
the tiṅ ādeśa `dhve`. Extends 8.2.24's scope to include `dh`.

  tās + dhve  →  tā + dhve = tādhve

Arm flag: state.meta["8_2_25_arm"] must be True.
Finds tāsi term with final s, where next term starts with D (dha).
Works before pada-merge (cross-term).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find_s_before_D(state: State):
    if not state.meta.get("8_2_25_arm"):
        return None
    # Cross-term scan: tāsi-s before D-initial tiṅ
    for i in range(len(state.terms) - 1):
        t1, t2 = state.terms[i], state.terms[i + 1]
        if not t1.meta.get("tAsi_vikaraṇa"):
            continue
        if t1.meta.get("8_2_25_done"):
            continue
        if not t1.varnas or t1.varnas[-1].slp1 != "s":
            continue
        if not t2.varnas or t2.varnas[0].slp1 != "D":
            continue
        return i
    # Also check within merged pada: ...s+D pattern
    if state.terms and "pada" in state.terms[0].tags:
        t = state.terms[0]
        for vi in range(len(t.varnas) - 1):
            if t.varnas[vi].slp1 == "s" and t.varnas[vi + 1].slp1 == "D":
                if not t.meta.get("8_2_25_done"):
                    return ("intra", vi)
    return None


def cond(state: State) -> bool:
    return _find_s_before_D(state) is not None


def act(state: State) -> State:
    hit = _find_s_before_D(state)
    if hit is None:
        return state
    if isinstance(hit, tuple):
        # intra-term (merged pada)
        _, vi = hit
        del state.terms[0].varnas[vi]
        state.terms[0].meta["8_2_25_done"] = True
    else:
        # cross-term
        t = state.terms[hit]
        del t.varnas[-1]  # drop final s
        t.meta["8_2_25_done"] = True
    state.meta.pop("8_2_25_arm", None)
    state.samjna_registry["8.2.25_dhi_ca"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Di ca",
    text_dev              = "धि च",
    padaccheda_dev        = "धि च",
    why_dev               = "(सूत्रम् 8.2.25) धि च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
