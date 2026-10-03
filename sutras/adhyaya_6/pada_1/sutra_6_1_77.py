"""
6.1.77  इको यणचि  —  VIDHI  (universal utsarga)

Sources consulted:
- ashtadhyayi.com data.txt row i=601077
- Kāśikā: इको यणणि (परस्मिन् अचि यणादेशः)
- Cross-validation: tests/unit/test_iko_yan_aci_samhita.py;
  tests/unit/test_phalAni_santi_as_lat_padanta_lesson.py (**1.1.58** blocks
  *phalāni*+अन्ति when **6.4.111** *padādi* *a*-lopa on *as*)

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
  • **1.1.58** (*padānta*): when a *pūrvapada* ends in *ik* and the following
    *tiṅānta* tape includes **6.4.111** *padādi* *ac* *lopa* on *as*, the lupta
    *a* is not *sthānivat* for this *padānta* *yaṇ* (``phalāni santi``, not *y*).
  • **1.1.58** (*dvirvacana*, tripāḍī **8.4.47**): *yaṇ* from this rule is
    *para-nimitta* — tag ``iko_yanaci_adesha``; it is **not** *sthānivat* for
    gemination of **other** consonants (``madhu``+``ari`` → ``maddhvari``).

Blindness: purely phonemic — no paradigm coordinates, no pipeline arm flags.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG
from sutras.adhyaya_6.pada_4.sutra_6_4_111 import META_PADADI_AC_LOPA


_YAN_MAP = {
    "i": "y", "I": "y",
    "u": "v", "U": "v",
    "f": "r", "F": "r",
    "x": "l", "X": "l",
}

# Full AC set including dīrgha representations used in the engine.
IKO_YANACI_ADESHA_TAG = "iko_yanaci_adesha"

_AC_ALL = frozenset({
    "a", "A", "i", "I", "u", "U",
    "f", "F", "x", "X",
    "e", "E", "o", "O",
})


def _blocked_by_padadi_ac_lopa_padanta(state: State, boundary_i: int) -> bool:
    """
    **1.1.58** (*padānta*): *para-nimitta* *ac* elided at *padādi* of the verbal
    *pada* (e.g. **6.4.111** on *as*) does not licence *yaṇ* on the preceding
    *prātipadika* before that verbal *tiṅ*'s initial *ac*.
    """
    if boundary_i + 1 >= len(state.terms):
        return False
    left = state.terms[boundary_i]
    if "prātipadika" not in left.tags:
        return False
    if not state.paribhasha_gates.get("1_1_58_na_padAnta_etc"):
        return False
    for t in state.terms[boundary_i + 1 :]:
        if t.meta.get(META_PADADI_AC_LOPA):
            return True
    return False


def _find_ik_ac_boundary(state: State) -> tuple[int, int] | None:
    """
    Flat scan of the varna stream.  Return ``(term_i, varna_i)`` of an IK
    vowel immediately followed by an AC vowel — across a Term boundary
    (left Term not pragṛhya / not already done / not 1.1.58-blocked) or
    inside one Term.
    """
    terms = state.terms
    for i, left in enumerate(terms):
        n = len(left.varnas)
        for k in range(n - 1):  # intra-term
            if left.varnas[k].slp1 in _YAN_MAP and left.varnas[k + 1].slp1 in _AC_ALL:
                return i, k
        if i + 1 >= len(terms) or not n or not terms[i + 1].varnas:
            continue
        if left.meta.get("iko_yanaci_done") or PRAGHYA_TERM_TAG in left.tags:
            continue
        if _blocked_by_padadi_ac_lopa_padanta(state, i):
            continue
        if left.varnas[-1].slp1 in _YAN_MAP and terms[i + 1].varnas[0].slp1 in _AC_ALL:
            return i, n - 1
    return None


def cond(state: State) -> bool:
    return _find_ik_ac_boundary(state) is not None


def act(state: State) -> State:
    hit = _find_ik_ac_boundary(state)
    if hit is None:
        return state
    j, k = hit
    left = state.terms[j]
    old = left.varnas[k].slp1
    yan = mk(_YAN_MAP[old])
    yan.tags.add(IKO_YANACI_ADESHA_TAG)
    left.varnas[k] = yan
    if k == len(left.varnas) - 1:
        left.meta["iko_yanaci_done"] = True
        left.meta["para_nimitta_yan_adesha"] = True
    state.meta["__why_now_dev__"] = (
        f"संधिः: {old} + अच् → {_YAN_MAP[old]} (यण्-आदेशः); (काशिका ६।१।७७)"
    )
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.77",
    sutra_type=SutraType.VIDHI,
    text_slp1='iko yaRaci',
    text_dev='इको यणचि',
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

__all__ = ["IKO_YANACI_ADESHA_TAG", "SUTRA"]
