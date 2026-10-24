"""
6.4.4  न तिसृचतसृ  —  VIDHI

Padaccheda: न तिसृ-चतसृ (लुप्तषष्ठ्यन्तनिर्देशः)

न तिसृचतसृ (6.4.4)
Pāṭha: ashtadhyayi.com data.txt row i=64004 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.declension import anga_and_sup
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

def _site(state: State):
    """न तिसृचतसृ — no dīrgha (6.4.3) for the aṅga तिसृ / चतसृ before the nuṭ-āma: तिसृणाम्, चतसृणाम्."""
    hit = anga_and_sup(state, "6.4.4")
    if hit is None:
        return None
    anga, sup = hit
    return anga if anga.meta.get("7_2_99_done") and sup.varnas and "nut_agama_inserted" in sup.varnas[0].tags else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    state.blocked_sutras.add("6.4.3")
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.4",
    sutra_type            = SutraType.PRATISHEDHA,
    text_slp1             = "na tisfcatasf",
    text_dev              = "न तिसृचतसृ",
    samagra_slp1          = "tisf-catasf-aNgasya nAmi dIrGaH na",
    samagra_dev           = "तिसृ-चतसृ-अङ्गस्य नामि दीर्घः न",
    padaccheda_dev        = "न तिसृ-चतसृ (लुप्तषष्ठ्यन्तनिर्देशः)",
    why_dev               = "(सूत्रम् 6.4.4) न तिसृचतसृ।",
    anuvritti_from        = ('6.1.1',),
    blocks_sutra_ids      = ('6.4.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
