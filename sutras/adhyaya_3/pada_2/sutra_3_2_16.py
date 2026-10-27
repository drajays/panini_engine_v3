"""
3.2.16  चरेष्टः  —  VIDHI (narrow: corrected-v2 **P005-A** *kurucarī*)

*Śāstra (laghu):* after *√car* in an *upapada* frame, the *kṛt* **ṭa** (*ṭ*) is
introduced.

Engine: armed ``corrected_v2_P005_A_3_2_16_arm`` — insert **wa** (ट् + अ) after the
``car`` *dhātu* ``Term`` as a ``kṛt`` *pratyaya* (SLP1 ``w`` = ट्).

Citation (CONSTITUTION Art. 14)
  Source #1 — ashtadhyayi.com row i = 32016 · चरेष्टः
              padaccheda: चरेः टः
              anuvṛtti:   31001: प्रत्ययः | 31002: परः च | 31091: धातोः कृत्तिङ् | 32004: सुपि | 32015: अधिकरणे
  Source #2 — Kāśikā 3.2.16 udāharaṇa:
                चरेर्धातोरधिकरणे सुबन्त उपपदे टप्रत्ययो भवति
                कुरुषु चरतीति कुरुचरः
                मद्रचरः
  Cross-check — surface pinned by: tests/unit/test_bhaNguram_Ghurac.py
  Reference record: sutra_ref_out/3_2_16.json
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, upapada_site, no_upasarga
from engine.vikalpa import policy_pick  # noqa: F401
from engine.vivaksha import vivaksita


def _site(state: State):
    return upapada_site(state, "aDikaraRa", dhatus=frozenset({"cara~"})) if no_upasarga(state) else None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_krt(state, "wa")


SUTRA = SutraRecord(
    sutra_id="3.2.16",
    sutra_type=SutraType.VIDHI,
    text_slp1='carezwaH',
    text_dev='चरेष्टः',
    samagra_slp1="pratyayaH paraSca AdyudAttaSca DAtoH careH waH kft karmaRi anupasarge supi aDikaraRe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev="प्रत्ययः परश्च आद्युदात्तश्च धातोः चरेः टः कृत् कर्मणि अनुपसर्गे सुपि अधिकरणे",
    padaccheda_dev="चरेः / टः",
    why_dev="उपपदे चरः परः टः कृत् (प००५-अ)।",
    anuvritti_from=("3.1.25",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
