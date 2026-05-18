"""
1.2.20  मृषस्तितिक्षायाम्  —  NIYAMA

Meaning: The root "mṛṣ" (to endure / tolerate) is seṭ before niṣṭhā suffixes
(kta / ktavatu~) specifically when it is used in the sense of "titikṣā"
(endurance, forbearance).

This is a niyama: without this sūtra the general aniṭ treatment from 1.2.18
would apply to mṛṣ; 1.2.20 carves out the titikṣā usage and grants seṭ there.

Engine:
  - Finds a dhātu Term whose upadesha_slp1 is "mfz" (SLP1 for mṛṣ).
  - Checks that the following pratyaya has upadesha_slp1 in {"kta", "ktavatu~"}.
  - Checks that the dhātu Term carries the tag "titikzA_usage" (set upstream
    by the semantic / anukaraṇa layer to indicate the titikṣā sense).
  - Guards re-entry via meta["seT_mrz_1_2_20"].
  - Adds "seT" to the dhātu Term; sets the registry flag.
  - r1_form_identity_exempt=True: no surface string changes at this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level constants — CONSTITUTION Article 2 (no runtime data reads)
_MRZ_UPADESHA: frozenset = frozenset({"mfz"})          # SLP1 for mṛṣ
_NISTHA_PRATYAYA: frozenset = frozenset({"kta", "ktavatu~"})


def _find(state: State) -> int | None:
    """Return index of the mṛṣ dhātu Term eligible for seṭ, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("seT_mrz_1_2_20"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in _MRZ_UPADESHA:
            continue
        # Semantic gate: must be in the sense of titikṣā
        if "titikzA_usage" not in t.tags:
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
    state.terms[i].meta["seT_mrz_1_2_20"] = True
    state.samjna_registry["1_2_20_mfz_titikzAyAm"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.20",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "mfzas titikzAyAm",
    text_dev              = "मृषस्तितिक्षायाम्",
    padaccheda_dev        = "मृषः / तितिक्षायाम्",
    why_dev               = ("मृष्-धातुः तितिक्षार्थे निष्ठा-प्रत्ययस्य पूर्वं सेट् भवति — "
                             "१.२.१८-अपवादः; मृषित इति रूपम्।"),
    anuvritti_from        = ("1.2.19",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
