"""
1.4.100  तङानावात्मनेपदम्  —  SAMJNA

*Padaccheda:* *taṅānau* (prathamā *dvivacanam* — *taṅ* + *ānau*), *ātmanepadam* (prathamā).

*Anuvṛtti:* *l̥* **1.4.99**; *eka* *sañjñā* **1.4.1**.

*Engine:* ``cond`` reads ``upadesha_slp1`` and tags only (CONSTITUTION Art. 2).  Tags
``atmanepada`` and removes ``parasmaipada`` on the same *Term* when both were present
(*eka*‑*sañjñā* *bādhana*).  Registry key ``1.4.100_atmanepada_adesha_slp1``.
Pāṭha: ashtadhyayi.com data.txt row i=14100 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State, Term

from sutras.adhyaya_1.pada_4.atmanepada_1_4_100 import (
    ATMANE_UPADESHA_SLP1,
    is_atmanepada_upadesha_slp1,
)


def _atmane_pratyaya_needing_tag(state: State) -> list[Term]:
    out: list[Term] = []
    for t in state.terms:
        if t.kind != "pratyaya":
            continue
        # The saṃjñā belongs to the sthānin (1.1.56): the ta / tam / ta that 3.4.101 puts in place of
        # tas / thas / tha (loṭ's tiṅ, by 3.4.85) is the ādeśa of a *parasmaipada* tiṅ and stays
        # parasmaipada, though ta now spells like the ātmanepada ta.
        if "parasmaipada" in t.tags and t.meta.get("3_4_101_tastha_done"):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if not is_atmanepada_upadesha_slp1(up):
            continue
        if "atmanepada" in t.tags:
            continue
        out.append(t)
    return out


def cond(state: State) -> bool:
    return bool(_atmane_pratyaya_needing_tag(state))


def act(state: State) -> State:
    pending = _atmane_pratyaya_needing_tag(state)
    state.samjna_registry["1.4.100_atmanepada_adesha_slp1"] = ATMANE_UPADESHA_SLP1
    for t in pending:
        t.tags.add("atmanepada")
        t.tags.discard("parasmaipada")
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.4.100",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = 'taNAnAvAtmanepadam',
    text_dev       = 'तङानावात्मनेपदम्',
    samagra_slp1   = "laH taNAnO Atmanepadam",
    samagra_dev    = "लः तङानौ आत्मनेपदम्",
    padaccheda_dev = "तङ्-आनौ (प्रथमा-द्विवचनम्) / आत्मनेपदम् (प्रथमा)",
    why_dev        = (
        "लकार-स्थाने तङ्-आदेशाः शानच्-कानच् च आत्मनेपद-संज्ञकाः; "
        "एकसंज्ञाधिकारे परस्मैपद-संज्ञां बाधन्ते।"
    ),
    anuvritti_from = ("1.4.1", "1.4.99"),
    cond           = cond,
    act            = act,
    skip_detail_cond_false = (
        "अत्र तिङ्-प्रत्ययः (तिप्) परस्मैपद-नियतः; तङ्-शानच्-कानच्-"
        "आत्मनेपद-नियम १.४.१०० अत्र न प्रवर्तते, अतः १.४.९९-दत्ता "
        "परस्मैपद-संज्ञा अनिर्बाधा।"
    ),
)

register_sutra(SUTRA)
