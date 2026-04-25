"""
engine/state.py — State, Term, Varna.
──────────────────────────────────────

The State is the SINGLE mutable object that flows through the dispatcher.
Every exec_*() takes a state clone, mutates it, and returns it.  Sūtra
files NEVER import anything else from engine except via engine/__init__.

Varna       : one phoneme (slp1) + its Devanāgarī form (dev) + tags.
Term        : a morphemic unit (prātipadika / pratyaya / āgama / ...).
State       : the full derivation state (terms + registries + trace).

See CONSTITUTION.md Article 2 for what cond(state) may and may not read.
"""
from __future__ import annotations

from copy       import deepcopy
from dataclasses import dataclass, field
from typing     import Any, Dict, List, Optional, Set


# ═════════════════════════════════════════════════════════════════════════
# VARNA
# ═════════════════════════════════════════════════════════════════════════

@dataclass
class Varna:
    """
    One phoneme.

    slp1   : SLP1 letter. Vowels: a A i I u U f F x X e E o O.
             Consonants: k K g G N c C j J Y w W q Q R t T d D n p P b B m
                         y v r l S z s h.
    dev    : Devanāgarī form. Consonant uses HALANTA ('क्' not 'क').
             Vowel uses standalone ('इ' not 'ि'). Empty str means
             "inherent a" after a consonant.
    tags   : set of strings, e.g. {'anunasika', 'it_candidate_nut_t',
             'it', 'sthanin'}. The joiner and exec_samjna use tags.

    Invariants (enforced by tests/unit/test_every_varna_wellformed.py):
      • slp1 must not be empty
      • dev must be consistent with slp1 according to phonology/varna.py
        canonical maps — except for the single case of inherent-'a' after
        a consonant, where dev == "" is intentional.
    """
    slp1 : str
    dev  : str
    tags : Set[str] = field(default_factory=set)

    def clone(self) -> "Varna":
        return Varna(slp1=self.slp1, dev=self.dev, tags=set(self.tags))


# ═════════════════════════════════════════════════════════════════════════
# TERM
# ═════════════════════════════════════════════════════════════════════════

@dataclass
class Term:
    """
    A morphemic unit in the derivation.

    kind     : 'prakriti' | 'pratyaya' | 'agama' | 'upasarga' | 'nipata'
    varnas   : List[Varna] — ordered phonemes of this Term
    tags     : set of Term-level saṃjñās
               (e.g. 'prātipadika', 'anga', 'pada', 'dhatu', 'sup', 'tin',
               'nadi', 'ghi', 'sarvanama', 'ardhadhatuka', 'sarvadhatuka').
    meta     : dict for scholarly annotations that cond() MAY read
               but only from an allowlist:
                 meta['upadesha_slp1']  : str — pratyaya's upadeśa id
                 meta['gana']           : int — dhātu's gaṇa
                 meta['dhatu_it']       : set of str — old it-markers from upadeśa
               FORBIDDEN keys (tests enforce):
                 'vibhakti', 'vacana', 'purusha', 'lakara', 'surface_gold'
    """
    kind   : str
    varnas : List[Varna] = field(default_factory=list)
    tags   : Set[str]    = field(default_factory=set)
    meta   : Dict[str, Any] = field(default_factory=dict)

    def clone(self) -> "Term":
        return Term(
            kind   = self.kind,
            varnas = [v.clone() for v in self.varnas],
            tags   = set(self.tags),
            meta   = deepcopy(self.meta),
        )

    # Convenience accessors (never read forbidden fields).
    @property
    def final_varna(self) -> Optional[Varna]:
        return self.varnas[-1] if self.varnas else None

    @property
    def initial_varna(self) -> Optional[Varna]:
        return self.varnas[0] if self.varnas else None


# ═════════════════════════════════════════════════════════════════════════
# STATE
# ═════════════════════════════════════════════════════════════════════════

