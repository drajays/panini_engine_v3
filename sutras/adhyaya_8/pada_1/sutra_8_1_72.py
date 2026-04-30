"""
8.1.72  आमन्त्रितं पूर्वमविद्यमानवत्  —  SAMJNA (narrow ``prakriya_32``)

**Pāṭha (cross-check: ``sutrANi.tsv`` / Kāśikā):** *āmantriṭaṃ pūrvam avidyamānavat* —
for accent purposes a preceding *āmantrita* *pada* may be treated like absent (*avidyamānavat*)
relative to a later vocative.

Narrow v3 (*tri-vocative apposition* demo **ऐडविड जटिलक अध्यापक**):
  • ``prakriya_32_8_1_72_arm`` + three *sāmantrita* stems ``EdaviDa``, ``jaWilaka``, ``aDyApaka``.
  • Registers ``samjna_registry['prakriya_32_pUrvAmantrita_avidyamAnavat']`` (superseded by **8.1.73**
    in this slice when *samānādhikaraṇa* holds).

No *svara* columns on ``Varna`` rows.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_32_8_1_72_arm"):
        return False
    if len(state.terms) != 3:
        return False
    ups = [state.terms[i].meta.get("upadesha_slp1") for i in range(3)]
    if ups != ["EdaviDa", "jaWilaka", "aDyApaka"]:
        return False
    for t in state.terms:
        if "sAmantrita" not in t.tags:
            return False
    if state.samjna_registry.get("prakriya_32_pUrvAmantrita_avidyamAnavat"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["prakriya_32_pUrvAmantrita_avidyamAnavat"] = True
    state.meta.pop("prakriya_32_8_1_72_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.72",
    sutra_type=SutraType.SAMJNA,
    text_slp1="AmantritaM pUrvam avidyamAnavat",
    text_dev="आमन्त्रितं पूर्वमविद्यमानवत्",
    padaccheda_dev="आमन्त्रितम् / पूर्वम् / अविद्यमानवत्",
    why_dev="पूर्वम् आमन्त्रितम् अविद्यमानवत् (*prakriya_32*; separated JSON **८।१।८२** → शास्त्रीय **८.१.७२**)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
