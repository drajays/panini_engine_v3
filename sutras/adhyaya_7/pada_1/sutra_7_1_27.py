"""
7.1.27  युष्मदस्मद्भ्यां ङसोऽश्  —  VIDHI

Padaccheda: युष्मद्-अस्मद्भ्याम् ङसः अश्

After asmad/yuzmad stem, replace the ṅas (genitive singular) pratyaya
with 'aś' (SLP1: "aS"). The ś is marked as it by 1.3.3 and deleted by 1.3.9,
leaving 'a'.

युष्मदस्मद्भ्यां ङसोऽश् (7.1.27)

Engine implementation:
  cond:
    • arm flag "7_1_27_arm" set in meta
    • stem upadesha_slp1 == "asmad"
    • a ṅas pratyaya follows (upadesha "Nas", varnas start with N or reduced to [a,s])
    • no "7_1_27_done" tag on pratyaya
  act:
    • replace pratyaya varnas with parse("aS") = [a, ś]
    • set upadesha_slp1 = "aS"
    • mark "7_1_27_done" on pratyaya
    Then 1.3.3 marks ś as halantyam-it, 1.3.9 deletes it, leaving [a].
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target(state: State):
    if not state.meta.get("7_1_27_arm"):
        return None
    for i, t in enumerate(state.terms):
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in {"asmad", "yuzmad"}:
            continue
        if "anga" not in t.tags:
            continue
        # Find ṅas pratyaya following
        for j in range(i + 1, len(state.terms)):
            pr = state.terms[j]
            if "sup" not in pr.tags:
                continue
            if "7_1_27_done" in pr.tags:
                continue
            pr_up = (pr.meta.get("upadesha_slp1") or "").strip()
            if pr_up == "Nas":
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
    # Replace pratyaya varnas with [a, ś]
    pr.varnas = parse_slp1_upadesha_sequence("aS")
    pr.meta["upadesha_slp1"] = "aS"
    pr.tags.add("7_1_27_done")
    pr.tags.add("sup")
    pr.tags.add("upadesha")
    pr.tags.add("has_halant_it")  # 'S' at end needs halantyam-it marking by 1.3.3
    state.samjna_registry["7_1_27_Nas_to_aS"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yuzmadasmadByAM Naso'S",
    text_dev              = "युष्मदस्मद्भ्यां ङसोऽश्",
    padaccheda_dev        = "युष्मद्-अस्मद्भ्याम् ङसः अश्",
    why_dev               = "अस्मद्-शब्दयोः ङस्-प्रत्ययस्य स्थाने अश् आदेशः "
                            "(सूत्रम् ७.१.२७ युष्मदस्मद्भ्यां ङसोऽश्)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
