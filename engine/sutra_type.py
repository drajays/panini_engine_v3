"""
engine/sutra_type.py — The 10-fold sūtra-lakṣaṇa type system.
────────────────────────────────────────────────────────────────

Constitution Article 1.  Every sūtra in the engine carries exactly ONE
SutraType.  The dispatcher (engine/dispatcher.py) routes on SutraType —
not on sūtra content.  This is how we keep the engine mechanically
blind.

This file is the SINGLE source of truth for:
  • the SutraType enum
  • the per-type execution CONTRACTS
  • the canonical SutraRecord dataclass

Editing this file requires a formal amendment (CONSTITUTION.md Art. 10).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum        import Enum, auto
from typing      import Any, Callable, Dict, FrozenSet, Optional, Tuple


# ═════════════════════════════════════════════════════════════════════════
# ARTICLE 1 — THE TEN SŪTRA TYPES
# ═════════════════════════════════════════════════════════════════════════

class SutraType(Enum):
    """
    दशविध सूत्रलक्षण.

        संज्ञा च परिभाषा च विधिर्नियम एव च ।
        अतिदेशोऽधिकारश्च षड्विधं सूत्रलक्षणम् ॥
        प्रतिषेधोऽनुवादश्च विभाषा च निपातनम् ।

    Engine routing contract:
        SAMJNA      → exec_samjna      — register a technical term
        PARIBHASHA  → exec_paribhasha  — set an interpretive gate
        VIDHI       → exec_vidhi       — apply a phonemic operation
        NIYAMA      → exec_niyama      — restrict a prior vidhi
        ATIDESHA    → exec_atidesha    — extend a property by analogy
        ADHIKARA    → exec_adhikara    — open/close a scope gate
        PRATISHEDHA → exec_pratishedha — block a named rule
        ANUVADA     → exec_anuvada     — restatement (trace only)
        VIBHASHA    → exec_vibhasha    — optional alternative (forks)
        NIPATANA    → exec_nipatana    — stamp an exceptional form
    """
    SAMJNA      = auto()
    PARIBHASHA  = auto()
    VIDHI       = auto()
    NIYAMA      = auto()
    ATIDESHA    = auto()
    ADHIKARA    = auto()
    PRATISHEDHA = auto()
    ANUVADA     = auto()
    VIBHASHA    = auto()
    NIPATANA    = auto()


# ═════════════════════════════════════════════════════════════════════════
# ARTICLE 2 — EXECUTION CONTRACTS
# Each type declares what its executor MUST / MUST NOT do.
# Dispatcher consults this table to validate post-conditions.
# ═════════════════════════════════════════════════════════════════════════

SUTRA_TYPE_CONTRACTS: Dict[SutraType, Dict[str, Any]] = {

    SutraType.SAMJNA: {
        "mutates_form"    : False,  # never touches state.varnas
        "mutates_registry": True,   # writes to state.samjna_registry
        "is_optional"     : False,
        "blocks_others"   : False,
        "r1_exempt"       : True,   # form_before == form_after is OK
        "dev_label"       : "संज्ञा",
    },

    SutraType.PARIBHASHA: {
        "mutates_form"    : False,
        "mutates_registry": True,   # writes to state.paribhasha_gates
        "is_optional"     : False,
        "blocks_others"   : False,
        "r1_exempt"       : True,
        "dev_label"       : "परिभाषा",
    },

    SutraType.VIDHI: {
        "mutates_form"    : True,   # MUST alter state.varnas
        "mutates_registry": False,
        "is_optional"     : False,
        "blocks_others"   : False,
        "r1_exempt"       : False,  # unchanged form = R1 VIOLATION
        "dev_label"       : "विधि",
    },

    SutraType.NIYAMA: {
        "mutates_form"    : True,   # conditionally — may narrow a vidhi
        "mutates_registry": True,   # writes to state.niyama_gates
        "is_optional"     : False,
        "blocks_others"   : False,
        "r1_exempt"       : False,
        "dev_label"       : "नियम",
    },

    SutraType.ATIDESHA: {
        "mutates_form"    : False,  # the *enabled* vidhi mutates, not this
        "mutates_registry": True,   # writes to state.atidesha_map
        "is_optional"     : False,
        "blocks_others"   : False,
        "r1_exempt"       : True,
        "dev_label"       : "अतिदेश",
    },

    SutraType.ADHIKARA: {
        "mutates_form"    : False,
        "mutates_registry": True,   # pushes to state.adhikara_stack
        "is_optional"     : False,
        "blocks_others"   : False,
        "r1_exempt"       : True,
        "dev_label"       : "अधिकार",
    },

    SutraType.PRATISHEDHA: {
        "mutates_form"    : False,
        "mutates_registry": True,   # adds to state.blocked_sutras
        "is_optional"     : False,
        "blocks_others"   : True,   # THE ONLY TYPE WHOSE JOB IS BLOCKING
        "r1_exempt"       : True,
        "dev_label"       : "प्रतिषेध",
    },

    SutraType.ANUVADA: {
        "mutates_form"    : False,
        "mutates_registry": False,
        "is_optional"     : False,
        "blocks_others"   : False,
        "r1_exempt"       : True,
        "dev_label"       : "अनुवाद",
    },

    SutraType.VIBHASHA: {
        "mutates_form"    : True,   # when the optional choice is True
        "mutates_registry": True,   # records the fork
        "is_optional"     : True,   # THE ONLY OPTIONAL TYPE
        "blocks_others"   : False,
        "r1_exempt"       : True,   # non-application is always valid
        "dev_label"       : "विभाषा",
    },

    SutraType.NIPATANA: {
        "mutates_form"    : True,   # replaces state.varnas wholesale
        "mutates_registry": True,   # sets state.nipatana_flag = True
        "is_optional"     : False,
        "blocks_others"   : True,   # freezes subsequent vidhis
        "r1_exempt"       : False,
        "dev_label"       : "निपातन",
    },
}


# ═════════════════════════════════════════════════════════════════════════
# ARTICLE 3 — THE CANONICAL SŪTRA RECORD
# ═════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class SutraRecord:
    """
    Single source of truth for one Pāṇinian sūtra.

    Required for ALL 10 types:
        sutra_id        : str    — "1.1.1", "8.4.2", etc.
        sutra_type      : SutraType
        text_slp1       : str    — FULL sūtra in SLP1 (anuvṛtti baked in)
        text_dev        : str    — FULL sūtra in Devanāgarī (anuvṛtti baked)
        padaccheda_dev  : str    — word-split Devanāgarī
        why_dev         : str    — Devanāgarī justification for the trace

    Metadata (not read by engine; scholars-only):
        anuvritti_from  : tuple  — earlier sūtra IDs contributing terms

    Behavioural fields — populated per type:
        cond            : Callable[[State], bool]        — precondition
        act             : Callable[[State], State]       — action (mutates clone)

        For PRATISHEDHA:
            blocks_sutra_ids : tuple of str

        For ADHIKARA:
            adhikara_scope   : (start_id, end_id) inclusive

        For VIBHASHA:
            vibhasha_default : bool  (apply unless recipe says otherwise)

        For ATIDESHA:
            atidesha_target, atidesha_source, atidesha_dest : str

        For NIPATANA:
            nipatana_form_slp1 : str  — the frozen varṇa sequence
    """
    sutra_id        : str
    sutra_type      : SutraType
    text_slp1       : str
    text_dev        : str
    padaccheda_dev  : str
    why_dev         : str

    # Metadata (never read by the engine, only shown by tools/)
    anuvritti_from  : Tuple[str, ...]                 = field(default_factory=tuple)

    # The two callables — required for VIDHI/NIYAMA/VIBHASHA, and for
    # any type whose executor actually consults the state (SAMJNA, PARIBHASHA,
    # ATIDESHA, ADHIKARA, PRATISHEDHA — they read the state to decide
    # whether their precondition holds). The cond returns True iff the rule
    # should fire; act takes a state clone, mutates it, and returns it.
    cond            : Optional[Callable[[Any], bool]]  = None
    act             : Optional[Callable[[Any], Any]]   = None

    # Type-specific fields.
    blocks_sutra_ids : Tuple[str, ...]                = field(default_factory=tuple)
    adhikara_scope   : Tuple[str, str]                = field(default=("", ""))
    vibhasha_default : bool                           = True
    atidesha_target  : Optional[str]                  = None
    atidesha_source  : Optional[str]                  = None
    atidesha_dest    : Optional[str]                  = None
    nipatana_form_slp1 : Optional[str]                = None

    # ─────────────────────────────────────────────────────────────────
    # Self-validation.  Raises at import time (fail-fast) if a sūtra
    # file violates its type contract.
    # ─────────────────────────────────────────────────────────────────
    def __post_init__(self) -> None:
        self._validate_basics()
        self._validate_type_specific()

    def _validate_basics(self) -> None:
        if not self.sutra_id or self.sutra_id.count(".") != 2:
            raise ValueError(
                f"SutraRecord needs a dotted sutra_id like 'X.Y.Z'; got {self.sutra_id!r}"
            )
        for fld in ("text_slp1", "text_dev", "padaccheda_dev", "why_dev"):
            if not getattr(self, fld):
                raise ValueError(
                    f"[{self.sutra_id}] missing required field {fld!r}"
                )

    def _validate_type_specific(self) -> None:
        st = self.sutra_type
        contract = SUTRA_TYPE_CONTRACTS[st]

        # Every type except ANUVADA and pure PRATISHEDHA with
        # static blocks_sutra_ids needs a cond and an act, because
        # even SAMJNA/PARIBHASHA/ADHIKARA usually have a trigger.
        # We require cond/act on ALL mutating or registry-writing types.
        if contract["mutates_form"] or contract["mutates_registry"]:
            # ANUVADA does nothing, so these are None-able.
            # PRATISHEDHA with static blocks is also exempted only when
            # cond == act == None (in which case adding the block is
            # unconditional for the stage the recipe schedules it in).
            if st is SutraType.ANUVADA:
                return
            if st is SutraType.PRATISHEDHA and not self.blocks_sutra_ids:
                raise ValueError(
                    f"[{self.sutra_id}] PRATISHEDHA must set blocks_sutra_ids"
                )
            if st is SutraType.ADHIKARA:
                if self.adhikara_scope == ("", ""):
                    raise ValueError(
                        f"[{self.sutra_id}] ADHIKARA must set adhikara_scope=(start,end)"
                    )
            if st is SutraType.ATIDESHA:
                if not all([self.atidesha_target,
                            self.atidesha_source,
                            self.atidesha_dest]):
                    raise ValueError(
                        f"[{self.sutra_id}] ATIDESHA must set "
                        "atidesha_target / atidesha_source / atidesha_dest"
                    )
            if st is SutraType.NIPATANA:
                if not self.nipatana_form_slp1:
                    raise ValueError(
                        f"[{self.sutra_id}] NIPATANA must set nipatana_form_slp1"
                    )
            # VIDHI / NIYAMA / VIBHASHA / SAMJNA / PARIBHASHA all need
            # a cond+act pair; the exec_* functions will invoke them.
            if st in (SutraType.VIDHI, SutraType.NIYAMA, SutraType.VIBHASHA,
                      SutraType.SAMJNA, SutraType.PARIBHASHA):
                if self.cond is None or self.act is None:
                    raise ValueError(
                        f"[{self.sutra_id}] {st.name} requires both cond and act"
                    )


# ═════════════════════════════════════════════════════════════════════════
# CENTRALIZED TYPE PREDICATES — CONSTITUTION v3.1 (merged amendments)
# ═════════════════════════════════════════════════════════════════════════
#
# These frozensets are the SINGLE source of truth for which SutraTypes
# are exempt from R1 and which are frozen by NIPATANA.  Previously this
# logic was scattered per-executor (r1_exempt flag in each contract
# entry) and implicit in engine/gates.py's is_frozen_by_nipatana().
# Centralizing makes the policy auditable in one place.
#
# Amendment procedure: to change membership, add a new frozenset
# (e.g. R1_EXEMPT_v3_2) and keep the old one available for regression.
# Do NOT mutate these in place.

R1_EXEMPT: "frozenset[SutraType]" = frozenset({
    SutraType.SAMJNA,       # form-preserving by contract
    SutraType.PARIBHASHA,   # gate-only
    SutraType.ATIDESHA,     # writes atidesha_map, no varṇa change
    SutraType.ADHIKARA,     # scope-only
    SutraType.PRATISHEDHA,  # writes blocked_sutras, no varṇa change
    SutraType.ANUVADA,      # explicit no-op
    SutraType.VIBHASHA,     # declining is a valid outcome
})

NIPATANA_FROZEN: "frozenset[SutraType]" = frozenset({
    SutraType.VIDHI,
    SutraType.NIYAMA,
    SutraType.VIBHASHA,
})
