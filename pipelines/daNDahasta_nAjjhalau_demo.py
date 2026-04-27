"""
pipelines/daNDahasta_nAjjhalau_demo.py — *daṇḍa*+*hasta* / *dadhi*+*śītalam* & **1.1.10**.

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/दण्डहस्त.md``

Glass-box: merged *saṃhitā* tapes, **1.1.9** (*savarṇa* saṃjñā) + **1.1.10**
(*paribhāṣā* gate) + **6.1.101** — surface must **not** show *savarṇa-dīrgha*
across *ac*–*hal* (``phonology.savarna.is_savarna`` implements *nājjhalau*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _samhitA_state(*parts: str) -> State:
    varnas = []
    for p in parts:
        varnas.extend(parse_slp1_upadesha_sequence(p))
    t = Term(kind="prakriti", varnas=varnas, tags={"samhitA_demo"})
    return State(terms=[t], meta={}, trace=[])


def _run_savarRa_dIrgha_probe(s: State) -> State:
    s = apply_rule("1.1.9", s)
    s = apply_rule("1.1.10", s)
    s = apply_rule("6.1.101", s)
    return s


def derive_daNDahasta_nAjjhalau_demo() -> State:
    """*daṇḍa* + *hasta* → ``daNDahasta`` (no *ā* at *a*–*h*)."""
    s = _samhitA_state("daNDa", "hasta")
    return _run_savarRa_dIrgha_probe(s)


def derive_dadhi_SItalam_nAjjhalau_demo() -> State:
    """*dadhi* + *śītalam* — boundary *i* + *ś* must not *dīrgha*."""
    s = _samhitA_state("dadhi", "SItalam")
    return _run_savarRa_dIrgha_probe(s)


__all__ = [
    "derive_daNDahasta_nAjjhalau_demo",
    "derive_dadhi_SItalam_nAjjhalau_demo",
]
