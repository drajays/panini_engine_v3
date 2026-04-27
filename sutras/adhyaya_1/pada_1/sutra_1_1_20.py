"""
1.1.20  (dādhā ghv adāp)  —  SAMJNA; *devanāgarī* = ``_TEXT_DEV`` (ashtadhyayi *i* 11020 *s* line).

**Pāṭha (ashtadhyayi-com ``data.txt`` i=11020):** the dhātus **dā** and **dhā**, and **ad** with
the 2nd-gaṇa **āp** marker (**ad**+**āp**), are termed **ghu** by anuvṛtti of the name *ghu* (see
*padaccheda* in the index: दा-धा · घु · अदाप्).  The surface sūtra reads **घ्व** (not **घु**) by
*śabda* rules before the **अ** of **अदाप्** (*ghu* of *ghoḥ* / *rāśi* in the pāṭha).

v3: ``samjna_registry['ghu']`` = *frozenset* of the canonical **upadeśa** SLP1 strings: **dā**,
**dhā**, **ad**+**āp**, and **deN** / **DheN** (देङ् रक्षणे, धेट् पाने) *śāstrīya* *ādeśa* to the
**dā**/**dhā** *pāramparya* for *ner*+**घु** in **8.4.17** (see *Kāśikā* *ādeca* 6.1.45, user prakriyā
notes: **प्रणिदयते** / **प्रणिधयति**).  *Vidhi* rules query ``dhatu_upadesha_slp1_is_ghu``; no *Term*
mutation here.
"""
from __future__ import annotations

from typing import FrozenSet

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# *dā* (ददँ), *dhā* (दधँ), *ad*+**āp** (2nd-gaṇa अदा॑प्) — *śāstrīya* upadeśa in SLP1/Velthuis.
# *E*-anta *de* / *Dhe* (ङित्) *ādeśa* to the *dā*/*dhā* *śākhā* for ghu-ṇatva in **8.4.17**
# (6.1.45 + *prakriyā*; no separate *sūtra* file in v3).
GHU_DHATU_UPADESHA_SLP1: FrozenSet[str] = frozenset(
    {
        "da~da",  # 01.0017 *dā* (दाने) — *dā* in *dā-dhā*
        "da~Da",  # 01.0008 *dhā* (धारणे) — *dhā*
        "adA~p",  # *ad*+**āp** — *Kāśikā* 2. *adāp* (भक्षण) (*upadeśa* may be absent in bhvādi-only corpora)
        "de~N",   # *de* (देङ् रक्षणे) — *Bhvādi* *E*-ādeśa *dā* class, **8.4.17**+**1.1.20** in notes
        "Dhe~N",  # *Dhe* (धेट् पाने) — same, **प्रणिधयति**-style
    }
)

# Registry key (R2) — *ghu* *saṃjñā* as a dhatu-upadeśa *set*.
GHU_KEY: str = "ghu"

# Bytes match ashtadhyayi ``s`` (i=11020).
_TEXT_DEV: str = "\u0926\u093e\u0927\u093e \u0918\u094d\u0935\u0926\u093e\u092a\u094d"


def cond(state: State) -> bool:
    return state.samjna_registry.get(GHU_KEY) != GHU_DHATU_UPADESHA_SLP1


def act(state: State) -> State:
    state.samjna_registry[GHU_KEY] = GHU_DHATU_UPADESHA_SLP1
    return state


def dhatu_upadesha_slp1_is_ghu(state: State, upadesha_slp1: str) -> bool:
    m = state.samjna_registry.get(GHU_KEY)
    if not isinstance(m, frozenset):
        return False
    return upadesha_slp1 in m


def ghu_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get(GHU_KEY) == GHU_DHATU_UPADESHA_SLP1


_WHY = (
    "दा-धाव् अद-आप् च, घु-संज्ञा — इति धातु-तात्पर्यं।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.20",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "dADhA ghv adA~p",
    text_dev       = _TEXT_DEV,
    padaccheda_dev = "दा-धा / घु / अदाप्",
    why_dev        = _WHY,
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
