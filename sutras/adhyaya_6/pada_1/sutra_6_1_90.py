"""
6.1.90  आटश्च  —  VIDHI

Extends 6.1.88 vṛddhireci to include āṭ: when the āṭ-āgama (reduced to ā
after IT-lopa of T) immediately precedes an ec vowel (E = ai), the ā is
absorbed — the two are replaced by just the ec vowel.

In karmani loṭ 1sg: ya | ā(āṭ) | E(ai-tiṅ)
  After 6.1.90: ā absorbed → ya | | E
  Then 6.1.88 vṛddhireci: ya-a + E → ya → y + E = yE (bhūyai)

Operative condition: a term tagged "aTa_agama" with single varṇa 'A'
immediately followed by a term starting with an EC vowel (E, e, O, o).
Arm: state.meta["6_1_90_loT_karmani_arm"] must be True.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_EC = frozenset({"E", "e", "O", "o"})


def _find_at_ec(state: State):
    if not state.meta.get("6_1_90_loT_karmani_arm"):
        return None
    for i in range(len(state.terms) - 1):
        t1 = state.terms[i]
        t2 = state.terms[i + 1]
        if not t1.varnas or not t2.varnas:
            continue
        if "aTa_agama" not in t1.tags:
            continue
        if len(t1.varnas) == 1 and t1.varnas[0].slp1 == "A":
            if t2.varnas[0].slp1 in _EC:
                return i
    return None


def cond(state: State) -> bool:
    return _find_at_ec(state) is not None


def act(state: State) -> State:
    i = _find_at_ec(state)
    if i is None:
        return state
    # Delete the ā varṇa from the āṭ-derived term (it merges into the ec)
    del state.terms[i].varnas[0]
    state.meta.pop("6_1_90_loT_karmani_arm", None)
    state.samjna_registry["6.1.90_AT_ec_merge"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "AwaSca",
    text_dev              = "आटश्च",
    padaccheda_dev        = "आटः च",
    why_dev               = (
        "लोट् उत्तम-१एक. में आट्-जन्य-आकार एच् (ऐ) से पूर्व: "
        "आ + ऐ → ऐ (आटाश्च वृद्धिः); "
        "आट्-पद विलुप्तः।"
    ),
    anuvritti_from        = ('6.1.88',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
