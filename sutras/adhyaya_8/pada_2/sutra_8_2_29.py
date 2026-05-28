"""
8.2.29  स्कोः संयोगाद्योरन्ते च  —  VIDHI

Two operational paths:
  1. Arm ``8_2_29_arm``: legacy gate-setter.
  2. Arm ``8_2_29_ashir_liG_arm``: āśīr-liṅ saṃyoga s-lopa.

āśīr-liṅ path (fires on terms, before _pada_merge):

Step A — yāsuṭ 's' before suṭ 's' (saṃyoga 'ss'):
  Find yāsuṭ term ending in 's' immediately followed by suṭ term (single 's').
  Drop the yāsuṭ-s.  This fires for all forms that have both yāsuṭ + suṭ
  (i.e. t-initial tiṅ: 3sg, 3du, 2du, 2pl).

Step B — suṭ 's' before final pure-consonant tiṅ (saṃyoga at pada-end):
  After Step A: find suṭ term (single 's') followed by a LAST term whose
  varṇas are all consonants (no vowels).  Drop the suṭ term.
  This fires only for 3sg (tiṅ = [t], pure consonant) — giving bhūyāt.
  Does NOT fire for 3du/2du/2pl (tiṅ = tāṃ/tam/ta, all contain vowels).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import HAL

_GATE_KEY: str = "8_2_29_skoH_29"


def _find_yasut_suw_pair(state: State):
    """Return index of yāsuṭ term that precedes a suṭ term."""
    for i, t in enumerate(state.terms):
        if "yasut_agama" not in t.tags:
            continue
        if t.meta.get("8_2_29_yasut_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "s":
            continue
        if i + 1 >= len(state.terms):
            continue
        nxt = state.terms[i + 1]
        if "suw_agama" not in nxt.tags:
            continue
        return i
    return None


def _all_hal(t) -> bool:
    return bool(t.varnas) and all(v.slp1 in HAL for v in t.varnas)


def cond(state: State) -> bool:
    if state.meta.get("8_2_29_ashir_liG_arm"):
        return _find_yasut_suw_pair(state) is not None
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_29_arm"))


def act(state: State) -> State:
    if state.meta.get("8_2_29_ashir_liG_arm"):
        j = _find_yasut_suw_pair(state)
        if j is None:
            return state

        yāsuṭ = state.terms[j]
        suṭ   = state.terms[j + 1]

        # Step A: drop yāsuṭ-s (last varṇa of yāsuṭ term)
        del yāsuṭ.varnas[-1]
        yāsuṭ.meta["8_2_29_yasut_done"] = True
        state.samjna_registry["8.2.29_yasut_s_lopa"] = True

        # Step B: drop suṭ when followed by final all-consonant tiṅ
        suw_idx = j + 1
        if suw_idx + 1 < len(state.terms):
            tin = state.terms[suw_idx + 1]
            if suw_idx + 1 == len(state.terms) - 1 and _all_hal(tin):
                state.terms.pop(suw_idx)
                state.samjna_registry["8.2.29_suw_s_lopa"] = True

        return state

    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"] = "8.2.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "skoH saMyogAdyorante ca",
    text_dev              = "स्कोः संयोगाद्योरन्ते च",
    padaccheda_dev        = "स्-कोः संयोग-आद्योः अन्ते च",
    why_dev               = (
        "आशीर्-लिङि: यासुट्-सकारस्य लोपः (सुट्-पूर्वं संयोग-आदि) — "
        "तदनन्तरं सुट्-सकारस्यापि लोपः यदि पद-अन्ते केवल-व्यञ्जन-तिङ् (३एकवचन)।"
    ),
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
