"""
6.4.23  श्नान्नलोपः  —  VIDHI

Padaccheda: श्नात् न-लोपः

श्नान्नलोपः (6.4.23)

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 64023 · श्नान्नलोपः
              padaccheda: श्नात् न-लोपः
              anuvṛtti:   64001: अङ्गस्य
  Source #2 — Kāśikā 6.4.23 udāharaṇa:
                तत उत्तरस्य नकारस्य लोपो भवति
                अनक्ति
                भनक्ति
  Cross-check — surface pinned by: tests/unit/test_c0_regressions_2026_09.py
  Reference record: sutra_ref_out/6_4_23.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_23_SnAnnalopa_23"


_NASAL = frozenset("NYRnmM")


def _find(state: State):
    """श्नान्नलोपः: a nasal right after śnam's na drops — हिन्स् → हिनस् (हिनस्ति),
    भन्ज् → भनज् (भनक्ति), उन्द् → उनद् (उनत्ति)."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags or t.meta.get("6_4_23_done"):
            continue
        vs = t.varnas
        for k in range(len(vs) - 1):
            if vs[k].slp1 == "n" and "snam" in vs[k].tags:
                j = k + 1
                if j < len(vs) and "snam" in vs[j].tags:
                    j += 1                                  # skip śnam's a
                if j < len(vs) and vs[j].slp1 in _NASAL:
                    return (i, j)
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    hit = _find(state)
    if hit is None:
        return state
    i, j = hit
    del state.terms[i].varnas[j]
    state.terms[i].meta["6_4_23_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.23",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "SnAnnalopaH",
    text_dev              = "श्नान्नलोपः",
    padaccheda_dev        = "श्नात् न-लोपः",
    why_dev               = "(सूत्रम् 6.4.23) श्नान्नलोपः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
