"""
8.1.73  नामन्त्रिते समानाधिकरणे सामान्यवचनम्  —  SAMJNA (narrow ``prakriya_32``)

**Pāṭha (cross-check: ``sutrANi.tsv`` / Kāśikā):** *nām antriṭe samānādhikaraṇe…* —
when vocatives stand in *samānādhikaraṇa* (here: apposition), **8.1.72**'s *avidyamānavat*
treatment does not block later *āmantrita* accent behaviour.

Narrow v3:
  • Requires ``prakriya_32_8_1_73_arm`` and registry flag from **8.1.72**.
  • Sets ``samjna_registry['prakriya_32_samAnAdhikaraRa']`` and clears the **8.1.72** stamp so
    **8.1.19** (*padāt parasmāt*) can apply to ``jaWilaka`` / ``aDyApaka``.

No *svara* columns on ``Varna`` rows.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_32_8_1_73_arm"):
        return False
    if not state.samjna_registry.get("prakriya_32_pUrvAmantrita_avidyamAnavat"):
        return False
    if len(state.terms) != 3:
        return False
    ups = [state.terms[i].meta.get("upadesha_slp1") for i in range(3)]
    if ups != ["EdaviDa", "jaWilaka", "aDyApaka"]:
        return False
    if state.samjna_registry.get("prakriya_32_samAnAdhikaraRa"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry.pop("prakriya_32_pUrvAmantrita_avidyamAnavat", None)
    state.samjna_registry["prakriya_32_samAnAdhikaraRa"] = True
    state.meta.pop("prakriya_32_8_1_73_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="8.1.73",
    sutra_type=SutraType.SAMJNA,
    text_slp1="nAmantrite samAnAdhikaraRe sAmAnyavacanam",
    text_dev="नामन्त्रिते समानाधिकरणे सामान्यवचनम्",
    padaccheda_dev="न आमन्त्रिते / समानाधिकरणे / सामान्यवचनम्",
    why_dev="समानाधिकरणे आमन्त्रितेषु **८.१.७२** अप्रवृत्तिः (*prakriya_32*)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
