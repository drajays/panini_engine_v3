"""
3.4.113  तिङ्-शित् सार्वधातुकम्  —  SAMJNA

*Padaccheda:* *tiṅ-śit* (prathamā = compound *pratyāhāra*), *sārvadhātukam* (nominative).

*Anuvṛtti:* *pratyayaḥ* **3.1.1**; *paraś ca* **3.1.2**; *ādyudāttaś ca* **3.1.3**; *dhātoḥ* **3.1.91** — a
*tiṅ* or *śit* *pratyaya* immediately *para* to a *dhātu* is *sārvadhātukam*.

*Engine (CONSTITUTION Art. 2):* ``cond`` only checks ``upadesha_slp1`` and *dhātu* *adjacency*; see
``sarvadhatuka_3_4_113`` for the *tiṅ* and *śit* *SLP1* *inventory*.

*Cross-refs:* **3.4.114** ( *ārdhadhātuka* *śeṣa* ), **3.4.115** / **3.4.116** ( *liṭ* / āśīr *liṅ* *ārdhadhākatva* in *tiṅ* ) —
not implemented in this sūtra’s *act* (see module docstring).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

from sutras.adhyaya_3.pada_4.sarvadhatuka_3_4_113 import (
    SARVADHATUKA_UPADESHA_SLP1,
    is_sarvadhatuka_upadesha_slp1,
)


SARVADHATUKA_113 = "sarvadhatuka_3_4_113"


def _dhatu_adjacent_sarvadhatuka_untagged(state: State) -> list[Term]:
    out: list[Term] = []
    for i, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if i == 0:
            continue
        if "dhatu" not in state.terms[i - 1].tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if not is_sarvadhatuka_upadesha_slp1(up):
            continue
        if SARVADHATUKA_113 in t.tags:
            continue
        out.append(t)
    return out


def cond(state: State) -> bool:
    return bool(_dhatu_adjacent_sarvadhatuka_untagged(state))


def act(state: State) -> State:
    pending = _dhatu_adjacent_sarvadhatuka_untagged(state)
    state.samjna_registry["3.4.113_sarvadhatuka_slp1"] = SARVADHATUKA_UPADESHA_SLP1
    for t in pending:
        t.tags.add(SARVADHATUKA_113)
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.113",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = (
        "pratyayaH, para z ca, AdyudAttaz ca, DAtA — DAtA paraH tiG-Sit pratya YaH sArvadhAtukam"
    ),
    text_dev       = "तिङ्-शित् सार्वधातुकम् (३.१.१–३, ३.१.९१)",
    padaccheda_dev = "धातोः (३.१.९१) / परः / तिङ्-शित्-प्रत्ययः / सार्वधातुकम्",
    why_dev        = (
        "तिङ्-तथा-शित्-प्रत्ययः सार्वधातुक-संज्ञकः, आर्धधातुकानि ३.४.११४-अग्रे।"
    ),
    anuvritti_from = ("3.1.1", "3.1.2", "3.1.3", "3.1.91"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
