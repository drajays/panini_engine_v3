"""
1.2.21  उदुपधाद्भावादिकर्मणोरन्यतरस्याम्  —  VIBHASHA

Meaning: A root whose penultimate phoneme is "u" or "ū" (u-upadeha),
optionally takes seṭ before niṣṭhā suffixes (kta / ktavatu~) when the
derivation is in bhāva (abstract action) or karma (patient-centred) sense.

Engine:
  - Module-level frozenset _U_UPADESHA_PHONEMES holds the penultimate vowels
    that trigger this rule.
  - Finds a dhātu Term whose upadesha_slp1 has a penultimate phoneme in
    _U_UPADESHA_PHONEMES (guards for len >= 2 before indexing [-2]).
  - Checks that the dhātu carries either "bhava_karma_usage" tag.
  - Checks that the following pratyaya has upadesha_slp1 in {"kta","ktavatu~"}.
  - Guards re-entry via meta["seT_vibhASA_1_2_21"].
  - vibhasha_default=True → the optional seṭ is applied by default (the
    engine handles the optional / paksha branching at a higher level).
  - r1_form_identity_exempt=True: no surface string changes at this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozensets — CONSTITUTION Article 2
_U_UPADESHA_PHONEMES: frozenset = frozenset({"u", "U"})   # SLP1 u / ū
_NISTHA_PRATYAYA: frozenset = frozenset({"kta", "ktavatu~"})


def _penultimate_phoneme(upadesha: str) -> str:
    """Return the penultimate character of upadesha, or '' if too short."""
    return upadesha[-2] if len(upadesha) >= 2 else ""


def _find(state: State) -> int | None:
    """Return index of eligible dhātu Term, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("seT_vibhASA_1_2_21"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if _penultimate_phoneme(up) not in _U_UPADESHA_PHONEMES:
            continue
        # Semantic gate: bhāva or karma usage
        if "bhava_karma_usage" not in t.tags:
            continue
        # Look for a following niṣṭhā pratyaya
        for j in range(i + 1, len(state.terms)):
            pt = state.terms[j]
            if "pratyaya" not in pt.tags:
                continue
            pup = (pt.meta.get("upadesha_slp1") or "").strip()
            if pup in _NISTHA_PRATYAYA:
                return i
            break
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("seT")
    state.terms[i].meta["seT_vibhASA_1_2_21"] = True
    state.samjna_registry["1_2_21_udupaDAt_vibhASA"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.21",
    sutra_type            = SutraType.VIBHASHA,
    vibhasha_default      = True,
    r1_form_identity_exempt = True,
    text_slp1             = "udupaDAt BAva-Adi-karmaNoH anyatarasyAm",
    text_dev              = "उदुपधाद्भावादिकर्मणोरन्यतरस्याम्",
    padaccheda_dev        = "उदुपधात् / भाव-आदि-कर्मणोः / अन्यतरस्याम्",
    why_dev               = ("उ-उपध-धातोः भाव-कर्मणोः निष्ठा-प्रत्ययस्य पूर्वं "
                             "विभाषा सेट् भवति — विकल्पेन इडागमो भवति।"),
    anuvritti_from        = ("1.2.19",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
