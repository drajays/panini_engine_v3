"""
1.2.19  निष्ठा शीङ्स्विदिमिदिक्ष्विदिधृषः  —  NIYAMA

Meaning: Before "niṣṭhā" suffixes (kta / ktavatu~), the roots śīṅ (to sleep),
svid (to sweat), mid (to be unctuous), ikṣvid, and dhṛṣ are seṭ.

This is a niyama that grants the seṭ property to specific dhātus in the
context of niṣṭhā (kta, ktavatu~) pratyayas, where the general expectation
might be aniṭ. It is in anuvṛtti from 1.2.18 and carves out an exception.

Engine:
  - Module-level frozenset NISTHA_ROOTS_SLP1 holds the upadeśa forms
    (SLP1) for śīṅ, svid, mid, ikṣvid, dhṛṣ.
  - Finds a dhātu Term whose upadesha_slp1 is in NISTHA_ROOTS_SLP1.
  - Checks that the following pratyaya has upadesha_slp1 in {"kta", "ktavatu~"}.
  - Guards re-entry via meta["seT_nistha_1_2_19"].
  - Adds "seT" to the dhātu Term.
  - r1_form_identity_exempt=True: no surface string changes in this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset — CONSTITUTION Article 2 (no runtime data reads)
# SLP1 upadeśa forms for: śīṅ, svid, mid, ikṣvid, dhṛṣ
NISTHA_ROOTS_SLP1: frozenset = frozenset({
    "SI\\~N",   # śīṅ — to sleep (anusvāra indicated by ~)
    "SIN",      # alternative SLP1 encoding
    "zvid",     # svid — to sweat
    "zvidA",    # svid with ā-variant
    "mid",      # mid — to be unctuous
    "midA",     # mid with ā-variant
    "ikzvid",   # ikṣvid
    "ikzvidA",  # ikṣvid with ā-variant
    "Dfz",      # dhṛṣ — to be bold
})

# niṣṭhā pratyaya upadeśa set
_NISTHA_PRATYAYA: frozenset = frozenset({"kta", "ktavatu~"})


def _find(state: State) -> int | None:
    """Return index of a dhātu Term to be granted seṭ, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("seT_nistha_1_2_19"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in NISTHA_ROOTS_SLP1:
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
    state.terms[i].meta["seT_nistha_1_2_19"] = True
    state.samjna_registry["1_2_19_nisTHA_roots"] = NISTHA_ROOTS_SLP1
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.19",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "niSTA SIN-zvid-mid-ikzvid-Dfz",
    text_dev              = "निष्ठा शीङ्स्विदिमिदिक्ष्विदिधृषः",
    padaccheda_dev        = "निष्ठा / शीङ्-स्विदि-मिदि-क्ष्विदि-धृषः",
    why_dev               = ("निष्ठा-प्रत्ययस्य (क्त-क्तवतु) पूर्वं शीङ्-स्विदि-मिदि-"
                             "क्ष्विदि-धृष्-धातवः सेट् भवन्ति — एतेभ्यः इडागमो भवति।"),
    anuvritti_from        = ("1.2.18",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
