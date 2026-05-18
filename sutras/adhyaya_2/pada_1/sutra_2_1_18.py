"""
2.1.18  पारे मध्ये षष्ठ्या वा  (pāre madhye ṣaṣṭhyā vā)  —  VIDHI

**Pāṭha:** The words *pāra* ("the other side") and *madhya* ("middle")
combine with a ṣaṣṭhī-ending subanta (optionally, *vā*) to form an
avyayībhāva samāsa.

Example: *gaṅgāyāḥ pāre* → *pāragaṅgam* ("on the far side of the Gaṅgā").

v3 narrow slice: gate-marks the compound with key
``2_1_18_pare_madhye_shashti``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_18_pare_madhye_shashti"

_PARE_SET: frozenset[str] = frozenset({"pAra", "maDya", "pAre", "maDye"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    for t in state.terms:
        if t.meta.get("upadesha_slp1") in _PARE_SET:
            return True
    return False


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pAre maDye zazWyA vA",
    text_dev              = "पारे मध्ये षष्ठ्या वा",
    padaccheda_dev        = "पारे / मध्ये / षष्ठ्या / वा",
    why_dev               = "पार-मध्य-शब्दयोः षष्ठ्यन्तेन सह विकल्पेन अव्ययीभावः (२.१.१८)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
