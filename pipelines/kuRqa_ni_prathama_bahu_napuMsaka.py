"""
pipelines/kuRqa_ni_prathama_bahu_napuMsaka.py — कुण्डानि (prathamā-bahu, napuṃsaka).

Implements the exact sūtra spine described in the user's `कुण्डानि.md` note:

  1. 1.2.45  prātipadika
  2. (meta vibhakti_vacana set to 1-3; napuṃsaka)
  3. 4.1.2   sup: jas
  4. 7.1.20  jas/śas → śi (napuṃsake)
  5. 1.3.7 + 1.3.9  it-lopa on śi's initial S
  6. 1.1.42  śi → sarvanāmasthāna
  7. 7.1.72  num-āgama on aṅga
  8. 1.1.47  mit placement gate (audit/niyama)
  9. 6.4.8   upadhā dīrgha before sarvanāmasthāna (asambuddhau)

Final expected surface (SLP1): ``kuRqAni``.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_kuRqAni() -> State:
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kuRqa")),
        tags={"anga"},
        meta={"upadesha_slp1": "kuRqa"},
    )
    stem.tags.add("napuṃsaka")
    s = State(terms=[stem], meta={"linga": "napuṃsaka"}, trace=[])
    s = apply_rule("1.2.45", s)
    s.meta["vibhakti_vacana"] = "1-3"
    s = apply_rule("4.1.2", s)
    s = apply_rule("7.1.20", s)
    s = apply_rule("1.3.7", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.1.42", s)
    s = apply_rule("7.1.72", s)
    s = apply_rule("1.1.47", s)
    s = apply_rule("6.4.8", s)
    return s


__all__ = ["derive_kuRqAni"]

