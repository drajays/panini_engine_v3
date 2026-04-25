"""
Support for **1.1.61** *luk–ślu–lup* saṃjñā — not a sūtra file.

Three technical names for **pratyaya** *lopa* when the *vidhi* names the
operation with *luk*, *śluḥ*, or *lup* respectively — distinct from generic
*lopa* (**1.1.60**) alone (*Kāśikā:* generic *lopaḥ* in rules like **6.1.68**
does not get these three designations).

**तिसृणां संज्ञानां प्रयोजनम् (saṅkṣepa):** each name unlocks different
follow-up *prayoga* — notably **śluḥ** so that **6.1.10** *ślau* doubles the
*prakṛti* after **2.4.75** removes *śap* (*dā* + *śap* + *ti* → *dā* + *dā* + *ti*
→ *dadāti*); **luk** for wholesale *pratyaya* loss without that *dvitva* (e.g.
**7.1.22** *jas*, **2.4.71** *sup*), and when a **taddhita** takes *luk*,
**1.2.49** *luktaddhitluki* extends *luk* to the *upasarjana*’s *strī* affix
(*āmalakyāḥ phalam* → *āmalakī* + *aṇ* → **4.3.163** *phale luk* → *āmalaka-*,
with *ṭāp* / *ī* also lost per **1.2.49**); **(c)** **[३.२]** *luk* also when
**1.1.62** *pratyayalakṣaṇam* would force unwanted *pratyaya*-driven *aṅga-kārya*
unless **1.1.63** *na lumatāṅgasya* is invoked via *luk*/*ślu*/*lup* naming
(e.g. *pañcan* + *jas* → *śi* → **7.1.22** *ṣaḍbhyo luk*, not *ślu*/*lup*, so
*pañca-* without spurious *upadhā-dīrgha* from **6.4.8**); **lup** for *lup*-named wholesale loss, which
triggers **1.2.51** *lupi yuktavad vyakti-vacane* (gender/number of the *lupta*
form follows the *prakṛti*, not the *viśeṣya* — e.g. *pañcālānām nivāsaḥ* → … →
*pañcālāḥ janapadaḥ* via **4.2.81** *janapade lup* on *aṇ*, etc., alongside cases
like **4.3.166** *lup ca*).

Registry token ``slu`` stands for *śluḥ* (SLP1 *upadeśa* orthography varies).
"""
from __future__ import annotations

from typing import Final

from engine.state import State

LUK_SLU_LUP_SAMJNA_KEY: Final[str] = "1.1.61_luk_slu_lup"
LUK_SLU_LUP_REGISTER_VALUE: Final[frozenset[str]] = frozenset({"luk", "slu", "lup"})


def luk_slu_lup_samjna_is_registered(state: State) -> bool:
    return state.samjna_registry.get(LUK_SLU_LUP_SAMJNA_KEY) == LUK_SLU_LUP_REGISTER_VALUE
