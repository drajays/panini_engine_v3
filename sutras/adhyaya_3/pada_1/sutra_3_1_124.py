"""
3.1.124  ऋहलोर्ण्यत्  —  VIDHI

Padaccheda: ऋ-हलोः ण्यत्

Krt suffix rule from dhatu: ऋहलोर्ण्यत् (124)
Pāṭha: ashtadhyayi.com data.txt row i=31124 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_attach import attach_krt, dhatu_ends_tape
from engine.vikalpa import policy_pick
from engine.vivaksha import vivaksita
from phonology.pratyahara import HAL

_DECLINED = "3_1_124_declined"


def cond(state: State) -> bool:
    """कृत्याः (3.1.95) ṇyat after a dhātu ending in ṛ-varṇa or a hal (ऋहलोः) — in the kṛtya sense the speaker means."""
    if state.meta.get(_DECLINED) or not (vivaksita(state, "krt", "kftya") and dhatu_ends_tape(state)):
        return False
    last = state.terms[-1].varnas[-1].slp1 if state.terms[-1].varnas else ""
    return last in ("f", "F") or last in HAL


def act(state: State) -> State:
    # ṇyat stands beside tavyat-tavya-anīyar (3.1.96); the reading takes one — engine.vikalpa.choose({"3.1.124": 1}) leaves ṇyat for them
    if policy_pick(state, "3.1.124", 2) == 0:
        return attach_krt(state, "Ryat")
    state.meta[_DECLINED] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fhalorRyat",
    text_dev              = "ऋहलोर्ण्यत्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH f-haloH Ryat kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः ऋ-हलोः ण्यत् कृत्",
    padaccheda_dev        = "ऋ-हलोः ण्यत्",
    why_dev               = "धातोः [ऋहलोर्ण्यत्]-प्रत्ययः विहितः (३.१.124)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
