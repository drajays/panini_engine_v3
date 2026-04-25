"""
**1.3.78** *śeṣāt kartari parasmaipadam* — modular helpers for *kartari* *pada* default.

Not a sūtra file.  Used by ``sutra_1_3_78``.

*Śāstra (laghu):* after the *ātmanepada* prescriptions (**1.3.12** *vibhāṣā* through **1.3.77**),
whatever *dhātu* situations remain (*śeṣa*) take *parasmaipada* affixes in *kartari*.

*Engine:* the recipe (or a future **1.3.12**–**1.3.77** chain) may set
``Term.meta['kartari_atmanepada_licensed']`` to a truthy value when *ātmanepada* is licensed for
*kartari* for that *dhātu* in the current derivation.  When that flag is absent or false,
**1.3.78** sets ``paribhasha_gates[GATE_KEY]['active']`` to ``True`` (*parasmaipada* default).

This key is **not** a forbidden *cond* coordinate (CONSTITUTION Art. 2).

*Cross-refs:* **1.3.14** (*kartari* *anuvṛtti*), **1.4.99** (*parasmaipada* *sañjñā* on *ādeśa*).
"""
from __future__ import annotations

from typing import Final

from engine.state import State, Term

GATE_KEY: Final[str] = "prayoga_1_3_78_seza_kartari_parasmaipada"

# Recipe / 1.3.12–77 chain: truthy ⇒ *ātmanepada* licensed for *kartari* for this *dhātu*.
ATMANE_LICENSE_META_KEY: Final[str] = "kartari_atmanepada_licensed"


def find_primary_dhatu(state: State) -> Term | None:
    for t in state.terms:
        if "dhatu" in t.tags:
            return t
    return None


def kartari_parasmaipada_seza_active(state: State) -> bool:
    """True iff the **1.3.78** gate says *śeṣa* → *parasmaipada* in *kartari*."""
    return state.paribhasha_gates.get(GATE_KEY, {}).get("active") is True


def _desired_gate_active(dhatu: Term) -> bool:
    return not bool(dhatu.meta.get(ATMANE_LICENSE_META_KEY))


def seza_parasmaipada_gate_needs_update(state: State) -> bool:
    d = find_primary_dhatu(state)
    if d is None:
        return False
    desired = _desired_gate_active(d)
    cur = state.paribhasha_gates.get(GATE_KEY, {}).get("active")
    return cur is None or cur is not desired