@dataclass
class State:
    """
    The FULL derivation state.

    Fields:
      terms               : ordered list of Terms currently in the derivation
      samjna_registry     : name → frozenset(member slp1 strings / tag names)
      paribhasha_gates    : key → any (gates set by PARIBHASHA sūtras)
      adhikara_stack      : list of {id, scope_end, text_dev}
      blocked_sutras      : set of sūtra_ids to skip
      niyama_gates        : sūtra_id → restriction value
      atidesha_map        : (source, dest) → target property string
      vibhasha_forks      : list of recorded forks (for audit)
      nipatana_flag       : bool — if True, VIDHI steps are frozen
      tripadi_zone        : bool — True once we enter 8.2.1 scope
      trace               : list of TraceStep-compatible dicts
      meta                : recipe-level scholarly annotations (not read by
                            cond() — only present for display)
    """
    terms            : List[Term]                    = field(default_factory=list)
    samjna_registry  : Dict[str, frozenset]          = field(default_factory=dict)
    paribhasha_gates : Dict[str, Any]                = field(default_factory=dict)
    adhikara_stack   : List[Dict[str, Any]]          = field(default_factory=list)
    blocked_sutras   : Set[str]                      = field(default_factory=set)
    niyama_gates     : Dict[str, Any]                = field(default_factory=dict)
    atidesha_map     : Dict[tuple, str]              = field(default_factory=dict)
    vibhasha_forks   : List[Dict[str, Any]]          = field(default_factory=list)
    nipatana_flag    : bool                          = False
    tripadi_zone     : bool                          = False
    # v3.1 amendment — three-phase model.  `phase` is authoritative;
    # `tripadi_zone` is retained for backward-compat and mirrors
    # (phase == "tripadi") at all times.  Executors must use phase.
    phase            : str                           = "angakarya"
    trace            : List[Dict[str, Any]]          = field(default_factory=list)
    meta             : Dict[str, Any]                = field(default_factory=dict)

    # ─────────────────────────────────────────────────────────────────
    # Mutation discipline:  every exec_* MUST call state.clone() first,
    # mutate the clone, and return it.  This makes "rollback on skip"
    # trivial and makes the dispatcher's form_before/form_after diff
    # reliable.
    # ─────────────────────────────────────────────────────────────────
    def clone(self) -> "State":
        return State(
            terms            = [t.clone() for t in self.terms],
            samjna_registry  = dict(self.samjna_registry),
            paribhasha_gates = dict(self.paribhasha_gates),
            adhikara_stack   = [dict(e) for e in self.adhikara_stack],
            blocked_sutras   = set(self.blocked_sutras),
            niyama_gates     = dict(self.niyama_gates),
            atidesha_map     = dict(self.atidesha_map),
            vibhasha_forks   = [dict(f) for f in self.vibhasha_forks],
            nipatana_flag    = self.nipatana_flag,
            tripadi_zone     = self.tripadi_zone,
            phase            = self.phase,
            trace            = [dict(s) for s in self.trace],
            meta             = deepcopy(self.meta),
        )

    # ─────────────────────────────────────────────────────────────────
    # Flat varṇa sequence — used by dispatcher to diff form_before /
    # form_after.  *It*-tagged Varṇas still on ``Term.varnas`` appear here until
    # **1.3.9** removes the rows (ādeśa/lopa is **1.3.9** only, not 1.3.3/8 *saṃjñā*).
    # ─────────────────────────────────────────────────────────────────
    def flat_slp1(self) -> str:
        from engine.it_phonetic import term_phonetic_slp1

        return "".join(term_phonetic_slp1(t) for t in self.terms)

    def flat_dev(self) -> str:
        """Halanta-naive concatenation over phonetic varṇas only."""
        from engine.it_phonetic import term_phonetic_varnas

        return "".join(v.dev for t in self.terms for v in term_phonetic_varnas(t))

    # For quick printing in traces.
    def render(self) -> str:
        return self.flat_slp1()
