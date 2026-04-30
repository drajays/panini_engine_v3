"""
6.1.152  प्रतिष्कशश्च कशेः  —  ANUVADA (``prakriya_25`` spine)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=61152):** *pratīṣkaśaś ca kaśeḥ* — *śīrṣa*
substitution in *kaśa*-contexts; **not** the *anudāttaṃ padam ekavarjam* rule
(that is **6.1.158** in the same *adhyāya*).

The user JSON ``ordered_sutra_sequence`` lists **6.1.152** next to accent commentary;
this engine records the sūtra in the trace for *śāstra* alignment, with no
phonetic change on the ``subrahmaRyom`` *prayoga* (CONSTITUTION Art. 2: no
*vibhakti* reads in ``cond``).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return bool(state.meta.get("prakriya_25_6_1_152_arm"))


def act(state: State) -> State:
    state.meta.pop("prakriya_25_6_1_152_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="6.1.152",
    sutra_type=SutraType.ANUVADA,
    text_slp1="pratizkaSaH ca kaSeH",
    text_dev="प्रतिष्कशश्च कशेः",
    padaccheda_dev="प्रतिष्कशः च / कशेः",
    why_dev="कश-प्रकरणे शीर्षादेश-अनुवादः (*prakriya_25* मध्ये पदच्छेद-स्मरणार्थम्)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
