"""
2.4.18  (avyayībhāva napuṃsaka)  —  SAMJNA (narrow v3 demo slice)

User requirement for the *adhistri* derivation: avyayībhāva samāsa is
napuṃsaka, which then licenses **1.2.47** hrasva.

Engine:
  - If the current block has ``avyayibhava`` structural tag, tag the head
    prātipadika aṅga as ``napuṃsaka``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_2.pada_1.sutra_2_1_6 import TAG_AVYAYIBHAVA


def cond(state: State) -> bool:
    if not any(TAG_AVYAYIBHAVA in t.tags for t in state.terms):
        return False
    return any("prātipadika" in t.tags and "napuṃsaka" not in t.tags for t in state.terms)


def act(state: State) -> State:
    if not any(TAG_AVYAYIBHAVA in t.tags for t in state.terms):
        return state
    for t in state.terms:
        if "prātipadika" in t.tags:
            t.tags.add("napuṃsaka")
    state.samjna_registry["2_4_18_avyayibhava_napuMsaka"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.18",
    sutra_type     = SutraType.SAMJNA,
    r1_form_identity_exempt=True,
    text_slp1      = "avyayIBAvasya napuMsakam",
    text_dev       = "अव्ययीभावस्य नपुंसकम्",
    padaccheda_dev = "अव्ययीभावस्य / नपुंसकम्",
    why_dev        = "अव्ययीभाव-समासः नपुंसकलिङ्गः (१.२.४७ ह्रस्व-प्रसङ्गः)।",
    anuvritti_from = ("2.1.5",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

