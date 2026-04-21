"""
1.1.1  वृद्धिरादैच्  (vfdDiH Adaic)  —  SAMJNA

"आ, ऐ, औ — इति वृद्धि-संज्ञाः।"
→ The phonemes {A, E, O} (SLP1 for ā, ai, au) get the technical name
'vṛddhi' (āt + ऐच् pratyāhāra, तपर-काल on āt per 1.1.70).

Pure SAMJNA: writes state.samjna_registry['vṛddhi'], does not mutate Varṇas.
(See panini_engine_v2/core/sutra_1_1_1.py — axiom-level registration.)
"""
from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    """Fires once until the vṛddhi set matches {A, E, O} (idempotent)."""
    existing = state.samjna_registry.get("vṛddhi")
    target = frozenset({"A", "E", "O"})
    return existing != target


def act(state: State) -> State:
    state.samjna_registry["vṛddhi"] = frozenset({"A", "E", "O"})
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.1",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "vfdDiH Adaic",
    text_dev       = "वृद्धिरादैच्",
    padaccheda_dev = "वृद्धिः आत्-ऐच्",
    why_dev        = "आ, ऐ, औ इति वृद्धि-संज्ञाः भवन्ति।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
