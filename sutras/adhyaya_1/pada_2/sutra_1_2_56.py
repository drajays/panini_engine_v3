"""
1.2.56  प्रधानप्रत्ययार्थवचनमर्थस्यान्यप्रमाणत्वात्  —  PARIBHASHA

*Padaccheda:* **प्रधान-प्रत्यय-अर्थ-वचनम्** / **अर्थस्य** / **अन्य-प्रमाणत्वात्**

"The statement of the principal pratyaya's meaning [takes precedence] because
other authorities govern the overall meaning."  This is a meta-paribhāṣā about
the authority hierarchy in meaning-derivation: when the primary suffix (pratyaya)
carries a meaning statement, that statement holds because other pramāṇas
(authorities) independently govern the complete meaning.

Operational role (v3):
  - Registers the gate ``1_2_56_praDAna_pratyaya`` in both ``paribhasha_gates``
    and ``samjna_registry``.
  - Downstream rules consult this gate when adjudicating between competing
    meaning-derivation authorities for principal pratyayas.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_56_praDAna_pratyaya"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.56",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "praDAnapratyayArTavacanaM arTasya anyapramARatvAt",
    text_dev                = "प्रधानप्रत्ययार्थवचनमर्थस्यान्यप्रमाणत्वात्",
    padaccheda_dev          = "प्रधान-प्रत्यय-अर्थ-वचनम् / अर्थस्य / अन्य-प्रमाणत्वात्",
    why_dev                 = (
        "प्रधानस्य प्रत्ययस्य अर्थवचनम् प्रामाणिकम् — अर्थस्य अन्यप्रमाणत्वात् "
        "प्रत्ययार्थकथनम् प्राधान्येन स्वीक्रियते इति परिभाषा।"
    ),
    anuvritti_from          = ("1.2.55",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
