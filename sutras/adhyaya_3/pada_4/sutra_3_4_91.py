"""
3.4.91  सवाभ्यां वामौ  —  VIDHI

In loṭ (imperative), this rule operates on two cells:
  1. 2sg (madhyamā ekavacana): se → sva
       (after 3.4.80 thāsasse has given thās→se)
  2. 2pl (madhyamā bahuvacana): Dve → Dvam
       (after 3.4.79 replaces Dvam's ṭi-am with e, giving Dve=dhve)

Arm: state.meta["3_4_91_loT_karmani_arm"] must be True.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence, mk as _mk


def _find_se(state: State):
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_91_done"):
            continue
        vs = t.varnas
        if len(vs) == 2 and vs[0].slp1 == "s" and vs[1].slp1 == "e":
            return (ti, "se")
    return None


def _find_dhve(state: State):
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        if t.meta.get("3_4_91_done"):
            continue
        vs = t.varnas
        # Dve: starts with D (dh), second is v, ends with e
        if len(vs) >= 3 and vs[0].slp1 == "D" and vs[-1].slp1 == "e":
            return (ti, "Dve")
    return None


def cond(state: State) -> bool:
    if not state.meta.get("3_4_91_loT_karmani_arm"):
        return False
    return _find_se(state) is not None or _find_dhve(state) is not None


def act(state: State) -> State:
    if not state.meta.get("3_4_91_loT_karmani_arm"):
        return state

    hit = _find_se(state)
    if hit is not None:
        ti, _ = hit
        t = state.terms[ti]
        # se → sva
        t.varnas = parse_slp1_upadesha_sequence("sva")
        t.meta["upadesha_slp1"] = "sva"
        t.meta["3_4_91_done"] = True
        state.meta.pop("3_4_91_loT_karmani_arm", None)
        state.samjna_registry["3.4.91_se_to_sva"] = True
        return state

    hit = _find_dhve(state)
    if hit is not None:
        ti, _ = hit
        t = state.terms[ti]
        # Dve → Dvam: replace terminal e with [a, m]
        t.varnas = list(t.varnas[:-1]) + [_mk("a"), _mk("m")]
        t.meta["upadesha_slp1"] = "".join(v.slp1 for v in t.varnas)
        t.meta["3_4_91_done"] = True
        state.meta.pop("3_4_91_loT_karmani_arm", None)
        state.samjna_registry["3.4.91_Dve_to_Dvam"] = True
        return state

    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "savAByAM vAmO",
    text_dev              = "सवाभ्यां वामौ",
    padaccheda_dev        = "स-वाभ्याम् वा-मौ",
    why_dev               = (
        "लोट् आत्मनेपदे: मध्यमा-एक. से → स्व (थासस्से-पश्चात्); "
        "मध्यमा-बहु. ध्वे → ध्वम् (टेरे-पश्चात्)।"
    ),
    anuvritti_from        = ('3.4.79',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
