"""
1.1.69  अणुदित् सवर्णस्य चाप्रत्ययः  (aNudit savarNasya cApratyayaH)  —  SAMJNA

Classical role:
  "An aṇ-phoneme (a, i, u — the pratyāhāra aṇ) or a ud-it term (one whose
  it-marker is 'u') stands for itself AND all its savarṇas (homogeneous
  sounds), EXCEPT when occurring as a pratyaya (suffix)."

  This extends the savarṇa-inclusion convention of the previous sūtras to
  the aṇ pratyāhāra and ud-it terms.  The "ca" (also) in the title picks up
  the 'savarṇa' reading from the preceding context, and "apratyayaḥ"
  carves out the pratyaya exception.

  SLP1: aṇ pratyāhāra = {a, i, u}
        ud-it = terms carrying 'u' as an it-marker

v3 engine role:
  - Registers the savarṇa-coverage rule for aṇ phonemes in samjna_registry
    under key "1_1_69_aN_udit_savarNa" as a frozenset({a, i, u}).
  - Also sets paribhasha_gates["1_1_69_aN_udit_savarNa"] = True so that
    downstream rules can gate-check without querying the registry value.
  - cond() reads ONLY samjna_registry (Art. 2 compliant: no vibhakti,
    vacana, lakāra, surface Devanāgarī, data, or reference access).
  - No arm flags.  r1_form_identity_exempt=True (pure SAMJNA, no rewrite).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# aṇ pratyāhāra = short vowels a, i, u  (SLP1)
_AN_PHONEMES: frozenset = frozenset({"a", "i", "u"})

_REGISTRY_KEY = "1_1_69_aN_udit_savarNa"
_GATE_KEY     = "1_1_69_aN_udit_savarNa"


def cond(state: State) -> bool:
    return state.samjna_registry.get(_REGISTRY_KEY) is not _AN_PHONEMES


def act(state: State) -> State:
    state.samjna_registry[_REGISTRY_KEY] = _AN_PHONEMES
    state.paribhasha_gates[_GATE_KEY]    = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.1.69",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "aNudit savarNasya cApratyayaH",
    text_dev                = "अणुदित् सवर्णस्य चाप्रत्ययः",
    padaccheda_dev          = "अण्-उदित् / सवर्णस्य / च / अप्रत्ययः",
    why_dev                 = (
        "अण्-प्रत्याहार-वर्णाः (अ, इ, उ) तथा उदित्-संज्ञकाः वर्णाः "
        "स्व-सवर्णान् अपि ग्राहयन्ति — प्रत्यय-प्रसङ्गे तु न।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)
