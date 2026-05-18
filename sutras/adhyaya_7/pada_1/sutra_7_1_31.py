"""
7.1.31  पञ्चम्या अत्  —  VIDHI

Padaccheda: पञ्चम्याः अत्

For asmad/yuzmad stem in pañcami (ablative) bahuvacana, replace the bhyas
pratyaya with 'at' (SLP1: "at").

पञ्चम्या अत् (7.1.31)

Engine implementation:
  cond:
    • arm flag "7_1_31_arm" set in meta
    • a bhyas pratyaya follows (upadesha "Byas")
    • no "7_1_31_done" tag on pratyaya
  act:
    • replace pratyaya varnas with parse("at")
    • set upadesha_slp1 = "at"
    • mark "7_1_31_done"
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target(state: State):
    if not state.meta.get("7_1_31_arm"):
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
            if "7_1_31_done" in pr.tags:
                continue
            pr_up = (pr.meta.get("upadesha_slp1") or "").strip()
            if pr_up == "Byas":
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
    pr.varnas = parse_slp1_upadesha_sequence("at")
    pr.meta["upadesha_slp1"] = "at"
    pr.tags.add("7_1_31_done")
    pr.tags.add("sup")
    pr.tags.add("upadesha")
    state.samjna_registry["7_1_31_Byas_to_at"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paYcamyA at",
    text_dev              = "पञ्चम्या अत्",
    padaccheda_dev        = "पञ्चम्याः अत्",
    why_dev               = "अस्मद्-शब्दयोः पञ्चमी-बहुवचने भ्यस्-प्रत्ययस्य स्थाने अत् "
                            "(सूत्रम् ७.१.३१ पञ्चम्या अत्)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
