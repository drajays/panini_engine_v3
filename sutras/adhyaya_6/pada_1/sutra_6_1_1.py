"""
6.1.1  एकाचो द्वे प्रथमस्य  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=61001):** *ekāco dve prathamasya* —
*dvitvādhikāraḥ* (scope through **6.1.12** दाश्वान् साह्वान् मीढ्वांश्च).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term


def cond(state: State) -> bool:
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
    # Glass-box: when a recipe explicitly arms dvitya, duplicate the first dhātu
    # as abhyāsa (structural but via apply_rule).
    if state.meta.get("6_1_1_dvitva_arm") and not state.samjna_registry.get("6.1.1_dvitva_done"):
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

