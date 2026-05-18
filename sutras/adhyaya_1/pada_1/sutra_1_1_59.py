"""
1.1.59  द्विर्वचनेऽचि  (dvirvacane'ci)  —  NIYAMA

Classical role:
  "In dvirvacana (reduplication), when followed by AC (a vowel), [the
  prior sthāni-rule / anuvṛtti applies differently]."

  This is a restricting paribhāṣā / niyama that conditions dvirvacana
  behaviour specifically in the AC (vowel) context.  Downstream rules
  check the gate "1_1_59_dvirvacane_aci" before deciding whether the
  standard dvirvacana treatment or the vowel-context treatment applies.

v3 engine role:
  - Installs gate "1_1_59_dvirvacane_aci" in paribhasha_gates and
    mirrors it in samjna_registry once per derivation.
  - cond() reads ONLY paribhasha_gates (Art. 2 compliant: no vibhakti,
    vacana, lakāra, surface Devanāgarī, data, or reference access).
  - No arm flags.  r1_form_identity_exempt=True (no surface change).

anuvritti: 1.1.58
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_1_59_dvirvacane_aci"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.1.59",
    sutra_type              = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1               = "dvirvacaneci",
    text_dev                = "द्विर्वचनेऽचि",
    padaccheda_dev          = "द्विर्वचने / अचि",
    why_dev                 = (
        "द्विर्वचन-प्रसङ्गे अचि परतः विशेष-नियमः — "
        "तद्-गेट् १_१_५९ द्वारा पूर्व-सूत्र-अनुवृत्तिः नियम्यते।"
    ),
    anuvritti_from          = ("1.1.58",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)
