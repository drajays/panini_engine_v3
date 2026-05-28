"""
6.1.1  एकाचो द्वे प्रथमस्य  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=61001):** *ekāco dve prathamasya* —
*dvitvādhikāraḥ* (scope through **6.1.12** दाश्वान् साह्वान् मीढ्वांश्च).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term


def _needs_sanadi_dvitva(state: State) -> bool:
    """Structural: dhātu + san (desiderative) suffix on tape, no abhyāsa yet.

    Only fires for the san desiderative pratyaya (upadesha "is"/"san").
    Does NOT fire for yaṅ (yaG) which is also tagged sanadi but needs its own
    dvitva path via P00_yang_dvitva_abhyasa_gate.
    """
    if state.samjna_registry.get("6.1.1_dvitva_done"):
        return False
    _SAN_UPADESHA = frozenset({"san", "is"})
    has_san = any(
        "sanadi" in t.tags
        and (t.meta.get("upadesha_slp1") or "").strip() in _SAN_UPADESHA
        for t in state.terms
    )
    if not has_san:
        return False
    if not any("dhatu" in t.tags for t in state.terms):
        return False
    return not any("abhyasa" in t.tags for t in state.terms)


def cond(state: State) -> bool:
    # Duplicate **``pawat``** *prātipadika* (vārttika *dvitva* before डाच्).
    if not state.samjna_registry.get("6.1.1_p017_dvitva_done"):
        if len(state.terms) == 1 and "prātipadika" in state.terms[0].tags:
            if "".join(v.slp1 for v in state.terms[0].varnas) == "pawat":
                return True
    # Structural sanādi dvitva (no arm needed).
    if _needs_sanadi_dvitva(state):
        return True
    # Allow an explicit dvitva action even if adhikāra is already open.
    if state.meta.get("6_1_1_dvitva_arm") and not state.samjna_registry.get("6.1.1_dvitva_done"):
        return True
    return not any(e.get("id") == "6.1.1" for e in state.adhikara_stack)


def act(state: State) -> State:
    if not any(e.get("id") == "6.1.1" for e in state.adhikara_stack):
        state.adhikara_stack.append({
            "id"        : "6.1.1",
            "scope_end" : "6.1.12",
            "text_dev"  : "एकाचो द्वे प्रथमस्य",
        })
    if not state.samjna_registry.get("6.1.1_p017_dvitva_done"):
        for i, t in enumerate(state.terms):
            if "prātipadika" not in t.tags:
                continue
            if "".join(v.slp1 for v in t.varnas) != "pawat":
                continue
            dup = Term(
                kind=t.kind,
                varnas=list(t.varnas),
                tags=set(t.tags),
                meta=dict(t.meta),
            )
            state.terms.insert(i + 1, dup)
            state.samjna_registry["6.1.1_p017_dvitva_done"] = True
            return state
    # Structural sanādi dvitva OR arm-gated dvitva: duplicate first dhātu as abhyāsa.
    if (_needs_sanadi_dvitva(state) or
            (state.meta.get("6_1_1_dvitva_arm") and not state.samjna_registry.get("6.1.1_dvitva_done"))):
        for i, t in enumerate(state.terms):
            if "dhatu" not in t.tags:
                continue
            abhy = Term(kind=t.kind, varnas=list(t.varnas), tags=set(t.tags) | {"abhyasa"}, meta=dict(t.meta))
            state.terms.insert(i, abhy)
            state.samjna_registry["6.1.1_dvitva_done"] = True
            break
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.1",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "ekAco dve prathamasya",
    text_dev       = "एकाचो द्वे प्रथमस्य",
    padaccheda_dev = "एकाचः / द्वे / प्रथमस्य",
    why_dev        = "द्वित्वाधिकारः — ६.१.१ तः ६.१.१२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.1.1", "6.1.12"),
)

register_sutra(SUTRA)

