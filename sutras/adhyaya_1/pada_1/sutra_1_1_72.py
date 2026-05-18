"""
1.1.72  येन विधिस्तदन्तस्य  (yena viDis tadantasya)  —  PARIBHASHA

Classical role:
  "When a rule is expressed using a term X, it applies to [words/stems]
  ending in X (tad-anta)."

  This is the tad-anta-vidhi paribhāṣā. For example, the rule "udāttasya"
  applies not only to a single phoneme that is udātta but to any pada
  whose final syllable is udātta. Similarly "āt" in a rule means "of what
  ends in ā", not merely "of ā alone."

  This paribhāṣā is fundamental to the interpretation of a large number
  of sandhi, taddhita, and kṛt rules in the Aṣṭādhyāyī.

v3 engine role:
  - Installs gate "1_1_72_yena_viDis_tadantasya" in paribhasha_gates
    once per derivation (idempotent guard via cond).
  - Mirrors it in samjna_registry for audit/pipeline inspection.
  - cond() reads ONLY paribhasha_gates (Art. 2 compliant: no vibhakti,
    vacana, lakāra, surface Devanāgarī, data, or reference access).
  - No arm flags.  r1_form_identity_exempt=True (no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_1_72_yena_viDis_tadantasya"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.1.72",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "yena viDis tadantasya",
    text_dev                = "येन विधिस्तदन्तस्य",
    padaccheda_dev          = "येन / विधिः / तद्-अन्तस्य",
    why_dev                 = (
        "यस्मिन् शब्दे (येन) विधिः (नियमः) उच्यते, "
        "स विधिः तद्-अन्तस्य — तेन अन्तेन युक्तस्य पदस्य — विषयः। "
        "यथा 'उदात्तस्य' इत्युक्ते उदात्त-अन्तस्य पदस्य विधिः।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
