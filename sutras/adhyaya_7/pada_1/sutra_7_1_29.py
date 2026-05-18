"""
7.1.29  शसो न  —  VIDHI

Padaccheda: शसः न (लुप्तप्रथमान्तनिर्देशः)

For asmad/yuzmad stem in dvitīyā bahuvacana, replace the ādi (initial) 'a' of
the śas pratyaya (after ś-it lopa → [a,s]) with 'n', giving [n,s] = "ns".

शसो न (7.1.29)

Engine implementation:
  cond:
    • arm flag "7_1_29_arm" set in meta
    • a śas pratyaya follows (upadesha "Sas", now [a,s] after ś-lopa)
    • no "7_1_29_done" tag on pratyaya
  act:
    • replace first varna 'a' with 'n' in the pratyaya (ādiḥ parasya 1.1.54)
    • set upadesha_slp1 = "ns" (or keep "Sas" with updated varnas)
    • mark "7_1_29_done"
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_target(state: State):
    if not state.meta.get("7_1_29_arm"):
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
            if "7_1_29_done" in pr.tags:
                continue
            pr_up = (pr.meta.get("upadesha_slp1") or "").strip()
            if pr_up != "Sas":
                continue
            # Check current varnas: after ś-lopa should be [a, s]
            vs = pr.varnas
            if len(vs) >= 1 and vs[0].slp1 == "a":
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
    # Replace first varna 'a' with 'n' (ādiḥ parasya 1.1.54)
    n_varna = parse_slp1_upadesha_sequence("n")
    pr.varnas[0] = n_varna[0]
    # Result: [n, s]
    pr.tags.add("7_1_29_done")
    pr.tags.add("sup")
    state.samjna_registry["7_1_29_Sas_to_ns"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Saso na",
    text_dev              = "शसो न",
    padaccheda_dev        = "शसः न (लुप्तप्रथमान्तनिर्देशः)",
    why_dev               = "अस्मद्-शब्दयोः शस्-प्रत्ययस्य आदि-'अ' स्थाने नकारः "
                            "(सूत्रम् ७.१.२९ शसो न)।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
