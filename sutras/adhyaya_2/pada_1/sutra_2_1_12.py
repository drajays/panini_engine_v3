"""
2.1.12  अपपरिबहिरञ्चवः पञ्चम्या  (apa-pari-bahis-añcavaḥ pañcamyā)  —  VIDHI

**Pāṭha:** The avyayas *apa*, *pari*, *bahis*, and *añcu* (and related
forms) combine with a pañcamī-ending subanta to form an avyayībhāva samāsa.

Example: *grāmāt bahis* → *bahirgrāmam* ("outside the village").

v3 narrow slice: gate-marks the compound with key
``2_1_12_apa_pari_bahis_pancami``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_12_apa_pari_bahis_pancami"

_APA_SET: frozenset[str] = frozenset({"apa", "pari", "bAhis", "bahis", "aYcu", "aYc"})

_APA_TAGS: frozenset[str] = frozenset({"avyaya", "nipata"})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    for t in state.terms:
        if t.meta.get("upadesha_slp1") in _APA_SET and _APA_TAGS & t.tags:
            return True
    return False


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "apa pari bAhir aYcavaH paYcamyA",
    text_dev              = "अपपरिबहिरञ्चवः पञ्चम्या",
    padaccheda_dev        = "अप-परि-बहिः-अञ्चवः / पञ्चम्या",
    why_dev               = "अप-परि-बहिस्-अञ्च्-शब्दानां पञ्चम्यन्तेन सह अव्ययीभावः (२.१.१२)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
