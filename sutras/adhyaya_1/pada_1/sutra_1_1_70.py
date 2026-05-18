"""
1.1.70  तपरस्तत्कालस्य  (taparas tatkAlasya)  —  PARIBHASHA

Classical role:
  "A phoneme followed by the marker 't' (e.g., 'at', 'it', 'ut') stands
  for phonemes of THAT duration (tatkāla = same mātrā) ONLY."

  Example: 'at' (a + t-marker) specifies short 'a' alone — NOT long 'ā'
  (2-mātrā) nor pluta 'a₃' (3-mātrā).  Without this paribhāṣā the aṇ or
  AC specification would include all lengths.

  This is one of the most fundamental interpretive paribhāṣās in Aṣṭādhyāyī
  and must be registered before any rule that uses tapara notation.

v3 engine role:
  - Installs gate "1_1_70_tapara_tatkAlasya" in paribhasha_gates once per
    derivation (idempotent guard via cond).
  - Mirrors it in samjna_registry for audit/pipeline inspection.
  - cond() reads ONLY paribhasha_gates (Art. 2 compliant: no vibhakti,
    vacana, lakāra, surface Devanāgarī, data, or reference access).
  - No arm flags.  r1_form_identity_exempt=True (no surface change).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_1_70_tapara_tatkAlasya"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.1.70",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "taparas tatkAlasya",
    text_dev                = "तपरस्तत्कालस्य",
    padaccheda_dev          = "त-परः / तत्-कालस्य",
    why_dev                 = (
        "त-परो वर्णः (यथा अत्, इत्, उत्) तत्-कालस्यैव — "
        "अर्थात् समान-मात्रिक-वर्णानाम् एव — ग्राहकः; "
        "दीर्घ-प्लुतयोः न।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)
