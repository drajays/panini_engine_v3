"""
6.1.77  इको यणचि  —  VIDHI  (universal utsarga)

If an IK vowel (i, I, u, U, ṛ/f, ṝ/F, ḷ/x, ḹ/X) at the end of one Term is
immediately followed by an AC vowel at the start of the next Term, replace the
IK with the corresponding YAṆ consonant:

  i / I → y,   u / U → v,   f / F → r,   x / X → l

This is a **universal utsarga** (general rule).  Exceptions (apavāda) are
handled by the engine's asiddha / pratiṣedha mechanism — e.g. 6.1.101
(savarṇa-dīrgha) or 6.1.84 (ekaḥ pūrvaparayoḥ) govern the actual ekādeśa
locus; those rules block or override 6.1.77 where they apply.

Exemptions enforced here:
  • **Pragṛhya** terms (1.1.11 ``PRAGHYA_TERM_TAG``) are immune — their final
    vowel is *not* liable to saṃdhi (1.1.11, 6.1.125).
  • A boundary already processed (``iko_yanaci_done`` on the left Term) is skipped.

Blindness: purely phonemic — no paradigm coordinates, no pipeline arm flags.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


_YAN_MAP = {
    "i": "y", "I": "y",
    "u": "v", "U": "v",
    "f": "r", "F": "r",
    "x": "l", "X": "l",
}

# Full AC set including dīrgha representations used in the engine.
_AC_ALL = frozenset({
    "a", "A", "i", "I", "u", "U",
    "f", "F", "x", "X",
    "e", "E", "o", "O",
})


def _find_ik_ac_boundary(state: State) -> int | None:
    """
    Scan all adjacent Term pairs.  Return index ``i`` where ``terms[i]``
    ends in an IK (or IK-dīrgha) vowel and ``terms[i+1]`` begins with an
    AC vowel, the left Term is not pragṛhya, and has not already undergone yaṇ.
    """
    for i in range(len(state.terms) - 1):
        left, right = state.terms[i], state.terms[i + 1]
        if not left.varnas or not right.varnas:
            continue
        if left.meta.get("iko_yanaci_done"):
            continue
        if PRAGHYA_TERM_TAG in left.tags:
            continue
        la = left.varnas[-1].slp1
        rf = right.varnas[0].slp1
        if la not in _YAN_MAP:
            continue
        if rf not in _AC_ALL:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_ik_ac_boundary(state) is not None


def act(state: State) -> State:
    j = _find_ik_ac_boundary(state)
    if j is None:
        return state
    left = state.terms[j]
    left.varnas[-1] = mk(_YAN_MAP[left.varnas[-1].slp1])
    left.meta["iko_yanaci_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.77",
    sutra_type=SutraType.VIDHI,
    text_slp1="iko yaR aci",
    text_dev="इको यणचि",
    padaccheda_dev="इकः यण् अचि",
    why_dev=(
        "इक्-समाप्तेः परे अच्-आदौ यण्-आदेशः — सार्वत्रिकः उत्सर्गः; "
        "प्राग्र्ह्य-वर्ज्यम् (१.१.११); अपवादाः यथायोग्यम् (६.१.१०१ इत्यादि)।"
    ),
    anuvritti_from=("6.1.72",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
