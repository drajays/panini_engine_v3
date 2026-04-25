"""
1.4.104  सुपः तिङ् च विभक्तिः  —  SAMJNA

*Padaccheda:* *supaḥ* (ṣaṣṭhī), *tiṅ* ( *pratyāhāra* ), *ca* ( *avyaya* ), *vibhaktiḥ* ( *prathamā-ekavacanam* ).

*Anuvṛtti:* *tiṅaḥ trīṇi trīṇi* **1.4.101** ( *tiṅ* ); **1.4.103** ( *sup* triples — *śāstra* ); **1.4.1** *ekasañjñā*.

*Śāstra:* *sup* *pratyaya* and *tiṅ* *pratyaya* receive the name *vibhakti* (seven *sup* triples, six *tiṅ* triples
in fixed order).

*Engine:* tags ``samjna_1_4_104_vibhakti`` on qualifying *pratyaya* ``Term``s; *registry* documents triple groupings
(R2).  *cond* is blind to ``vibhakti_vacana`` *meta* (Art. 2).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

from sutras.adhyaya_1.pada_4.vibhakti_samjna_1_4_104 import (
    SUP_VIBHAKTI_TRIPLES_SLP1,
    TAG_1_4_104_VIBHAKTI,
    TIN_VIBHAKTI_TRIPLES_SLP1,
    terms_needing_1_4_104_vibhakti,
)


def cond(state: State) -> bool:
    return bool(terms_needing_1_4_104_vibhakti(state))


def _apply_104(t: Term) -> None:
    t.tags.add(TAG_1_4_104_VIBHAKTI)


def act(state: State) -> State:
    pending = terms_needing_1_4_104_vibhakti(state)
    state.samjna_registry["1.4.104_sup_vibhakti_triples_slp1"] = SUP_VIBHAKTI_TRIPLES_SLP1
    state.samjna_registry["1.4.104_tin_vibhakti_triples_slp1"] = TIN_VIBHAKTI_TRIPLES_SLP1
    # Monotonic stamp so a second pass (new *tiṅ* / *sup* ``Term``s) still satisfies R2 — same pattern
    # issue as **1.4.101** when static registry values are re-written.
    state.samjna_registry["1.4.104_apply_stamp"] = (
        int(state.samjna_registry.get("1.4.104_apply_stamp", 0)) + 1
    )
    for t in pending:
        _apply_104(t)
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.104",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "supaH tiN ca vibhaktiH",
    text_dev       = "सुपः तिङ् च विभक्तिः (१.४.१, १.४.१०१–१०३-अनुवृत्ति)",
    padaccheda_dev = "सुपः / तिङ् / च / विभक्तिः",
    why_dev        = (
        "सुप्-तिङ्-प्रत्ययानां विभक्ति-संज्ञा; सुप्-सप्त-त्रिकाः, तिङ्-षट्-त्रिकाः (३.४.७८)।"
    ),
    anuvritti_from = ("1.4.1", "1.4.101", "1.4.103"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
