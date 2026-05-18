"""
2.1.14  लक्षणेनाभिप्रती आभिमुख्ये  (lakṣaṇenābhipratī ābhimukhye)  —  VIDHI

**Pāṭha:** The avyayas *abhi* and *prati* (when they convey locus/mark
+ direction = ābhimukhya, "facing towards") combine with a subanta to
form an avyayībhāva samāsa.

Example: *agnim abhi* → *abhyagnim* ("facing the fire").

Note: 2.1.13 covers the narrower *prati* + pañcamī = ābhimukhya slice.
This sūtra (2.1.14 per the JSON) handles the broader locus (*lakṣaṇa*)
+ *abhi*/*prati* reading.

v3 narrow slice: gate-marks with key ``2_1_14_lakshana_abhi_prati``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_14_lakshana_abhi_prati"

_ABHI_SET: frozenset[str] = frozenset({"aBi", "prati"})

_ABHI_TAGS: frozenset[str] = frozenset({"avyaya", "nipata"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    for t in state.terms:
        if t.meta.get("upadesha_slp1") in _ABHI_SET and _ABHI_TAGS & t.tags:
            return True
    return False


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lakzaNeBABipratI ABimuKye",
    text_dev              = "लक्षणेनाभिप्रती आभिमुख्ये",
    padaccheda_dev        = "लक्षणेन / अभि-प्रती / आभिमुख्ये",
    why_dev               = "लक्षण-योगे अभि/प्रति-अव्ययानां आभिमुख्ये अव्ययीभावः (२.१.१४)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
