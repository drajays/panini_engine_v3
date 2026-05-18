"""
1.4.8  पतिः समास एव  (patiḥ samāsa eva)  —  NIYAMA

**Pāṭha:** *Pati* (the pronominal stem *pati*) receives the *ghi* (or *nadī*)
designation ONLY in a compound (*samāsa*), not elsewhere.

v3: if any Term has upadesha_slp1 == "pati", has the *nadi* tag, but is NOT
tagged *samasa*, the *nadi* tag is removed (the rule negates the application
of 1.4.3/1.4.7 to *pati* outside compounds).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _eligible(state: State):
    for t in state.terms:
        if t.meta.get("upadesha_slp1") != "pati":
            continue
        if "nadi" not in t.tags:
            continue
        if "samasa" in t.tags:
            continue
        if t.meta.get("1_4_8_done"):
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry["pati_nadi_samasa_only"] = frozenset({"pati_exception"})
    for t in _eligible(state):
        t.tags.discard("nadi")
        t.meta["1_4_8_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.8",
    sutra_type             = SutraType.NIYAMA,
    text_slp1              = "patiH samAsa eva",
    text_dev               = "पतिः समास एव",
    padaccheda_dev         = "पतिः / समासे / एव",
    why_dev                = "पतिशब्दस्य नदीसंज्ञा समासे एव; पृथक्-प्रयोगे न।",
    anuvritti_from         = ("1.4.1", "1.4.3"),
    r1_form_identity_exempt= True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
