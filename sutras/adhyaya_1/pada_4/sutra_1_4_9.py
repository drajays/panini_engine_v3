"""
1.4.9  षष्ठीयुक्तश्छन्दसि वा  (ṣaṣṭhīyuktaś chandasi vā)  —  VIBHASHA

**Pāṭha:** [*Pati*] associated with a genitive (*ṣaṣṭhī*) compound member
optionally [receives the *ghi*/*nadī* designation] in Vedic (*chandas*).

v3: records the optional-in-chandas gate.  The actual tag mutation is deferred
to context where the chandas flag is active.  ``vibhasha_default=False`` — the
optional path is OFF by default (classical grammar prefers the niyama from 1.4.8).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _eligible(state: State):
    for t in state.terms:
        if t.meta.get("upadesha_slp1") != "pati":
            continue
        if not state.meta.get("chandas"):
            continue
        if "SaSTI_yukta" not in t.tags:
            continue
        if t.meta.get("1_4_9_done"):
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry["pati_SaSTI_chandasi_vA"] = frozenset({"optional_chandas"})
    for t in _eligible(state):
        t.tags.add("nadi")
        t.meta["1_4_9_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.9",
    sutra_type             = SutraType.VIBHASHA,
    text_slp1              = "SaSTIyuktaS chandasi vA",
    text_dev               = "षष्ठीयुक्तश्छन्दसि वा",
    padaccheda_dev         = "षष्ठी-युक्तः / छन्दसि / वा",
    why_dev                = "षष्ठीसमासे पतिशब्दस्य छन्दसि वा नदीसंज्ञा।",
    anuvritti_from         = ("1.4.1", "1.4.3", "1.4.8"),
    r1_form_identity_exempt= True,
    vibhasha_default       = False,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
