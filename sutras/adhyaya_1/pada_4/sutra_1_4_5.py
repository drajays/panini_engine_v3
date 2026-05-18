"""
1.4.5  वाऽऽमि  (vā'mi)  —  VIBHASHA

**Pāṭha:** Optionally (*vā*) [the prātipadika is treated as *nadī*] before
the suffix *āmi* (*āmi* — genitive plural marker).

v3: optionally adds the *nadi* tag to eligible prātipadika–stri Terms that
appear in an *āmi* context and have not yet been processed by this sūtra.
The default choice is to apply (``vibhasha_default=True``).
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _eligible(state: State):
    for t in state.terms:
        if "prātipadika" not in t.tags:
            continue
        if "stri" not in t.tags:
            continue
        if "aami_context" not in t.meta:
            continue
        if t.meta.get("1_4_5_done"):
            continue
        yield t


def cond(state: State) -> bool:
    return next(_eligible(state), None) is not None


def act(state: State) -> State:
    state.samjna_registry["nadi_vA_Ami"] = frozenset({"optional_nadi_before_Ami"})
    for t in _eligible(state):
        t.tags.add("nadi")
        t.meta["1_4_5_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id               = "1.4.5",
    sutra_type             = SutraType.VIBHASHA,
    text_slp1              = "vA~Ami",
    text_dev               = "वाऽऽमि",
    padaccheda_dev         = "वा / आमि",
    why_dev                = "आमि परे स्त्री-प्रातिपदिकस्य वा नदीसंज्ञा।",
    anuvritti_from         = ("1.4.1", "1.4.3"),
    r1_form_identity_exempt= True,
    vibhasha_default       = True,
    cond                   = cond,
    act                    = act,
)

register_sutra(SUTRA)
