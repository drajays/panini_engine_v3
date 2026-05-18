"""
2.1.24  द्वितीया श्रितातीतपतितगतात्यस्तप्राप्तापन्नैः
        (dvitīyā śritātīta-patita-gatā-tyasta-prāptāpannaiḥ)  —  VIDHI

**Pāṭha:** A dvitīyā-ending subanta combines with one of the kṛt-derived
adjectives *śrita*, *atīta*, *patita*, *gata*, *atyasta*, *prāpta*, or
*āpanna* to form a tatpuruṣa samāsa.

Example: *kṛṣṇam śritaḥ* → *kṛṣṇaśritaḥ* ("devoted to Kṛṣṇa").

v3 narrow slice: gate-marks the tatpuruṣa compound with key
``2_1_24_dvitiya_shrita``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_24_dvitiya_shrita"

_SHRITA_SET: frozenset[str] = frozenset({
    "Srita", "atIta", "patita", "gata", "atyasta", "prApta", "Apanna",
})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    for t in state.terms:
        if t.meta.get("upadesha_slp1") in _SHRITA_SET:
            return True
    return False


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]     = "2.1.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvitIyA SritAtItapatitaGatAtyastaprAptApannEH",
    text_dev              = "द्वितीया श्रितातीतपतितगतात्यस्तप्राप्तापन्नैः",
    padaccheda_dev        = "द्वितीया / श्रित-अतीत-पतित-गत-अत्यस्त-प्राप्त-आपन्नैः",
    why_dev               = "द्वितीयान्तस्य श्रित-आदि-कृदन्तैः सह तत्पुरुषः (२.१.२४)।",
    anuvritti_from        = ("2.1.22",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
