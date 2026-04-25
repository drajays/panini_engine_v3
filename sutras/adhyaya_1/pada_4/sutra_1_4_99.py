"""
1.4.99  लः परस्मैपदम्  —  SAMJNA

*Padaccheda:* *l̥* (ṣaṣṭhī, *lakārāpādeṣu*), *parasmaipadam* (prathamā).

*Anuvṛtti* from **1.4.1** *ā kaḍārād ekā sañjñā* — the *ekasañjā* *adhikāra* for *lakārāpāda*.

*Content:* the *ādeśa* *pratyaya* that replace a *lakāra* and belong to the *parasmaipadīya*
set are named *parasmaipadam*; see ``parasmaipada_1_4_99`` for the engine’s SLP1 list
(nine *tiṅ* from 3.4.78, *śatṛ* / *kvasu* from 3.2.124 / 3.2.107 — the *śāstrīya* *net* of
eleven *ādeśa* after the **1.4.100** *bādhana* narrative).

*Engine:* ``cond`` uses only ``Term.meta['upadesha_slp1']`` and tags (CONSTITUTION Art. 2).
Registers ``1.4.99_parasmaipada_adesha_slp1`` in ``samjna_registry`` and the ``parasmaipada`` *tag* on
each matching *pratyaya* *Term*.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

from sutras.adhyaya_1.pada_4.parasmaipada_1_4_99 import (
    PARASMAI_UPADESHA_SLP1,
    is_parasmaipada_upadesha_slp1,
)


def _parasmai_pratyaya_needing_tag(state: State) -> list[Term]:
    out: list[Term] = []
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if not is_parasmaipada_upadesha_slp1(up):
            continue
        if "parasmaipada" in t.tags:
            continue
        out.append(t)
    return out


def cond(state: State) -> bool:
    return bool(_parasmai_pratyaya_needing_tag(state))


def act(state: State) -> State:
    pending = _parasmai_pratyaya_needing_tag(state)
    state.samjna_registry["1.4.99_parasmaipada_adesha_slp1"] = PARASMAI_UPADESHA_SLP1
    for t in pending:
        t.tags.add("parasmaipada")
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.99",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "lasaH parasmaipadam",
    text_dev       = "लः परस्मैपदम् (आकडारादेकाः संज्ञाऽधिकारे)",
    padaccheda_dev = "लः (षष्ठी) / परस्मैपदम् (प्रथमा)",
    why_dev        = (
        "लकार-स्थानि तिङादेशादिषु अन्त्यैकादश-प्रकारेषु परस्मैपद-संज्ञा; "
        "तङादिषु १.४.१०० इति पृथक् (एकसंज्ञा-सापेक्ष)।"
    ),
    anuvritti_from = ("1.4.1",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
