"""
1.4.102  तानि त्रीणि त्रीणि तिङः एकवचन-द्विवचन-बहुवचनानि एकशः  —  SAMJNA

*Padaccheda:* *tāni* (prathamā *bahuvacanam*), *trīṇi trīṇi* (dvis), *tiṅaḥ* (ṣaṣṭhī),
*ekavacana-dvivacana-bahuvacanāni* (prathamā *bahuvacanam*), *ekaśaḥ* (avyaya).

*Anuvṛtti:* *tiṅaḥ trīṇi trīṇi* **1.4.101**; **1.4.1** *ekasañjñā*.

*Śāstra:* within each *puruṣa* triplet of *tiṅ* *ādeśa*, the three affixes are named *ekavacana*,
*dvivacana*, *bahuvacana* in order (*ekaśaḥ*).

*Engine:* ``cond`` delegates to ``terms_needing_tin_102_vacana``; *tags* ``tin_102_*``; *registry*
``1.4.102_tin_vacana`` holds the ordered *tag* *names* (R2).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

from sutras.adhyaya_1.pada_4.tin_vacana_1_4_102 import (
    TIN_102_ALL_VACANA_TAGS,
    TIN_102_VACANA_ORDER,
    terms_needing_tin_102_vacana,
    vacana_102_tag_for_tin_adesha,
)


def cond(state: State) -> bool:
    return bool(terms_needing_tin_102_vacana(state))


def _apply_vacana_102(t: Term) -> None:
    t.tags -= TIN_102_ALL_VACANA_TAGS
    up = (t.meta.get("upadesha_slp1") or "").strip()
    new_tag = vacana_102_tag_for_tin_adesha(up)
    assert new_tag is not None
    t.tags.add(new_tag)


def act(state: State) -> State:
    pending = terms_needing_tin_102_vacana(state)
    state.samjna_registry["1.4.102_tin_vacana"] = TIN_102_VACANA_ORDER
    for t in pending:
        _apply_vacana_102(t)
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.102",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = (
        "tAni trIRi trIRi tiNgaH ekavacana-dvivacana-bahuvacanAni ekaSaH"
    ),
    text_dev       = (
        "तानि त्रीणि त्रीणि तिङः एकवचन-द्विवचन-बहुवचनानि एकशः (१.४.१०१-अनुवृत्ति, एकसंज्ञा)"
    ),
    padaccheda_dev = "तानि / त्रीणि-त्रीणि / तिङ् / एकवचन-द्विवचन-बहुवचनानि / एकशः",
    why_dev        = (
        "प्रत्येक-पुरुष-त्रिके क्रमेण एक-द्वि-बहु-वचन-संज्ञा; अष्टादश-तिङ्-क्रमः ३.४.७८।"
    ),
    anuvritti_from = ("1.4.1", "1.4.101"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
