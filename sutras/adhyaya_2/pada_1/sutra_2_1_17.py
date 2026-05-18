"""
2.1.17  तिष्ठद्गुप्रभृतीनि च  (tiṣṭhadgu-prabhṛtīni ca)  —  VIDHI

**Pāṭha:** The *gaṇa* words beginning with *tiṣṭhadgu* are also treated
as avyayībhāva compounds (listed by tradition as a *gaṇapāṭha*).

These are a fixed list of idiomatic compounds whose avyayībhāva status
is established by enumeration (nipatana-like listing) rather than
derivational rule.

v3 narrow slice: gate-marks the compound with key
``2_1_17_tisthadgu_gana``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_17_tisthadgu_gana"

# Canonical gaṇa (representative members; not exhaustive in narrow slice)
_TISTHADGU_GANA: frozenset[str] = frozenset({
    "tizWadgu", "tizWanmaDye", "BavadDana",
})


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    for t in state.terms:
        if t.meta.get("upadesha_slp1") in _TISTHADGU_GANA:
            return True
    # Also fire when explicitly armed by pipeline
    return bool(state.meta.get("2_1_17_tisthadgu_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["avyayibhava_kind"]    = "2.1.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tizWadgu praBftIni ca",
    text_dev              = "तिष्ठद्गुप्रभृतीनि च",
    padaccheda_dev        = "तिष्ठद्गु-प्रभृतीनि / च",
    why_dev               = "तिष्ठद्गु-गणपाठस्थानां च अव्ययीभावसंज्ञा (२.१.१७)।",
    anuvritti_from        = ("2.1.5",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
