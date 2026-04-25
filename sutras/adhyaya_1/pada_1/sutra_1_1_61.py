"""
1.1.61  प्रत्ययस्यादर्शनं लुक्श्लुलुपः  —  SAMJNA (*luk* / *ślu* / *lup*)

**Pāṭha (baked *anuvṛtti* from **1.1.60** *adarśanam*):**
*pratyayasyādarśanaṃ luk-ślu-lupaḥ*.

**Śāstra (laghu):** when a *pratyaya*’s non-appearance (*adarśanam*) is taught
by the specific words *luk*, *śluḥ*, or *lup*, that *lopa* is respectively named
*luk*, *śluḥ*, or *lup* — the three subdivisions of *pratyaya-lopa*; other
*lopa* rules that say only *lopaḥ* (**6.1.68**, **6.4.50**, …) do **not** invoke
these names.  **1.1.63** *na lumat …* refers jointly to *luk*–*ślu*–*lup*;
*alopa* paribhāṣās (**1.1.52**, **1.1.54**) do not apply to *luk*/*ślu*/*lup*
deletion of the **whole** *pratyaya*.

*Engine:* registers ``samjna_registry[LUK_SLU_LUP_SAMJNA_KEY]`` (R2).  Requires
**1.1.60** *lopa* saṃjñā to be active first.  Actual deletion remains **vidhi**
sūtras (e.g. **1.3.9**, **2.4.71**, **4.3.166**, …).

**तिसृणां संज्ञानां प्रयोजनम्**

1. **Śluḥ** — *ślu*-saṃjñā-*lopa* triggers **6.1.10** *ślau* on the *prakṛti*
   (*dvi*-tva).  Example (*laghu*): *dā* + *laṭ* → *dā* + *tip* → *dā* + *śap* +
   *ti* → **2.4.75** *juhotyādibhyaḥ śluḥ* (loss of *śap*) → *dā* + *dā* + *ti* →
   *d* + *dā* + *ti* (**7.4.59** *hrasaḥ* in *abhyāsa*) → *dadāti*.

2. **Luk** — (a) wholesale *pratyaya* disappearance without the **6.1.10** *ślau*
   follow-up (e.g. **7.1.22** *ṣaḍbhyo luk* on *jas*, **2.4.71** *supo … luk*).
   (b) **[३.१] लुक्-संज्ञायाः विशेषं प्रयोजनम्:** when a **taddhita** *pratyaya*
   undergoes *luk*, **1.2.49** *luktaddhitluki* extends *luk* to the *strī*
   affix of the *upasarjana* as well (*Kāśikā:* *upasarjanasya strīpratyayasya
   api luk*).  Example (*laghu*): *āmalakyāḥ phalam* → *āmalakī* + *aṇ*
   (**4.3.135** *avayave …*) → **4.3.163** *phale luk* (*luk* of *aṇ*) →
   *āmalaka-*; here **1.2.49** removes the feminine (*ṭāp* / *ī*) marking on the
   first member so the compound surfaces as *āmalaka-* (neuter/masculine stem
   shape as taught), not *āmalakī-*.
   (c) **[३.२] लुक्-संज्ञायाः सामान्यं प्रयोजनम्:** by default **1.1.62**
   *pratyayalopaḥ pratyayalakṣaṇam* makes *pratyaya*-specific *aṅga-kārya*
   obligatory after *pratyaya-lopa*; when that *aṅga-kārya* is **not** wanted,
   the *lopa* must be taught with one of *luk* / *śluḥ* / *lup* so that **1.1.63**
   *na lumatāṅgasya* can suspend it.  If *śluḥ* or *lup* would over-generate
   (e.g. unwanted *dvi*tva, wrong *vacana*/*liṅga* tracking), **luk** is the
   remaining designation.  Example (*laghu*): *pañcan* + *jas* → *pañcan* + *śi*
   (**7.1.20**) → **7.1.22** *ṣaḍbhyo luk* on *jas*/*śi* (not *śluḥ* / *lup*):
   *pañcan* → *pañca-*; here **1.1.63** blocks the undesired *upadhā-dīrghaḥ*
   (**6.4.8**) that would otherwise follow from *pratyayalakṣaṇa*, while **8.2.7**
   *n*-loss (not *aṅga-kārya* in the relevant sense) still applies.

3. **Lup** — **[२] लुप्-संज्ञायाः प्रयोजनम्:** *lup*-saṃjñā-*lopa* invokes
   **1.2.51** *lupi yuktavad vyakti-vacane*: the *liṅga* and *vacana* of the
   surface word whose *pratyaya* underwent *lup* track the **prakṛti** (the
   base stem), not the *viśeṣya* (the meaning-head such as *janapada*).  Example
   (*laghu*): *pañcālānām nivāsaḥ* → *pañcāla* + *aṇ* (e.g. **4.2.69**) → *ṣaṣṭī*
   *luk* (**2.4.71**) → *aṇ* removed by **4.2.81** *janapade lup* (*lup* of *aṇ*)
   → the surviving stem *pañcāla-* takes **plural** like the tribal name in usage
   (*pañcālāḥ janapadaḥ*), though *janapada-* itself is notionally singular in the
   construction.  Other *lup* sites include **4.3.166** *lup ca* on *aṇ*, etc.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

from sutras.adhyaya_1.pada_1.lopa_samjna_1_1_60 import lopa_samjna_is_registered
from sutras.adhyaya_1.pada_1.luk_slu_lup_samjna_1_1_61 import (
    LUK_SLU_LUP_REGISTER_VALUE,
    LUK_SLU_LUP_SAMJNA_KEY,
    luk_slu_lup_samjna_is_registered,
)


def cond(state: State) -> bool:
    if not lopa_samjna_is_registered(state):
        return False
    return not luk_slu_lup_samjna_is_registered(state)


def act(state: State) -> State:
    state.samjna_registry[LUK_SLU_LUP_SAMJNA_KEY] = LUK_SLU_LUP_REGISTER_VALUE
    return state


_WHY = (
    "प्रत्ययस्य लोपः यदा 'लुक्' / 'श्लुः' / 'लुप्' इति विशिष्टेन शब्देनोक्तः, "
    "तदा स लोपः तथैव संज्ञकः; केवलं 'लोपः' इति शब्देनोक्तस्तु न — "
    "१.१.६३ इत्यादौ 'लु' इति सामान्यनिर्देशः; सम्पूर्ण-प्रत्ययलोपे "
    "१.१.५२, १.१.५४ न। "
    "तिसृणां प्रयोजनम् — श्लौ ६.१.१० इति श्लुः-संज्ञकलोपानन्तरं प्रकृतेः द्वित्वम् "
    "(यथा दा+शप्+ति → ददाति); लुक् समूहलोपे, तद्धिते लुकि "
    "१.२.४९ लुक्तद्धितलुकि उपसर्जन-स्त्रीप्रत्ययस्यापि लुक् "
    "(यथा आमलक्याः फलम् → आमलक+…, ४.३.१६३); "
    "१.१.६२–६३ प्रत्ययलक्षणम् / न लुमताङ्गस्य — अनिष्टाङ्गकार्ये "
    "लुक्-श्लु-लुप्-संज्ञा (यथा पञ्चन्+जस् → पञ्च, ७.१.२२); लुप्-संज्ञायां "
    "१.२.५१ लुपि युक्तवद् व्यक्तिवचने इति लिङ्ग-वचने प्रकृतिम् अनुसरतः "
    "(यथा पञ्चालानां निवासः → पञ्चालाः जनपदः, ४.२.८१ इत्यादौ लुप्)।"
)

SUTRA = SutraRecord(
    sutra_id       = "1.1.61",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "pratyayasya adarSanam luk slu lupAH",
    text_dev       = "प्रत्ययस्य अदर्शनं लुक्श्लुलुपः",
    padaccheda_dev = (
        "प्रत्ययस्य (षष्ठी-एकवचनम्) / अदर्शनम् (अन्वा. १.१.६०) / "
        "लुक्-श्लु-लुपः (प्रथमा-बहुवचनम्)"
    ),
    why_dev        = _WHY,
    anuvritti_from = ("1.1.60",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
