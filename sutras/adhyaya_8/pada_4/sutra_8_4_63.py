"""
8.4.63  शश्छोऽटि  —  VIBHASHA

Padaccheda: शः । छः । अटि

Sources consulted:
- ashtadhyayi.com data.txt row i=84063 (samagra: पदान्तात् झयः शः छः वा अटि)
- Kāśikā: "झय उत्तरस्य शकारस्याटि परतश्छकारादेशो भवत्यन्यतरस्याम्। वाक्छेते, वाक् शेते। अग्निचिच्छेते, अग्निचित् शेते। …
  त्रिष्टुप् छेते, त्रिष्टुप् शेते॥"
- SK: "पदान्तात् झयः परस्य शस्य छो वा स्यादटि ।"
- Cross-validation: LK cases tests/fixtures/lk_cases/a8.json (8.4.63: vAkCete, declined vAkSete).

A pada-initial श that follows a pada-final jhay and stands before an aṭ letter (a vowel, ह, य, व, र) is replaced, optionally,
by छ. Pada-final / pada-initial is read off the tape: the jhay is the last varṇa of one `pada` Term and the श the first of the next.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk

_JHAY = frozenset("kKgGcCjJwWqQtTdDpPbB")
_AT = frozenset("aAiIuUfFxXeEoOhyvr")


def _pada(t) -> bool:
    return t.kind == "pada" or "pada" in t.tags


def _site(state: State):
    if not state.tripadi_zone:
        return None
    for left, right in zip(state.terms, state.terms[1:]):
        if not (_pada(left) and _pada(right) and left.varnas and len(right.varnas) > 1):
            continue
        if left.varnas[-1].slp1 in _JHAY and right.varnas[0].slp1 == "S" and right.varnas[1].slp1 in _AT:
            return right
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    _site(state).varnas[0] = mk("C")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.63",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = False,
    text_slp1             = 'SaSCowi',
    text_dev              = 'शश्छोऽटि',
    samagra_slp1          = "padAntAt JayaH SaH CaH vA awi",
    samagra_dev           = "पदान्तात् झयः शः छः वा अटि",
    padaccheda_dev        = "शः । छः । अटि",
    why_dev               = "(सूत्रम् 8.4.63) पदान्तात् झयः परस्य शस्य छो वा अटि — वाक्छेते, वाक् शेते।",
    anuvritti_from        = ('8.4.62',),
    vibhasha_scope        = cond,
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
