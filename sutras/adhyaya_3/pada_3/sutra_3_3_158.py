"""
3.3.158  समानकर्तृकेषु तुमुन्  —  SAMJNA (narrow ``split_prakriyas_11`` **P001**)

**Pāṭha (ashtadhyayi-com ``data.txt`` i=33158):** *samānakartṛkeṣu tumun* — *tumun*
after the root when the purpose (*icchārtha*) shares the same agent (*samānakartṛka*).

**Engine:** one-shot glass-box stamp ``samjna_registry['3.3.158_samAnakartruka_tumun_prakriya_P001']``
when ``meta['prakriya_P001_3_3_158_arm']``, ``meta['prakriya_P001_samAnakartRk_tumun_note']``, and the
witness ``BU`` ``Term`` carries ``prakriya_P001_Bavitum_demo``. No ``varṇa`` change — morphological
*tumun* attachment is supplied by the recipe tape (**tumn** … **tumun** ancestry in ``meta``).

Cross-check *anuvṛtti* (**धातोः**, **कृत्**, **इच्छार्थेषु** **3.3.157**) via ``data.txt`` offline.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _site(state: State) -> bool:
    if not state.meta.get("prakriya_P001_3_3_158_arm"):
        return False
    if not state.meta.get("prakriya_P001_samAnakartRk_tumun_note"):
        return False
    if not state.terms:
        return False
    if not any("prakriya_P001_Bavitum_demo" in t.tags for t in state.terms):
        return False
    if state.samjna_registry.get("3.3.158_samAnakartruka_tumun_prakriya_P001"):
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    state.samjna_registry["3.3.158_samAnakartruka_tumun_prakriya_P001"] = True
    state.meta.pop("prakriya_P001_3_3_158_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.3.158",
    sutra_type=SutraType.SAMJNA,
    text_slp1="samAnakartrukezu tumun",
    text_dev="समानकर्तृकेषु तुमुन्",
    padaccheda_dev="समानकर्तृकेषु / तुमुन्",
    why_dev="समानकर्तृकेतुमर्थे तुमुन् (*split_prakriyas_11* **P001**, **भवितुम्**)।",
    anuvritti_from=(),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
