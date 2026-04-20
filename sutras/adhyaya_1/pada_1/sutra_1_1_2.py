"""
1.1.2  अदेङ् गुणः  (at eng guṇaH)  —  SAMJNA

"अ, ए, ओ — इति गुणसंज्ञाः।"
→ The phonemes {a, e, o} get the technical name 'guṇa'.

This is a pure SAMJNA.  It MUST write to state.samjna_registry['guṇa']
and MUST NOT touch any varṇa.
"""
from engine            import SutraType, SutraRecord, register_sutra
from engine.state      import State


# ═══════════════════════════════════════════════════════════════════════
# cond(state) — the precondition.
# ═══════════════════════════════════════════════════════════════════════

def cond(state: State) -> bool:
    """Fires unconditionally ONCE, i.e. only if 'guṇa' is not yet
    registered.  Idempotent: if already registered with the same
    members, this will return False (R2 would otherwise flag it)."""
    existing = state.samjna_registry.get("guṇa")
    target   = frozenset({"a", "e", "o"})
    return existing != target


# ═══════════════════════════════════════════════════════════════════════
# act(state) — the operation.
# ═══════════════════════════════════════════════════════════════════════

def act(state: State) -> State:
    state.samjna_registry["guṇa"] = frozenset({"a", "e", "o"})
    return state


# ═══════════════════════════════════════════════════════════════════════
# The record.
# ═══════════════════════════════════════════════════════════════════════

SUTRA = SutraRecord(
    sutra_id       = "1.1.2",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "adeN guRaH",
    text_dev       = "अदेङ् गुणः",
    padaccheda_dev = "अत्-एङ् गुणः",
    why_dev        = "अ, ए, ओ इति गुण-संज्ञाः भवन्ति।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
