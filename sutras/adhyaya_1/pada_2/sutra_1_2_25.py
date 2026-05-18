"""
1.2.25  तृषिमृषिकृशेः काश्यपस्य  (tṛṣimṛṣikṛśeḥ kāśyapasya)  —  NIYAMA

Meaning: The roots tṛṣ (to thirst), mṛṣ (to endure), kṛś (to become thin)
— according to the view of Kāśyapa — [are seṭ, i.e., they take the iṭ augment].

This is a niyama (restriction / specification) that fixes these three roots as
seṭ according to the opinion of the grammarian Kāśyapa. The ruling overrides
any aniṭ tendencies these roots might otherwise have inherited from surrounding
sūtras (aniṭ rules of 1.2.10 ff.).

SLP1 root forms (as upadesha_slp1 in the dhātu-pāṭha):
  tṛṣ → "tfz"  (तृष्)
  mṛṣ → "mfz"  (मृष्)
  kṛś → "kfS"  (कृश्)

Engine:
  - Module-level TRSIMRSIKRSA frozenset holds the three SLP1 upadesha forms.
  - cond: finds a dhātu Term whose upadesha_slp1 is in the set, has no "seT"
    tag yet, and has not already been processed by this rule.
  - act: adds "seT" tag; sets meta flag; updates samjna_registry.
  - r1_form_identity_exempt=True: no surface string changes at this step.
  - Anuvṛtti: seṭ domain from 1.2.1.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# Module-level frozenset — CONSTITUTION Article 2
# SLP1 upadesha forms for tṛṣ, mṛṣ, kṛś
TRSIMRSIKRSA: frozenset = frozenset({"tfz", "mfz", "kfS"})


def _find(state: State) -> int | None:
    """Return index of eligible dhātu Term, or None."""
    for i, t in enumerate(state.terms):
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("seT_kASyapa_1_2_25"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up not in TRSIMRSIKRSA:
            continue
        if "seT" in t.tags:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("seT")
    state.terms[i].meta["seT_kASyapa_1_2_25"] = True
    state.samjna_registry["1_2_25_tfzi_mfzi_kfzi"] = TRSIMRSIKRSA
    return state


_WHY_DEV = (
    "तृषि-मृषि-कृशेः काश्यपस्य मते सेट् भवन्ति — "
    "एते त्रयः धातवः इडागमं गृह्णन्ति। "
    "काश्यपाचार्यस्य मतेन अयं नियमः।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.25",
    sutra_type              = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1               = "tfzimfzikfSeH kASyapasya",
    text_dev                = "तृषिमृषिकृशेः काश्यपस्य",
    padaccheda_dev          = "तृषि-मृषि-कृशेः / काश्यपस्य",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.1",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA", "TRSIMRSIKRSA"]
