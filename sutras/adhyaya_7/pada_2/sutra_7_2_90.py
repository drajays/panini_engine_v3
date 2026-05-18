"""
7.2.90  शेषे लोपः  —  VIDHI

Padaccheda: शेषे लोपः

Delete the final consonant ('d') from the asmad stem. Fires in two modes:

Mode A (after stem-replacement + 6.1.97):
  When any of the stem-change done tags is present AND asmad_ato_gune_done.
  E.g. after 7.2.94: [a,h,a,d] → [a,h,a]

Mode B (arm-driven, no stem-replacement):
  When arm flag "7_2_90_direct_arm" is set. Used for cells where the stem
  stays as-is (e.g. 4-3 asmad+bhyam, 5-3 asmad+at, 6-3 asmad+ākam).

शेषे लोपः (7.2.90)
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology     import HAL


def _find_target(state: State):
    """
    Return stem term index. Two modes:

    Mode A: after stem-replacement + 6.1.97 merger.
      - any of the asmad stem-change done tags present
      - "asmad_ato_gune_done" set in meta
      - ends in HAL consonant
      - no "7_2_90_done"

    Mode B: arm-driven (no stem replacement).
      - arm flag "7_2_90_direct_arm" set in state.meta
      - stem upadesha_slp1 == "asmad"
      - ends in 'd'
      - no "7_2_90_done"
    """
    _ASMAD_DONE_TAGS = {
        "7_2_94_done", "7_2_92_done", "7_2_93_done",
        "7_2_95_done", "7_2_96_done",
    }
    for i, t in enumerate(state.terms):
        if "anga" not in t.tags:
            continue
        if "7_2_90_done" in t.tags:
            continue
        if not t.varnas:
            continue

        # Mode A: stem-replacement done + 6.1.97 merger done
        if (t.tags & _ASMAD_DONE_TAGS) and t.meta.get("asmad_ato_gune_done"):
            if t.varnas[-1].slp1 in HAL:
                return i

        # Mode B: arm-driven direct deletion
        if state.meta.get("7_2_90_direct_arm"):
            up = (t.meta.get("upadesha_slp1") or "").strip()
            if up == "asmad" and t.varnas[-1].slp1 == "d":
                return i

    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    i = _find_target(state)
    if i is None:
        return state
    stem = state.terms[i]
    # Delete the final consonant (the 'd')
    del stem.varnas[-1]
    stem.tags.add("7_2_90_done")
    state.samjna_registry["7_2_90_sheSe_lopa"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Seze lopaH",
    text_dev              = "शेषे लोपः",
    padaccheda_dev        = "शेषे लोपः",
    why_dev               = "अस्मद्-शब्दे शेषे (द्-अन्त-व्यञ्जनस्य) लोपः "
                            "(सूत्रम् ७.२.९०) — 'अह' अवशिष्यते।",
    anuvritti_from        = ("7.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
