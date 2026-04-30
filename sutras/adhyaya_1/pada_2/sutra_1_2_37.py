"""
1.2.37  न सुब्रह्मण्यायां स्वरितस्य तूदात्तः  —  ANUVADA (narrow *glass-box*)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=12037):** *na subrahmaṇyāyāṃ svaritasya …*
— *śāstra* *pāṭha* for the *subrahmaṇyā* *āhvāna* context.

The user ``prakriya_26`` narrative (Vedic *āhvāna* after *subrahmaṇyā*) records an
*udātta* lift on the syllable that had received *svarita* from **8.4.66** in the
pedagogical sequence.  This engine slice only registers that audit closure when
``state.meta['prakriya_26_1_2_37_arm']`` is True and **8.4.66** has already marked
``samjna_registry['prakriya_26_svarita_locus']``.

No flat-tape mutation (CONSTITUTION Art. 2).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("prakriya_26_1_2_37_arm"):
        return False
    if not state.samjna_registry.get("prakriya_26_svarita_locus"):
        return False
    if state.meta.get("prakriya_26_subrahmaNyAhvAna_closure"):
        return False
    return True


def act(state: State) -> State:
    if not cond(state):
        return state
    state.meta["prakriya_26_subrahmaNyAhvAna_closure"] = True
    state.meta.pop("prakriya_26_1_2_37_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="1.2.37",
    sutra_type=SutraType.ANUVADA,
    text_slp1="na subrahmaNyAyAM svaritasya tUdAttaH",
    text_dev="न सुब्रह्मण्यायां स्वरितस्य तूदात्तः",
    padaccheda_dev="न / सुब्रह्मण्यायाम् / स्वरितस्य / तूदात्तः",
    why_dev="सुब्रह्मण्याह्वान-सन्दर्भे स्वरितोदात्त-अनुवादः (*prakriya_26*)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
