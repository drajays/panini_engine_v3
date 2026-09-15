"""
3.3.13  लृट् शेषे च  —  VIDHI

Padaccheda: लृट् शेषे च

krt-suffix rule: लृट् शेषे च

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 33013 · लृट् शेषे च
              padaccheda: लृट् शेषे च
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ् | 33003: भविष्यति | 33010: क्रियायाम्  क्रियार्थायाम्
  Source #2 — Kāśikā 3.3.13 udāharaṇa:
                शेषः क्रियार्थोपपदादन्यः
                करिष्यामीति व्रजति
                हरिष्यामीति व्रजति
  Cross-check — surface pinned by: tests/unit/test_tinanta_abhavisyat_lrg.py
  Reference record: sutra_ref_out/3_3_13.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_13_lfw_13"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.13", gate_key=_GATE_KEY, adhikara_id="3.1.1")
    return bool(state.meta.get("lfT_recipe"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lfw Seze ca",
    text_dev              = "लृट् शेषे च",
    padaccheda_dev        = "लृट् शेषे च",
    why_dev               = "धातोः प्रत्ययः (३.3.13)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
