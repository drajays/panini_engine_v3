"""
1.2.9  इको झल्  —  NIYAMA

Anuvṛtti: seṭ (under 1.2.1 adhikāra region).

Meaning: Before a jhal consonant (jhal-ādi pratyaya), roots ending in an ik
vowel are aniṭ — they do NOT take the iṭ augment.  This is a restriction
(niyama) on the seṭ domain established by 1.2.1.

IK  = short forms of i, u, ṛ, ḷ  (SLP1: i, u, f, x)
JHAL = pratyāhāra of consonants (SLP1 set from phonology.JHAL)

Engine:
  - Finds a dhātu Term whose upadesha_slp1 ends in an IK phoneme AND the
    immediately following Term (the pratyaya) has an upadesha_slp1 that
    starts with a JHAL consonant.
  - Tags the dhātu Term "aniT" and guards re-entry via meta["aniT_1_2_9"].
  - r1_form_identity_exempt=True: no surface string changes in this step.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import IK, JHAL

# Expose the pratyāhāra sets at module level (frozensets, as required).
_IK: frozenset   = IK
_JHAL: frozenset = JHAL


def _find(state: State):
    """Return (dhatu_index, pratyaya_index) or None."""
    for i in range(len(state.terms) - 1):
        t = state.terms[i]
        if "dhatu" not in t.tags:
            continue
        if t.meta.get("aniT_1_2_9"):
            continue
        # Check dhātu upadesha ends in IK.
        up_dhatu = (t.meta.get("upadesha_slp1") or "").strip()
        if not up_dhatu or up_dhatu[-1] not in _IK:
            continue
        # Check the next term (pratyaya) starts with JHAL.
        pr = state.terms[i + 1]
        if "pratyaya" not in pr.tags:
            continue
        up_pr = (pr.meta.get("upadesha_slp1") or "").strip()
        if not up_pr or up_pr[0] not in _JHAL:
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find(state) is not None


def act(state: State) -> State:
    i = _find(state)
    if i is None:
        return state
    state.terms[i].tags.add("aniT")
    state.terms[i].meta["aniT_1_2_9"] = True
    state.samjna_registry["1_2_9_ikaH_jhal"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "1.2.9",
    sutra_type            = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1             = "iko jhal",
    text_dev              = "इको झल्",
    padaccheda_dev        = "इकः / झल् (अनिट्)",
    why_dev               = ("इक्-अन्त-धातुः झल्-आदि-प्रत्यये परे अनिट् — "
                             "इडागमः न भवति (नियम-संज्ञा)।"),
    anuvritti_from        = ("1.2.1",),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
