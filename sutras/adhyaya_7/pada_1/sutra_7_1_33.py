"""
7.1.33  साम आकम्  —  VIDHI

Padaccheda: सामः आकम्

For asmad/yuzmad stem in ṣaṣṭhī (genitive) bahuvacana, replace the ām
pratyaya entirely with 'ākam' (SLP1: "Akam").

साम आकम् (7.1.33)

Engine implementation:
  cond:
    • arm flag "7_1_33_arm" set in meta
    • an ām pratyaya follows (upadesha "Am")
    • no "7_1_33_done" tag on pratyaya
  act:
    • replace pratyaya varnas with parse("Akam")
    • set upadesha_slp1 = "Akam"
    • mark "7_1_33_done"
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target(state: State):
    if not state.meta.get("7_1_33_arm"):
        return None
    for i, t in enumerate(state.terms):
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in {"asmad", "yuzmad"}:
            continue
        if "anga" not in t.tags:
            continue
        for j in range(i + 1, len(state.terms)):
            pr = state.terms[j]
            if "sup" not in pr.tags:
                continue
            if "7_1_33_done" in pr.tags:
                continue
            pr_up = (pr.meta.get("upadesha_slp1") or "").strip()
            if pr_up == "Am":
                return (i, j)
    return None


def cond(state: State) -> bool:
    return _find_target(state) is not None


def act(state: State) -> State:
    target = _find_target(state)
    if target is None:
        return state
    _si, pj = target
    pr = state.terms[pj]
    pr.varnas = parse_slp1_upadesha_sequence("Akam")
    pr.meta["upadesha_slp1"] = "Akam"
    pr.tags.add("7_1_33_done")
    pr.tags.add("sup")
    pr.tags.add("upadesha")
    state.samjna_registry["7_1_33_Am_to_Akam"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sAma Akam",
    text_dev              = "साम आकम्",
    padaccheda_dev        = "सामः आकम्",
    why_dev               = "अस्मद्-शब्दयोः षष्ठी-बहुवचने आम्-प्रत्ययस्य स्थाने आकम् "
                            "(सूत्रम् ७.१.३३ साम आकम्)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
