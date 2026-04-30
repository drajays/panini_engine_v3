"""
8.1.3  अनुदात्तं च  —  SAMJNA (narrow demo)

**Pāṭha (ashtadhyayi-com style):** *anudāttaṃ ca*.

Engine (``prakriya_17`` — **Phit 4.18** list, *sarvānudātta* block):
  • **Śikṣā / Phit** source for the enumerated stems is **not** a numbered
    Aṣṭādhyāyī sūtra; this module **reuses** the **8.1.3** anchor only for
    registry placement in the Tripāḍī–*anudātta* neighbourhood.
  • When ``phiSa_pratipadika`` + ``upadesha_slp1`` ∈ ``PHIT_418_…`` and
    ``phit_4_18_arm``, register ``samjna_registry['phit_418_sarvAnudAtta']``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from phonology.phit_lexicon import PHIT_418_SARVANUDATTA_PRATIPADIKA_SLP1


def _stem(state: State):
    if not state.terms:
        return None
    t0 = state.terms[0]
    if "phiSa_pratipadika" not in t0.tags:
        return None
    up = (t0.meta.get("upadesha_slp1") or "").strip()
    if not up:
        return None
    return t0, up


def cond(state: State) -> bool:
    if not state.meta.get("phit_4_18_arm"):
        return False
    hit = _stem(state)
    if hit is None:
        return False
    _, up = hit
    if up not in PHIT_418_SARVANUDATTA_PRATIPADIKA_SLP1:
        return False
    if "phit_418_sarvAnudAtta" in state.samjna_registry:
        return False
    return True


def act(state: State) -> State:
    hit = _stem(state)
    if hit is None:
        return state
    _, up = hit
    state.samjna_registry["phit_418_sarvAnudAtta"] = frozenset({up})
    state.meta.pop("phit_4_18_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.1.3",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "anudAttaM ca",
    text_dev       = "अनुदात्तं च",
    padaccheda_dev = "अनुदात्तम् च",
    why_dev        = "फिट् ४.१८-गणे प्रातिपदिकं सर्वानुदात्तम् (पञ्जी, न स्वर-वर्णः)।",
    anuvritti_from = ("8.1.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
