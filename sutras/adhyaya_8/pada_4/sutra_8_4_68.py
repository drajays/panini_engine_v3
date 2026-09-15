"""
8.4.68  अ अ इति  —  ANUVADA

Padaccheda: अ · अ · इति

Acts as a tripāḍī zone marker. No phonemic transformation — sets a gate and
sandhi_kind meta. Fires whenever the gate has not yet fired for this derivation.

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 84068 · अ अ इति
              padaccheda: अ · अ · इति
  Source #2 — Kāśikā 8.4.68 udāharaṇa:
                अअ
                अआ
                आअ
  Cross-check — surface pinned by: tests/constitutional/test_astadhyayi_kram_respected.py, tests/test_bhavati_glassbox.py, tests/unit/test_autonomous_vs_recipe.py
  Reference record: sutra_ref_out/8_4_68.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_68_a_68"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.68", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]         = "8.4.68"
    return state


SUTRA = SutraRecord(
    sutra_id                = "8.4.68",
    sutra_type              = SutraType.ANUVADA,
    r1_form_identity_exempt = True,
    text_slp1               = "a a iti",
    text_dev                = "अ अ इति",
    padaccheda_dev          = "अ · अ · इति",
    why_dev                 = "(सूत्रम् 8.4.68) अ अ इति।",
    anuvritti_from          = ('8.1.1',),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)
